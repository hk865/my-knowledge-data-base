# Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2203.15103)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：腿足 RL 只给速度跟踪奖励时，策略会学出高频抖腿、高冲击接触这类钻仿真空子的动作，上不了真机；常见的补救是堆十几项手调的风格惩罚，调参费力，换平台、换任务又要重调。
- **核心方法**：把 [AMP](../arxiv-2104.02180/README.md)（Peng 等 2021，一句话：用判别器区分数据集与策略的状态转移，输出作为风格奖励）从图形学搬到四足实机 A1 上。风格奖励来自 4.5 秒德国牧羊犬动作捕捉，经逆运动学重定向到 A1；任务奖励只有线速度与偏航角速度跟踪两项；风格与任务权重为 0.65 与 0.35。对照组是 [Rudin 2021](../arxiv-2109.11978/README.md) 由 13 项风格项组成的奖励。仿真中，在 0.4–1.6 m/s 四档前进命令下，AMP 策略的机械运输代价（COT，一句话：单位重量、单位距离消耗的正机械功，越低越省能）为 0.93–1.12，手调奖励组为 1.37–1.54，低 21%–32%；不加任何风格项的策略靠抖腿前进，COT 为 5.2–14.0，作者判断无法上真机（表 II）。真机上速度命令从 1 m/s 跳到 2 m/s 时，策略从溜蹄（pace）切换到带腾空相的跑步（canter），数据里有的步态切换被先验带了出来。
- **为什么在这个库里**：[运动控制与腿足运动的基线](../../fields/control-locomotion/BASELINES.md)中「训练信号」一格：用数据驱动的风格先验替代手调惩罚项的四足代表。读它时要记住边界：实验只有平地上的速度跟踪，没有地形、感知或摔倒恢复；真机部分是定性展示；四档命令下 AMP 策略的实测速度都略低于命令（1.6 m/s 命令下为 1.52），手调奖励组为 1.67，说明风格权重压过任务时会牺牲一点跟踪；论文没有局限一节。与[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)的关系：动作数据里没有脱困动作时，风格奖励可能与恢复目标冲突。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2203.15103
- 作者：Alejandro Escontrela、Xue Bin Peng、Wenhao Yu、Tingnan Zhang、Atil Iscen、Ken Goldberg、Pieter Abbeel（UC Berkeley 与 Google Brain）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2203.15103)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
