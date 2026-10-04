# PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2408.13740)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：跑酷要求同时理解自身状态和前方地形，而深度相机有延迟和噪声；此前的跑酷方法多用教师-学生两阶段训练（蒸馏时有信息损失），或依赖复杂的地形重建模块。
- **核心方法**：单阶段端到端训练：用非对称 actor-critic（一句话：critic 训练时可以用特权信息，actor 只用部署时可得的观测）代替两阶段蒸馏；估计器把近期深度图和本体感知历史经 CNN/MLP、共享 Transformer 和 GRU 融合，同时输出显式量（机身速度、足端离地高度、高程图编码）和隐式量（按 DreamWaQ 的做法，用 VAE 隐变量预测下一时刻的本体感知），与 PPO 同步训练。在低成本的 DEEP Robotics Lite3 四足上零样本部署到跑酷地形。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向感知跑酷一支，相对 [Robot Parkour Learning](../arxiv-2309.05665/README.md)、[Extreme Parkour](../arxiv-2309.14341/README.md) 的两阶段蒸馏，改的是「训练流程」和「状态估计」两个部件。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2408.13740
- 作者：Shixin Luo、Songbo Li 等（共 6 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2408.13740)
- 发表：IEEE RA-L（arXiv 注释）
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
