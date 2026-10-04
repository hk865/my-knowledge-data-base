# The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2505.22617)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：推理 RL 中，策略熵在训练早期急剧降到接近 0，模型过早确定，性能随之饱和。
- **核心方法**：在多种模型上拟合出性能与熵的经验关系 R = −a·exp(H) + b：性能是用熵"换"来的，熵耗尽时性能上限可以预测；推导出熵的变化由"动作概率与对数几率变化的协方差"驱动，在策略梯度下正比于优势，高概率且优势高的 token 会压低熵；据此只限制高协方差 token 的更新（Clip-Cov、KL-Cov）。作者报告在 Qwen2.5-32B 上 AIME24、AIME25 比 GRPO 分别提高 15.0% 与 14.6%，并指出直接加熵正则无效。
- **为什么在这个库里**：后训练总览"熵坍缩"一条的机制解释，[RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)"裁剪"一格；与 DAPO 的 Clip-Higher 对照着读（原文把 Clip-Higher 作为主要基线）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2505.22617 · [全文 PDF](https://arxiv.org/pdf/2505.22617) · 上海人工智能实验室、清华大学、UIUC、北京大学等
- 方向：llm/posttraining/rl
