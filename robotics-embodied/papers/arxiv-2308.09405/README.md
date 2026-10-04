# Robust Quadrupedal Locomotion via Risk-Averse Policy Learning

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2308.09405)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：特权蒸馏、场景建模和外部传感器提高了四足策略的泛化与鲁棒性，但地形突变、意外外力这类不确定情况仍难处理。
- **核心方法**：从风险敏感的角度改策略学习：critic 用分位数回归学习分布式价值函数（一句话：估计回报的整个分布而不只是均值），表示环境的偶然不确定性；策略优化 CVaR（条件风险价值，一句话：回报分布中最差一部分的均值）这类风险扭曲度量，即针对最坏情况优化，得到风险规避策略；更新仍用 GAE 和 PPO-Clip。在仿真和 Aliengo 四足实机上，对各种外部扰动更鲁棒。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「RL 目标」部件上的改动。在[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)中属于「算法与损失」一类，回答「怎样少进入低概率、高代价的坏情况」，与恢复本身分开评估。与 [Schneider 等 2023](../arxiv-2309.14246/README.md) 是同期、不同团队的同类工作。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2308.09405
- 作者：Jiyuan Shi、Chenjia Bai 等（共 9 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2308.09405)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
