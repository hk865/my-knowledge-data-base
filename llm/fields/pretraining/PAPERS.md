# 预训练论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

按[入门页](README.md)主线历史的六个阶段排列；每篇链接到唯一的单篇目录，"格"指它在 [Baseline 表](BASELINES.md)中的位置（部件 = 改法）。跨方向的论文只列与预训练有关的那一面，不重复计数。综合表 [synthesis.csv](synthesis.csv) 中还没有单篇目录的报告，在每个阶段末尾列出原文链接。

## 1 基础：配方收敛到 decoder-only 与计算最优配比（2017–2023）

- [Attention Is All You Need](../../papers/transformer/README.md) · 2017 · Google · 技术精读 · 格：基线之前的节点（架构）
- [Language Models are Few-Shot Learners](../../papers/gpt3/README.md)（GPT-3） · 2020 · OpenAI · 技术精读 · 格：基线之前的节点（规模）
- [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](../../papers/arxiv-1910.10683/README.md)（T5） · 2019 · Google · 文献卡 · 格：基线之前的节点（训练目标与数据）
- [PaLM: Scaling Language Modeling with Pathways](../../papers/arxiv-2204.02311/README.md) · 2022 · Google Research · 文献卡 · 格：基线之前的节点；损失与任务 = z-loss
- [Training Compute-Optimal Large Language Models](../../../cross-domain/papers/arxiv-2203.15556/README.md)（Chinchilla） · 2022 · DeepMind · 文献卡（归属训练科学，在此交叉引用） · 格：基线之前的节点（数据与参数配比）
- [GPT-4 Technical Report](../../papers/arxiv-2303.08774/README.md) · 2023 · OpenAI · 文献卡 · 格：中途评估 = 用小模型预测终点

综合表中尚无单篇目录：
[Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)（2014）；
[Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)（2014）；
[Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)（GPT，2018）；
[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](../../papers/arxiv-1810.04805/README.md)（2018）；
[Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)（GPT-2，2019）；
[Scaling Laws for Neural Language Models](../../../cross-domain/papers/arxiv-2001.08361/README.md)（2020）；
[What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot Generalization?](https://arxiv.org/abs/2204.05832)（2022）；
[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)（2023）。

## 2 稳定性成为一等问题（2022–2025）

- [Small-scale proxies for large-scale Transformer training instabilities](../../papers/arxiv-2309.14322/README.md)（Wortsman 等） · 2023 · Google DeepMind · 文献卡 · 格：注意力 = QK-Norm；损失与任务 = z-loss；优化器 = AdamW 内调稳；中途评估 = 先兆量
- [2 OLMo 2 Furious](../../papers/arxiv-2501.00656/README.md)（OLMo 2） · 2024 · Allen Institute for AI 等 · 文献卡 · 格：注意力 = QK-Norm；残差与归一化 = reordered norm；数据组成 = 删除重复 n-gram；课程 = 中段训练
- [Gemma 2: Improving Open Language Models at a Practical Size](../../papers/arxiv-2408.00118/README.md) · 2024 · Google DeepMind · 文献卡 · 格：注意力 = 局部/全局交错（1:1）；损失与任务 = 知识蒸馏
- [Gemma 3 Technical Report](../../papers/arxiv-2503.19786/README.md) · 2025 · Google DeepMind · 文献卡 · 格：注意力 = QK-Norm、局部/全局交错（5:1）；课程 = 分级加长；损失与任务 = 知识蒸馏
- [Qwen3 Technical Report](../../papers/arxiv-2505.09388/README.md) · 2025 · 阿里巴巴 Qwen 团队 · 文献卡 · 格：注意力 = QK-Norm；数据组成 = 配比与合成；课程 = 退火（S2）与分级加长；FFN = 细粒度 MoE

综合表中尚无单篇目录：[Gemma 4 Technical Report](https://arxiv.org/abs/2607.02770)（2026，局部/全局 5:1，全局层 key 兼作 value）。

## 3 开源团队把规模科学做细（2024）

- [DeepSeek LLM: Scaling Open-Source Language Models with Longtermism](../../papers/arxiv-2401.02954/README.md) · 2024 · DeepSeek-AI · 文献卡 · 格：数据组成 = 配比、不用选择题数据；课程 = 阶梯学习率；中途评估 = 用小模型预测终点
- [The Llama 3 Herd of Models](../../papers/arxiv-2407.21783/README.md) · 2024 · Meta · 文献卡 · 格：稠密基线；数据组成 = 分类器与规模定律定配比；课程 = 退火、分级加长；中途评估 = 两步法预测、退火评估数据
- [Qwen2.5 Technical Report](../../papers/arxiv-2412.15115/README.md) · 2024 · 阿里巴巴 Qwen 团队 · 文献卡 · 格：数据组成 = 配比（7T → 18T）；课程 = 超参规模定律
- [Qwen2 Technical Report](../../papers/arxiv-2407.10671/README.md) · 2024 · 阿里巴巴 Qwen 团队 · 文献卡 · 格：Qwen3 去掉的 QKV 偏置所在的前一代

## 4 稀疏化：用更少的激活参数装更多知识（2024）

- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](../../papers/arxiv-2101.03961/README.md) · 2021 · Google · 文献卡 · 格：FFN = MoE 的前作（附录 A：专家化注意力在 bfloat16 下发散）
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](../../papers/arxiv-2401.06066/README.md) · 2024 · DeepSeek-AI · 文献卡 · 格：FFN = 细粒度专家 + 共享专家
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../papers/deepseek-v2/README.md) · 2024 · DeepSeek-AI · 技术精读 · 格：注意力 = MLA；FFN = 细粒度专家 + 共享专家
- [Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](../../papers/arxiv-2408.15664/README.md) · 2024 · DeepSeek-AI · 文献卡 · 格：FFN = 无辅助损失均衡
- [DeepSeek-V3 Technical Report](../../papers/arxiv-2412.19437/README.md) · 2024 · DeepSeek-AI · 文献卡 · 格：稀疏基线；损失与任务 = MTP、FIM；数值精度 = FP8 训练

