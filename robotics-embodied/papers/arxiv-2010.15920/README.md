# Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2010.15920)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在真实世界里学新任务需要大量探索，而安全要求限制探索，两者冲突。
- **核心方法**：相对把任务与安全放进同一目标联合优化的做法（约束优化或奖励塑形），拆成两步：先用离线数据学出容易违反约束的区域，再训练两个策略：任务策略只优化任务奖励，恢复策略在即将违反约束时接管，把智能体带回安全区域。在 6 个仿真环境（含两个接触丰富的操作任务和一个基于图像的导航任务）和一个实机图像避障任务上，与 5 种安全 RL 方法比较，约束违反与任务成功之间的权衡效率在仿真中高 2–20 倍，实机上高 3 倍。
- **为什么在这个库里**：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)方向安全强化学习的代表。在[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)中属于「算法与损失」一类，是「站着卡住」在库内最接近的结构参考；借用前要先把「卡住」定义成可预测的约束状态。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2010.15920
- 作者：Brijen Thananjeyan、Ashwin Balakrishna 等（共 10 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2010.15920)
- 发表：IEEE RA-L 与 ICRA 2021（arXiv 注释）；[IEEE 页面](https://ieeexplore.ieee.org/document/9392290/)。arXiv 首版为 2020 年 10 月
- 方向：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)、[运动控制与腿足运动](../../fields/control-locomotion/README.md)
