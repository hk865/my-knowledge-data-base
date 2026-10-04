# 视觉语言模型（VLM）

> 状态：领域入门页 · v2 · 依据 [synthesis.csv](synthesis.csv)（18 篇）
>
> 速览：
> 1. VLM 把图像和文字一起交给语言模型，让它用文字回答。主线问题是"视觉编码器怎样接到 LLM 上、哪些参数在哪个阶段训练"：2022–2023 年试过门控交叉注意力（Flamingo）、查询瓶颈（BLIP-2 的 Q-Former）和直接投影进 token 序列（LLaVA），2024 年起开源模型几乎都收敛到"ViT + MLP + LLM"。
> 2. 2024 年的主战场是分辨率：固定的 224/336/448 输入看不清文档和小字，各家改用切块（InternVL 1.5、DeepSeek-VL2）或原生动态分辨率（Qwen2-VL、Kimi-VL）。Qwen2-VL-7B 的消融中，每图 64 个视觉 token 时 InfoVQA 只有 28.9，3136 个时 77.3。
> 3. 训练流程逐步变成 LLM 流水线的镜像：对齐 → 多模态预训练 → SFT → 偏好优化 / RL / 蒸馏。LLM 后训练里的坑也一一重现：语言能力被挤掉、几千条重复样本让模型复读、过度思考、奖励被钻空子。
> 4. 评测本身是最大的坑：POPE 发现早期模型对"图里有没有某物"95% 以上答"有"；MMStar 发现 GeminiPro 不看图在 MMMU 上也有 42.9%；Cambrian-1 发现 MMMU、MathVista、AI2D 开不开图像差距不到 5%；Molmo 的人评中 Qwen2-VL 学术分高、人评偏低。
> 5. `[判断]` 团队押注：Qwen 押注原生分辨率与坐标接地、视觉塔反复重选；InternVL 押注 6B 大视觉编码器与开放数据；DeepSeek 与 Kimi 押注 MoE 语言侧和"不损伤语言能力"；Google 从 Flamingo、PaLI 走到闭源的原生多模态 Gemini；AI2 押注不蒸馏闭源模型的开放数据。VLA 的骨干就是这些 VLM。

本页是[多模态总目录](../../README.md)下的视觉语言模型方向。按 STYLE 第 3 节的目标驱动模板写，而不用[视觉表征](../visual-representation/README.md)的研究对象变体（3.6）：VLM 有自己的任务（看图回答、按图对话、读文档、定位物体）和专属 benchmark，好坏可以直接在任务上测；编码器本身好不好，留给视觉表征方向。"benchmark 是否真的测到了看图"是本领域的问题，写在"用什么衡量进展"。拆分后的基线见 [Baseline 页](BASELINES.md)，学习步骤见[路线图](ROADMAP.md)，论文列表见[论文目录](PAPERS.md)。

## 这个领域在解决什么

结论：VLM 让语言模型"看见"：先把图像变成语言模型能读的一串向量，回答仍用下一词预测生成。

拍一张电费单问"这个月比上个月多交了多少钱"，模型要读出小字（OCR）、找到两个数字在哪、做减法，再用中文回答。[CLIP](../../papers/clip/README.md) 这类图文对比模型只能给"图和某句话有多匹配"打分（见[图文对齐](../alignment/README.md)），不会生成回答。VLM 的做法是把视觉编码器（通常是 CLIP 式训练的 ViT，把图切成 14×14 像素的小块，每块输出一个向量）的输出接进 LLM：

```
图像 ─► 视觉编码器（ViT）─► 连接器 ─► 视觉 token ┐
                                                 ├─► LLM ─► 文字回答（损失只算在回答的 token 上）
文字 ─────────────────► 分词 + 词嵌入 ──────────┘
```

视觉 token 是连续向量，没有词表编号，也不是输出目标；输出只有文字（[LLaVA 精读](../../papers/llava/reading.md)第 2 节有逐维的形状推导）。"怎样接"有四类做法：

| 接法 | 怎么接 | 代表 | 直觉 | 后来怎样 |
|---|---|---|---|---|
| 门控交叉注意力 | LLM 冻结；在层间插入新的交叉注意力层，文字 token 去查视觉特征；门控系数 tanh(α) 中 α 初始化为 0，开训时模型与原 LLM 完全相同 | Flamingo | 不动 LLM，保住语言能力 | 本页 2024 年后的开源模型都不用 |
| 查询瓶颈 | 一组可学的查询向量从视觉特征里抽出固定数量的 token | BLIP-2 的 Q-Former（32 个）、Qwen-VL 的单层交叉注意力（256 个） | token 少，省算力 | 被 MLP 取代 |
| 投影进序列 | 每个图像块特征经线性层或两层 MLP 变成 LLM 的输入嵌入，与文字 token 排在同一序列里 | LLaVA、LLaVA-1.5 及其后多数模型 | 最简单，信息不过瓶颈 | 成为默认，另用相邻 2×2 合并减少 token |
| 早融合 / 原生多模态 | 图像离散成 token 与文字共用词表，或从预训练起就混合多模态数据 | Chameleon；Gemini（官方只写"从一开始就是多模态"） | 理解与生成在同一个模型里 | 仍在探索，见历史末节 |

### 训练流程：LLM 流水线的镜像

结论：VLM 的训练与 [LLM 后训练](../../../llm/fields/posttraining/README.md)几乎一一对应，只在最前面多一步"对齐"；每一步的坑也和 LLM 一侧同源。

