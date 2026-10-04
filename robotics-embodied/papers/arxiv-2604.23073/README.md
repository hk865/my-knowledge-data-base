# RL Token: Bootstrapping Online RL with Vision-Language-Action Models

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2604.23073)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：通用 VLA 开箱能做很多任务，但拧螺丝、插网线这类精密阶段的成功率和速度不够；对整个 VLA 做 RL 太贵，小网络从像素开始做真机 RL（[HIL-SERL](../arxiv-2410.21845/README.md) 式）又丢掉了 VLA 已有的知识。
- **核心方法**：在冻结的 π0.6 上加一个小的 Transformer 编码器-解码器，把 VLA 的内部表示压成一个"RL token"；只在这个 token 上训练一个小的 actor-critic（类似 TD3 的离策略算法，回放池混合 VLA 预热数据、在线回合与可选的人工干预，更新/数据比为 5）。actor 的输入是 RL token 和 VLA 提出的参考动作块，输出修正后的动作块，并被正则到 VLA 动作附近，所以在线 RL 变成"在一个好先验附近做局部修正"。四个任务（装螺丝、扎扎带、插充电器、插网线）各用约 15 分钟到 5 小时真机数据，关键阶段的速度最高提升约 3 倍，装螺丝成功率从 20% 到 65%，插网线比专家遥操作还快。对照中，单步残差方法（PLD）因信用分配的时域太长学不动，扩散噪声引导（DSRL）成功率相近但提速少得多，DAgger 式微调的速度受限于人类示范。
- **为什么在这个库里**：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)方向"RL 回到模仿之上"的最新一步：[π*0.6](../arxiv-2511.14759/README.md) 的 RECAP 是离线、分轮、对整个 VLA 做优势条件化，本篇是在线、只训一个小头、贴着 VLA 先验修正。作者写明训练时仍要人给奖励信号、做干预，并在 RL 与基座策略之间切换。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2604.23073（Xu、Springenberg、Equi、Amin、Esmail、Levine、Ke；Physical Intelligence；v2，2026-04-30）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2604.23073)
- 方向：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)（另见[视觉-语言-动作模型](../../fields/vla/README.md)）
