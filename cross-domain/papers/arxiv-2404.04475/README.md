# Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.04475)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用 LLM 自动打分的评测（AlpacaEval、MT-Bench 等）与人类偏好高度相关，但部分靠的是输出长度、列表等虚假相关；AlpacaEval 偏爱更长的输出，作为排行榜时被模型钻了空子（摘要、§2）。
- **核心方法**：把长度看作因果图中不希望起作用的中介变量：拟合一个广义线性模型，用"模型与基线的长度差"及其他特征预测裁判的偏好，再把长度差设为 0 预测偏好，得到长度控制胜率（AlpacaEval-LC，回答"如果两份回答一样长，裁判会偏好谁"）。只让模型改变详略程度：原版 AlpacaEval 上基线模型 gpt4_1106_preview 的胜率在 22.9% 到 64.3% 之间变化，长度控制后为 41.9% 到 51.6%；与 Chatbot Arena 排名的 Spearman 相关从 0.94 升到 0.98。自述局限：只在 AlpacaEval 上验证；"按同样长度比较"本身是一个简化假设；不处理 LLM 裁判的其他问题。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"裁判偏差"一节的统计修正代表：偏差能被测出就能被回归掉，但只针对事先猜到的那个变量。它的作者在 Hashimoto 组，同组还有 [污染检验](../arxiv-2310.17623/README.md)与 [HELM](../arxiv-2211.09110/README.md)。后训练报告（如 DeepSeek-R1）报告的正是长度控制版胜率，见[后训练方向](../../../llm/fields/posttraining/README.md)"用什么衡量进展"。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2404.04475 · [全文 PDF](https://arxiv.org/pdf/2404.04475) · Stanford University
- 发表：COLM 2024
- 方向：cross-domain/evaluation、llm/posttraining/preferences
