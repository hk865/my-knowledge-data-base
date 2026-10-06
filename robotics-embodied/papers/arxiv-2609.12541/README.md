# Agent as Policy for Robotic Manipulation

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.12541)

- **解决什么**：通用代码Agent能否在不另训动作策略的情况下，把观察、几何计算与机器人执行组合成新任务程序。
- **核心方法**：沿Code as Policies的程序接口路线，冻结Agent在真实运行时选择观测、写程序并调用末端、关节和夹爪接口，根据执行误差继续修正。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中的冻结模型加物理工具主线，适合与HarnessVLA的已有动作原语路线对照。优先级：必读。