- [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](../../papers/arxiv-2403.05530/README.md) · 2024 · Google DeepMind · 文献卡（归属长上下文方向，在此交叉引用） · 格：FFN = MoE（报告只写明是稀疏 MoE，不给预训练配方）

## 5 Token 效率：优化器与数据改写（2025）

- [Muon is Scalable for LLM Training](../../papers/arxiv-2502.16982/README.md)（Moonlight） · 2025 · Moonshot AI · 文献卡 · 格：优化器 = Muon
- [Kimi K2: Open Agentic Intelligence](../../papers/arxiv-2507.20534/README.md) · 2025 · Kimi Team · 文献卡 · 格：优化器 = MuonClip；数据组成 = 改写；FFN = 更多专家；中途评估 = 最大 logit

## 6 为长程推理改造注意力与深度（2025–2026）

问题②的两篇失败证据早于本阶段（2023），因为它们定义了本阶段要解决的问题，放在这里：

- [Efficient Streaming Language Models with Attention Sinks](../../papers/arxiv-2309.17453/README.md)（StreamingLLM） · 2023 · MIT、Meta AI、CMU、NVIDIA · 文献卡 · 格：注意力 = 显式提供 sink
- [Lost in the Middle: How Language Models Use Long Contexts](../../papers/arxiv-2307.03172/README.md) · 2023 · Stanford、UC Berkeley、Samaya AI · 文献卡 · 格：长上下文评测的位置效应（"课程 = 分级加长"一行的代价）

本阶段的报告：