| 阶段 | 在 LLM 里对应什么 | VLM 做什么 | 例子 | 这一阶段的坑 |
|---|---|---|---|---|
| 对齐 | 无 | 冻结 ViT 与 LLM，只训连接器，让视觉向量落进 LLM 的输入空间 | LLaVA 用约 59.5 万对图文；Qwen3-VL 的 S0 用 67B token | 要不要这一步、数据多少，各家结论相反（见开放问题） |
| 多模态预训练 | [预训练](../../../llm/fields/pretraining/README.md) | 解冻 LLM（常也解冻 ViT），在图文对、OCR、交错网页、定位数据上继续训练，并混入纯文本 | Qwen2-VL 1.4T token，Qwen2.5-VL 4.1T | 语言能力被挤掉：DeepSeek-VL 直接用多模态数据训练时语言指标急剧下降 |
| SFT（视觉指令微调） | SFT | 在"图 + 指令 → 回答"上做下一词预测 | LLaVA 158K 条，LLaVA-1.5 665K 条 | 数据缺是非题，模型一律答"是"（LLaVA）；几千条重复样本让模型复读（InternVL 2.5） |
| 偏好优化 | RLHF、[DPO](../../../llm/papers/dpo/README.md)（直接偏好优化：不训奖励模型，直接在好坏回答对上优化） | 在成对的好坏回答上优化 | Qwen2.5-VL 的 DPO，InternVL3 的 MPO（DPO 加质量与生成损失的混合目标） | — |
| RL 与蒸馏 | 可验证奖励的 RL、on-policy 蒸馏 | 在数学、定位、计数等可判对错的任务上做 RL；用更强教师蒸馏 | Kimi-VL-Thinking、Qwen3-VL | 过度思考（Kimi 加长度惩罚）；工具调用奖励被钻空子（Qwen3-VL） |

### 与相邻方向的分工

| 方向 | 管什么 | 与 VLM 的接口 |
|---|---|---|
| [视觉表征](../visual-representation/README.md) | 编码器本身学到什么性质 | VLM 是编码器的一个使用方式；Cambrian-1 反过来用 VLM 当编码器的评测协议 |
| [图文对齐](../alignment/README.md) | CLIP、SigLIP 这类双塔怎样训练 | 提供 VLM 最常用的视觉塔 |
| [视频与时序](../video-temporal/README.md) | 视频表征与时间建模 | Qwen2-VL 起的视频输入、M-RoPE 的时间维、时间戳 token |
| [视觉生成](../generation/README.md) | 从噪声生成图像与视频 | Chameleon、Gemini 想把理解与生成放进同一个模型 |
| [VLA](../../../robotics-embodied/fields/vla/README.md) | 从像素和指令直接输出机器人动作 | VLA 的骨干就是 VLM（见"与 VLA 的共性"） |

## 主线历史

结论：2022–2023 年回答"怎样以最小代价把视觉接上一个现成 LLM"；2024 年转向"看得清"（分辨率、OCR、定位）和"测得准"（盲答、幻觉、人评）；2025 年转向"会推理"，训练流程整体向 LLM 后训练看齐；2026 年进一步追问联合训练的时机、视觉初始化与音视频工具闭环。每个节点先写上一节点留下的问题，再写改变，最后写做不好的场景；`[判断]` 是从后续工作反推的结论。

### 1 冻结 LLM、外挂视觉：Flamingo 与 PaLI（2022，DeepMind 与 Google）

留下的问题：CLIP 只会打相似度分，不能回答开放问题；能生成文字的视觉语言模型又要每个任务上万条标注来微调。

改变：[Flamingo](../../papers/arxiv-2204.14198/README.md) 冻结 70B 的 Chinchilla 语言模型和对比预训练的 NFNet 视觉编码器，只训练两类新模块：Perceiver Resampler（一组可学查询，把任意大小的特征图压成 64 个视觉 token）和插在 LLM 层间的门控交叉注意力。训练数据中最关键的是从约 4300 万个网页抽出的图文交错文档 M3W：消融中去掉它，总分下降 17% 以上；改为微调 LLM 下降 8.0%，从零训练 LLM 下降 12.9%（作者称为灾难性遗忘）；去掉零初始化门控下降 4.2% 并且训练不稳。最终只给 32 个示例做少样本提示，在 16 个任务中的 6 个超过逐任务微调的最好结果。[PaLI](../../papers/arxiv-2209.06794/README.md) 走 encoder–decoder：13B 的 mT5-XXL 加新训的 4B ViT-e，视觉约占 25% 参数，作者认为扩视觉侧的回报更高；主预训练阶段冻结 ViT，VQAv2（自然图像短答案问答）84.3%。

做不好的场景：Flamingo 自述分类不如对比模型，继承了 LLM 的幻觉和无依据猜测，少样本结果对示例的选择和顺序敏感；输入只有 320×320，VQAv2 的 32-shot 为 67.3%，要升到 480 并解冻视觉编码器做微调才到 82.0%；代码与数据不公开。PaLI 自述描述多物体的复杂场景不够完整，英文数据微调后丢失部分多语言能力，开放式生成的同义答案被判错。`[判断]` 站在现在看，"冻结 LLM 保语言"后来被"解冻 LLM、混入大比例纯文本"取代（DeepSeek-VL、Kimi-VL）；Flamingo 自己也提示了方向：解冻视觉并提高分辨率才拿到最好成绩。

### 2 轻量连接器：BLIP-2（2023 年 1 月，Salesforce）

留下的问题：Flamingo 要训练约 10B 参数，数据私有；作者认为只用图生文损失不足以弥合模态差距。

改变：[BLIP-2](../../papers/arxiv-2301.12597/README.md) 的 Q-Former（188M 参数，BERT-base 初始化）用 32 个 768 维的可学查询，从冻结 ViT-L 的 257×1024 特征中抽取信息。训练分两段：先接冻结的图像编码器做图文表征学习（对比、匹配、图生文三个目标），再接冻结的 LLM 做生成学习。零样本 VQAv2 65.0%，比 Flamingo-80B 的 56.3% 高 8.7 个百分点，可训练参数少 54 倍。

做不好的场景：自述给 LLM 加上下文示例不提升 VQA，原因是训练数据每条只有一对图文；知识型的 OK-VQA 仍不如 Flamingo-80B；继承 LLM 的知识错误与偏见。`[判断]` 站在现在看，重采样器这条路被放弃：[LLaVA-1.5](../../papers/arxiv-2310.03744/README.md) 附录写明，现有重采样器在同等数据下收敛不如它的 MLP 高效，并指出 InstructBLIP 只微调 Q-Former 时控制不了回答长短；[InternVL 1.5](../../papers/arxiv-2404.16821/README.md) 把 InternVL 1 的 8B "语言中间件"换成 MLP；[Qwen2-VL](../../papers/arxiv-2409.12191/README.md) 把 Qwen-VL 的 256 查询交叉注意力换成 2×2 合并的 MLP。瓶颈省下的 token 抵不过它丢掉的细节和训练效率。

### 3 投影加视觉指令微调：LLaVA 与 LLaVA-1.5（2023，Wisconsin 与 Microsoft）

留下的问题：BLIP-2 会描述，不会按指令对话；学术 VQA 数据只教一两个词的短答案。

