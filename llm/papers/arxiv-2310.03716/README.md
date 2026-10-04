# A Long Way to Go: Investigating Length Correlations in RLHF

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.03716)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：RLHF 常让回答变长，这种变长在 RLHF 的"改进"里占多大比重。
- **核心方法**：在三个开源偏好设定上分析 RLHF 怎样提高奖励：奖励的提高主要来自回答变长，而不是其他特征；只用"回答长度"做奖励就能复现相对 SFT 的大部分提升；在一系列抵消长度的干预中，偏差的主要来源是奖励模型，它们不稳健，容易被偏好数据中的长度偏差带偏。
- **为什么在这个库里**：[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)"长度偏置"的主证据；后来的长度控制版评测、SimPO 的长度归一化、DeepSeek-R1 训练奖励模型时让被选与被拒回答长度相当，都在处理这个坑。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2310.03716 · [全文 PDF](https://arxiv.org/pdf/2310.03716) · UT Austin、Princeton、Salesforce · COLM 2024
- 方向：llm/posttraining/preferences
