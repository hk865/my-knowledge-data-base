# 长上下文论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

本目录按[入门页](README.md)主线历史的阶段排列。每篇链接到唯一的单篇目录；"格"指它在 [Baseline 表](BASELINES.md)中的位置。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 1 窗口由训练长度决定（2017–2022）

- [Attention Is All You Need](../../papers/transformer/README.md) · 2017 · Google · 技术精读 · 格：位置表示（正弦位置编码）
- [RoFormer: Enhanced Transformer with Rotary Position Embedding](../../papers/arxiv-2104.09864/README.md) · 2021 · 追一科技 · 文献卡 · 格：位置表示 = RoPE

## 2 位置插值（2023）

- [Extending Context Window of Large Language Models via Positional Interpolation](../../papers/arxiv-2306.15595/README.md) · 2023 · Meta · 文献卡 · 格：位置表示 = 线性插值
- [YaRN: Efficient Context Window Extension of Large Language Models](../../papers/arxiv-2309.00071/README.md) · 2023 · Nous Research、EleutherAI 等 · 文献卡 · 格：位置表示 = 分频段插值
- [Effective Long-Context Scaling of Foundation Models](../../papers/arxiv-2309.16039/README.md) · 2023 · Meta · 文献卡 · 格：位置表示 = 提高基频；长依赖数据 = 质量优先（基线）
- [Efficient Streaming Language Models with Attention Sinks](../../papers/arxiv-2309.17453/README.md) · 2023 · MIT 等 · 文献卡 · 格：注意力结构 = sink + 滑动窗口
- [Lost in the Middle: How Language Models Use Long Contexts](../../papers/arxiv-2307.03172/README.md) · 2023 · Stanford 等 · 文献卡 · 格：评测 = 证据位置受控实验

## 3 百万窗口与评测反思（2024）

- [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](../../papers/arxiv-2403.05530/README.md) · 2024 · Google · 官方技术报告 · 格：评测 = 多模态与多针大海捞针
- [RULER: What's the Real Context Size of Your Long-Context Language Models?](../../papers/arxiv-2404.06654/README.md) · 2024 · NVIDIA · 文献卡 · 格：评测 = 合成多任务（评测基线）
- [The Llama 3 Herd of Models](../../papers/arxiv-2407.21783/README.md) · 2024 · Meta · 文献卡 · 格：课程 = 六级扩长；后训练 = 0.1% 合成长数据（基线）

## 4 开源百万上下文（2025 上半年）

- [Qwen2.5-1M Technical Report](../../papers/qwen2.5-1m/README.md) · 2025 · 阿里巴巴 Qwen 团队 · 技术精读 · 格：长依赖数据 = 合成任务；推理外推与执行 = DCA + 稀疏 prefill（基线）
- [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](../../papers/arxiv-2502.11089/README.md) · 2025 · DeepSeek、北京大学等 · 文献卡 · 格：注意力结构 = 训练时稀疏
- [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](../../papers/arxiv-2505.06708/README.md) · 2025 · 阿里巴巴 Qwen 团队 · 文献卡 · 格：注意力结构 = 消除注意力汇聚

## 5 为长程推理与智能体改造注意力（2025 下半年–2026）

- [Kimi Linear: An Expressive, Efficient Attention Architecture](../../papers/arxiv-2510.26692/README.md) · 2025 · Kimi（Moonshot AI） · 文献卡 · 格：注意力结构 = 线性注意力混合；位置表示 = 全局层 NoPE
- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](../../papers/arxiv-2512.02556/README.md) · 2025 · DeepSeek · 文献卡 · 格：注意力结构 = 索引器选 top-k
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](../../papers/arxiv-2606.19348/README.md) · 2026 · DeepSeek · 文献卡 · 格：注意力结构 = CSA/HCA
- [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](../../papers/arxiv-2609.19969/README.md) · 2026 · DeepSeek · 文献卡（主归属预训练方向） · 格：注意力结构 = 层间复用全局 KV、FP4 KV 缓存
- [Kimi K3: Open Frontier Intelligence](../../papers/arxiv-2607.24653/README.md) · 2026 · Kimi（Moonshot AI） · 文献卡 · 格：长依赖数据 = 读遍 1M 的合成任务；注意力结构 = 线性注意力混合

同期其他团队与窗口之外的做法（2025-12 – 2026）：

- [NVIDIA Nemotron 3: Efficient and Open Intelligence](../../papers/arxiv-2512.20856/README.md) · 2025 · NVIDIA · 文献卡（主要归架构） · 格：注意力结构 = Mamba-2 为主的混合，注意力层不用 RoPE
- [Recursive Language Models](../../papers/arxiv-2512.24601/README.md) · 2025 · MIT · 文献卡 · 格：推理外推与执行 = 递归调用自己
- [Kimi K2.5: Visual Agentic Intelligence](../../papers/arxiv-2602.02276/README.md) · 2026 · Kimi（Moonshot AI） · 文献卡（主要归推理时计算） · 格：推理外推与执行 = 并行子智能体的上下文分片
- [GLM-5: from Vibe Coding to Agentic Engineering](../../papers/arxiv-2602.15763/README.md) · 2026 · 智谱、清华 · 文献卡（主要归强化学习） · 格：注意力结构 = 转换为 DSA
- [Qwen3.5-397B-A17B（官方模型卡）](../../papers/qwen3.5/README.md) · 2026 · 阿里巴巴 Qwen 团队 · 文献卡 · 格：注意力结构 = Gated DeltaNet 3:1 混合
- [The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence](../../papers/arxiv-2605.26494/README.md) · 2026 · MiniMax · 文献卡（主要归强化学习） · 格：注意力结构 = 全注意力（反例）

## 交叉引用（主归属在其他方向）

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](../../papers/mamba/reading.md) · 2023 · 架构方向 · 技术精读 · 格：注意力结构 = 换序列算子
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](../../papers/arxiv-2601.07372/README.md) · 2026 · 预训练方向 · 文献卡 · 格：推理外推与执行 = 查表记忆
- [Frozen Memory Is Not Enough: Rethinking External Memory as Extraction](../../papers/arxiv-2608.17050/README.md) · 2026 · 预训练方向 · 文献卡 · 格：推理外推与执行 = 外部记忆
- [GQA](../../papers/arxiv-2305.13245/README.md)、[KIVI](../../papers/arxiv-2402.02750/README.md)、[vLLM](../../papers/arxiv-2309.06180/README.md) · 2023–2024 · 推理时计算方向 · 文献卡 · 格：推理外推与执行 = KV 缓存的头数、精度与分页

## 交叉引用（2026-10-04 补）

- [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](../../papers/arxiv-2405.21060/README.md)（Mamba-2） · 2024 · Princeton、CMU · 文献卡 · 格：序列混合 = 状态空间对偶（A 为标量乘单位阵，约 10% 注意力层的混合最好）

## 2026年10月4日补充

- [On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability](../../papers/arxiv-2608.30320/README.md) · 2026 · 文献卡

## 任务内的自适应记忆压缩

- [SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents](../../../cross-domain/papers/arxiv-2606.28434/README.md) · 2026 · 文献卡
