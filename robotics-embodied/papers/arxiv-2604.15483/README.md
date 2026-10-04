# $π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2604.15483)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：通用机器人策略开箱即用的能力有限；训练时又只适合用"做得好的示范"，次优的自主数据、失败数据和非机器人数据难以利用。
- **核心方法**：沿用 [π*0.6](../arxiv-2511.14759/README.md) 的 VLA 结构和 MEM 记忆系统，把提示从一句任务描述扩展成多模态上下文：细化的子任务指令、由轻量世界模型生成的子目标图像，以及标注质量、速度和失误的回合元数据。这样既能按"怎么做"精确引导模型，也能把示范、自主（含失败）和非机器人数据放在一起训练；动作仍由约 8.6 亿参数的流匹配动作专家生成。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向"任务条件（提示）"部件上的改动，是 Physical Intelligence 的 π 系列最新一版：从 [π0](../arxiv-2410.24164/README.md)、[π0.5](../arxiv-2504.16054/README.md) 到这里，变化集中在给同一类动作专家喂什么条件。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2604.15483（Physical Intelligence，88 位署名；当前 v2，2026-04）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2604.15483)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)）
