# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2204.05862)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用偏好建模与 RLHF 训练一个既有帮助又无害的助手，并测它对其他能力的影响。
- **核心方法**：分别收集帮助性与无害性（红队）的对比数据训练偏好模型，用 PPO 训练策略，并每周用最新模型在线迭代数据。发现：小模型 RLHF 后多数评测下降（对齐税，一句话：为对齐付出的能力代价），13B 与 52B 在 zero-shot 评测上反而变好；RL 奖励与"策略相对初始模型的 KL 的平方根"大致成线性；偏好模型给分越高越不可靠，大偏好模型更稳健；早期策略对一切稍敏感的问题都给出"建议寻求专业帮助"之类夸张回答，作者归因于对无害性过度优化、对帮助性优化不足（§4.4）。
- **为什么在这个库里**：[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)中"对齐税"与"帮助性—无害性张力"的主要证据；后者直接导致 Llama 2 分开训练两个奖励模型。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2204.05862 · [全文 PDF](https://arxiv.org/pdf/2204.05862) · Anthropic
- 方向：llm/posttraining/preferences、llm/posttraining/rl
