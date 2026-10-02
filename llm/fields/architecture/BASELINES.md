# 架构与效率：Baseline与对照阅读

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md)

这些条目用于建立问题、机制或评估的参照。跨方向辅助阅读不是对本方向的完整覆盖，也不代表这些方法在所有任务上都构成可直接比较的实验baseline。

## transformer

[Attention Is All You Need](../../papers/transformer/README.md)

清楚定义注意力、因果解码、自注意力/交叉注意力和位置表征的原始架构参照。

## mamba

[Mamba: Linear-Time Sequence Modeling with Selective State Spaces](../../papers/mamba/README.md)

状态选择与递推作为注意力以外的序列建模基线；线性复杂度不等于线性注意力。

## deepseek-v2

[DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../papers/deepseek-v2/README.md)

同篇用DeepSeekMoE解释条件计算，用MLA解释KV压缩；两种收益分开记录，非MoE历史首篇。

