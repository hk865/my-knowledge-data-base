# Real-Time Execution of Action Chunking Flow Policies

> 状态：文献卡 · 2025

- **解决什么**：大模型生成动作块时，旧动作仍在执行；跨块停顿与跳变影响闭环。
- **核心方法**：RTC 把异步接续写成前缀条件补全，在推理时引导连续生成策略接续旧队列。 [1]
- **为什么在这个库里**：[VLA Baseline](../../fields/vla/BASELINES.md)的“推理调度”一格；与训练时 RTC 对照读。优先级：必读。

## 参考文献

[1] [官方原文](https://arxiv.org/abs/2506.07339)。
