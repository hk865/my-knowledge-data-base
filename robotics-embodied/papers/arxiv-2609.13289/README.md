# Extending the Speed Limit of Quadrupedal Locomotion via Refined Actuator Modeling and Adaptive Command Scheduling

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.13289v1)

- **解决什么**：高速四足训练中，电机能力被高估、速度命令跳到当前状态难以实现的位置，都会使策略失稳。
- **核心方法**：相对简化力矩—转速包络与全范围均匀命令采样，细化电压耦合和磁饱和建模，并以当前实际速度为中心限制下一条速度命令的邻域。
- **为什么在这个库里**：补充[控制基线](../../fields/control-locomotion/BASELINES.md)中的“仿真器保真度”和“训练分布”，与 [TARC](../arxiv-2510.23176/README.md) 对照命令内容与更新时间；具体辨析见[命令与时间专题](../../fields/control-locomotion/time-and-command.md)。优先级：必读。
