# Naturalness of Attention: Revisiting Attention in Code Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.13508)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：此前对代码语言模型的注意力分析只看注意力权重，忽略了注意力机制中权重以外的因素，可能看错模型捕获的代码性质。
- **核心方法**：相对只分析注意力权重的前作（Sharma 等、Wan 等对 CodeBERT 一类模型的注意力分析），沿用 Kobayashi 等的范数分析，把多头注意力的输出拆成注意力权重与被读取向量经变换后的范数两部分，在 CodeBERT（在源代码与自然语言上预训练的 BERT 式编码器）上比较哪一部分更符合代码语法结构；在 Java 与 Python 上，经权重缩放的变换范数比单看权重更好地反映语法结构。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 3 节节点：权重显示位置关系，被读出的内容在变换后的向量里，这是第 1 节 A 与 V 分工在实验中的体现。上一节点 [In-context Learning and Induction Heads](../../../cross-domain/papers/arxiv-2209.11895/README.md) 把注意力头拆成 QK 与 OV 两个电路；下一节点 [FFN 键值记忆](../../../cross-domain/papers/arxiv-2012.14913/README.md) 转向 FFN。同样研究代码模型捕获了哪些语法结构的 [Probing Pretrained Models of Source Code](../arxiv-2202.08975/README.md) 与 [INSPECT](../../../cross-domain/papers/arxiv-2312.05092/README.md) 从各层整体表示入手，位于这条链之外。优先级：选读（ICSE 2024 NIER 赛道的初步研究，只覆盖 CodeBERT）。

## 身份信息

- 稳定标识：arxiv:2311.13508 · [全文 PDF](https://arxiv.org/pdf/2311.13508)
- 方向：llm/architecture、cross-domain/interpretability
