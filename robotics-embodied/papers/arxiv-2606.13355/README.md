# Real-Time Execution with Autoregressive Policies

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.13355)

- **解决什么**：自回归动作的串行生成怎样在不停止机器人的情况下部署。
- **核心方法**：π0-REALFAST 分段 FAST 分词，以队列前缀条件化，用受限解码控制 token 合法性与预算。
- **为什么在这个库里**：[VLA Baseline](../../fields/vla/BASELINES.md)的"动作表示 + 推理调度"一格；为"离散只用于训练"提供有范围的反例。优先级：必读。
