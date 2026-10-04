# Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.05695)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：人形机器人结构复杂，sim-to-real 差距比四足更大，缺一个容易上手、能零样本迁移到实机的训练框架。
- **核心方法**：基于 Isaac Gym 做大规模并行 RL（代码复用 legged_gym 与 rsl_rl 的 LeggedRobot 实现），加入针对人形的奖励和域随机化；新增从 Isaac Gym 到 MuJoCo 的 sim-to-sim 验证：GPU 仿真快但精度较低，先在校准过的 MuJoCo 中检查策略，再上实机。在 RobotEra 的 XBot-S（1.2 m）和 XBot-L（1.65 m）两种人形上零样本迁移。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向的训练基础设施（人形版），相当于 [Rudin 等 2021](../arxiv-2109.11978/README.md) 流程向人形的移植；sim-to-sim 这一步同样适用于四足策略上机前的检查。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2404.05695
- 作者：Xinyang Gu、Yen-Jen Wang、Jianyu Chen
- 全文：[arXiv PDF](https://arxiv.org/pdf/2404.05695)
- 发表：ICRA 2024 Workshop on Agile Robotics（arXiv 期刊信息）
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
