# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

> 状态：技术精读 · 2023 · [原文](https://arxiv.org/abs/2312.00752)

[返回大语言模型目录](../../README.md)

- **解决什么**：线性注意力、门控卷积、结构化状态空间模型（SSM：把历史压进固定大小的状态、按线性递推更新的序列模型）等次二次方架构，在语言上都不如注意力；关键弱点是不能按内容选择记住或忘掉什么。
- **核心方法**：相对 S4 等参数不随时间变化的 SSM，让 SSM 的参数（步长 Δ 和 B、C）随当前输入变化，即选择机制；代价是不能再用卷积训练，于是设计硬件感知的并行 scan 算法。整块网络不用注意力，也不用单独的 MLP 块。推理吞吐是 Transformer 的 5 倍，计算随序列长度线性增长；Mamba-3B 在语言建模上超过同规模 Transformer，与两倍大的 Transformer 相当。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"注意力与状态空间模型"一格的代表；与同一递推谱系的 [LRU](../arxiv-2303.06349/README.md)、线性注意力混合架构 [Kimi Linear](../arxiv-2510.26692/README.md) 对照。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json) · [作者归属与许可](ATTRIBUTION.md)
- 关系页：[递推状态谱系](../../../foundations/relations/recurrent-state.md)第 4 节"Mamba"节点（转移随输入变化、不随状态变化，因而既能按内容选择又能并行 scan）

## 阅读顺序

[Attention Is All You Need](../transformer/README.md)（被替代的注意力）→ [Resurrecting Recurrent Neural Networks for Long Sequences](../arxiv-2303.06349/README.md)（线性递推的稳定参数化）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2312.00752 · [全文 PDF](https://arxiv.org/pdf/2312.00752v2) · 精读依据 v2
- 作者：Albert Gu（CMU）、Tri Dao（普林斯顿）
- 方向：llm/architecture、llm/pretraining、llm/inference
