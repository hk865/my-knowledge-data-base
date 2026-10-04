# Learning Quadruped Locomotion using Bio-Inspired Neural Networks with Intrinsic Rhythmicity

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2305.07300)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CPG 本质上是循环网络，与 MLP 一起用梯度训练需要沿时间反传，代价高；以往要么把 CPG 当作环境的一部分，要么用进化算法等非梯度方法单独优化 CPG 参数。
- **核心方法**：沿用 Campanaro 等 2021 只在单条跳跃腿上验证过的思路：把 CPG 的内部状态暴露为网络的输入和输出，使其变成可完全微分的无状态前馈网络，再与负责感觉反馈的 MLP 一起用深度 RL 联合训练，扩展到 12 自由度的仿真四足，不需要外部相位输入。仿真中策略能盲走不平地形、抵抗推力，并随速度自行调节步频和步长。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向 CPG 路线的另一种接法，与 [CPG-RL](../arxiv-2211.00458/README.md) 对照：那里策略调振荡器设定值，这里 CPG 参数本身参与训练。结果只有仿真。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2305.07300
- 作者：Chuanyu Yang、Can Pu 等（共 5 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2305.07300)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
