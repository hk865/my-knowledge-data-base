# FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing

> 状态：文献卡 · 2023 · [原文](https://proceedings.mlr.press/v229/stachowicz23a.html)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：让小型 RC 车只凭视觉、在真实世界里用强化学习学会激进驾驶，不依赖仿真、专家示范或人工重置。
- **核心方法**：先用离线 RL（IQL，一句话：只从固定数据集学价值函数和策略、不在线交互的强化学习算法）在其他机器人的大规模导航数据集 RECON 上预训练视觉表征；再从一圈慢速示范起步，用 RLPD（一句话：混合在线数据与少量离线数据、用 critic 集成抑制高估的样本高效离策略 RL）在线学习。有限状态机按检查点轮换目标；碰撞（侧向加速度大）或 3 秒不动时切到脚本恢复策略做"伪重置"，同时给固定的卡住惩罚。不到 20 分钟在线训练即学会多条赛道；去掉伪重置的消融会让车卡住，表现同样差。
- **为什么在这个库里**：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)方向"真实世界免重置训练"的例子；在[四足故障后恢复笔记](../../../perspectives/notes/quadruped-recovery.md)里，它是"卡住后怎样回到可学习状态"的轮式对照。优先级：选读。

## 身份信息

- 稳定标识：url:https://proceedings.mlr.press/v229/stachowicz23a.html（Stachowicz、Shah、Bhorkar、Kostrikov、Levine；第 7 届 CoRL，PMLR 229:3100–3111，2023）
- 全文：[PMLR PDF](https://proceedings.mlr.press/v229/stachowicz23a/stachowicz23a.pdf)
- 方向：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)（另见[运动控制与腿足运动](../../fields/control-locomotion/README.md)、[导航与规划](../../fields/navigation-planning/README.md)）
