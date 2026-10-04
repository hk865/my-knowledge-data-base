# SimPO: Simple Preference Optimization with a Reference-Free Reward

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.14734)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：DPO 的隐式奖励与生成时用的似然不一致，而且训练时要额外加载参考模型。
- **核心方法**：用回答的平均对数概率（按长度归一化）作隐式奖励，去掉参考模型，并在 Bradley–Terry 目标里加一个目标奖励间隔；在 AlpacaEval 2 上比 DPO 最多高 6.4 分、在 Arena-Hard 上最多高 7.5 分，回答长度没有明显增加。作者自述：偏好优化普遍会降低 GSM8K 这类推理任务的表现，SimPO 有时与 DPO 持平或更差，一种解释是目标拉大了间隔，却没有提高被选回答的似然（附录 A）。
- **为什么在这个库里**：[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)"损失形式 = 长度归一化、无参考模型"一格；它记录的数学退化，与 Llama 3 给 DPO 加 NLL 项处理的是同一个坑。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2405.14734 · [全文 PDF](https://arxiv.org/pdf/2405.14734) · 弗吉尼亚大学、Princeton
- 方向：llm/posttraining/preferences
