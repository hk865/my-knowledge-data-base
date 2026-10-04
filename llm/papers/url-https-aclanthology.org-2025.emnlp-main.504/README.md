# Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps

> 状态：文献卡 · 2025 · [原文](https://aclanthology.org/2025.emnlp-main.504/)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：思维链（CoT）写出的推理是否忠实于模型参数中的信念（参数忠实性）。
- **核心方法**：此前的工作多通过扰动 CoT 中的 token 观察预测变化来测忠实性；本篇提出测量参数忠实性的框架及其实例 FUR：用遗忘（unlearning，从模型参数中抹去某段信息）删除某个推理步骤所含的信息，以预测因此改变的程度作为忠实性。在 4 个模型、5 个多选问答数据集上，遗忘关键步骤常能精确改变模型对该实例的预测；遗忘后模型生成的 CoT 会支持不同的答案。
- **为什么在这个库里**：[模型科学方向](../../../cross-domain/fields/model-science/README.md)与[评估与监督可靠性方向](../../../cross-domain/fields/evaluation/README.md)"思维链忠实性"一问的参数层面测量；与 [Making Reasoning Matter](../url-https-aclanthology.org-2024.findings-emnlp.882/README.md) 的行为层面因果分析对照。优先级：选读。

## 身份信息

- 稳定标识：doi:10.18653/v1/2025.emnlp-main.504 · [全文 PDF](https://aclanthology.org/2025.emnlp-main.504.pdf) · EMNLP 2025 主会（arXiv 页注明获 Outstanding Paper）· 预印本 arXiv:2502.14829
- 作者：Martin Tutek、Fateme Hashemi Chaleshtori、Ana Marasović、Yonatan Belinkov（以色列理工学院、犹他大学）
- 方向：llm/inference、cross-domain/model-science、cross-domain/evaluation
