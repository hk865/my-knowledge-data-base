# AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2104.02180)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让物理仿真角色既完成任务（走到目标、打中目标、越过障碍），动作又像动作捕捉数据那样自然。逐帧跟踪参考动作的方法要手工设计姿态误差度量，用相位变量把策略与片段对齐；数据集一大，还要一个运动规划器决定此刻跟踪哪一段。
- **核心方法**：相对 [DeepMimic](../arxiv-1804.02717/README.md) 的逐片段跟踪，改成分布匹配。训练一个判别器区分「数据集里的状态转移 (s, s′)」和「策略产生的状态转移」，只看状态、不需要示范者的动作；它的输出换算成 [0, 1] 的风格奖励，与任务奖励线性相加（论文所有任务各取 0.5），用 PPO（近端策略优化，[库内页面](../../../llm/papers/ppo/README.md)）训练。为了稳定对抗训练，判别器用最小二乘 GAN 的损失（一句话：把数据样本回归到 +1、策略样本回归到 −1，代替会因 sigmoid 饱和而梯度消失的交叉熵；原文引 Mao 等 2017，说它最小化 Pearson χ² 散度），并惩罚判别器在数据样本上的梯度。消融中梯度惩罚是最关键的部件：去掉后训练过程大幅震荡，最终动作有明显瑕疵（§5.4、§8.5）。数据可以是无标注、未切分的片段，走、跑、翻滚、出拳之间怎样衔接由先验自动组合出来。
- **为什么在这个库里**：[运动控制与腿足运动的基线](../../fields/control-locomotion/BASELINES.md)中「训练信号 = 参考动作」一支的中间节点：[DeepMimic](../arxiv-1804.02717/README.md) 逐片段跟踪 → 本篇分布匹配 → [ASE](../arxiv-2205.01906/README.md) 可复用的技能嵌入；[Escontrela 等 2022](../arxiv-2203.15103/README.md) 把它搬到四足实机上。它的局限也是读这条线要先记住的：作者自述对抗式 RL 不稳定，大数据集上会模式坍缩、只模仿一小部分行为；前空翻上收敛到「往前挪步不摔倒」的局部最优；只给走路数据时，策略在高目标速度下也只会走、跟不上速度（图 4）。加入起身片段后，角色摔倒能起身并继续任务，还会自己团身翻滚过渡（§8.2），这与[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)的问题直接相关。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2104.02180
- 作者：Xue Bin Peng、Ze Ma、Pieter Abbeel、Sergey Levine、Angjoo Kanazawa
- 发表：ACM Transactions on Graphics 40(4)，2021（DOI 10.1145/3450626.3459670）；arXiv v2 为作者版本，未与正式版逐字比对
- 全文：[arXiv PDF](https://arxiv.org/pdf/2104.02180)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
