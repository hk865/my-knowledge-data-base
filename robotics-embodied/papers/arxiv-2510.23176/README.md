# TARC: Time-Adaptive Robotic Control

> 状态：文献卡 · 2025 首发 / CoRL 2026 · [原文](https://arxiv.org/abs/2510.23176v2)

- **解决什么**：固定高频策略查询消耗计算，而固定低频查询又会延后动态阶段的反应。
- **核心方法**：相对固定频率 PPO，策略同时选择动作和保持时长，在查询预算下学习何时更新；通过查询代价折中性能与频率，或以自适应拉格朗日乘子追踪预算。
- **为什么在这个库里**：补充[控制基线](../../fields/control-locomotion/BASELINES.md)的“动作接口”和“系统结构”，与 [ACS](../arxiv-2609.13289/README.md) 对照主动安排更新时间与限制命令变化；见[命令与时间专题](../../fields/control-locomotion/time-and-command.md)。优先级：必读。
