# Scaling Laws for Reward Model Overoptimization

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2210.10760)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：奖励模型是人类偏好的不完美代理，优化过头会伤害真实目标（Goodhart 定律），但这一效应缺少系统测量。
- **核心方法**：用一个固定的大"黄金"奖励模型充当人类，为代理奖励模型提供标签，测量用 RL 或 best-of-n 优化代理奖励时黄金分数怎样变化：黄金分数先升后降，两种优化方式的函数形式不同，系数都随奖励模型参数量平滑变化；更大的策略本身更好，但过度优化的程度相近；在他们的 RL 设定中，KL 惩罚能提高给定 KL 下的代理分数，却没有改善黄金分数与 KL 的前沿（作者提醒这一结论可能对超参数敏感）。
- **为什么在这个库里**：后训练总览"奖励过度优化"一条的定量依据，[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)"正则"一格；DeepSeek-R1 放弃过程奖励模型时引用它。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2210.10760 · [全文 PDF](https://arxiv.org/pdf/2210.10760) · OpenAI
- 方向：llm/posttraining/preferences、llm/posttraining/rl
