# Proximal Policy Optimization Algorithms

> 状态：技术精读 · 2017 · [原文](https://arxiv.org/abs/1707.06347)

[返回大语言模型目录](../../README.md)

- **解决什么**：普通策略梯度每批数据只能更新一次，样本利用率低；TRPO（信赖域策略优化：每步要求新旧策略的平均 KL 散度不超过阈值）稳定，但要做二阶近似的约束优化，实现复杂。
- **核心方法**：相对 TRPO 的 KL 约束，把"不离旧策略太远"写进目标函数：用新旧策略的概率比乘优势（这个动作比该状态下的平均水平好多少），再把概率比裁剪在 [1−ε, 1+ε]，取未裁剪与裁剪两项中较小的一项。这样同一批数据可以做多轮小批量更新，只需一阶优化器。在模拟机器人运动和 Atari 上，样本复杂度、实现难度和运行时间的综合表现优于其他在线策略梯度方法。
- **为什么在这个库里**：[强化学习方向](../../fields/posttraining/rl/README.md)的算法基线：[InstructGPT](../instructgpt/README.md) 用它做 RLHF；[DeepSeek-R1](../arxiv-2501.12948/README.md) 用的 GRPO 去掉了它的价值网络，改用同组回答的相对得分。机器人控制也大量使用。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

[强化学习讲义](../../../foundations/lessons/05b-reinforcement-learning.md)第 4–5 节（策略梯度与优势）→ 本篇。

## 身份信息

- 稳定标识：arxiv:1707.06347 · [全文 PDF](https://arxiv.org/pdf/1707.06347v2) · 精读依据 v2
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov（OpenAI）
- 方向：llm/posttraining/rl、robotics/control、robotics/embodied-policies
