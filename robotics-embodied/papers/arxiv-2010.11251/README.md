# Learning Quadrupedal Locomotion over Challenging Terrain

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2010.11251)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：腿式机器人的传统控制器靠越来越复杂的状态机触发动作基元和反射，仍达不到动物在自然地形上的通用性和鲁棒性。
- **核心方法**：两阶段特权学习：先用 RL 训练能看到地形真值、足端接触等特权信息（一句话：仿真中可得、实机上测不到的量）的教师策略，再用 DAgger（一句话：由教师在学生实际到达的状态上给标签的模仿学习）蒸馏出只用本体感知历史的学生策略，学生用 TCN（时间卷积网络，一句话：用因果膨胀卷积处理长时间序列）读取历史，不再显式估计接触和打滑。训练地形由自适应课程生成：用粒子滤波维持「有挑战但能通过」的地形参数分布。策略只在仿真中训练，零样本带两代 ANYmal 走过泥、雪、碎石、茂密植被和水流。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「教师-学生 + 本体感知历史」路线的基线；[RMA](../rma/README.md) 换了蒸馏目标，[Miki 等 2022](../arxiv-2201.08117/README.md) 加入外部感知，都可看作在这一结构上替换部件 [判断]。在[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)中属于「场景」一类：地形难度随策略表现自适应调整，[Rudin 等 2021](../arxiv-2109.11978/README.md) 的游戏式课程由它简化而来。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2010.11251
- 作者：Joonho Lee、Jemin Hwangbo 等（共 5 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2010.11251)
- 发表：Science Robotics, Vol. 5, Issue 47, 2020（arXiv 期刊信息）
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
