# ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2205.01906)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：物理仿真角色的控制器通常每个任务从零训练，常见动作每次都要重学，样本效率低，也限制了能完成的任务复杂度。
- **核心方法**：在对抗运动先验（[AMP](../arxiv-2104.02180/README.md)，Peng 等 2021，一句话：用判别器让策略的状态转移分布接近动作数据集，而不逐帧跟踪某一片段）的基础上加入无监督技能发现：预训练一个以隐变量 z 为条件的低层技能策略，模仿目标让行为像数据集，互信息目标让不同的 z 产生可区分的行为；下游任务只训练一个输出 z 的高层策略，奖励可以很简单。借助 Isaac Gym 大规模并行仿真累计十年以上的模拟经验，训练数据是无标注、未切分的动作片段。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「动作先验」部件的演进：从 [DeepMimic](../arxiv-1804.02717/README.md) 的逐片段跟踪，到 [AMP](../arxiv-2104.02180/README.md) 的分布匹配，再到本篇的可复用技能嵌入；人形[行为基础模型](../arxiv-2506.20487/README.md)沿用了「先预训练技能空间、下游再调用」的思路 [判断]。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2205.01906
- 作者：Xue Bin Peng、Yunrong Guo 等（共 5 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2205.01906)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