改变：[LLaVA](../../papers/llava/README.md)（2023 年 4 月）把冻结的 CLIP ViT-L/14 网格特征经一个线性层投影进 Vicuna，让只读文字的 GPT-4 根据 COCO 的标题和物体框生成 158K 条视觉指令数据；先只训投影层，再训投影层与 LLM。[LLaVA-1.5](../../papers/arxiv-2310.03744/README.md)（2023 年 10 月）做受控对照：换成两层 MLP 和 336 像素的 CLIP，加入学术 VQA 数据，并在短答案题后加格式提示"Answer the question using a single word or phrase"。只加 VQAv2 和格式提示，MME（是非题形式的感知与认知考卷）就从 809.6 升到 1323.8；最终只用约 120 万条公开数据、8 张 A100 约 1 天训完，在 12 个 benchmark 中的 11 个领先。

做不好的场景：[POPE](../../papers/arxiv-2305.10355/README.md)（2023 年 5 月，中国人民大学）把物体幻觉改写成"图里有没有 X"的是非题，原版 LLaVA、MultiModal-GPT、mPLUG-Owl 有 95%–99% 的回答是"有"，最容易被编出来的是指令数据里高频或常共现的物体。LLaVA-1.5 把原版"倾向答 yes"归因于训练数据缺这类题，并发现输入提到 448 后详细描述里的幻觉显著减少：分辨率不够看清标注里的细节、这类数据又足够多时，模型学会了编。它自述高分辨率训练慢、不支持多图、部分领域解题能力有限；开源 CLIP 最高只有 336 像素，LLaVA-1.5-HD 只好把图切成 224 的格子分别编码。

### 4 加大视觉侧、解冻视觉塔、保住语言：Qwen-VL、InternVL、DeepSeek-VL（2023 年 8 月 – 2024 年 3 月）

留下的问题：LLaVA 一族的视觉侧是 0.3B 的冻结 CLIP、输入 336 像素，读字、读表、定位都弱；开源模型多把算力花在指令阶段。

改变：
- [Qwen-VL](../../papers/arxiv-2308.12966/README.md)（阿里 Qwen）：1.9B ViT + 单层交叉注意力（256 个查询）+ 7.7B LLM，三阶段训练：冻结 LLM、在 224 分辨率上训 ViT 与适配器（50 亿对图文清洗到 14 亿）；升到 448 并解冻全部参数，做含定位与 OCR 的 7 类多任务；冻结 ViT 做 SFT。物体框坐标归一化到 [0, 1000) 后直接写成文字。
- [InternVL](../../papers/arxiv-2312.14238/README.md)（上海人工智能实验室，2023 年 12 月）：指出 LLM 已到上千亿参数，视觉编码器仍在 1B 左右，"胶水层"轻且随机初始化；把视觉编码器扩到 6B（InternViT-6B），先对比学习、再生成式学习，逐步与 LLM 对齐。
- [DeepSeek-VL](../../papers/arxiv-2403.05525/README.md)（2024 年 3 月）：SigLIP-L（Google 的 CLIP 式图文对比编码器，384 像素）与 SAM-B（Meta 分割模型 SAM 的编码器，1024 像素）两路编码器合成 576 个 token；发现直接在 LLM 上做多模态预训练，多模态指标涨、语言指标急剧下降，要保留至少 70% 纯文本，并从文本为主逐步提高多模态比例；加大"只训连接器"那一阶段的数据没有收益。

做不好的场景：输入仍是固定尺寸（448 或 1024），极端长宽比和超大图只能缩放。DeepSeek-VL2 后来自述 1024 固定输入在 InfographicVQA、稠密 OCR 和精细定位上吃亏；DeepSeek-VL 自述 MathVista（数学图表推理）36.1 落后 GPT-4V 的 47.8。`[判断]` 站在现在看，视觉塔的处理从"全程冻结"变成"中段解冻、SFT 再冻"：Qwen-VL、Qwen2-VL、Qwen2.5-VL 都在 SFT（及 DPO）时冻结 ViT；[Cambrian-1](../../papers/arxiv-2406.16860/README.md) 用 23 个视觉骨干验证解冻普遍有益；VLA 一侧 OpenVLA 冻结视觉编码器后成功率从约 70% 降到 47%。

### 5 分辨率与 token 预算：切块与原生分辨率（2024）

留下的问题：固定方形输入看不清文档、图表和截图；"把图放大"又会让 token 数按面积增长。

改变：两条路。**切块**：InternVL 1.5（2024 年 4 月）按长宽比把图切成 1–40 块 448×448（最高约 4K）再加一张缩略图，用 pixel shuffle（把相邻 2×2 个特征拼到通道维）把每块 1024 个 token 压到 256；[DeepSeek-VL2](../../papers/arxiv-2412.10302/README.md)（2024 年 12 月）改用单个 SigLIP-SO400M 最多切 9 块，语言侧换成 DeepSeekMoE（混合专家：每个 token 只激活一部分 FFN）。**原生**：Qwen2-VL（2024 年 9 月）去掉 ViT 的绝对位置编码、换成二维 RoPE，任意分辨率的图都变成不定长的 token 序列，相邻 2×2 个 token 经 MLP 合成一个（224×224 的图得到 66 个）；M-RoPE 把旋转位置编码拆成时间、高、宽三份，图像和视频共用。Qwen2-VL-7B 的消融（Table 7）给出了分辨率的价值：固定 64、576、1600、3136 个 token 时 InfoVQA（信息图问答）为 28.9、65.7、75.0、77.3，动态分辨率平均 1924 个 token 得 75.9；MMMU（大学多学科配图考题）四档都在 53 左右。

做不好的场景：切块边缘的图像块缺少相邻上下文，Molmo 改用重叠切块弥补。Qwen2-VL 把小图放大过头时 OCRBench（综合读字评测）严重下降，作者归因于放大后的图偏离训练分布；MMMU 不随分辨率变，说明它的瓶颈在推理；视觉语言导航上 Qwen2-VL 与 GPT-4o 都远落后专用模型，作者归因于从多张图建出的地图不完整。[Kimi-VL](../../papers/arxiv-2504.07491/README.md) 批评 DeepSeek-VL2 仍用固定尺寸编码器、上下文只有 4K。

### 6 回头检验：评测测到"看"了吗，数据能否不靠闭源模型（2024）

