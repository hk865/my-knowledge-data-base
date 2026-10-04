# 架构与效率：论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

按[入门页](README.md)主线历史的阶段排列；每篇链接到唯一的单篇目录，"格"指它在 [Baseline 表](BASELINES.md)中的位置，"DeepSeek 架构线"指入门页同名一节的步骤。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 1 原点（2017）

- [Attention Is All You Need](../../papers/transformer/README.md) · 2017 · Google · 技术精读 · 格：两个基线的原点（多头注意力、Post-LN、稠密 FFN）

## 2 给注意力和归一化打补丁（2019–2020）

- [Fast Transformer Decoding: One Write-Head is All You Need](../../papers/arxiv-1911.02150/README.md)（MQA） · 2019 · Google · 文献卡 · 格：KV 缓存 = 所有头共用一组 K、V
- [On Layer Normalization in the Transformer Architecture](../../papers/arxiv-2002.04745/README.md)（Pre-LN） · 2020 · Microsoft Research Asia 等 · 文献卡 · 格：深度方向 = Pre-LN
- [Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention](../../papers/arxiv-2006.16236/README.md) · 2020 · Idiap、EPFL · 文献卡 · 格：序列混合 = 线性注意力

## 3 稀疏专家规模化（2021）

- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](../../papers/arxiv-2101.03961/README.md) · 2021 · Google · 文献卡 · 格：通道混合 = top-1 MoE

## 4 递推结构回归，GQA 成为默认（2023）

- [Resurrecting Recurrent Neural Networks for Long Sequences](../../papers/arxiv-2303.06349/README.md)（LRU） · 2023 · DeepMind（另有 ETH Zurich 作者） · 文献卡 · 格：序列混合 = 线性递推
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](../../papers/mamba/README.md) · 2023 · CMU、Princeton · 技术精读 · 格：序列混合 = 选择性 SSM
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](../../papers/arxiv-2305.13245/README.md) · 2023 · Google Research · 文献卡 · 格：KV 缓存 = 分组共享

## 5 混合架构与 DeepSeek 的稀疏栈（2024）

- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](../../papers/arxiv-2401.06066/README.md) · 2024 · DeepSeek-AI · 技术精读 · 格：通道混合 = 细粒度 + 共享专家 · DeepSeek 架构线第 1 步
- [Repeat After Me: Transformers are Better than State Space Models at Copying](../../papers/arxiv-2402.01032/README.md) · 2024 · Harvard · 文献卡 · 格：序列混合 = 选择性 SSM 的代价
- [Simple linear attention language models balance the recall-throughput tradeoff](../../papers/arxiv-2402.18668/README.md)（Based） · 2024 · Stanford · 文献卡 · 格：序列混合 = 线性注意力 + 小滑窗
- [Jamba: A Hybrid Transformer-Mamba Language Model](../../papers/arxiv-2403.19887/README.md) · 2024 · AI21 Labs · 文献卡 · 格：层排布 = 注意力:Mamba 1:7
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](../../papers/arxiv-2403.03853/README.md) · 2024 · Baichuan、中科院软件所 · 文献卡 · 格：深度方向 = Pre-LN 的代价（深层冗余）
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../papers/deepseek-v2/README.md) · 2024 · DeepSeek-AI · 技术精读 · 格：KV 缓存 = MLA；稀疏基线 · DeepSeek 架构线第 2 步
- [Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](../../papers/arxiv-2408.15664/README.md) · 2024 · DeepSeek-AI、北京大学 · 文献卡 · 格：通道混合 = 偏置均衡 · DeepSeek 架构线第 3 步的前作
- [Hyper-Connections](../../papers/arxiv-2409.19606/README.md) · 2024 · ByteDance Seed · 文献卡 · 格：深度方向 = 多条残差流 · DeepSeek 架构线第 6 步的前作
- [DeepSeek-V3 Technical Report](../../papers/arxiv-2412.19437/README.md) · 2024 · DeepSeek-AI · 技术精读 · 格：通道混合 = 偏置均衡与 MTP；稀疏基线 · DeepSeek 架构线第 3 步

## 6 训练时稀疏、规模化的线性混合、门控与超连接（2025）

