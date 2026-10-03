# Probing Pretrained Models of Source Code

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2202.08975)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CodeBERT、CodeT5 等通用预训练代码模型在许多代码任务上超过了专用模型，但它们可能并没有理解源代码的某些性质，需要逐项检验。
- **核心方法**：把 NLP 中成熟的探针方法（在冻结模型的隐藏表示上训练简单的线性模型，看能否预测某个性质）用到代码模型上：设计一组诊断任务，在每个模型每一层提取的表示上训练线性分类器或回归器（另用 3 层 MLP 复核，结果相近）。结果显示预训练代码模型的表示中含有代码语法结构与正确性、标识符、数据流、命名空间和自然语言命名的信息；论文还比较了代码专用预训练目标、模型规模和微调对探针结果的影响。
- **为什么在这个库里**：本篇位于[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)之外：探针读取的是整层输出，其中混合了注意力与 FFN 两个子层的贡献。它与链上第 3 节的 [Naturalness of Attention](../arxiv-2311.13508/README.md) 研究同一个问题，即代码模型捕获了哪些语法结构，后者从注意力内部拆分权重与被读取的向量，本篇从各层表示整体读取。它对应[机制与可信解释](../../../cross-domain/fields/interpretability/README.md)入门页指出的边界：探针能预测某个性质，说明信息存在于表示中，模型是否依赖它还需要干预实验来检验。后续的 [INSPECT](../../../cross-domain/papers/arxiv-2312.05092/README.md) 在相关工作中引用并对照了本篇的逐层结果。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2202.08975 · [全文 PDF](https://arxiv.org/pdf/2202.08975)
- 方向：llm/pretraining、cross-domain/interpretability
