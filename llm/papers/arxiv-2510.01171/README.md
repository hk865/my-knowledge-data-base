# Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.01171)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：后训练对齐常让 LLM 的输出多样性下降，即模式坍缩（回答集中到少数典型说法上）。
- **核心方法**：已有工作把模式坍缩归因于算法；本篇指出一个数据层面的驱动：偏好数据中的典型性偏差（认知心理学发现标注者系统性地偏爱熟悉的文本），在理论上形式化，并在偏好数据集上做了实证验证。据此提出无需训练的提示法 Verbalized Sampling：让模型说出一组回答及其概率（例如"生成 5 个关于咖啡的笑话及各自的概率"）。在创意写作中多样性比直接提示高 1.6–2.1 倍，事实准确性和安全性不降；能力越强的模型获益越多。
- **为什么在这个库里**：[偏好学习方向](../../fields/posttraining/preferences/README.md)"偏好数据本身带来什么副作用"、[模型科学方向](../../../cross-domain/fields/model-science/README.md)"对齐后的输出分布为何变窄"两问的证据，并给出[推理时计算方向](../../fields/inference/README.md)中不改权重的补救。与 [InstructGPT](../instructgpt/README.md)、[DPO](../dpo/README.md) 对照阅读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2510.01171 · [全文 PDF](https://arxiv.org/pdf/2510.01171) · 代码在 CHATS-lab/verbalize-sampling
- 作者：Jiayi Zhang、Simon Yu、Derek Chong、Anthony Sicilia、Michael R. Tomz、Christopher D. Manning、Weiyan Shi（东北大学、斯坦福、西弗吉尼亚大学）
- 方向：llm/inference、llm/posttraining/preferences、cross-domain/model-science
