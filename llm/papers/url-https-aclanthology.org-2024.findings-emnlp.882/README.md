# Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning

> 状态：文献卡 · 2024 · [原文](https://aclanthology.org/2024.findings-emnlp.882/)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让 LLM 先分步推理再作答效果更好，但最终答案在多大程度上真的依据了它写出的推理步骤并不清楚。
- **核心方法**：先在 12 个 LLM 上做因果中介分析，发现模型生成答案时并不可靠地使用自己的中间推理步骤。再提出 FRODO 来训练小模型：推理模块用隐式的因果奖励学会生成正确的推理步骤，作答模块用反事实与因果偏好目标学会忠实地依据这些步骤作答。FRODO 优于四个基线，分布外测试更稳健，理由与答案的一致性高于标准 SFT。
- **为什么在这个库里**：[模型科学方向](../../../cross-domain/fields/model-science/README.md)与[评估与监督可靠性方向](../../../cross-domain/fields/evaluation/README.md)中"思维链忠实性"一问：写出来的推理不一定是模型真正使用的推理。与 [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](../url-https-aclanthology.org-2025.emnlp-main.504/README.md) 对照：本篇做行为层面的因果干预并训练修正，后者从参数层面删除步骤来测量。优先级：选读。

## 身份信息

- 稳定标识：doi:10.18653/v1/2024.findings-emnlp.882 · [全文 PDF](https://aclanthology.org/2024.findings-emnlp.882.pdf) · Findings of EMNLP 2024 · 预印本 arXiv:2402.13950
- 作者：Debjit Paul、Robert West、Antoine Bosselut、Boi Faltings（EPFL）
- 方向：llm/inference、cross-domain/model-science、cross-domain/evaluation
