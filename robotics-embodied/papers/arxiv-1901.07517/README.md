# Robust Recovery Controller for a Quadrupedal Robot using Deep Reinforcement Learning

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1901.07517)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：腿式机器人摔倒后需要自己起身。此前多依赖预先设计的轨迹，动作不自然，在腿压在机身下这类边角情况里不鲁棒，还需要大量针对具体系统的工程。
- **核心方法**：用无模型深度 RL 训练分层控制器：自翻正、站起、行走三个行为策略分别在仿真中用 TRPO（信赖域策略优化）训练，再训练一个行为选择器，按近期观测、命令和上一个行为调度它们；另学一个机身高度估计网络，因为倒地时依赖足端接触的状态估计会漂移。自翻正的训练初始状态是让 ANYmal 从 0.5 m 高处以随机关节角落下，回合只按时间上限终止。在 ANYmal（狗大小的四足机器人，12 个自由度）上测试 100 多次，从任意倒地姿态 5 秒内恢复，成功率高于 97%。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「恢复控制」的代表作，[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)中「摔倒后起身」一类的直接方案。它的初始状态分布和「只按时限终止」正对应笔记第 8.1 条「失败状态是否进入训练数据」。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1901.07517
- 作者：Joonho Lee、Jemin Hwangbo、Marco Hutter
- 全文：[arXiv PDF](https://arxiv.org/pdf/1901.07517)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
