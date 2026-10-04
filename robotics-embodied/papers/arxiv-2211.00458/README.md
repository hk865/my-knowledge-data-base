# CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2211.00458)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：从本体感知直接映射到关节指令难学，容易陷入不良局部最优；给策略加入时间（相位）结构能改善学习，CPG（中枢模式发生器，一句话：用耦合振荡器产生周期节律的结构）是一种生物启发的做法。
- **核心方法**：策略不直接输出关节目标，而是调节一组耦合振荡器的幅值与频率设定值，并协调各振荡器之间的节律；振荡器状态经足端轨迹映射和逆运动学转换为关节目标。在 Unitree A1 上 sim-to-real，能承受训练中未见过的 13.75 kg 动态附加负载（约为机身质量的 115%）；观测中除振荡器状态外只给足端接触布尔量、且不做域随机化，策略也能部署。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「动作接口」部件的结构先验，可对照讲义中「关节目标位置」接口；与 [MLP-CPG](../arxiv-2305.07300/README.md)、[相位引导控制器](../arxiv-2201.00206/README.md) 是同一路线的三种接法。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2211.00458
- 作者：Guillaume Bellegarda、Auke Ijspeert
- 全文：[arXiv PDF](https://arxiv.org/pdf/2211.00458)
- 发表：IEEE RA-L 2022（arXiv 注释）
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
