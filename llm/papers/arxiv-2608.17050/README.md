# Frozen Memory Is Not Enough: Rethinking External Memory as Extraction

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2608.17050)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Engram 式哈希记忆把学到的信息存在外部可寻址的表里，再由一个小的读取器使用；把这张表搬到另一个主干模型上时，决定效果的是冻结的表本身，还是目标模型一侧的读取器。
- **核心方法**：相对 [Engram](../arxiv-2601.07372/README.md) 在同一模型内训练并使用记忆表，本篇做"跨模型冻结记忆抽取"：在源模型上训练好的表冻结后接到另一个目标模型，只训练一个轻量读取器。消融显示，表的内容与正确寻址都有作用，但表只有通过与目标模型对齐的读取器才发挥作用；双层、四分支的读取器在下游问答任务上几乎追平同模型复用。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 9 节"记忆表成为可以移植的部件"节点：它在模块尺度上重现了 [Dissecting Recall](../../../cross-domain/papers/arxiv-2304.14767/README.md)（第 6 节）在 Transformer 内部看到的形状，即存储与读出是两个部件，读出一侧决定存下的东西能否被用上。上一节点是 [Engram](../arxiv-2601.07372/README.md)，同一节点的 [Tokenizer-Agnostic Engram Module](../arxiv-2607.29065/README.md) 处理的是表与分词器的绑定。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2608.17050 · [全文 PDF](https://arxiv.org/pdf/2608.17050)
- 题名：arXiv v1–v2 的题名为 *Cross-Model Memory Transfer via Target-Side Reader Adaptation*；v3（2026-09-30）起改为现题名，摘要未变。
- 方向：llm/architecture
