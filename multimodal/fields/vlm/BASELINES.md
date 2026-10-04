# 视觉语言模型的基线

[回到入门](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 基线是谁、为什么是它

**主基线：[LLaVA-1.5](../../papers/arxiv-2310.03744/README.md)（2023 年 10 月），连同原版 [LLaVA](../../papers/llava/README.md)。** 它定义了此后开源 VLM 的默认接口与训练范式：

- **接口**：图像经 ViT 变成网格特征，经 MLP 投影成视觉 token，与文字 token 排进同一条序列，LLM 用下一词预测输出文字。336 像素输入、14 像素切块时每图 576 个视觉 token。
- **训练范式**：两段。第一段冻结 ViT 与 LLM，只训连接器（约 56 万对图文）；第二段训练连接器与 LLM（约 67 万条指令数据，含学术 VQA 与格式提示）。视觉塔全程冻结。
- **评估方式**：学术 VQA（VQAv2、GQA、TextVQA 等）加面向指令模型的综合考卷（MME、MMBench、SEED、MM-Vet）和幻觉评测 POPE，共 12 个。

选它而不选更早的 Flamingo、BLIP-2，是因为本方向收录的 2024 年以后的开源模型（Qwen2-VL 起的 Qwen 系列、InternVL 1.5 起、DeepSeek-VL 与 VL2、Kimi-VL、Molmo）都写明采用"ViT–MLP–LLM"这一结构，后续工作几乎都可以读成"改了它的哪个部件"。

**两个对照基线**：[Flamingo](../../papers/arxiv-2204.14198/README.md)（冻结 LLM + 门控交叉注意力 + 交错网页数据 + 少样本提示）和 [BLIP-2](../../papers/arxiv-2301.12597/README.md)（冻结两端 + Q-Former 查询瓶颈）。它们代表被放弃的两种连接方式，读它们是为了理解 LLaVA-1.5 的选择为什么胜出。

## 基线的结构拆分

| 部件 | LLaVA-1.5 的选择 | 这个部件决定什么 |
|---|---|---|
| 1 视觉编码器 | CLIP ViT-L/14-336，约 0.3B，全程冻结 | 能看到哪些性质（语义还是空间细节）；冻结与否决定能否为下游调整 |
| 2 输入分辨率与切分 | 固定 336×336（HD 版切成 224 的格子） | 能否读小字、看密集图表；视觉 token 数 |
| 3 连接器 | 两层 MLP，每个图像块一个 token | 视觉信息进入 LLM 的通道宽度与 token 数 |
| 4 语言模型 | Vicuna-7B / 13B，稠密 | 推理与知识上限；推理成本 |
| 5 训练阶段与冻结日程 | 对齐（只训 MLP）→ 指令微调（MLP + LLM） | 新能力学到多少、旧能力保住多少 |
| 6 数据 | 公开图文对 + GPT 生成的对话 + 学术 VQA，约 120 万条 | 覆盖哪些技能（OCR、定位、计数）；是否蒸馏闭源模型 |
| 7 后训练目标 | 只有 SFT（下一词交叉熵） | 推理、偏好、幻觉控制 |
| 8 评测 | 12 个学术与综合 benchmark | 分数是否真的来自看图 |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 1 视觉编码器 | 扩大到 6B 并持续训练 | [InternVL](../../papers/arxiv-2312.14238/README.md)、[InternVL 1.5](../../papers/arxiv-2404.16821/README.md)、[InternVL 2.5](../../papers/arxiv-2412.05271/README.md) | 2.5 版称用约 1/10 训练 token 达到更好表现；6B 视觉塔推理贵，小模型仍用 300M |
| 1 视觉编码器 | 中段解冻，与 LLM 一起训练 | [Qwen-VL](../../papers/arxiv-2308.12966/README.md)、[Qwen2-VL](../../papers/arxiv-2409.12191/README.md)、[DeepSeek-VL2](../../papers/arxiv-2412.10302/README.md)、[Cambrian-1](../../papers/arxiv-2406.16860/README.md) | Cambrian-1 在 23 个骨干上验证解冻普遍有益；显存与算力增加，大视觉模型难以解冻 |
| 1 视觉编码器 | 自训新 ViT（窗口注意力、RMSNorm、SwiGLU） | [Qwen2.5-VL](../../papers/arxiv-2502.13923/README.md) | 原生分辨率下计算随块数线性增长；下一代 Qwen3-VL 又换回 SigLIP-2 |
| 1 视觉编码器 | 多编码器组合（语义 + 空间 / 高分辨率） | [DeepSeek-VL](../../papers/arxiv-2403.05525/README.md)（SigLIP + SAM）、[Cambrian-1](../../papers/arxiv-2406.16860/README.md)（加 DINOv2 等） | 视觉中心与 OCR 任务提升；多路编码成本高，DeepSeek-VL2 回到单编码器 |
| 2 分辨率 | 按长宽比切块 + 缩略图 | [InternVL 1.5](../../papers/arxiv-2404.16821/README.md)、[DeepSeek-VL2](../../papers/arxiv-2412.10302/README.md)、[Molmo](../../papers/arxiv-2409.17146/README.md)（重叠切块） | 文档、图表、OCR 大幅提升；切块边缘缺上下文，token 随块数增加 |
| 2 分辨率 | 原生动态分辨率（2D-RoPE、打包） | [Qwen2-VL](../../papers/arxiv-2409.12191/README.md)、[Qwen2.5-VL](../../papers/arxiv-2502.13923/README.md)、[Kimi-VL](../../papers/arxiv-2504.07491/README.md)、[Qwen3-VL](../../papers/arxiv-2511.21631/README.md) | InfoVQA 随 token 数从 28.9 升到 77.3；小图放大过头会落到训练分布之外 |
| 3 连接器 | 门控交叉注意力 / 查询瓶颈（对照基线） | [Flamingo](../../papers/arxiv-2204.14198/README.md)、[BLIP-2](../../papers/arxiv-2301.12597/README.md)、[Qwen-VL](../../papers/arxiv-2308.12966/README.md) | token 少、可冻结 LLM；收敛慢、丢细节，后被 MLP 取代 |
| 3 连接器 | MLP + 相邻 2×2 合并（pixel shuffle） | [InternVL 1.5](../../papers/arxiv-2404.16821/README.md) 起、[Qwen2-VL](../../papers/arxiv-2409.12191/README.md) 起、[Kimi-VL](../../papers/arxiv-2504.07491/README.md) | token 减为 1/4，成为默认 |
| 3 连接器 | 空间感知聚合 / 多层注入 | [Cambrian-1](../../papers/arxiv-2406.16860/README.md)（SVA）、[Qwen3-VL](../../papers/arxiv-2511.21631/README.md)（DeepStack） | 用更少 token 保留多尺度、多层次信息；结构更复杂 |
| 4 语言模型 | 换成 MoE | [DeepSeek-VL2](../../papers/arxiv-2412.10302/README.md)、[Kimi-VL](../../papers/arxiv-2504.07491/README.md)、[Qwen3-VL](../../papers/arxiv-2511.21631/README.md) | 激活参数少、推理省；Kimi-VL 自述注意力参数偏小限制长上下文 |
| 4 语言模型 | encoder–decoder 并平衡两侧参数 | [PaLI](../../papers/arxiv-2209.06794/README.md) | 视觉侧扩容回报更高；此后的通用模型多为 decoder-only |
| 4 语言模型 | 离散图像 token 早融合，从零训练 | [Chameleon](../../papers/arxiv-2405.09818/README.md)、[Gemini 1.0](../../papers/arxiv-2312.11805/README.md)（官方只写"从一开始就多模态"） | 可图文交错生成；OCR 受分词器限制，训练易发散 |
| 5 训练日程 | 三段：先训视觉侧 → 全量解冻 → SFT 冻 ViT | [Qwen-VL](../../papers/arxiv-2308.12966/README.md)、[Qwen2-VL](../../papers/arxiv-2409.12191/README.md)、[Qwen2.5-VL](../../papers/arxiv-2502.13923/README.md) | 兼顾对齐与细节；阶段多、调参成本高 |
| 5 训练日程 | 多模态预训练中混大比例纯文本 | [DeepSeek-VL](../../papers/arxiv-2403.05525/README.md)、[Kimi-VL](../../papers/arxiv-2504.07491/README.md) | 保住语言能力；DeepSeek-VL 发现至少要 70% 文本 |
| 5 训练日程 | 去掉单独的连接器对齐阶段 | [Molmo](../../papers/arxiv-2409.17146/README.md)；反方 [Cambrian-1](../../papers/arxiv-2406.16860/README.md) | 更简单；Cambrian-1 发现对齐阶段与更多适配数据有益 |
| 5 训练日程 | 文本与多模态合并成一个"原生"预训练阶段 | [InternVL3](../../papers/arxiv-2504.10479/README.md) | 与多段训练的 InternVL2-8B 表现相当，流程更简单；仍从预训练 LLM 初始化 |
| 5 训练日程 | 冻结 LLM 的少样本路线（对照基线） | [Flamingo](../../papers/arxiv-2204.14198/README.md) | 防遗忘、可上下文学习；分类弱于对比模型 |
| 6 数据 | 大规模清洗的网页图文 + 定位与 OCR 合成数据 | [Qwen-VL](../../papers/arxiv-2308.12966/README.md)、[PaLI](../../papers/arxiv-2209.06794/README.md)（WebLI） | 覆盖多语言、读字、定位；含内部数据，难复现 |
| 6 数据 | 人工口述描述与指向数据，不用任何 VLM 生成 | [Molmo](../../papers/arxiv-2409.17146/README.md) | 同量下优于 GPT-4V 生成的描述；标注成本高 |
| 6 数据 | 严格过滤异常样本 | [InternVL 2.5](../../papers/arxiv-2412.05271/README.md) | 减少复读、改善 CoT；无法根除 |
| 7 后训练 | DPO / MPO 偏好优化 | [Qwen2.5-VL](../../papers/arxiv-2502.13923/README.md)、[InternVL3](../../papers/arxiv-2504.10479/README.md) | MPO 让 78B 与 38B 的推理均分各高 4.1、4.5 |
| 7 后训练 | 长 CoT SFT + 可验证奖励 RL + 蒸馏 | [Kimi-VL](../../papers/arxiv-2504.07491/README.md)、[Qwen3-VL](../../papers/arxiv-2511.21631/README.md) | 数学与多学科推理提升；过度思考、工具奖励被钻空子 |
| 8 评测 | 是非题测物体幻觉 | [POPE](../../papers/arxiv-2305.10355/README.md) | 暴露"一律答是"；只测物体有无 |
| 8 评测 | 剔除不看图可答与泄漏的题 | [MMStar](../../papers/arxiv-2403.20330/README.md) | 最好模型降到 57.1%；只有 1500 题 |
| 8 评测 | 开关图像对照、把传统视觉任务改写成问答 | [Cambrian-1](../../papers/arxiv-2406.16860/README.md)（CV-Bench） | 找出依赖 LLM 的 benchmark；CV-Bench 只覆盖四类空间能力 |
| 8 评测 | 人评 Elo | [Molmo](../../papers/arxiv-2409.17146/README.md) | 发现学术分与用户偏好不一致的模型；成本高、题型影响排名 |

## 2026 年重新打开的三个部件

| 部件 | 旧问题 → 改法 | 代表 | 证据与边界 |
|---|---|---|---|
| 训练日程 | 末期视觉注入引起模态冲击 → 更早联合训练；文本 SFT 后再做视觉 RL | [Kimi K2.5](../../../llm/papers/arxiv-2602.02276/README.md)、[Qwen3.5](../../../llm/papers/qwen3.5/README.md) | K2.5 有固定预算消融；Qwen3.5 提供另一配方，非同条件对照 |
| 视觉塔初始化 | 对比预训练初始化是否总有利 → 从零随下一词目标训练 | [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md) | §2.4 比较梯度稳定性与视觉成绩；限于该训练规模 |
| 输入与执行 | 一次读图 → 音视频按时间组织、调用工具再次取证 | [Qwen3.8-Omni](../../papers/arxiv-2609.25611/README.md) | 默认与工具辅助评测分列；系统框架承担一部分闭环能力 |

## 批注

**易误读**

- "约 56 万对图文、约 67 万条指令"是 LLaVA-1.5 Table 3 的 558K 与 665K；原版 LLaVA 第一段为 59.5 万对、第二段 158K 条（[LLaVA 精读](../../papers/llava/reading.md)第 3–4 节）。
- 表中"InfoVQA 从 28.9 升到 77.3"是 Qwen2-VL-7B 固定 64 与 3136 个 token 的对比（Qwen2-VL Table 7）；"MPO 各高 4.1、4.5"是 InternVL3 Table 13 中七个推理 benchmark 的均分。

**与其他论文的关联**

- 部件 1 的冻结与解冻，与[视觉表征方向](../visual-representation/README.md)"冻结即用"趋势的边界是同一问题，VLA 一侧的证据见 [OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)。
- 部件 7 的方法与坑来自 [LLM 后训练](../../../llm/fields/posttraining/README.md)；部件 4 的 MoE 见 [LLM 架构方向](../../../llm/fields/architecture/README.md)。
- 部件 8 的通用评测问题见[评测方向](../../../cross-domain/fields/evaluation/README.md)。

**未核实 / 待验证**

- LLaVA-NeXT、LLaVA-OneVision、InternVL3.5、PaliGemma 没有单篇目录，本轮没有打开原文，未列入表中。
