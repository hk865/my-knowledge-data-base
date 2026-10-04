# Reasoning Does Not Necessarily Improve Role-Playing Ability

> 状态：文献卡 · 2025 · [原文](https://aclanthology.org/2025.findings-acl.537/)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：推理技术（思维链、专为推理优化的模型）能否提升 LLM 的角色扮演能力。
- **核心方法**：在 6 个角色扮演基准、24 个 LLM 上比较三种策略：直接零样本扮演、加 CoT 扮演、用推理优化模型扮演。发现 CoT 可能降低扮演表现，推理优化模型不适合角色扮演，推理能力打乱了角色扮演的规模规律，大模型在高级扮演上仍不足；提出角色感知的 CoT 与面向角色扮演的强化学习两个方向。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)中"推理增益的边界"一问的反例证据；[评估与监督可靠性方向](../../../cross-domain/fields/evaluation/README.md)里可与 [PersonaEval](../../../cross-domain/papers/arxiv-2508.10014/README.md)（评审模型能否像人一样评判角色扮演）一起读。优先级：存档。

## 身份信息

- 稳定标识：doi:10.18653/v1/2025.findings-acl.537 · [全文 PDF](https://aclanthology.org/2025.findings-acl.537.pdf) · Findings of ACL 2025 · 预印本 arXiv:2502.16940
- 作者：Xiachong Feng、Longxu Dou、Lingpeng Kong（香港大学、Sea AI Lab）
- 方向：llm/inference、cross-domain/evaluation、cross-domain/model-science
