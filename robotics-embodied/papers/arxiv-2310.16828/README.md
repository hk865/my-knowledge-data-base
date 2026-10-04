# TD-MPC2: Scalable, Robust World Models for Continuous Control

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.16828)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：通用具身智能体要从大量未整理数据中学多种连续控制任务，现有算法对任务变化不够鲁棒。
- **核心方法**：在 TD-MPC 基础上：不学解码器，只学对规划有用的潜变量（SimNorm 归一化），用 MPPI 加策略先验在潜空间规划，加可学习的任务嵌入与动作遮罩做多任务。317M 参数的单一模型训练 80 个任务，一套超参在 104 个任务上超过 SAC 与 DreamerV3；离散动作仍是开放问题。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)方法谱系"无解码器的潜变量"一行，部署时规划的代表。优先级：选读。
