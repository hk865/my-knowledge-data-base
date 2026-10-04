# Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2304.13705)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：精细的双臂操作（穿扎带、装电池）要求毫米级精度，模仿学习中小的动作误差会放大成状态偏差，即复合误差；DAgger 一类方法需要在线专家，向示范加噪声又可能直接导致任务失败（§I）。
- **核心方法**：搭建成本低于 2 万美元的双臂遥操作系统 ALOHA，提出 ACT（Action Chunking with Transformers）：
  - **动作分块**：每次观测后输出接下来 k 步（默认 100 步）的目标关节位置，把有效时域缩短 k 倍；
  - **时间集成**：每步都查询策略，把重叠块对同一时刻的预测按指数权重平均，消除换块时的抖动；
  - **CVAE**：把策略训练成条件变分自编码器，以表示人类示范的多样性（§IV）。
  
  每个任务 50 条示范（约 10 分钟）。真实任务上，四个基线（BC-ConvMLP、BeT、RT-1、VINN）的最终成功率都是 0，ACT 在装电池上 96%、开拉链袋上 88%（Table I）。消融：不分块（k=1）时成功率 1%，k=100 时 44%（4 个仿真设定平均）；在人类示范上去掉 CVAE，从 35.3% 降到 2%（§VI）。
  
  做不好的场景：穿扎带只有 20%，作者归因于黑色扎带与黑色桌面对比度低；拆糖纸 10 次全失败，策略在没有接缝的地方撕（附录 F）。
- **为什么在这个库里**：[模仿与强化学习方向](../../fields/imitation-reinforcement-learning/README.md)中"用动作分块缓解复合误差"一格的代表，不需要在线专家，与 [DAgger](../arxiv-1011.0686/README.md) 是处理同一问题的两条路；[Diffusion Policy](../diffusion-policy/README.md) 与 π0 系列继承了动作块。优先级：必读。
