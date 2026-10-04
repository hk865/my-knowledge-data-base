# Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2011.01387)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用奖励描述不同的双足步态很难：参考动作难获得，又把可学的动作限得太窄；无参考的奖励（如「向前走」）欠约束，换个随机种子学出的行为差别很大，或要大量试错式奖励塑形。
- **核心方法**：把奖励写成作用在足端力和足端速度上的简单概率性周期代价之和：摆动相惩罚足端力、允许速度，支撑相反之；用这一参数化奖励覆盖站立、走、单脚跳、跑、跳步（skipping）等常见双足步态，在 Cassie 双足机器人上 sim-to-real，并训练出能在所有两拍步态之间切换的单一策略。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「奖励设计」部件：不用参考动作也能指定步态，与 [DeepMimic](../arxiv-1804.02717/README.md) 式参考跟踪、[CPG-RL](../arxiv-2211.00458/README.md) 式结构先验构成指定步态的三种办法。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2011.01387
- 作者：Jonah Siekmann、Yesh Godse、Alan Fern、Jonathan Hurst
- 全文：[arXiv PDF](https://arxiv.org/pdf/2011.01387)
- 发表：ICRA 2021（arXiv 注释）
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