留下的问题：2023–2024 年 benchmark 分数快速上涨，但分数来自看图还是来自 LLM 的知识？开源模型的指令数据又多由 GPT-4V 生成，等于在蒸馏闭源模型。

改变：[MMStar](../../papers/arxiv-2403.20330/README.md)（2024 年 3 月，中国科学技术大学、香港中文大学与上海人工智能实验室）发现两类问题。一是不用看图：ScienceQA（中小学科学选择题）超过 50%、MMMU（大学多学科配图考题）约 20% 的题被多数纯文本 LLM 直接答对，GeminiPro 不看图在 MMMU 上 42.9%。二是数据泄漏：Sphinx-X-MoE 不看图在 MMMU 上 43.6%，比它自己的 LLM 底座高 17.9 个百分点。作者人工挑出 1500 道必须看图的题，最好的高分辨率 GPT-4V 只有 57.1%。Cambrian-1（2024 年 6 月，NYU）在 23 个视觉骨干上比较开图与关图：ScienceQA 图像子集、MMMU、MathVista、AI2D 差距不到 5%；TextVQA（图中文字问答）、GQA（场景图组合问答）关图后仍比随机猜高近 40 个百分点，存在语言偏差；它另建 2638 题的 CV-Bench，测空间关系、计数、深度顺序与相对距离。[Molmo](../../papers/arxiv-2409.17146/README.md)（2024 年 9 月，AI2 与华盛顿大学）完全不用 VLM 生成的数据：让标注员对着图口述 60–90 秒，得到 71.2 万张图的长描述，另有 230 万个点标注用于指向与计数；同等数量下这些描述比 ShareGPT4V（GPT-4V 生成的描述）训练效果更好。它的人评 Elo（按两两对比的胜负算出的排名分）中 Molmo-72B 仅次于 GPT-4o；学术分与人评总体一致，例外是 Qwen2-VL，学术分强、人评偏弱。

做不好的场景：MMStar 只有 1500 题，自述要扩成在线测试集来防泄漏；Molmo 的指向数据只训到 40 个以内的计数，独立的 Chatbot Arena 上 Molmo-72B 仍低于 GPT-4o 和 Claude 3.5 Sonnet；Cambrian-1 自述没有采用任意分辨率，并提醒只按 benchmark 优化会得到"答题机器"。

### 7 推理、RL 与"原生"预训练（2024 年 12 月 – 2025）

