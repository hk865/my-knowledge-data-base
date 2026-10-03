# Tokenizer-Agnostic Engram Module

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.29065)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Engram（DeepSeek 的条件记忆模块，按 N-gram 哈希查嵌入表）按 token 级 N-gram 做哈希，嵌入表与所用分词器绑定，换用不同分词器的模型必须从头训练自己的表。
- **核心方法**：相对 [Engram](../arxiv-2601.07372/README.md) 只改哈希例程：不再把各阶 N-gram 当作互不相交的空间，而是把 N-gram 看作从跨 token 的全部字节序列中采样，用一般的多项式哈希替换基于 XOR 的哈希，各阶 N 共用一个嵌入空间。这一替换的性能与原方法相近，并使字节相同的 token 序列得到相同的哈希，表因此能在分词器不同的 Engram 模型之间复用。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 9 节"记忆表成为可以移植的部件"节点：上一节点 [Engram](../arxiv-2601.07372/README.md) 把静态模式做成查表，本篇解除表与分词器的绑定；同一节点的 [Cross-Model Memory Transfer](../arxiv-2608.17050/README.md) 研究把表搬到另一个模型时需要什么样的读取器。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2607.29065 · [全文 PDF](https://arxiv.org/pdf/2607.29065)
- 方向：llm/architecture
