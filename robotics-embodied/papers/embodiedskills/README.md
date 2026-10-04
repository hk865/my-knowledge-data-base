# EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents

> 状态：逐步教学版 · 2026 · [原文](https://arxiv.org/abs/2609.01281)

[返回机器人与具身目录](../../README.md)

- **解决什么**：VLA 只负责预测动作，长时程任务还需要协调感知、规划、执行、进度检查和失败恢复；模型给出的技能决策本身，既不保证在当前状态下有效，也不保证结果会被核对。
- **核心方法**：把每个技能决策当作"执行提案"：运行时执行前检查前置条件，执行后验证结果。高层技能选择、受限的低层 VLA 执行和事后验证共用一个固定的可执行技能接口，因此低层 VLA 可以替换；规划、执行、验证、恢复事件都记成结构化轨迹，用作各部件的训练监督。相对 [SayCan](../saycan/README.md) 只在选技能时用价值函数估计可行性，本篇在执行前后两端都做核对。以 Qwen3-VL 加 OpenPI/π0.5 实例化：RoboTwin 2.0（一句话：双臂操作仿真基准）的 50 个任务平均 86.20%、LIBERO（一句话：桌面操作仿真基准）四套 97.40%，依赖记忆的 RMBench 四个任务只有 12.5%。
- **为什么在这个库里**：[具身 Agents](../../fields/embodied-agents/README.md)方向"执行循环（选择—检查—执行—验证—恢复）"一格的代表。优先级：选读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:2609.01281（Wang 等 17 位作者；v1，2026-09）
- 全文：[arXiv PDF v1](https://arxiv.org/pdf/2609.01281v1)
- 方向：[具身 Agents](../../fields/embodied-agents/README.md)（跨领域另见[智能体](../../../cross-domain/fields/agents/README.md)）