留下的问题：感知做好以后，难题（MMMU、MathVision 等）要靠推理；LLM 一侧已有 o1、[DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 式的长思维链 RL。

改变：
- [InternVL 2.5](../../papers/arxiv-2412.05271/README.md)（2024 年 12 月）：配 6B 视觉编码器的 78B 模型只用约 120B token，作者对比 Qwen2-VL 累计的 1.4T；MMMU 用 CoT（思维链：先写推理步骤再给答案）达 70.1%，比直接回答高 3.7，是第一个过 70% 的开源模型。它还发现 LLM 对数据噪声远比视觉编码器敏感：微调数据中区区几千条重复样本，就让模型在长输出和 CoT 中陷入循环。
- [Qwen2.5-VL](../../papers/arxiv-2502.13923/README.md)（2025 年 2 月）：重新设计并从零训练 ViT（32 层中只有 4 层全局注意力，其余是窗口注意力）；定位坐标改用真实像素而非归一化值；预训练 4.1T token；后训练为 SFT + DPO，两段都冻结 ViT。
- Kimi-VL（2025 年 4 月，月之暗面）：16B 总参数、2.8B 激活的 MoE 语言模型 + 400M 原生分辨率 MoonViT；从已训 5.2T 文本 token 的中间检查点接着做 4.4T token 的联合训练，凡是更新语言模型的阶段都混入文本；Thinking 版用长 CoT SFT 加 RL，并用长度奖励惩罚过长回答。
- [InternVL3](../../papers/arxiv-2504.10479/README.md)（2025 年 4 月）：把语言预训练和多模态对齐合成一个"原生多模态预训练"阶段，所有层一起训（仍从预训练好的 LLM 基座与 ViT 初始化），后接 SFT 与 MPO；MMMU 72.2%，承诺公开训练数据。
- [Qwen3-VL](../../papers/arxiv-2511.21631/README.md)（2025 年 11 月）：视觉塔改为在 SigLIP-2 上继续训练；DeepStack 把 ViT 三个层级的特征分别加到 LLM 前三层；后训练分三段：长 CoT SFT、只用文本数据的强到弱蒸馏、推理 RL 与通用 RL；全部以 Apache 2.0 开放。

做不好的场景：InternVL 2.5 自述过滤数据也无法根除复读，长回答中仍有幻觉；InternVL3 在 MMHal（幻觉评测之一）上略有下降；Qwen2.5-VL 自述 CoT 的中间步骤可能忽略或误读视觉线索。Qwen3-VL 的通用 RL 专门用来纠正 SFT 留下的"强而错的先验"，例子是反直觉的计数和复杂表盘读时；在"用图思考"（让模型调用裁剪、放大等工具再看图）的工具 RL 中，模型退化成只调一次工具来骗取另两项奖励，只好再加一项按任务难度设定调用次数的奖励。Kimi-VL 自述注意力参数只相当于 3B 模型，128K 上下文在极长输入上仍不够。`[判断]` 站在现在看，Qwen3-VL 自己写出了 Qwen2.5-VL 的两个坑：M-RoPE 把维度切成时间、高、宽三组造成频谱不均，伤害长视频；绝对时间的位置编号在长视频里过大且稀疏，还要求训练数据覆盖各种帧率。两者在下一代都被替换（交错 M-RoPE、文字时间戳）。

### 8 从"给 LLM 接眼睛"到共同训练与反复取证（2026）

**留下的问题**：2025 年的模型已经能读高分辨率图片并写长推理，但视觉什么时候加入训练、视觉塔是否必须先做图文对比、模型会不会真正用视觉证据，仍是三个独立问题。以下四篇按这三个问题读，比只按总分选模型更有用。

- **先读 [Kimi K2.5](../../../llm/papers/arxiv-2602.02276/README.md)**：在固定图文 token 预算的消融中，把较低比例视觉数据更早混入，比训练末期集中加入更好；其 zero-vision SFT 指只用文本示范激活工具行为，前提是基座已做图文联合预训练。随后仍需视觉 RL，修正模型忽略图像的行为。
- **接着读 [Qwen3.5](../../../llm/papers/qwen3.5/README.md)**：官方模型卡把早期图文融合与混合注意力一起列为基础设计，延续 ViT 视觉编码器接口，同时让长上下文计算成为架构问题。它适合作为另一团队的路线对照；模型卡中的跨模型成绩不等于"早融合"这一变量的受控消融。
- **再读 [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md) §2.4**：它保留 ViT + MLP 接口，却将视觉塔改为从零用下一词目标训练。相对 SigLIP 初始化的对照，报告给出更稳定的视觉梯度和相当的视觉评测，直接追问"预训练视觉塔究竟提供了什么"。
- **做音视频工具任务时读 [Qwen3.8-Omni](../../papers/arxiv-2609.25611/README.md)**：图像、声音与时间戳进入共同上下文，工具可以再次截取并读取音视频。问题从"这张图是什么"移到"证据在哪段、下一步应该调用什么工具"。

`[判断]` 这一阶段保留了简单的视觉接入接口，却重新打开训练日程、视觉初始化和交互接口的设计空间。读者应分别检查视觉梯度是否稳定、无图对照是否掉分、工具执行是否真的改善任务，而不是用一个"原生多模态"标签概括它们。

### 并行的一支：早融合与"从一开始就多模态"

[Gemini 1.0](../../papers/arxiv-2312.11805/README.md)（2023 年 12 月）的官方报告只写到：视觉编码借鉴 Flamingo、CoCa 与 PaLI，区别是模型"从一开始就是多模态"，能用离散图像 token 直接输出图像，支持可变输入分辨率；Gemini Ultra 的 MMMU 为 62.4%。参数量、视觉部件结构和训练数据都未公开；长上下文的后续版本见 [Gemini 1.5](../../../llm/papers/arxiv-2403.05530/README.md)。[Chameleon](../../papers/arxiv-2405.09818/README.md)（2024 年 5 月，Meta）是公开细节最完整的早融合模型：512×512 的图像量化成 1024 个离散 token（码本 8192），与文字共用词表，从零在约 10T token 上训练 34B 模型，图文可以交错生成。做不好的场景：作者自述分词器重建多文字图像很差，给重 OCR 任务设了上限；共享全部权重时各模态"竞争"使范数缓慢增长，训练后期在 bf16 下发散（不做图像生成的消融不发散），要加 QK-Norm 才稳定；VQAv2 上 LLaVA-1.5 仍高于它。`[判断]` 本页收录的开源理解模型（Qwen、InternVL、DeepSeek-VL、Kimi-VL、Molmo）都用连续视觉特征加 MLP，没有走离散图像 token；InternVL3 的"原生"指训练日程，不是 Chameleon 式的早融合。理解与生成怎样统一，见[视觉生成](../generation/README.md)与[观点页：生成收敛](../../../perspectives/generative-convergence.md)。

## 技术地基

- **ViT 与视觉 token 数**：图像切成 P×P 的块，token 数 N = HW/P²；336 像素、14 像素块时 N = 576。连接器的 2×2 合并或 pixel shuffle 再把 N 除以 4。见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 13 节与 [ViT 精读](../../papers/vit/README.md)。
- **图文对比训练的视觉塔**：CLIP、SigLIP 用整张图与一句话做对比学习，特征天然靠近语言；Cambrian-1 指出这类特征的行为像词袋，空间细节弱。训练方法见[图文对齐](../alignment/README.md)，性质见[视觉表征](../visual-representation/README.md)。
- **交叉注意力与序列拼接**：Flamingo 让文字作查询、视觉作键值；LLaVA 把视觉 token 和文字 token 拼成一条序列做自注意力。机制见 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)。
- **旋转位置编码的多维扩展**：RoPE 把位置写成按频率旋转的角度；二维 RoPE 给图像块分别编行列号，M-RoPE 再加时间维。RoPE 本身见 [LLM 架构方向](../../../llm/fields/architecture/README.md)。
- **冻结、解冻与灾难性遗忘**：哪些参数在哪个阶段更新，决定了保住旧能力还是学会新能力，原理见[迁移与元学习讲义](../../../foundations/lessons/05c-transfer-meta-learning.md)第 2–3 节。
- **后训练与 MoE**：SFT、DPO、可验证奖励 RL 见 [LLM 后训练](../../../llm/fields/posttraining/README.md)；DeepSeek-VL2、Kimi-VL、Qwen3-VL 的 MoE 见 [SSM、GNN 与 MoE 讲义](../../../foundations/lessons/18-ssm-gnn-moe.md)。

## 主要路线与团队偏好

[判断] 到 2024 年，本页所列开源理解模型的接入方式明显收敛，差异转到视觉塔、分辨率策略、语言侧结构和数据开放程度；2026 年的后继重新打开了视觉初始化与联合训练日程的选择。

| 团队 | 押注 | 代表 | 代价与后来的修正 |
|---|---|---|---|
| Google DeepMind / Google Research | 复用自家最大的单模态模型，先冻结后接（Flamingo 冻 LLM，PaLI 冻 ViT），再到"从一开始就多模态"的 Gemini | Flamingo、PaLI、Gemini | 三篇都不公开代码或权重，Gemini 报告不写结构细节 |
| Salesforce | 冻结两端、只训轻量 Q-Former | BLIP-2 | 不会上下文学习；Q-Former 被 MLP 取代 |
| Wisconsin 与 Microsoft | 最简结构、公开数据、低成本 | LLaVA、LLaVA-1.5 | 视觉侧受限于 336 像素的 CLIP，幻觉与分辨率相关 |
| 阿里 Qwen | 多阶段冻结日程，坐标写成文字的定位，原生动态分辨率，视频统一进位置编码 | Qwen-VL → Qwen2-VL → Qwen2.5-VL → Qwen3-VL | 视觉塔三代三换（DFN 初始化 → 从零训练 → SigLIP-2），M-RoPE 与绝对时间编号被下一代自己改掉；Molmo 人评中 Qwen2-VL 偏弱 |
| 上海人工智能实验室 InternVL | 大视觉编码器（6B）、切块高分辨率、开放权重并逐步开放数据 | InternVL → 1.5 → 2.5 → 3 | InternViT-6B 的对比预训练"收益有限"，改用下一词预测损失继续训练；连接器从 8B 中间件退回 MLP |
| DeepSeek | 保住语言能力、MoE 语言侧 | DeepSeek-VL → DeepSeek-VL2 | 混合编码器被切块取代；VL2 只支持少量图、上下文 4K |
| 月之暗面 Kimi | Kimi-VL 用 MoE、原生分辨率和长思维链 RL；K2.5 加强图文联合训练与视觉工具，K3 从零训练视觉塔 | Kimi-VL → K2.5 → K3 | Kimi-VL 自述模型规模与注意力参数偏小；K3 报告从零初始化的视觉梯度更稳定 |
| AI2 | 权重、数据、代码全开放，不蒸馏闭源 VLM；用"指向"做接地 | Molmo / PixMo | 计数上限 40；Arena 上仍落后闭源模型 |
| NYU | 以视觉为中心：用 VLM 评测视觉编码器，组合多种编码器 | Cambrian-1 | 未用任意分辨率 |
| Meta | 早融合、离散图像 token、图文交错生成 | Chameleon | OCR 受分词器限制，训练稳定性要专门处理 |

