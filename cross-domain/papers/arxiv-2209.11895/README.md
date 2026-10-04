# In-context Learning and Induction Heads

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2209.11895)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大模型的上下文学习（不更新参数、只靠提示中的例子学会新模式；作者用"序列中越靠后的 token 损失越低"来度量）由什么机制实现。
- **核心方法**：作者的前作 *A Mathematical Framework for Transformer Circuits*（Elhage 等 2021）在 2 层纯注意力模型中发现了 induction head（完成 [A][B] … [A] → [B] 续写的注意力头，由"前一 token 头"与 induction head 两个头跨层组合实现）；本篇把分析推广到带 MLP 的各种规模模型，发现 induction head 的形成与上下文学习能力的骤升发生在训练早期的同一时刻（训练损失曲线上的一个"鼓包"），并给出六条互补证据：小型纯注意力模型上的证据是因果性的，带 MLP 的大模型上是相关性的。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 2 节节点："前一 token 头"只按相对位置读取，induction head 的前缀匹配发生在决定注意力模式的 QK 电路、复制发生在决定输出内容的 OV 电路，正是第 1 节"A 决定读哪里、V 决定读到什么"的分工（[15-qkv-deep-dive.md](../../../foundations/lessons/15-qkv-deep-dive.md) 第 4–5 节）。下一节点 [Naturalness of Attention](../../../llm/papers/arxiv-2311.13508/README.md) 在代码模型上说明只看注意力权重会漏掉被读出的内容；链尾的 [Engram](../../../llm/papers/arxiv-2601.07372/README.md) 与本篇形成对照：induction head 依赖当前上下文复制模式，Engram 用参数表存储静态 N-gram。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2209.11895 · [全文 PDF](https://arxiv.org/pdf/2209.11895)
- 方向：cross-domain/model-science
