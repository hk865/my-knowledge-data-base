# ExBody2: Advanced Expressive Humanoid Whole-Body Control

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.13196)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：人形机器人要在保持平衡的前提下跟踪表现力强的全身动作；人类动作数据里有大量超出机器人物理能力的动作，不加筛选地训练会拖累跟踪效果。
- **核心方法**：相对只跟踪上半身、下半身只跟根速度的 ExBody，改为全身关键点与关节跟踪，并把整体速度跟踪与身体关键点跟踪解耦。数据侧先用全量数据训练一个策略，按下半身跟踪误差自动筛掉不可行动作、保留上半身多样性，再训练通才策略，并针对特定动作组微调出专才策略；教师用特权信息，学生用更长的本体感知历史蒸馏。在 Unitree G1 上实机行走、下蹲、跳舞；作者也报告，在少量数据上微调能显著提高该类动作的跟踪，代价是其他动作变差。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向人形「全身动作跟踪」一支，核心观点是数据的可行性与多样性取舍；[BeyondMimic](../arxiv-2508.08241/README.md)、[GMR 重定向](../arxiv-2510.02252/README.md)在同一问题上继续推进。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2412.13196
- 作者：Mazeyu Ji、Xuanbin Peng 等（共 7 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2412.13196)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
