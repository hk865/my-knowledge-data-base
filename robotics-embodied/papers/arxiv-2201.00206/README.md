# Learning Free Gait Transition for Quadruped Robots via Phase-Guided Controller

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2201.00206)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：一个策略学多种步态及其切换属于多任务学习：从零设计奖励很费力，用动作模仿又无法覆盖所有起始状态下的切换。
- **核心方法**：用四条腿各自独立的相位作为步态生成器与策略之间的接口：相位与速度命令合成多项式参考足端轨迹，供模仿奖励使用；策略输入速度命令、四个相位和机器人状态，输出关节目标位置。相位可由改进的 Hopf 振荡器 CPG（中枢模式发生器，一句话：用耦合振荡器产生周期节律的结构）生成，换连接矩阵即可在 walk、trot、pace、bound 之间切换，也可由手工函数生成混合节律的「舞蹈」。在中型犬大小的 Black Panther 四足上部署。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「步态表示」部件上 CPG 与 RL 结合的一种接法：CPG 只产生相位，策略负责平衡和速度跟踪；可与 [CPG-RL](../arxiv-2211.00458/README.md) 对照。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2201.00206
- 作者：Yecheng Shao、Yongbin Jin 等（共 6 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2201.00206)
- 发表：IEEE RA-L（arXiv 注释）
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
