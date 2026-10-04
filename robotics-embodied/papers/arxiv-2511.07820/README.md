# SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2511.07820)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：人形全身控制多靠逐任务手调的奖励，难以放大规模；[BeyondMimic](../arxiv-2508.08241/README.md) 一类动作跟踪器只覆盖少量动作，单个多技能策略又探索不足、动作不自然。
- **核心方法**：把"跟踪动作捕捉参考"当作一个可以无限放大的统一任务，用密集的跟踪监督代替手写奖励：700 小时、170 名受试者、超过 1 亿帧（50 Hz）的动作捕捉，经 [GMR](../arxiv-2510.02252/README.md) 重定向到 Unitree G1；网络从 1.2M 放大到 42M 参数。策略只看本体感知（关节位置与速度、根部角速度、重力方向，都表达在机器人朝向坐标系里），输出关节目标角交给 PD。三条轴里数据量带来的增益最大，模型与算力次之；真机上 50 条动作（舞蹈、跳跃、移动操作）全部成功，作者称零样本迁移、没有失败。上层接一个在潜空间里自回归生成动作的实时运动学规划器（笔记本上不到 5 ms、Jetson Orin 上 12 ms），并用统一的 token 接口让 VR 遥操作、人体视频和 VLA 都驱动同一个策略：用 300 条遥操作轨迹微调的 GR00T N1.5 做"把苹果放到盘子上"，20 次中 95%。
- **为什么在这个库里**：[运动控制方向](../../fields/control-locomotion/README.md)"动作模仿"一格在人形上的规模化（[DeepMimic](../arxiv-1804.02717/README.md) → BeyondMimic → 本篇），也是"[为什么绕不开模仿学习](../../fields/control-locomotion/README.md#为什么绕不开模仿学习)"的最新正面证据；它给出 VLA 与全身控制器之间的一种接口（VLA → 运动学规划器 → 跟踪策略）。作者自述安全、柔顺、能效、部署时的输入噪声都还没有正式处理，各模块分开训练留下了模态差距。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2511.07820（NVIDIA，Luo、Yuan 等 28 位作者；v1 2025-11-11，当前 v4 2026-08-13；发表于 [Science Robotics 11(117), eaed4592 (2026)](https://doi.org/10.1126/scirobotics.aed4592)，期刊信息以 arXiv v4 摘要页为据）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2511.07820)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)、[VLA](../../fields/vla/README.md)）
