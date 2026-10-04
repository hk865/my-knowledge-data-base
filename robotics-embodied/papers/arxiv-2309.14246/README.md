# Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.14246)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：危险环境中部署的腿式控制器没有显式建模动作的风险，想让机器人更谨慎只能反复调奖励。
- **核心方法**：把 PPO 中的期望价值换成完整的价值分布，经风险度量（Wang 度量或 CVaR）得到风险敏感的价值估计，再接回 PPO，称为 DPPO（Distributional PPO）；风险偏好由一个参数从规避连续调到偏好，可在运行时动态调整，不需要为风险敏感另调奖励。在仿真和 ANYmal 上出现风险敏感的行走行为；视频与代码公开。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「RL 目标」部件上的改动，与 [Shi 等 2023](../arxiv-2308.09405/README.md) 同类；区别在于用一个参数连续调节风险偏好。在[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)中属于「算法与损失」一类，可作为「避免卡住」一侧的备选。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2309.14246
- 作者：Lukas Schneider、Jonas Frey、Takahiro Miki、Marco Hutter
- 全文：[arXiv PDF](https://arxiv.org/pdf/2309.14246)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