`[判断]` 团队偏好（同一团队两篇以上、有替代方案时仍重复同一选择）：Qwen 在 Qwen-VL、Qwen2-VL、Qwen2.5-VL 中都用"先训视觉侧、再全量解冻、SFT 冻结 ViT"的三段日程，都把定位坐标写成纯文字；InternVL 在 1、1.5、2.5、3 中都保留自研 InternViT（大模型用 6B），1.5 起都用切块加 pixel shuffle；DeepSeek 在 VL 与 VL2 中都显式控制文本与多模态数据的比例（VL 至少 70% 文本，VL2 为 70% 多模态、30% 文本），VL 结论中承诺的 MoE 在 VL2 兑现；Google 在 Flamingo 与 PaLI 中都冻结一端的预训练模型以保住已有能力。

`[判断]` 团队之间的竞争直接写在论文里：InternVL 2.5 用"只用 Qwen2-VL 十分之一的 token"论证大视觉编码器；Molmo 用人评指出 Qwen2-VL 学术分与用户体验不一致；Kimi-VL 以 DeepSeek-VL2 的固定尺寸编码器和 4K 上下文为出发点；DeepSeek-VL2 按激活参数与 InternVL2、Qwen2-VL 比；InternVL3 的首图把 Qwen2.5-VL 与 Gemini 2.5 Pro 并列。收敛的部分：ViT + MLP + LLM，动态或切块高分辨率，中段解冻视觉塔，训练流程对齐 LLM 后训练，语言侧走向 MoE（DeepSeek-VL2、Kimi-VL、Qwen3-VL）。分化的部分：视觉塔自训还是借用 SigLIP；切块还是原生；数据开放到哪一层。

## 与 VLA 的共性

结论：VLA 的骨干就是 VLM，VLM 的每个坑都会原样传到机器人上。

