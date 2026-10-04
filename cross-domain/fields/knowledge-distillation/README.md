# 知识蒸馏：让一个模型学另一个模型

> 状态：领域入门页（§3 模板）· v1 · 依据 [synthesis.csv](synthesis.csv)（15 篇）
>
> 速览：
> 1. 知识蒸馏让学生模型去学教师模型的输出，而不只学人标的答案。教师给的东西从"伪数据上的标签"（2006）一路变成"逐 token 的概率分布"（2015 起）、"中间层特征"（FitNets、MiniLM）、"整段推理轨迹"（DeepSeek-R1）和"学生自己写出的每个 token 上的评分"（on-policy 蒸馏）。
> 2. 用途换了三次：压缩部署成本（2006–2020）→ 给小模型加训练信号、把大模型的推理能力搬下来（Gemma 2、DeepSeek-R1、Qwen3）→ 把多个专家合并成一个模型（2026 年的 MiMo-V2-Flash、GLM-5、DeepSeek-V4、Kimi K3；视觉里 NVIDIA 的 RADIO 系列合并 SigLIP 2、DINOv3、SAM 3）。
> 3. 每个阶段都有原文记录的坑：迁移数据不够时师生差距拉大（Ba & Caruana）；中间层提示过度正则（FitNets）；4 层 BERT 学生在 CoLA 上差教师约 9 分（TinyBERT）；教师越大学生不一定越好（MiniLM 要加助教模型，Gemma 3 发现结论随训练长度反转）；只在教师轨迹上学会出现训练与生成不一致（GKD、MiniLLM）；on-policy 蒸馏在思维模式不兼容或教师没有新东西时失败，越往长轨迹后部教师的信号越弱（清华 2026）。
> 4. `[判断]` 站在 2026 年看，蒸馏已经从"训练完之后的压缩步骤"变成后训练的主干之一：大规模 RL 负责造出各领域的教师，蒸馏负责把它们合成可发布的模型。逐 token 估计（Kimi K3、MiMo）与全词表 logit（DeepSeek-V4）两种做法目前没有同条件对照。

知识蒸馏是一种训练方法，目标很明确：在给定的部署或训练成本下，让学生尽量接近教师（或几个教师）的能力。它用"学生与教师的差距、学生与同尺寸从头训练的模型的差距、付出的算力"来衡量，所以本页按 STYLE §3 的任务模板写，没有用 §3.6 的研究对象变体（理由见批注）。2006–2015 年四篇原始文献的来源记录在 [history.md](history.md)。

## 这个领域在解决什么

结论：蒸馏回答"怎样让一个便宜的模型学到一个昂贵模型已经学会的东西"，各家做法的区别在于教师传什么、在谁写出的数据上传。

一个具体任务：DeepSeek-R1 有 671B 参数，能在 AIME 数学竞赛题上写出几千 token 的推理；想要一个 7B 模型在手机或单卡上做同样的事。只用人写的解答训练 7B 模型，它学到的是答案格式；如果让它学 R1 写出的推理过程、甚至学 R1 在每个位置上对下一个 token 的概率分布，它能拿到多得多的信息。DeepSeek-R1 的 7B 蒸馏模型在 AIME 2024 上 pass@1 为 55.5%，同期的 GPT-4o 为 9.3%（[DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) Table 15）。

做法可以按两条轴来分：

| 教师传什么 | 一句话的直觉 | 代表 |
|---|---|---|
| 标签或整段输出（序列级） | 教师当标注员，给大量数据打标签或写答案，学生照着学 | Model Compression（2006）、DeepSeek-R1 的 80 万条蒸馏数据 |
| 输出分布（logit 级） | 不只告诉学生对的是哪个，还告诉它错的选项各有多像 | Hinton 等（2015）的温度软目标；Gemma 2/3 的预训练目标 |
| 中间表示 | 让学生的某一层去预测教师某一层的特征 | FitNets 的提示层、MiniLM 的注意力关系、RADIO 的逐块特征 |

| 数据由谁写出 | 一句话的直觉 | 代表 |
|---|---|---|
| 教师或固定数据集（离线、off-policy） | 学生只见过"走对的路" | 2023 年以前的大多数蒸馏；R1 蒸馏 |
| 学生自己（在线、on-policy） | 学生自己走，教师在学生走到的每一步打分 | GKD、MiniLLM、Qwen3、DeepSeek-V4、Kimi K3 |

后一条轴读者在机器人里见过：on-policy 蒸馏和 DAgger 是同一种结构（见"不同模态的差异"一节）。

## 现状：最新的官方材料怎样用蒸馏

结论：2026 年公开了后训练细节的中国大模型团队（小米、智谱、DeepSeek、Moonshot）都把"先训练领域专家、再用 on-policy 蒸馏合成一个模型"写进了正式流程，Qwen 在 2025 年已把 on-policy 蒸馏用于小模型；Google 的做法另成一路，把蒸馏放进预训练；视觉一侧，多教师蒸馏成了合并几个基础编码器的标准做法。下表从新到旧排列。

