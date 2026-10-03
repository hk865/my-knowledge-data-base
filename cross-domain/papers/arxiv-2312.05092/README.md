# INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2312.05092)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：预训练代码模型已用于代码补全等实际场景，但它们从源代码中学到了什么，仍所知甚少。
- **核心方法**：扩展作者 ASE 2021 的前作 *What do pre-trained code models know about code?*（arXiv:2108.11308），用一个可扩展的框架定义 15 个探针任务（在冻结模型的各层表示上训练简单分类器，看能否预测某个性质），覆盖源代码的表层、语法、结构与语义特征，对 8 个预训练代码模型和自然语言模型 BERT（作为基线）做探针。融入结构信息的模型（如 GraphCodeBERT）对代码特征表示得更好；BERT 在部分任务上与代码模型不相上下，说明代码专用预训练在这些特征上还有改进空间。
- **为什么在这个库里**：本篇位于[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)之外：探针读取的是整层表示，其中混合了注意力与 FFN 两个子层的贡献。它与链上第 3 节的 [Naturalness of Attention](../../../llm/papers/arxiv-2311.13508/README.md) 都在问代码模型捕获了哪些语法结构，本篇的比较维度是模型之间与层之间；相关工作中引用并对照了 [Probing Pretrained Models of Source Code](../../../llm/papers/arxiv-2202.08975/README.md) 的逐层结果。它的逐层发现是结构类任务在中间层表现最好、语义类任务倾向于在末层最好，可与 [FFN 键值记忆](../arxiv-2012.14913/README.md)中"低层偏浅层模式、高层偏语义模式"对照（两者测量的对象不同：本篇是整层表示，后者是 FFN 的 key）。它也对应[机制与可信解释](../../fields/interpretability/README.md)入门页指出的边界：探针能预测某个性质，说明信息存在于表示中，模型是否依赖它还需要干预实验来检验。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2312.05092 · [全文 PDF](https://arxiv.org/pdf/2312.05092)
- 发表：IEEE Transactions on Software Engineering
- 方向：cross-domain/interpretability、cross-domain/evaluation