[RT-2](../../../robotics-embodied/papers/arxiv-2307.15818/README.md) 微调 PaLI-X 与 PaLM-E，[OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 的底座 Prismatic 把 DINOv2 与 SigLIP 两路特征拼接后经两层 MLP 投影进 Llama 2，接口与 LLaVA 相同，[π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md) 建在 Google 的 3B PaliGemma 上，[InternVLA-A1](../../../robotics-embodied/papers/arxiv-2601.02456/README.md) 以 InternVL3 和 Qwen3-VL 为底座，[Qwen-VLA](../../../robotics-embodied/papers/arxiv-2605.30280/README.md) 从 Qwen 的 VLM 扩展而来。`[判断]` 三个坑是共通的：（1）视觉塔冻结：Cambrian-1 发现解冻普遍有益，OpenVLA 冻结视觉编码器成功率从约 70% 降到 47%；（2）空间与接地：Qwen2.5-VL 改用绝对像素坐标、Molmo 用"指向"回答问题，Molmo 作者明确设想机器人"指向要抓的物体"；Qwen2-VL 在视觉语言导航上远落后专用模型；（3）语言能力被挤掉：DeepSeek-VL 的语言退化与 VLA 一侧 Knowledge Insulation 指出的"动作头梯度损伤 VLM"是同一类问题，处理方式都是保留原任务数据或隔离梯度（见 [VLA 方向](../../../robotics-embodied/fields/vla/README.md)主线历史第 4、5 节）。

## 用什么衡量进展

benchmark 的替换就是目标的迁移：

- **2022 年：学术 VQA 与描述**。VQAv2、OK-VQA（需要外部知识的问答）、COCO 与 NoCaps 描述（CIDEr 分）、TextVQA（图中文字问答）。Flamingo 用少样本、BLIP-2 用零样本、PaLI 用微调，三种口径并存。
- **2023 年：面向指令模型的综合考卷与幻觉**。MME（是非题感知与认知）、MMBench（选项循环打乱的多选题）、SEED-Bench、LLaVA-Bench（由 GPT-4 给相对评分的开放对话）与 MM-Vet、POPE（物体有无的是非题，分随机、热门、对抗三种负样本）。
- **2023–2024 年：知识推理与文档**。MMMU、MathVista；DocVQA、InfoVQA（信息图）、ChartQA、OCRBench；HallusionBench 等更难的幻觉评测。
- **2024 年：只能靠看的题**。MMStar（1500 道人工核过的必须看图的题）、Cambrian-1 的 CV-Bench、RealWorldQA、V*（超高分辨率中找小物体）；以及人评 Elo（Molmo）。
- **2025 年：推理、长视频与智能体**。MathVision、Video-MME、LongVideoBench、MMLongBench-Doc（长文档）、ScreenSpot-Pro 与 OSWorld（看屏幕操作电脑）。

**已知的口径问题**：
- **盲答与泄漏**：MMStar 与 Cambrian-1 的数字见历史第 6 节；Cambrian-1 用主成分分析把常用 benchmark 分成"综合、知识、图表与 OCR、视觉中心"四簇，MMMU 与其他 benchmark 几乎不相关。
- **是非题的偏置**：POPE 的正负样本 1:1，一律答"是"也能拿到约 50% 准确率，所以它同时报 F1 和"是"的比例；它自述只测物体有无，回答里不含 yes/no 字样时会误判。
- **学术分与真实使用**：Molmo 的人评与学术分整体一致，Qwen2-VL 是例外；InternVL 2.5 提醒 OpenCompass 榜单只由 8 个学术 VQA 组成；Cambrian-1 称只按 benchmark 优化会得到"答题机器"，在训练数据里加系统提示才保住对话能力。
- **同名不同测**：LLaVA-1.5 表中原版 LLaVA-7B 的 POPE F1 为 70–76，POPE 原文里同名模型为 67–69，评测版本与设置不同；Chameleon 的人评一致性 Krippendorff α 只有约 0.34。跨论文比较要对齐评测代码、提示和是否用 CoT（InternVL 2.5 的 MMMU 70.1 是 CoT 结果）。评测方法的一般问题见[评测方向](../../../cross-domain/fields/evaluation/README.md)。

## 当前开放问题

- **视觉塔与连接器怎样训？** 解冻视觉塔：Cambrian-1 说普遍有益，Qwen 系列只在中段解冻；单独的连接器对齐阶段：DeepSeek-VL 发现加数据无益，Molmo 发现可以跳过，Cambrian-1 却发现更多适配数据更好。三者的视觉塔、数据和规模都不同，没有一篇做过同条件对照。入口：[Cambrian-1](../../papers/arxiv-2406.16860/README.md)、[Molmo](../../papers/arxiv-2409.17146/README.md)、[DeepSeek-VL](../../papers/arxiv-2403.05525/README.md)。
- **分辨率、token 与多层特征怎样取舍？** 原生分辨率、切块、Cambrian-1 的 SVA（空间感知的连接器，只用 576 个 token，在图表、OCR 与视觉中心类 benchmark 上胜过用 2880 个 token 的模型）、Qwen3-VL 的 DeepStack 多层注入是四种回答。入口：[Qwen2-VL](../../papers/arxiv-2409.12191/README.md)、[InternVL 1.5](../../papers/arxiv-2404.16821/README.md)、[Qwen3-VL](../../papers/arxiv-2511.21631/README.md)。
- **怎样确认模型真的在看？** 物体幻觉、盲答、CoT 中途丢掉视觉线索、SFT 留下的错误先验（计数、读表），都说明"答对"不等于"看对"。入口：[POPE](../../papers/arxiv-2305.10355/README.md)、[MMStar](../../papers/arxiv-2403.20330/README.md)、[Qwen2.5-VL](../../papers/arxiv-2502.13923/README.md)、[Qwen3-VL](../../papers/arxiv-2511.21631/README.md)。
- **"后接"会被原生多模态取代吗？** Gemini 不公开细节，Chameleon 受分词器与稳定性限制，InternVL3 只把训练日程合并；Qwen3-VL 把"统一理解与生成"列为下一步。入口：[Chameleon](../../papers/arxiv-2405.09818/README.md)、[InternVL3](../../papers/arxiv-2504.10479/README.md)、[观点页：生成收敛](../../../perspectives/generative-convergence.md)。

## 阅读顺序

1. [LLaVA 精读](../../papers/llava/reading.md)：先看清基线的数据流、两阶段里冻结和训练的部分、损失只算在哪些 token 上。
2. [LLaVA-1.5](../../papers/arxiv-2310.03744/README.md)：同一结构上的受控对照，看 MLP、分辨率、格式提示各贡献多少，以及幻觉与分辨率的关系。
3. [Flamingo](../../papers/arxiv-2204.14198/README.md) 与 [BLIP-2](../../papers/arxiv-2301.12597/README.md)：两种被放弃的接法，重点看它们为什么冻结 LLM、消融里什么最重要。
4. [POPE](../../papers/arxiv-2305.10355/README.md)、[MMStar](../../papers/arxiv-2403.20330/README.md)、[Cambrian-1](../../papers/arxiv-2406.16860/README.md)：在读更多模型之前先学会怀疑分数。
5. [Qwen2-VL](../../papers/arxiv-2409.12191/README.md) → [Qwen3-VL](../../papers/arxiv-2511.21631/README.md)，对照 [InternVL 2.5](../../papers/arxiv-2412.05271/README.md)：一个团队三代内改了什么，另一个团队为什么押了相反的视觉塔。
6. [LLM 后训练](../../../llm/fields/posttraining/README.md)与 [VLA 方向](../../../robotics-embodied/fields/vla/README.md)：把 VLM 的训练流程和坑放回上下游。

## 批注

**易误读**

- BLIP-2 的"高 8.7 个百分点"是零样本 VQAv2 的 65.0 对 Flamingo-80B 的 56.3（BLIP-2 Table 1–2）；Flamingo 的 VQAv2 有 32-shot（67.3）与微调（82.0）两个数，后者解冻了视觉编码器并把输入升到 480（Flamingo 附录 B.2.2）。
- Flamingo 的"下降 17%、8.0%、12.9%、4.2%"是 Flamingo-3B 在 5 个开发集 benchmark 上 4-shot 的归一化总分变化，用的是缩短的训练日程（Flamingo §3.3、Table 3）。
- LLaVA-1.5 的 MME 809.6 → 1323.8 是 7B、224 分辨率下只加 VQAv2 与格式提示的结果（LLaVA-1.5 Table 2）；"12 个 benchmark 中 11 个领先"按其 Table 3–4 的对照模型统计，带 * 的数据集训练时见过训练集图像。
- Qwen2-VL 的 InfoVQA 数字来自 Qwen2-VL-7B 的 Table 7，固定 token 时按 token 数缩放并保持长宽比。
- InternVL 2.5 的"1/10 token"比较的是 InternVL2.5-78B 约 120B token 与 Qwen2-VL 累计 1.4T token（InternVL 2.5 Table 3 说明），两者的数据组成不同，不是同条件消融。
- InternVL3 的"原生多模态预训练"仍从预训练好的 LLM 基座（Qwen2.5、InternLM3）和 InternViT 初始化（InternVL3 §2.1），与 Chameleon 的从零早融合不是一回事。
- MMStar 的 GeminiPro 42.9% 与 Sphinx-X-MoE 43.6% 都是不输入图像时的 MMMU 成绩（MMStar §1）；Cambrian-1 的"差距不到 5%"是 23 个模型开图与关图平均分之差（Cambrian-1 §3.1、Fig.3）。
- DeepSeek-VL 的"至少 70% 文本"与 DeepSeek-VL2 的"70% 多模态、30% 文本"出自不同阶段的数据配方，后者基座已换成 DeepSeekMoE（DeepSeek-VL §1、DeepSeek-VL2 §3.2）。
- 旧路线图的提醒仍然成立：LLaVA 的 85.1 是 GPT-4 给出的相对评分，ScienceQA 的 92.53 是与 GPT-4 集成后的结果，都不是单模型准确率（见 [LLaVA 精读](../../papers/llava/reading.md)）。

**2026 年节点的证据边界**

- Kimi K2.5 的训练时机对照与 zero-vision SFT 见 [v2 §2.1–2.3](https://arxiv.org/html/2602.02276v2#S2)；"zero-vision"只修饰 SFT 数据，不修饰预训练或 RL。
- Qwen3.5 的依据是[官方模型卡](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)，不是未公开训练过程的独立复现；Kimi K3 的初始化对照见 [v2 §2.4、Fig.6](https://arxiv.org/html/2607.24653v2#S2.SS4)，结论限定于其训练规模与配方。
- Qwen3.8-Omni 的工具辅助与默认评测分列；其工具框架和模型能力的边界见报告 §5–7。将这些工作串成"共同训练与反复取证"是本页的跨论文判断。

**判断的支撑论文**（各行见 [synthesis.csv](synthesis.csv)）

- "接入接口收敛后，训练日程、视觉初始化与交互接口仍可改变"（节点 8 与团队表前的判断）：Kimi K2.5 §2.1、Table 1 比较视觉注入时机，§2.2–2.3 区分文本 SFT 与视觉 RL；Kimi K3 §2.4、Fig.6 保留 ViT + MLP，却改为从零训练视觉塔；Qwen3.8-Omni §5–7 报告音视频工具接口。边界：Qwen3.5 模型卡不是早融合的受控消融；K3 的结论限于其训练规模；接入接口相同不意味着训练过程相同。
- Kimi 表中各阶段事实：Kimi-VL §2.1、§2.4 与 §5 支撑原生分辨率、长思维链 RL 和容量局限；Kimi K3 §2.4 支撑初始化与梯度稳定性比较。Kimi-VL 的未来计划包含扩规模，但两份报告没有证明这就是 K2.5/K3 每项设计变化的原因。
- "冻结 LLM 被混文本取代"：Flamingo Table 3 (viii)；DeepSeek-VL §3.2.2 与 Fig.4；Kimi-VL Fig.4（凡更新 LLM 的阶段都是联合训练）。反例：BLIP-2 冻结 LLM 仍拿到当时最好的零样本 VQAv2。
- "重采样器被放弃"：LLaVA-1.5 §3.2 与附录 C；InternVL 1.5 Fig.3（MLP 投影）；Qwen2-VL §2.1（2×2 合并 MLP）。反例：Cambrian-1 的 SVA 仍是一种带空间先验的查询式聚合，在 576 token 下于图表、OCR 与视觉中心类 benchmark 上胜过 2880 token 的模型（Cambrian-1 Table 9），说明"查询式"本身并未被证伪，被放弃的是"强瓶颈 + 冻结 LLM"的组合。
- "视觉塔中段解冻、SFT 再冻"：Qwen-VL §3.3、Qwen2-VL §2.2、Qwen2.5-VL §2.3.4；Cambrian-1 Finding 4；OpenVLA Table 1。反例：PaLI 主预训练冻结 ViT 反而略好（PaLI Table 15），Qwen3-VL 的 S0 也冻结视觉塔。
- 团队偏好与竞争：Qwen 三代的训练段落（Qwen-VL §3、Qwen2-VL §2.2、Qwen2.5-VL Table 2）；InternVL 2.5 Table 1–3；DeepSeek-VL §1 与 §5、DeepSeek-VL2 §3；Molmo §5；Kimi-VL §1。边界：团队竞争只取论文中明写的对比，没有推测动机。
- "三个坑与 VLA 共通"：Cambrian-1 Finding 4、OpenVLA Table 1；Qwen2.5-VL §2.2.1、Molmo §1；DeepSeek-VL §3.2.2 与 VLA 方向第 5 节的 Knowledge Insulation。证据是两个领域各自的发现，没有论文直接做过跨领域对照。
- "开源理解模型不走离散图像 token"：只覆盖本页收录的模型；Chameleon 与 Gemini 是反例方向的证据。

**与其他论文的关联**

- LLaVA 的视觉塔取 CLIP 倒数第二层，[视觉表征方向](../visual-representation/README.md)把它作为"全局与局部拉扯"的例子；Cambrian-1 把 DINOv2 这类自监督编码器拼进来，与 OpenVLA 拼接 DINOv2 和 SigLIP 是同一个选择。
- InternVL 2.5 的复读问题与 [DeepSeek LLM](../../../llm/papers/arxiv-2401.02954/README.md) 中"数学 SFT 数据越多越容易无限重复"同源；Kimi-VL 的长度惩罚与 [Kimi k1.5](../../../llm/papers/arxiv-2501.12599/README.md) 的长度控制一脉相承；Qwen3-VL 的强到弱蒸馏与 [Qwen3](../../../llm/papers/arxiv-2505.09388/README.md) 的 on-policy 蒸馏是同一套做法。
- Qwen2-VL 的原生分辨率引用 NaViT（Dehghani 等）的打包做法，Kimi-VL 的 MoonViT 也沿用这一打包；视频侧的 M-RoPE 与时间戳 token 接到[视频与时序方向](../video-temporal/README.md)。
- Chameleon 的离散图像 token 与 DALL·E、Parti 的自回归生成同属一支，见[视觉生成方向](../generation/README.md)。

**未核实 / 待验证**

- Gemini 1.0 的视觉编码器结构、参数量与训练数据，官方报告未写；本页只引用报告 §2 的原话。Gemini 2.x 的官方报告本轮没有打开。
- Chameleon 权重的实际发布范围与许可，论文未声明，没有另查官方博客。
- InternVL3 承诺公开训练数据，脚注称数据仍在整理；实际发布情况没有另查。
- BLIP-2、Qwen-VL、DeepSeek-VL、MMStar 的正式发表会议没有核实，本页只写 arXiv 时间。
- LLaVA-NeXT（LLaVA-1.6）、LLaVA-OneVision、InternVL3.5、PaliGemma 本轮没有打开原文，只在其他论文的引用中出现。
- Prismatic 的原文没有打开，OpenVLA 底座的描述来自 [OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)第 2 节。