| 材料（日期） | 蒸馏放在哪里 | 教师与学生 | 目标的写法 | 原文写出的问题或边界 |
|---|---|---|---|---|
| [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)（Moonshot，arXiv v2 2026-08-07） | 后训练第三段：SFT → 领域 × 推理强度的 RL 专家 → 多教师 on-policy 蒸馏（MOPD） | 3 档推理强度 × 多个领域共 9 个专家 → 1 个统一模型 | 每个 token 的奖励 = 教师对数概率 − 学生对数概率，截断到 ±Rmax，直接接进 RL 框架 | 试过更细的 top-k 蒸馏目标，收敛速度与最终效果都没有明显优势（§4.1.3） |
| [Gemma 4](https://arxiv.org/abs/2607.02770)（Google DeepMind，报告日期 2026-06-19） | 预训练与后训练"与 Gemma 3 相近" | 未写明教师 | 报告没有重述蒸馏细节 | 最新一代的官方报告不再单写蒸馏，只能沿 Gemma 3 理解（见批注） |
| [RADIO1D](../../../multimodal/papers/arxiv-2607.03624/README.md)（NVIDIA，2026-07-07） | 视觉编码器的整个训练 | SigLIP 2、DINOv3、SAM 3 → 输出长度可变的 1D token 序列的学生 | 多教师特征蒸馏加只在训练时用的解码器 | 出发点是 VLM 训练中视觉特征越来越抽象、空间一致性变差，少数 token 就能概括全图（摘要） |
| [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)（DeepSeek，2026，原文称预览版） | 把 V3.2 后训练里的混合 RL 阶段整段换成多教师 on-policy 蒸馏 | 十多个领域教师（数学、代码、agent、指令遵循等）→ 1 个统一模型 | 按权重加和的反向 KL（学生分布相对每个教师），用全词表 logit 计算 | 常见的逐 token 估计方差大、常致训练不稳；全词表要缓存教师最后一层隐状态、按教师排序样本才能放进显存（§5.1.2、§5.2.2） |
| [Rethinking OPD](../../../llm/papers/arxiv-2604.13016/README.md)（清华等，2026-04-15） | 研究 on-policy 蒸馏本身 | 1.5B–7B 的推理模型 | — | 思维模式不兼容或教师没有学生没见过的能力时失败；轨迹越长教师信号越弱 |
| [GLM-5](../../../llm/papers/arxiv-2602.15763/README.md)（智谱、清华，2026-02） | 顺序做推理 RL、agent RL、通用 RL 之后，最后一段做跨阶段 on-policy 蒸馏 | 各阶段的最终检查点当教师 | on-policy 蒸馏 | 顺序优化多个目标会累积损失先前学到的能力（§3.5） |
| [C-RADIOv4](../../../multimodal/papers/arxiv-2601.17237/README.md)（NVIDIA，2026-01-24） | 视觉编码器的整个训练 | SigLIP2-g、DINOv3-7B、SAM3 → 412M 与 631M 学生 | 摘要向量与逐块特征的多教师蒸馏 | SAM3 当教师在所选评测上没有带来提升；学生会模仿教师的固定模式噪声，要随机平移对齐 |
| [MiMo-V2-Flash](https://arxiv.org/abs/2601.02780)（小米，v2 2026-01-08） | 后训练：通用 SFT → 领域 RL/SFT 教师 → MOPD | 多个领域教师 → 1 个学生 | 逐 token 反向 KL 当作稠密奖励，再加上结果奖励模型的优势 | 动机是"跷跷板"：提升一项能力会让其他能力退步（§4.1） |
| [Qwen3](../../../llm/papers/arxiv-2505.09388/README.md)（阿里巴巴，2025-05） | 小模型的后训练：离线蒸馏 → on-policy 蒸馏 | Qwen3-235B-A22B 或 32B → 0.6B 到 30B-A3B 共 6 个模型 | 学生在自己的回答上对齐教师 logit，最小化 KL | 对照只做了 8B、只用数学与代码题（Table 21） |
| [DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md)（DeepSeek，2025-01；Nature 正式版 2025） | R1 训练完成后，把 80 万条数据给开放小模型做 SFT | R1 → Qwen2.5 1.5B–32B、Llama 3 8B/70B | 序列级：学 R1 写出的完整推理 | 蒸馏模型只做 SFT 没做 RL；超越人类边界仍需更强的基座和更大规模的 RL（附录 F） |

Google 一路的做法：[Gemma 2](../../../llm/papers/arxiv-2408.00118/README.md)（2024）的 2B、9B 不再以真实下一个 token 为目标，而以教师的下一词分布为目标；Gemma 2 的后训练还在学生自己的分布上向教师蒸馏（引用 GKD 与 MiniLLM）；[Gemma 3](../../../llm/papers/arxiv-2503.19786/README.md)（2025）所有尺寸都这样预训练，后训练用"改进版的知识蒸馏"（同样引用 GKD）。

## 主线历史

结论：每一次推进都来自上一阶段的一个具体失败：伪数据不够 → 软目标；只传输出 → 传中间层；任务内压缩 → 预训练阶段压缩；学生只见过教师的路 → 让学生自己走；一个教师 → 多个专家。

| 时期 | 代表 | 教师传什么 | 数据由谁写出 | 留下的问题 |
|---|---|---|---|---|
| 2006 | Model Compression | 集成的标签 | 合成的伪数据 | 伪数据分布不对时失效 |
| 2014–2015 | Ba & Caruana、Hinton 等 | logit、温度软目标 | 原训练集或无标签集 | 只传输出，深而窄的学生训不动 |
| 2015 | FitNets | 中间层特征 | 训练集 | 选哪一层、会不会过度正则 |
| 2019–2020 | DistilBERT、TinyBERT、MiniLM | 输出 + 隐状态 / 注意力 | 预训练语料 + 任务数据 | 小学生在难任务上差距大；师生差距太大时变差 |
| 2023–2024 | MiniLLM、GKD、Gemma 2/3 | 逐 token 分布 | 学生自己生成（on-policy）；或海量预训练 token | 教师越大不一定越好；成本 |
| 2025 | DeepSeek-R1、Qwen3 | 整段推理轨迹；在学生回答上的 logit | 教师（R1）；学生（Qwen3） | 学生上限是教师；只验证了数学与代码 |
| 2026 | MiMo-V2-Flash、GLM-5、DeepSeek-V4、Kimi K3 | 多个专家的逐 token 分布 | 学生自己生成 | 逐 token 与全词表之争；长轨迹上信号变弱 |

### 1 用教师给数据打标签（2006）

留下的问题：最好的分类器常是成百上千个模型的集成，存不下、跑不动；Buciluă、Caruana、Niculescu-Mizil 的例子是 Google 的大规模测试集、PDA 的存储和助听器的算力。

改变：[Model Compression](../../papers/url-cornell-compression.kdd06/README.md)（Cornell，KDD 2006）让集成去标注一大批无标签数据，再用这批数据训练一个神经网络去模仿它。没有现成的无标签数据时，作者提出 MUNGE：在相邻训练样本之间交换、扰动属性值，合成贴近真实分布的伪数据。8 个二分类问题上，模仿网络的平均 RMSE 0.264，集成为 0.263，直接用原始 4k 训练集训练的网络为 0.282；压缩拿到了可能提升的 97%，而模型小 100 到 100,000 倍、快 100 到 10,000 倍。

做不好的场景：
- ADULT 上压缩无效：模仿网络只比直接训练的网络略好，还不如集成库里最好的单模型。作者给出两个猜测：这个数据集有 14、16、41 种取值的离散属性，独热展开后神经网络不擅长；或者 MUNGE 造不出这类数据（§3）。
- 伪数据分布与真实流形重叠太少时，标签再准也覆盖不到要学的区域；分布太宽时大部分样本浪费在无关区域（§2）。

### 2 匹配 logit 与温度软目标（2014–2015）

留下的问题：深网络已经在语音和视觉上领先；它的优势来自深度本身，还是来自训练方法？压缩能否用在深网络上？

改变：
- [Ba & Caruana](../../papers/arxiv-1312.6184/README.md)（Toronto、Microsoft Research，NIPS 2014）让只有一个隐藏层的浅网络去回归深网络 softmax 之前的 logit（L2 损失），理由是 logit 保留了各类之间的相对关系。在 TIMIT 上，参数量相同的浅网络直接训练比 CNN 低 3.5–4.1 个百分点，模仿训练后能接近深模型。
- [Hinton、Vinyals、Dean](../../papers/arxiv-1503.02531/README.md)（Google，2015）把它推广成"蒸馏"：教师与学生的 softmax 都除以温度 T，让错误选项的小概率也带出信息；软目标的梯度按 1/T² 缩放，所以与硬标签合用时要乘回 T²。原文证明高温极限下蒸馏就等价于 Ba & Caruana 的 logit 匹配（§2.1）。在 2000 小时的 Android 语音数据上，10 个模型的集成帧准确率 61.1%，基线 58.9%，蒸馏出的单模型 60.8%，拿到了集成提升的 80% 以上。只用 3% 的数据时，硬标签训练的同一模型过拟合到 44.5%，软目标训练的到 57.0%（Table 5）。

做不好的场景：
- 迁移数据不够：TIMIT 没有额外的无标签数据，只能拿训练集本身当迁移集，教师在训练点上过拟合，师生差距随之拉大（Ba & Caruana §3.2）。
- 结构差太远：CIFAR-10 上不带卷积的网络无论多深都学不好，浅学生只能加一层卷积与池化（Ba & Caruana §4.1）。
- 迁移集里缺类：MNIST 上去掉所有"3"，学生对 3 的偏置太低，手动加 3.5 后 98.6% 的 3 能认对；只保留 7 和 8 时，调偏置前测试误差 47.3%（Hinton 等 §3）。
- 专家合不回来：Hinton 等在 JFT 上训练了一批区分易混类别的专家模型，结论写明"尚未证明能把专家的知识蒸馏回单个大网络"（§8）。这个问题十年后由多教师 on-policy 蒸馏回答（阶段 7）。

### 3 传中间层：提示与关系（2015）

留下的问题：只传输出，学生要自己找出中间表示；学生比教师更深、更窄时训练困难。

改变：[FitNets](../../papers/arxiv-1412.6550/README.md)（Montréal，ICLR 2015）让学生中间的"被引导层"经一个回归器去预测教师中间的"提示层"，分两段训练：先只对齐提示，再用蒸馏损失训练整个网络。CIFAR-10 上，约 862K 参数的 11 层学生达到 91.06%，超过约 9M 参数的 5 层教师（90.18%），参数少约 10.4 倍、推理快 4.6 倍；最深的 19 层学生（约 2.5M 参数）达到 91.61%（Table 5）。

做不好的场景：
- 提示本身是正则，被引导层选得越深，学生越容易被过度正则化，作者只取两边的中间层（§2.2）。
- 3 千万次乘法的计算预算下，标准反传训不动 5 层以上的网络，只加蒸馏也只能训到 7 层，加上提示才训到 13 层（§4.1）。软目标让训练更平滑，单靠它解决不了深窄网络的优化问题。

### 4 预训练语言模型的压缩（2019–2020）

留下的问题：BERT（2018，Google，[文献卡](../../../llm/papers/arxiv-1810.04805/README.md)）用遮蔽语言模型预训练、再对每个任务微调，BERT-base 有 110M 参数、BERT-large 有 340M。微调后的模型要上线服务、上手机，延迟和内存都不够；而此前的蒸馏多在单个任务上做，每个任务压一次。

改变：三个团队在三个位置下手。
- [DistilBERT](../../../llm/papers/arxiv-1910.01108/README.md)（Hugging Face）把蒸馏搬到预训练阶段，学生层数减半，用遮蔽语言建模、软目标、隐状态余弦三项损失训练；参数少 40%，保留 97% 的 GLUE 分数，快 60%。
- [TinyBERT](../../../llm/papers/arxiv-1909.10351/README.md)（华为诺亚方舟）逐层对齐嵌入、注意力矩阵、隐状态与预测层，并在预训练与任务微调两个阶段都蒸馏，任务阶段用 BERT 与 GloVe 做词替换扩充数据。4 层的 TinyBERT 有 14.5M 参数、快 9.4 倍，GLUE 测试集平均 77.0，教师 79.5。
- [MiniLM](../../../llm/papers/arxiv-2002.10957/README.md)（Microsoft Research）只蒸教师最后一层的自注意力分布与 value 之间的关系，省去层与层的映射，学生的层数和宽度都可以自由选。

做不好的场景：
- 难任务上差距大：DistilBERT 的 RTE 从 69.3 降到 59.9、CoLA 从 56.3 降到 51.3（Table 1）；TinyBERT 写明所有 4 层学生在 CoLA（判断句子是否合乎语法）上都与教师差距很大，它自己是 44.1 对 52.8（§4）。
- 依赖数据增强：TinyBERT 去掉任务阶段的数据增强，四项平均从 75.6 降到 68.4，CoLA 从 50.8 降到 29.8（Table 2）。
- 师生差距太大：MiniLM 写明教师与学生尺寸差距大时要先蒸到一个中等大小的"助教"模型，再蒸到学生（§3.3）。

`[判断]` 这一阶段奠定了 LLM 时代的两个习惯：在预训练阶段就蒸馏（DistilBERT → Gemma 2），以及"蒸什么"可以不止是输出（MiniLM → RADIO 的逐块特征）。

### 5 生成模型的白盒蒸馏：逐 token 分布与在线采样（2023–2024）

留下的问题：分类模型只输出一个分布；生成模型要连续写几百个 token，学生在训练时看到的是教师或数据集写好的前缀，推理时却要接着自己写出的前缀往下写，一步写偏，后面全是没见过的状态。此外，2023 年的小模型大多是拿 ChatGPT 的回答做 SFT（黑盒蒸馏），拿不到概率分布。

改变：
- [MiniLLM](https://arxiv.org/abs/2306.08543)（清华、Microsoft Research，ICLR 2024）把标准蒸馏用的前向 KL 换成反向 KL（一句话：前向 KL 逼学生覆盖教师认为可能的所有回答，反向 KL 让学生集中在教师认为好的回答上），理由是前者会让学生高估教师分布中概率很低的区域；用学生自己的采样做策略优化。它与 MiniLM 出自同一组作者（Li Dong、Furu Wei）。
- [GKD](https://arxiv.org/abs/2306.13649)（Google DeepMind，ICLR 2024）直接针对"训练时所见序列与推理时学生自己生成的序列不一致"：学生生成序列，教师在这些序列的每个位置给出分布，散度可以在前向 KL、反向 KL、JSD 之间换。T5-XL 教师、T5-Small 到 Large 学生，在摘要、翻译、GSM8K 上都好于在固定序列上的蒸馏。
- 蒸馏成为预训练目标：[Gemma 2](../../../llm/papers/arxiv-2408.00118/README.md)（2024）的动机是小模型的进步主要靠加长训练，而收益随数据量只按对数增长；改用一个更大的教师模型给出的下一词分布为目标（报告没有写明教师是哪个模型），在超过计算最优 50 倍的 token 上训练 2B 与 9B。消融中 2B 模型训 500B token，从头训练三项平均 60.3，蒸馏 67.7（Table 6）。[Gemma 3](../../../llm/papers/arxiv-2503.19786/README.md) 每个 token 按教师概率采 256 个 logit，在这些位置上学教师的分布，其余位置置零、重新归一化。
- 黑盒一侧，[CodePLAN](../../../llm/papers/arxiv-2403.13271/README.md)（LREC-COLING 2024）把大模型的"解题计划"和代码一起作为小模型的训练目标，是后来推理轨迹蒸馏的早期形态。

做不好的场景：
- 教师越大不一定越好：MiniLLM 引述已有研究，指出加大教师不保证学生变好，有时反而有害；[Busbridge 等](https://arxiv.org/abs/2502.08606)（Apple，ICML 2025）把这个"容量差距"量化成蒸馏的规模定律：学生损失按幂律变化，并在"学生相对教师的学习能力"上切换两种行为；如果只蒸一个学生、而教师还要专门训练，直接监督训练通常更划算。
- 结论随训练长度反转：Gemma 3 用一大一小两个教师蒸馏同一个学生，训练短时小教师更好，训练长时大教师更好；作者认为以往"小学生配小教师"的结论多来自短训练，此时差教师的正则效果盖过了好教师的收益（§5.4）。
- 在线采样的代价：GKD 指出 MiniLLM 要靠多种技巧压住高方差、奖励黑客与长度偏差。

### 6 推理轨迹蒸馏：蒸馏比 RL 便宜（2025）

留下的问题：2025 年初 DeepSeek-R1 与 Kimi k1.5 用大规模 RL 训出会写长推理的模型；小模型能不能自己用 RL 训到同样水平？

改变：
- [DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 用 R1 生成 80 万条数据（推理数据由第一阶段 RL 检查点拒绝采样得到），对 Qwen2.5 与 Llama 3 的 6 个基座只做 2–3 轮 SFT，不做 RL。同一个 Qwen2.5-32B 基座上，RL 一万步以上的 Qwen2.5-32B-Zero 在 AIME 2024 上 pass@1 为 47.0，蒸馏得到的 R1-Distill-Qwen-32B 为 72.6（Table 16）。作者的两条结论：把强模型蒸给小模型效果很好，小模型自己做大规模 RL 算力巨大、可能还达不到蒸馏的水平；超越人类智能的边界仍需更强的基座与更大规模的 RL。
- [Qwen3](../../../llm/papers/arxiv-2505.09388/README.md) 把小模型的后训练整个换成"强到弱蒸馏"：先离线蒸馏教师在思考与非思考两种模式下的回答，再做 on-policy 蒸馏，学生自己写回答、对齐教师 logit。从同一个离线蒸馏的 8B 检查点出发，RL 用 17,920 GPU 小时把 AIME'24 提到 67.6，on-policy 蒸馏用 1,800 GPU 小时提到 74.4；RL 没有提高 pass@64（仍为 90.0），蒸馏提到 93.3（Table 21）。
- Thinking Machines 的[博客](../../../llm/papers/thinking-machines-on-policy-distillation/README.md)（2025）在开放权重上复现了这个做法，并把差别概括成：RL 每条轨迹只教 O(1) 比特，on-policy 蒸馏教 O(N) 比特（N 是 token 数）。

做不好的场景：
- 学生的提升集中在数学：R1-Distill-Qwen-1.5B 的 AIME 2024 为 28.9（GPT-4o 9.3），GPQA Diamond 为 33.8、LiveCodeBench 为 16.9，都低于 GPT-4o 的 49.9 与 32.9（Table 15）。
- 学生的上限是教师：R1 的蒸馏模型没做 RL，作者把"加上 RL"留给社区（附录 F）；[Yue 等](../../../llm/papers/arxiv-2504.13837/README.md)发现蒸馏能引入教师的新推理模式，RL 主要在基座已有的回答里重新分配概率（详见[后训练总览](../../../llm/fields/posttraining/README.md)）。
- 证据的口径窄：Qwen3 的 RL 与蒸馏对照只在 8B、只用数学与代码题。

### 7 多教师 on-policy 蒸馏：用蒸馏合并专家（2025 末–2026）

留下的问题：一个模型要同时会数学、代码、agent、写作；多个领域一起做 RL 会互相拖累（MiMo-V2-Flash 称为"跷跷板"），顺序做 RL 又会忘掉前面学的（GLM-5 §3.5）；权重平均式的合并也会掉性能。

改变：先在各领域单独训练 RL 专家，再让一个学生在自己写出的回答上，按题目所属领域去对齐相应专家的逐 token 分布。这正是 Hinton 等 2015 年没做成的"把专家蒸回一个模型"。
- 小米 [MiMo-V2-Flash](https://arxiv.org/abs/2601.02780)（2026-01）把这一形态命名为 MOPD（多教师 on-policy 蒸馏），把逐 token 的反向 KL 当作稠密奖励，并与结果奖励模型给的优势相加（§4.4）。
- [GLM-5](../../../llm/papers/arxiv-2602.15763/README.md)（2026-02）在推理 RL、agent RL、通用 RL 之后，用前面各阶段的最终检查点当教师做跨阶段 on-policy 蒸馏，用来恢复被后续阶段冲掉的能力。
- [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)（2026）把 [V3.2](../../../llm/papers/arxiv-2512.02556/README.md) 后训练中的混合 RL 阶段整段换成多教师 on-policy 蒸馏，十多个教师，目标是按权重加和的反向 KL，理由是它避开了权重合并与混合 RL 常见的性能下降（§5.1.2）。
- [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)（2026-07）把领域与推理强度（低、高、最高）交叉，训练 9 个专家，用 MOPD 合成一个模型，并在 K3 报告中引用 MiMo-V2-Flash、DeepSeek-V4 与 Thinking Machines 博客作为这一做法的来源。
- 同样的做法也出现在图像生成里：[Qwen-Image-2.0-RL](../../../multimodal/papers/arxiv-2606.27608/README.md) 用在策略蒸馏把文生图与编辑两个 RL 教师合成一个学生，效果好于混合数据直接做 RL。

做不好的场景：
- 两家对目标的判断相反：DeepSeek-V4 认为逐 token 的 KL 估计方差大、常致训练不稳，坚持全词表 logit，为此要把教师权重放在分布式存储里按需加载、只缓存教师最后一层隐状态再现场算 logit（§5.2.2）；Kimi K3 用逐 token 估计加截断，试过更细的 top-k 目标"没有明显优势"。没有同条件对照。
- 什么时候失败：[Li 等（清华，2026-04）](../../../llm/papers/arxiv-2604.13016/README.md)发现 on-policy 蒸馏成功要两个条件，师生的思维模式要兼容，以及教师得有学生训练中没见过的能力；同一家族的 1.5B 与 7B 教师在学生看来分布上几乎无法区分，所以"更强"不等于"更可学"。
- 长轨迹上信号变弱：同一篇让教师接着学生写到一半的推理往下写，学生前缀截在 1K token 时教师续写能把准确率提高 0.366，截在 16K token 时只提高 0.024（Figure 11），作者据此质疑 on-policy 蒸馏能否扩到长程 agent 任务。

`[判断]` 从这一阶段回看，2025 年初"纯 RL 造推理模型"的叙事已经被修正：大规模 RL 主要用来造出各领域的专家和数据，最终发布的模型更多由蒸馏得到。支撑与反例见批注；这一判断在[后训练总览](../../../llm/fields/posttraining/README.md)第 6 节有同一组证据。

**两种新的诊断问题。** [Rethinking OPD II](../../../llm/papers/arxiv-2609.04172/README.md)用极少提示反复采样，考察教师匹配是否受学生吸收速度限制；它仍使用大量 rollout 和逐 token 监督。[Solving Without Stopping](../../../llm/papers/arxiv-2609.37326/README.md)把数学解题、答案提取和停止行为分开，说明同一家族小学生的解题改善可以与停止退化并存。前者研究提示与学习瓶颈，后者研究评测分数背后的行为分解。

## 不同模态的差异

结论：语言模型蒸馏的是 token 分布，视觉蒸馏的是特征图，机器人蒸馏的是动作策略；三边的"教师"来源不同，坑却很像。

**视觉：从压缩到合并基础模型。**
- [DeiT](../../../multimodal/papers/arxiv-2012.12877/README.md)（Facebook AI，2020）给 ViT 加一个"蒸馏 token"去学 CNN 教师（RegNetY-16GF）的预测，只用 ImageNet-1K 就达到 85.2%；CNN 当教师比 Transformer 当教师更好，作者推测学生继承了卷积的归纳偏置。
- Meta 的 [DINOv2](../../../multimodal/papers/arxiv-2304.07193/README.md) 与 [DINOv3](../../../multimodal/papers/arxiv-2508.10104/README.md) 先训练一个最大的自监督模型，再蒸馏出一族小模型发布，蒸馏成了发布流程的最后一步。
- NVIDIA 的 [AM-RADIO](../../../multimodal/papers/arxiv-2312.06709/README.md)（CVPR 2024）不用任何标签，只用图像让一个学生经各自的适配头同时匹配 CLIP、DINOv2、SAM 的摘要向量与逐块特征；ViT-H 学生在 ImageNet k 近邻上 86.06，超过 DINOv2-g 的 83.41，零样本分类 82.93，略低于 DFN CLIP 的 83.90（Table 1）。它的后续 [C-RADIOv4](../../../multimodal/papers/arxiv-2601.17237/README.md)（2026-01）把教师换成 SigLIP2-g、DINOv3-7B、SAM3，[RADIO1D](../../../multimodal/papers/arxiv-2607.03624/README.md)（2026-07）把输出改成长度可变的 1D token 序列。

视觉一侧做不好的场景：AM-RADIO 低分辨率只训 CLIP 与 DINOv2、高分辨率才训 SAM，学生因此出现"模式切换"，输入到约 720 像素时特征突然变样（Fig.5）；C-RADIOv4 发现学生会连教师的固定模式噪声一起学去（SigLIP 2 特征图边缘的空洞、SAM 的窗口边界伪影），要对学生和每个教师施加互相独立的随机平移、只在对齐位置算损失；摘要向量的损失要按各教师嵌入的角度离散度归一化，防止某个教师压过其他教师（DINOv3-7B 的离散度 2.186，约为 SigLIP2 的 3 倍，Table 3）；SAM3 当教师在所选评测上没有带来提升。这些失败在语言模型的多教师蒸馏里有对应：多个教师的信号尺度不同，需要加权或按领域路由（DeepSeek-V4 的 wᵢ、K3 按领域与推理强度选教师）。详见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。

**机器人：特权教师与 DAgger。** 读者熟悉的四足训练流程本身就是蒸馏：先在仿真里用 RL 训练一个能看到特权信息（一句话：仿真中可得、实机上测不到的量，例如地形真值、摩擦系数）的教师，再把它蒸馏成只用真机传感器的学生。[Lee 等 2020](../../../robotics-embodied/papers/arxiv-2010.11251/README.md) 用 DAgger 蒸馏出只读本体感知历史的学生；[RMA](../../../robotics-embodied/papers/rma/reading.md) 蒸馏的对象换成了环境隐变量 zₜ：适应模块从最近 50 步的状态与动作历史回归 zₜ，数据由当前的适应模块驱动冻结的基础策略采集、由仿真里的特权编码器打标签；[Extreme Parkour](../../../robotics-embodied/papers/arxiv-2309.14341/README.md) 用同样的方式蒸馏出以深度图为输入的策略。

`[结构]` 这三者与语言模型的 on-policy 蒸馏是同一个形式：学生按自己的策略执行，到达自己会犯错的状态，再由一个"在该状态下知道正确答案"的教师打标签（[DAgger](../../../robotics-embodied/papers/arxiv-1011.0686/README.md)）。视觉语言导航里也有一例：[R2R](../../../robotics-embodied/papers/r2r/reading.md)（CVPR 2018）的基线用 student-forcing 训练，执行模型自己采样的动作，到新位置后由最短路重新计算下一步标签；作者写明它等价于在线版 DAgger。四者的标签不同：R2R 是最短路上的下一步动作，RMA 是仿真特权编码，Lee 等是教师策略的动作，Qwen3 与 DeepSeek-V4 是教师模型的 token 分布。R2R 的 student-forcing 把见过建筑上的成功率从 27.1% 提到 38.6%，没见过的建筑只从 19.6% 到 21.8%（R2R 精读 Table 1）：在策略采样修的是"只见过正确路径"，修不了"环境没见过"，这与 RMA 自述盲走机器人在下楼跌落、多条腿同时被挡这类大扰动下会失败是同一类边界。

机器人一侧做不好的场景：学生看不到的信息，教师再好也传不过去。RMA 的盲走学生要先踩到变化，历史里才有信号；同组作者的 [Agarwal 等 2022](../../../robotics-embodied/papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md) 加上前向深度相机才走上楼梯，训练仍是"先 RL、再监督蒸馏"两段。[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)把"蒸馏丢信息"列为交互式模仿的代价。

## 技术地基

结论：读本页需要五个概念，其中 KL 的方向和 DAgger 读者已经在别处见过。

- **软目标与温度**：softmax 前的分数（logit）除以温度 T 再归一化，T 越大分布越平，错误选项之间的相对大小越清楚。交叉熵、软目标与 KL 的关系见[概率分类讲义](../../../foundations/lessons/modules/objectives/02-classification-probabilities.md)第 2 节与第 8 节，第 8 节末尾专门提到蒸馏要说清温度、KL 方向和求和位置。
- **前向 KL 与反向 KL**：KL(教师‖学生) 逼学生覆盖教师所有可能的回答，KL(学生‖教师) 让学生集中在教师认为最好的回答上；同一讲义第 8 节用手算说明 KL 不对称。MiniLLM、DeepSeek-V4、MiMo-V2-Flash 都选反向 KL。
- **教师强制与暴露偏差**：自回归模型训练时总是接着正确前缀往下写，推理时接着自己写出的前缀，两者不一致叫暴露偏差。这就是机器人模仿学习里的复合误差，见[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)。
- **on-policy 蒸馏与 RL 的关系**：把"教师对数概率 − 学生对数概率"当成每个 token 的奖励，on-policy 蒸馏就能直接放进 RL 框架（K3、MiMo），只是奖励是稠密的、来自教师而非验证器。策略梯度与优势见[强化学习讲义](../../../foundations/lessons/05b-reinforcement-learning.md)，语言模型 RL 见[后训练总览](../../../llm/fields/posttraining/README.md)。
- **规模定律与计算最优**：Gemma 2 的"超过计算最优 50 倍的 token"、Busbridge 等的蒸馏规模定律，都以 [Kaplan 等](../../papers/arxiv-2001.08361/README.md)与 [Chinchilla](../../papers/arxiv-2203.15556/README.md) 的计算最优配比为参照，见[训练科学方向](../training-science/README.md)。

## 主要路线与团队偏好

结论：团队之间最大的分歧在两处：蒸馏放在预训练还是后训练，以及在线蒸馏用逐 token 估计还是全词表。

| 团队 | `[判断]` 押注 | 代表材料 | 代价与做不好的地方 |
|---|---|---|---|
| Google / Google DeepMind | 蒸馏是小模型的主训练目标：从 Hinton 的软目标，到 GKD 的在线蒸馏，再到 Gemma 2、3 在预训练里用教师分布代替真实 token | Hinton 等、GKD、Gemma 2、Gemma 3、Gemma 4 | 教师未公开；Gemma 4 报告不再写蒸馏细节 |
| DeepSeek | RL 负责造能力，蒸馏负责分发与合并：R1 → 开放小模型，V3.2 专家蒸馏，V4 多教师全词表 on-policy 蒸馏 | R1、V3.2、V4 | 全词表蒸馏的工程负担（教师权重卸载、隐状态缓存、按教师排序样本） |
| Qwen（阿里巴巴） | 大模型完整训练，小模型全靠强到弱蒸馏；同一做法用到 VL 与图像生成 | Qwen3、Qwen3-VL、Qwen-Image-2.0-RL | 公开对照只在 8B、数学与代码题上 |
| Kimi（月之暗面）、小米 MiMo、智谱 | 多教师 on-policy 蒸馏作为后训练最后一段，逐 token 奖励接进 RL 框架 | K3、MiMo-V2-Flash、GLM-5 | 逐 token 估计的方差（V4 的批评）；长轨迹上信号变弱 |
| NVIDIA | 多教师特征蒸馏，把当下最好的几个视觉基础模型合成一个编码器，并随教师换代 | AM-RADIO、C-RADIOv4、RADIO1D | 学生会学到教师的伪影；某个教师可能没有贡献（SAM3） |
| Microsoft Research（Li Dong、Furu Wei 一组） | 研究"蒸什么"：注意力关系（MiniLM）→ 反向 KL 与在线采样（MiniLLM） | MiniLM、MiniLLM | 在线采样需要多种稳定技巧 |
| Meta | 先训最大的自监督视觉模型，再蒸馏出一族发布 | DeiT、DINOv2、DINOv3 | 详见视觉表征方向 |

`[判断]` 收敛的部分：
- 在线采样（学生自己写、教师打分）成为大模型后训练中蒸馏的默认形态，2023 年 GKD、MiniLLM 提出，2025–2026 年 Qwen3、MiMo、GLM-5、V4、K3 都采用；
- 反向 KL 是默认的散度方向（MiniLLM、MiMo、V4）；
- "教师强、学生弱"之外出现了"同尺寸专家合并成一个模型"的用法，学生不一定比教师小。

分化的部分：
- 逐 token 估计（K3、MiMo，可直接复用 RL 框架）对全词表 logit（V4，更稳但工程重）；
- 蒸馏放在预训练（Gemma）还是只放在后训练（DeepSeek、Qwen、Kimi）；
- 合并发生在一个阶段的末尾（GLM-5 跨阶段）还是取代整个混合 RL 阶段（V4）。

## 用什么衡量进展

结论：蒸馏没有专属 benchmark，好坏看三组比较：学生对教师保留了多少、学生对同尺寸从头训练的模型强多少、花了多少算力。每组比较都有会改变结论的口径。

| 比较 | 常见写法 | 例子 | 已知的口径问题 |
|---|---|---|---|
| 学生保留了教师多少 | "保留 97% 的性能"；平均分之比 | DistilBERT 97%、TinyBERT 96.8%、MiniLM 99% 以上 | 平均分会掩盖单项的大差距：DistilBERT 的 RTE 掉 9.4 分；比的是开发集还是测试集要看清（DistilBERT 用开发集，TinyBERT 用测试集） |
| 学生对从头训练强多少 | 同尺寸、同 token 数下的分数或困惑度 | Gemma 2 Table 6（60.3 → 67.7）、R1 Table 16（47.0 → 72.6） | 从头训练的一方是否调到最好；token 数是否相同；R1 的对照是"蒸馏"对"RL"，不是对 SFT |
| 花了多少算力 | GPU 小时、教师前向的成本 | Qwen3 Table 21：1,800 对 17,920 GPU 小时 | 是否计入训练教师的成本：Busbridge 等发现如果教师要专门训练、只服务一个学生，监督训练通常更划算；Thinking Machines 的"便宜 9 倍"不含教师生成数据的成本，算上约 30 倍 |
| 多教师合并后掉了多少 | 统一模型对各领域专家的分数 | V3.2、V4、K3 的后训练章节 | 2026 年的报告多数只给统一模型的最终分数，没给"专家 vs 合并后"的逐项对照 |
| 能否扩展探索 | pass@k 在大 k 下是否提高 | Qwen3 的 pass@64：蒸馏 90.0 → 93.3，RL 不变 | 只在 8B、数学题上测过 |

推理模型的评测口径（温度、采样次数、pass@1 怎样平均）见[后训练总览](../../../llm/fields/posttraining/README.md)"用什么衡量进展"；视觉编码器的评测协议（k 近邻、线性探针、接入 VLM）见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。

## 当前开放问题

- **蒸馏缺的是更多提示，还是更好地吸收教师并交付答案？** [OPD II](../../../llm/papers/arxiv-2609.04172/README.md)比较少量提示与大量在策略轨迹；[Solving Without Stopping](../../../llm/papers/arxiv-2609.37326/README.md)分别测解题与停止。两种诊断应分开，数学小模型结果能否推广到长程 Agent 仍需检验。

- **逐 token 还是全词表？** V4 认为逐 token 估计方差大，K3 认为更细的 top-k 没有优势，两家都没有给出同条件对照。入口：[DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md) §5.1.2、[Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md) §4.1.3、[Li 等](../../../llm/papers/arxiv-2604.13016/README.md)。
- **on-policy 蒸馏能否扩到长程 agent 任务？** 学生前缀越长，教师的逐 token 信号越不可靠；K3 的 agent 环境要求成百上千次工具调用、数百万累计上下文 token（§1）。入口：[Li 等](../../../llm/papers/arxiv-2604.13016/README.md)第 6 节、[Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)。
- **教师该多大、学生要训多久？** Gemma 3 的大小教师之争随训练长度反转，Busbridge 等给出了蒸馏的规模定律，但只在固定的语言模型族上拟合。入口：[Gemma 3](../../../llm/papers/arxiv-2503.19786/README.md) §5.4、[Busbridge 等](https://arxiv.org/abs/2502.08606)、[训练科学方向](../training-science/README.md)。
- **蒸馏能否超过教师？** 合并后的统一模型能否在某些领域超过对应的专家，2026 年的报告没有给逐项对照；R1 的作者认为超越人类边界仍要靠更强的基座与 RL。入口：[DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 附录 F、[后训练总览](../../../llm/fields/posttraining/README.md)"RL 能否超出基座的能力边界"。
- **多教师的伪影与冲突怎样处理？** 视觉里 C-RADIOv4 要去掉教师的固定模式噪声、平衡教师的损失尺度；语言里各家按领域路由教师，冲突的处理方式没有公开对照。入口：[C-RADIOv4](../../../multimodal/papers/arxiv-2601.17237/README.md)、[DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)。

## 阅读顺序

1. [Hinton 等 2015](../../papers/arxiv-1503.02531/README.md)：温度、软目标、T² 缩放，以及"专家没蒸回来"这个十年后才解决的问题；前作 [Model Compression](../../papers/url-cornell-compression.kdd06/README.md) 与 [Ba & Caruana](../../papers/arxiv-1312.6184/README.md) 可快速翻过。
2. [FitNets](../../papers/arxiv-1412.6550/README.md) → [MiniLM](../../../llm/papers/arxiv-2002.10957/README.md)：从"传输出"到"传中间层"，看提示层怎样被关系矩阵取代。
3. [DistilBERT](../../../llm/papers/arxiv-1910.01108/README.md) 与 [TinyBERT](../../../llm/papers/arxiv-1909.10351/README.md)：对照两种 BERT 压缩，注意 CoLA、RTE 上的差距。
4. [Gemma 2](../../../llm/papers/arxiv-2408.00118/README.md) → [Gemma 3](../../../llm/papers/arxiv-2503.19786/README.md)：蒸馏怎样变成预训练目标，以及大小教师之争。
5. [DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 附录 F → [Qwen3](../../../llm/papers/arxiv-2505.09388/README.md) §4.5 与 Table 21 → [Thinking Machines 博客](../../../llm/papers/thinking-machines-on-policy-distillation/README.md)：离线到在线，蒸馏与 RL 的直接对照。
6. [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md) §5.1–5.2 与 [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md) §4.1，再读 [Li 等](../../../llm/papers/arxiv-2604.13016/README.md)：当前形态、两家的分歧与失败条件。视觉一侧接 [AM-RADIO](../../../multimodal/papers/arxiv-2312.06709/README.md) → [C-RADIOv4](../../../multimodal/papers/arxiv-2601.17237/README.md)。

基线拆分见 [BASELINES.md](BASELINES.md)，带检验题的路线见 [ROADMAP.md](ROADMAP.md)，全部文献见 [PAPERS.md](PAPERS.md)。

## 批注

**易误读**

- 为什么不用 §3.6 变体：蒸馏是一种训练方法，有明确的目标（在给定成本下逼近教师）和可直接比较的量（师生差距、对从头训练的增益、算力），不需要先界定"研究对象是什么"。它没有专属 benchmark，这一点在"用什么衡量进展"一节用三组比较代替。
- FitNets 摘要的"参数少约 10.4 倍"对应 Table 5 中的 FitNet 2（约 862K 参数、91.06%）；Table 1 报告的 91.61% 是更深的 FitNet 4（约 2.5M 参数，只比教师少约 3.6 倍）。两个数字不要拼在一起引用。
- "保留 97%"一类的数字是平均分之比，DistilBERT 用 GLUE 开发集（Table 1），TinyBERT 用 GLUE 测试集（Table 1），两者不能直接比。
- R1 的 Table 16 对照的是"同一基座上的蒸馏"与"同一基座上的大规模 RL"，不是蒸馏与 SFT 的对照；R1-Distill 模型的基座有两个是 Qwen2.5-Math（1.5B、7B），一个是已经指令微调过的 Llama-3.3-70B-Instruct（Table 6）。
- Qwen3 Table 21 的两条路线都从同一个离线蒸馏的 8B 检查点出发，只用数学与代码题；RL 的 pass@64 没有变化不等于 RL 无用，k = 1 时 RL 也有大幅提升（55.0 → 67.6）。
- Li 等的"0.366 → 0.024"是教师续写带来的准确率增益，不是 on-policy 蒸馏训练后的分数（Figure 11b）。
- Gemma 4 报告（arXiv 2607.02770 v2）的预训练与指令微调两节只写"与 Gemma 3 相近"，全文没有出现蒸馏的具体描述；第三方文章对 Gemma 4 蒸馏的说法不能当作官方事实。

**判断的支撑论文**

- "蒸馏成为后训练主干之一"（速览 4、阶段 7）：MiMo-V2-Flash §4.1 与 §4.4、GLM-5 §3.5、DeepSeek-V4 §5.1、Kimi K3 §4.1、Qwen3 §4.5 与 Table 21、R1 附录 F。边界：DeepSeek-V3.2 的统一模型在专家蒸馏之后仍做混合 RL（后训练总览第 6 节）；Nemotron 3（[卡片](../../../llm/papers/arxiv-2512.20856/README.md)）走的是多领域同时 RL，是"专家加蒸馏"之外的对照。
- 团队偏好按"两篇以上、存在替代方案时重复同一选择"判断：Google 在 Gemma 2、Gemma 3 都用教师分布做预训练目标，并在两份报告的后训练部分都引用 GKD；DeepSeek 在 R1（蒸给开放小模型）、V3.2（专家蒸馏）、V4（多教师 OPD）三份报告中都由 RL 造教师、由蒸馏分发；Qwen 在 Qwen3、Qwen3-VL、Qwen-Image-2.0-RL 中都用 on-policy 蒸馏；NVIDIA 在 AM-RADIO、C-RADIOv4、RADIO1D 中都用多教师蒸馏，AM-RADIO 写明"更好的教师得到更好的学生"，C-RADIOv4 按这一前提把教师整体换代；Microsoft 的 Li Dong、Furu Wei 同时署名 MiniLM 与 MiniLLM。边界：本库只在 K3 一份报告里看到 Kimi 用多教师 OPD，MiMo、智谱也各只有一份，所以三家合为一行，写成同一类做法，不单独算作某一家的偏好。
- `[结构]` on-policy 蒸馏与 DAgger 的对应：R2R 精读第 3 节（作者自述 student-forcing 等价于在线 DAgger）、RMA 精读第 3 节（作者自述类似 DAgger）、Lee 等 2020 的卡片、Thinking Machines 博客与后训练总览"与机器人强化学习的共性"。

**与其他论文的关联**

- [后训练总览](../../../llm/fields/posttraining/README.md)与 [SFT 方向](../../../llm/fields/posttraining/sft/README.md)第 6 节：本页阶段 6、7 的同一组证据，从"奖励从哪来"的角度展开；Yue 等关于 RL 与蒸馏能力边界的结论在那里。
- [预训练方向](../../../llm/fields/pretraining/README.md)：Gemma 2/3 的蒸馏作为预训练目标、局部与全局注意力交错，在那里与其他预训练配方对照。
- [视觉表征方向](../../../multimodal/fields/visual-representation/README.md)：Baseline 页"训练信号 = 多教师蒸馏"一行与入门页"组合从拼接移到蒸馏"一节，是本页视觉部分的展开。
- [模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)：特权教师—学生蒸馏、DAgger 与复合误差。
- [训练科学方向](../training-science/README.md)：Gemma 2 与 Busbridge 等的"计算最优"以 Kaplan 与 Chinchilla 的规模定律为参照。

**未核实 / 待验证**

- 正文另用到、未进综合表的材料（均打开原文核对过所引段落）：MiMo-V2-Flash（摘要、§4.1、§4.4）、GLM-5（§1、§3.5）、Li 等（摘要、§1、Figure 11）、C-RADIOv4（摘要、§1、§2.1）、RADIO1D（摘要）、Gemma 3（§2.2、§4、§5.4）、Gemma 4（§2.3–2.4、§3）、Busbridge 等（摘要、§1）。
- DeepSeek-V3.2 的专家蒸馏细节取自后训练总览与 V3.2 卡片，本轮没有重新打开 V3.2 原文。
- Qwen3-VL 的强到弱蒸馏、DINOv2/v3 的蒸馏发布、DeiT 的数字取自各自文献卡，本轮没有重新打开原文。
- [综述 DOI 10.1016/j.mlwa.2024.100605](history.md) 与"2011 年起源"的说法仍未核实，见 history.md。
- 已知存在、本轮没有打开的更新材料：清华之外的 on-policy 蒸馏综述（腾讯 Song 等 [arXiv 2604.00626](https://arxiv.org/abs/2604.00626) 只读了摘要）；搜索结果中的 Nemotron-Cascade 2、OneReason、Data-free OPD 等 2026 年的 OPD 论文。
