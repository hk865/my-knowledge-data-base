# Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2504.13837)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：RLVR 是否真的让模型获得基座没有的新推理能力。
- **核心方法**：用大 k 的 pass@k（k 次采样中至少一次答对的比例）衡量"能力边界"，覆盖多个模型族、六种 RL 算法（PPO、GRPO、Reinforce++、RLOO、ReMax、DAPO）与数学、代码、视觉推理：RLVR 模型在小 k（如 k = 1）上更好，k 大时基座的 pass@k 反而更高；RLVR 模型的推理路径已包含在基座的采样分布中，训练越久边界越窄；六种算法差别不大，离"基座潜力"这个上界都很远；蒸馏能引入老师的新推理模式，真正扩大边界。作者自述：最强的模型与训练流程多是闭源的，无法纳入（§7）。
- **为什么在这个库里**：后训练总览"RL 能否超出基座能力"一问的主要证据，[RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)"评测口径"一行；结论与 DeepSeekMath §5.2.2、Qwen3 Table 21 一致。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2504.13837 · [全文 PDF](https://arxiv.org/pdf/2504.13837) · 清华大学 LeapLab、上海交通大学
- 方向：llm/posttraining/rl
