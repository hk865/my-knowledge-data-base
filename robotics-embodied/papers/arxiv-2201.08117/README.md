# Learning robust perceptive locomotion for quadrupedal robots in the wild

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2201.08117)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：纯本体感知要先「踩到」地形才能调整步态，速度受限；外部感知又会被雪、植被、水、反光、遮挡等误导，直接依赖它不鲁棒。
- **核心方法**：沿用 [Lee 等 2020](../arxiv-2010.11251/README.md) 的教师-学生特权学习，把学生换成基于注意力的循环信念编码器：输入本体感知和从高程图（以机器人为中心的 2.5D 地形高度图）采样的高度点，输出一个整合的信念状态，并训练它还原地形真值；训练中给高程图加入大噪声、偏差和缺失，使策略在外部感知可信时提前规划落脚，不可信时退回本体感知。控制器在多个季节的自然与城市环境中测试，在阿尔卑斯山按人类推荐用时完成一小时徒步。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「观测」部件上加入外部感知的代表；在[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)中属于「加维度」一类。作者在讨论中写明，需要与正常行走差别很大的动作时仍做不到，例如腿卡进窄洞后脱出、爬上高台，这正是「站着卡住」一类问题的边界。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2201.08117
- 作者：Takahiro Miki、Joonho Lee 等（共 6 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2201.08117)
- 发表：Science Robotics, Vol. 7, Issue 62, 2022（arXiv 期刊信息）
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