- [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](../../papers/arxiv-2502.11089/README.md)（NSA） · 2025 · DeepSeek-AI、北京大学 · 技术精读 · 格：序列混合 = 训练时稀疏 · DeepSeek 架构线第 4 步
- [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](../../papers/arxiv-2505.06708/README.md) · 2025 · 阿里巴巴 Qwen · 文献卡 · 格：稳定性部件 = 输出门控
- [Kimi K2: Open Agentic Intelligence](../../papers/arxiv-2507.20534/README.md) · 2025 · Kimi Team · 文献卡 · 格：稳定性部件 = QK-Clip；通道混合 = 384 个专家
- [Kimi Linear: An Expressive, Efficient Attention Architecture](../../papers/arxiv-2510.26692/README.md) · 2025 · Kimi Team · 文献卡 · 格：层排布 = KDA:MLA 3:1
- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](../../papers/arxiv-2512.02556/README.md) · 2025 · DeepSeek-AI · 技术精读 · 格：序列混合 = DSA · DeepSeek 架构线第 5 步
- [mHC: Manifold-Constrained Hyper-Connections](../../papers/arxiv-2512.24880/README.md) · 2025 · DeepSeek-AI · 技术精读 · 格：深度方向 = 双随机约束 · DeepSeek 架构线第 6 步

## 7 深度与记忆成为新轴，KV 缓存成为一等目标（2026）

- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](../../papers/arxiv-2601.07372/README.md)（Engram） · 2026 · 北京大学、DeepSeek-AI · 技术精读 · 格：通道混合 = 条件记忆 · DeepSeek 架构线第 7 步
- [Attention Residuals](../../papers/arxiv-2603.15031/README.md) · 2026 · Kimi Team · 文献卡 · 格：深度方向 = 跨层注意力
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](../../papers/arxiv-2606.19348/README.md) · 2026 · DeepSeek-AI · 技术精读 · 格：KV 缓存 = CSA/HCA；层排布 = 哈希路由 · DeepSeek 架构线第 8 步
- [Kimi K3: Open Frontier Intelligence](../../papers/arxiv-2607.24653/README.md) · 2026 · Kimi Team · 文献卡 · 格：层排布 = KDA 混合 + 最后一层全局；深度方向 = AttnRes
- [Tokenizer-Agnostic Engram Module](../../papers/arxiv-2607.29065/README.md) · 2026 · 文献卡 · 格：通道混合 = 条件记忆的后续（表与分词器解绑）
- [Frozen Memory Is Not Enough: Rethinking External Memory as Extraction](../../papers/arxiv-2608.17050/README.md) · 2026 · 文献卡 · 格：通道混合 = 条件记忆的后续（跨模型读取器）
- [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](../../papers/arxiv-2609.19969/README.md) · 2026 · DeepSeek-AI · 技术精读 · 格：KV 缓存 = CSA2 + FP4 · DeepSeek 架构线第 9 步

## 推理期方法（在其他方向详述）

- [Efficient Streaming Language Models with Attention Sinks](../../papers/arxiv-2309.17453/README.md)（StreamingLLM） · 2023 · 文献卡 · 格：序列混合 = 推理期保留开头 token 加滑窗；主页面在[长上下文方向](../long-context/README.md)
- [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](../../papers/arxiv-2402.02750/README.md) · 2024 · 文献卡 · 格：KV 缓存 = 低比特量化；主页面在[推理时计算方向](../inference/README.md)

## 跨方向交叉引用（归属其他方向，在此不展开）

- [Qwen2 Technical Report](../../papers/arxiv-2407.10671/README.md) · 2024 · 文献卡
- [Qwen2.5-1M Technical Report](../../papers/qwen2.5-1m/README.md) · 2025 · 技术精读（长上下文方向）
- [Language Models are Few-Shot Learners](../../papers/gpt3/README.md) · 2020 · 技术精读（预训练方向）
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](../../papers/arxiv-2002.10957/README.md) · 2020 · 文献卡（模型压缩）
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](../../papers/arxiv-1910.01108/README.md) · 2019 · 文献卡（模型压缩）
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](../../papers/arxiv-2009.08366/README.md) · 2020 · 文献卡（代码表示）
- [Naturalness of Attention: Revisiting Attention in Code Language Models](../../papers/arxiv-2311.13508/README.md) · 2023 · 文献卡（模型科学，见[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 3 节）
