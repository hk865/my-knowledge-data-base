# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

> 状态：逐步教学版 · 2023 · [原文](https://arxiv.org/abs/2305.18290)

[返回大语言模型目录](../../README.md)

- **解决什么**：RLHF（基于人类反馈的强化学习）要先拟合奖励模型、再用强化学习优化语言模型，流程复杂且不稳定。
- **核心方法**：相对 InstructGPT 的"奖励模型 + PPO"，给 RLHF 中带 KL 正则（约束新模型不偏离参考模型太远）的目标换一种奖励参数化，使最优策略有闭式解；于是只需在偏好对（同一提示下被偏好与不被偏好的两个回答）上用一个简单的分类损失直接训练语言模型，比较时扣除冻结参考模型对两者原有的偏向，训练中不需要从模型采样。情感控制上超过基于 PPO 的 RLHF，摘要与单轮对话上相当或更好。
- **为什么在这个库里**：[偏好学习方向](../../fields/posttraining/preferences/README.md)的基线：[Qwen2](../arxiv-2407.10671/README.md) 的离线偏好阶段直接用它，[过度思考](../url-https-proceedings.mlr.press-v267-chen25bx.html/README.md)等工作把它与其变体 RPO、SimPO 并列比较。教学版从一对回答出发推到损失与梯度。优先级：必读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json) · [作者归属与许可](ATTRIBUTION.md)

## 阅读顺序

[Training language models to follow instructions with human feedback](../instructgpt/README.md)（DPO 要简化的 RLHF 流程）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2305.18290 · [全文 PDF](https://arxiv.org/pdf/2305.18290v3) · NeurIPS 2023 · 教学版依据 v3
- 作者：Rafael Rafailov、Archit Sharma、Eric Mitchell、Stefano Ermon、Christopher D. Manning、Chelsea Finn（斯坦福，另有 CZ Biohub）
- 方向：llm/posttraining/preferences