- [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](../../papers/arxiv-2502.11089/README.md)（NSA） · 2025 · DeepSeek-AI、北京大学、华盛顿大学 · 文献卡 · 格：注意力 = 训练时就稀疏
- [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](../../papers/arxiv-2505.06708/README.md) · 2025 · 阿里巴巴 Qwen 团队 · 文献卡 · 格：注意力 = 输出门控
- [Qwen2.5-1M Technical Report](../../papers/qwen2.5-1m/README.md) · 2025 · 阿里巴巴 Qwen 团队 · 技术精读 · 格：损失与任务 = 合成必须读远处的任务；课程 = 分级加长
- [Kimi Linear: An Expressive, Efficient Attention Architecture](../../papers/arxiv-2510.26692/README.md) · 2025 · Kimi Team · 文献卡 · 格：注意力 = 线性注意力混合；中途评估 = 分布外验证集
- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](../../papers/arxiv-2512.02556/README.md) · 2025 · DeepSeek-AI · 文献卡 · 格：注意力 = 训练时就稀疏（DSA）；课程 = 稠密预热后转稀疏
- [mHC: Manifold-Constrained Hyper-Connections](../../papers/arxiv-2512.24880/README.md) · 2025 · DeepSeek-AI · 文献卡 · 格：残差与归一化 = 约束混合矩阵
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](../../papers/arxiv-2601.07372/README.md)（Engram） · 2026 · 北京大学、DeepSeek-AI · 文献卡 · 格：FFN = 查表记忆
- [Attention Residuals](../../papers/arxiv-2603.15031/README.md) · 2026 · Kimi Team · 文献卡 · 格：残差与归一化 = 跨层注意力
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](../../papers/arxiv-2606.19348/README.md) · 2026 · DeepSeek-AI · 文献卡 · 格：注意力 = 训练时就稀疏（CSA/HCA）、显式 sink；残差 = mHC；优化器 = Muon；数值精度 = FP4 专家
- [Kimi K3: Open Frontier Intelligence](../../papers/arxiv-2607.24653/README.md) · 2026 · Kimi Team · 文献卡 · 格：注意力 = 线性注意力混合；残差 = Attention Residuals；优化器 = 按头正交化；课程 = 改回余弦
- [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](../../papers/arxiv-2609.19969/README.md) · 2026 · DeepSeek-AI · 文献卡 · 格：注意力 = 训练时就稀疏（CSA2，无稠密预热）；FFN = 查表记忆；数值精度 = FP4 KV 缓存
- [Tokenizer-Agnostic Engram Module](../../papers/arxiv-2607.29065/README.md) · 2026 · 文献卡 · 格：FFN = 查表记忆的后续（开放问题"知识能否从 FFN 里再拆出去"）
- [Frozen Memory Is Not Enough: Rethinking External Memory as Extraction](../../papers/arxiv-2608.17050/README.md) · 2026 · 文献卡 · 格：同上

同期其他团队（2025-12 – 2026）：

- [Olmo 3](../../papers/arxiv-2512.13961/README.md) · 2025 · AI2 · 文献卡（主要归强化学习） · 格：数据 = 完全公开的三段数据（Dolma 3、Dolmino、Longmino）
- [NVIDIA Nemotron 3: Efficient and Open Intelligence](../../papers/arxiv-2512.20856/README.md) · 2025 · NVIDIA · 文献卡（主要归架构） · 格：数值精度 = NVFP4 预训练；注意力 = Mamba-2 为主的混合
- [GLM-5: from Vibe Coding to Agentic Engineering](../../papers/arxiv-2602.15763/README.md) · 2026 · 智谱、清华 · 文献卡（主要归强化学习） · 格：注意力 = 中段训练后转成 DSA
- [The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence](../../papers/arxiv-2605.26494/README.md) · 2026 · MiniMax · 文献卡（主要归强化学习） · 格：注意力 = 全注意力（滑窗混合的反例）

只读了官方博客、未建卡：[Introducing Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/)（Meta，2026-04，称算力比 Llama 4 Maverick 少一个数量级以上，无结构与配方）。

## 存档与跨方向

以下单篇目录登记在预训练方向下，但不在入门页的主线上：

- [OLMo: Accelerating the Science of Language Models](../../papers/arxiv-2402.00838/README.md) · 2024 · 文献卡 · OLMo 2 的前一代
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](../../papers/mamba/README.md) · 2023 · 技术精读 · 线性递推一路的前作，在[架构与效率方向](../architecture/README.md)展开
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](../../papers/arxiv-1910.01108/README.md) · 2019 · 文献卡 · 编码器模型的蒸馏压缩，见[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](../../papers/arxiv-2002.10957/README.md) · 2020 · 文献卡 · 同上
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](../../papers/arxiv-2009.08366/README.md) · 2020 · 文献卡 · 代码表示的编码器预训练
- [Probing Pretrained Models of Source Code](../../papers/arxiv-2202.08975/README.md) · 2022 · 文献卡 · 代码模型的探针分析，见[模型科学](../../../cross-domain/fields/model-science/README.md)
