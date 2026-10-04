# Learning Agile Robotic Locomotion Skills by Imitating Animals

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2004.00784)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让四足机器人学会动物那样多样、敏捷的步态与动作。作者在引言里写了两条不走纯 RL 的理由：RL 训出的智能体容易学出不自然、在真机上危险或不可行的行为；为每个技能设计能引出目标行为的奖励，本身就要繁琐的逐技能调参。手工控制器则开发周期长、要大量专门知识。
- **核心方法**：沿用 [DeepMimic](../arxiv-1804.02717/README.md) 的「跟踪参考动作 + RL」配方，把参考换成真狗的动作捕捉：先用逆运动学把狗的动作重定向到 18 自由度的 Laikago 上，在仿真中用 PPO 训练模仿策略，训练时做域随机化，并让策略以一个经信息瓶颈约束的动力学隐变量为条件；上真机后不更新网络权重，只在隐变量空间里用 AWR（优势加权回归，一句话：按优势的指数给样本加权做回归）搜索，每个策略约 50 次真机试验完成适应（§VI-C、§VII-A）。真机狗式小跑达到 1.08 m/s，厂商自带的最快步态约 0.84 m/s（§VII-B）。作者自述没能学会大跳和奔跑这类更动态的动作，学到的行为也不如最好的手工控制器稳定（§VIII）。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)「为什么绕不开模仿学习」一节中，四足上「先模仿、再在真机上用 RL 适应」的例子；对照 [Escontrela 等 2022](../arxiv-2203.15103/README.md)：同一作者群后来把逐帧跟踪换成 [AMP](../arxiv-2104.02180/README.md) 的风格奖励。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2004.00784
- 作者：Xue Bin Peng、Erwin Coumans、Tingnan Zhang、Tsang-Wei Lee、Jie Tan、Sergey Levine（Google Research 与 UC Berkeley）
- 发表：arXiv 页面与 PDF 未写会议；正式发表信息未核实
- 全文：[arXiv PDF](https://arxiv.org/pdf/2004.00784)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
