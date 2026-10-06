# SimEX: Simulation-Integrated Robotics AutoResearch

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.38982)

- **解决什么**：机器人上的程序试错昂贵，怎样先在模拟环境里改进工具，再用少量真机反馈修正。
- **核心方法**：相对一次性生成策略代码，Agent反复在仿真测试并改写代码工具箱，用真机rollout对齐模拟器，再并行比较修复程序。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中的“实验工具与程序经验”主线，把仿真作为可修改的外部工具。优先级：必读。
