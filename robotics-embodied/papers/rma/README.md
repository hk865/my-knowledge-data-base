# RMA: Rapid Motor Adaptation for Legged Robots

> 状态：技术精读 · 2021 · [原文](https://arxiv.org/abs/2107.04034)

[返回机器人与具身目录](../../README.md)

- **解决什么**：仿真训练的腿足策略搬到真机时，地面、负载、电机强度都与仿真不同且会变化：域随机化只能学出保守的折中策略，系统辨识难而且不必要，真机上继续训练慢且有损坏风险。
- **核心方法**：两个部件：先在仿真中训练能看到环境参数（压成 8 维隐变量）的基础策略；再训练适应模块，从最近 50 步本体状态和动作历史估计这个隐变量，部署时替代拿不到的真值。全程仿真训练，不用参考轨迹或预定义足端轨迹生成器（相对 [Lee 等 2020](../arxiv-2010.11251/README.md) 去掉了这类手工先验），在 A1 上零微调部署，几分之一秒内适应岩石、湿滑、可变形等地面。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向"盲走 + 隐式环境估计"的基线；在[四足故障后恢复笔记](../../../perspectives/notes/quadruped-recovery.md)里代表"加维度"中的时间感知，作者自述多条腿同时被挡这类大扰动下会失败。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

教学顺序：[PPO](../../../llm/papers/ppo/README.md)（训练算法）→ [ESKF 教程](../eskf/README.md)（本体状态从哪里来）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2107.04034（Kumar、Fu、Pathak、Malik；RSS 2021）
- 全文：[arXiv PDF v1](https://arxiv.org/pdf/2107.04034v1)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)）
