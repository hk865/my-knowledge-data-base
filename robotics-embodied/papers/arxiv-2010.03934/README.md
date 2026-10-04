# Prioritized Level Replay

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2010.03934)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：程序生成环境中训练关卡一般均匀采样，与策略当前能从中学到什么无关，样本效率和泛化都受限。
- **核心方法**：给每个见过的关卡打分，按「再次访问时预计还能学到多少」优先采样下一关；用 TD 误差（一句话：当前价值预测与「一步奖励加下一状态价值」之差）的大小估计这份学习潜力，由此自然形成由易到难的课程。在 Procgen（程序生成关卡的强化学习泛化基准）上显著提高样本效率和泛化，与当时的最佳方法结合后，测试回报相对标准 RL 基线提高超过 76%。
- **为什么在这个库里**：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)方向「训练分布随策略调整」的代表。在[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)中是「场景」一类的算法依据：把容易卡住的障碍与初始状态当作关卡优先采样（迁移到四足是推断，论文只在 Procgen 上验证）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2010.03934
- 作者：Minqi Jiang、Edward Grefenstette、Tim Rocktäschel
- 全文：[arXiv PDF](https://arxiv.org/pdf/2010.03934)
- 方向：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)、[运动控制与腿足运动](../../fields/control-locomotion/README.md)
