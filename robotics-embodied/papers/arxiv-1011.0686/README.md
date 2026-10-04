# A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

> 状态：文献卡 · 2011 · [原文](https://arxiv.org/abs/1011.0686)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：模仿学习里，学习者自己的动作会决定下一步看到什么，这违反了监督学习的独立同分布假设；只在专家走过的状态上训练（行为克隆），一旦偏离就不知道怎样回来（§1）。
- **核心方法**：给出两条界并据此提出 DAgger（Dataset Aggregation）。
  - 行为克隆的界：在专家状态分布上错误率为 ε 时，T 步任务的总代价最多比专家多 T²ε（定理 2.1，代价有界于 [0,1]、损失为 0-1 损失或其上界），论文指出这个界是紧的。
  - 改为在策略自己的状态分布上控制误差后，界降为 uTε，u 是"犯一次错之后专家要多付出的代价"（定理 2.2；最坏情况 u 可达 O(T)）。
  - DAgger 每轮用当前策略（第一轮可与专家混合）采样，向专家查询这些状态上该做什么，把新标签并入总数据集重训，最后取验证最好的一轮（算法 3.1）。
  - 实验结果：Super Tux Kart 中，行为克隆加数据也不改善，因为"训练圈都很相似，学不会怎样恢复"；DAgger 迭代 15 次后不再掉出赛道。Super Mario 中，行为克隆常卡在障碍前，因为专家总在很远处起跳，学习者没见过贴着障碍的状态（§5）。
  - 前提：每一轮都需要一个能随时查询的专家。
- **为什么在这个库里**：[模仿与强化学习 Baseline 表](../../fields/imitation-reinforcement-learning/BASELINES.md)中"数据分布纠正"一格的源头；腿足的教师-学生蒸馏（[Lee 2020](../arxiv-2010.11251/README.md)、[Extreme Parkour](../arxiv-2309.14341/README.md)）、[HIL-SERL](../arxiv-2410.21845/README.md) 与 [π*0.6](../arxiv-2511.14759/README.md) 的人工纠正都是它的变体。优先级：必读。
