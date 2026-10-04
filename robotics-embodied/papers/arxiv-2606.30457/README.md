# Behavior Prompting Policy: Demonstrations as Prompts for Manipulation

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.30457)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：让机器人在推理时只凭一段人类示范（称为行为提示）就做新任务，不为新任务付出微调成本。
- **核心方法**：以最接近的前作 [ICRT](../arxiv-2408.15980/README.md)（自回归的上下文视觉运动策略）为参照，提出上下文视觉运动结构 BPP，把行为提示和当前观测翻译成机器人动作；作者发现任务多样性是提示能力的主要来源，为此做了手持采集接口 iPhUMI 收集多样数据，并提出 DrawAnything、LIBERO-Gen 两个测试时泛化基准。在 DrawAnything 未见图形上误差比 ICRT 降低 33.3%。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)与[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)交界处"任务怎样指定"的一条路线：用示范而不是语言指定任务，与 [Zero-WAM](../zero-wam/README.md)（用人类视频做上下文）同属上下文模仿。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2606.30457（Patel、Pekarek、Castro Hernandez、Song；v1，2026-06）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2606.30457) · 项目页：[behavior-prompting.github.io](https://behavior-prompting.github.io/)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)）
