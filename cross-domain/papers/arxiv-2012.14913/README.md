# Transformer Feed-Forward Layers Are Key-Value Memories

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2012.14913)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：FFN（前馈子层）约占 Transformer 参数的三分之二，它在网络中起什么作用却很少被研究。
- **核心方法**：把 FFN(x) = f(xW_1)W_2 读作键值记忆（这一形式与 Sukhbaatar 等 2015 的键值神经记忆几乎相同）：W_1 的列是 key，与训练样本中的文本模式相关；W_2 的行是 value，在输出词表上诱导一个分布。在一个 16 层、WikiText-103 上训练的语言模型里，key 对应人能读懂的模式，低层偏浅层模式、高层偏语义模式；高层 value 把概率集中在紧跟该模式之后可能出现的词上；一层 FFN 的输出是多条记忆的组合，再经残差连接逐层修正成最终的输出分布。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 4 节"FFN 是一张用参数写成的键值表"节点：FFN 与注意力同形，只是 key 和 value 换成了固定参数、softmax 换成了 ReLU。上一节点 [Naturalness of Attention](../../../llm/papers/arxiv-2311.13508/README.md) 讨论注意力内部的分工；下一节点 [ROME](../arxiv-2202.05262/README.md) 用因果追踪定位事实，并把单个中层 MLP 当作这张键值表来改写；链尾的 [Engram](../../../llm/papers/arxiv-2601.07372/README.md) 在相关工作中直接引用本篇。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2012.14913 · [全文 PDF](https://arxiv.org/pdf/2012.14913)
- 方向：cross-domain/model-science
