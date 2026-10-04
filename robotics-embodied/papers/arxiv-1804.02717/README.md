# DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

> 状态：文献卡 · 2018 · [原文](https://arxiv.org/abs/1804.02717)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：物理仿真角色的动作既要像动作捕捉片段一样自然，又要能抗扰动、适应形态变化并完成指定目标；手写控制器难以兼顾两者。
- **核心方法**：把「跟踪参考动作片段」写成模仿奖励，与任务奖励相加，用 PPO（近端策略优化，[库内页面](../../../llm/papers/ppo/README.md)）训练策略。消融表明两项训练设置对空翻、旋踢这类高动态动作至关重要：参考状态初始化（RSI，一句话：每个回合从参考动作中随机抽一帧作为起始状态，而不总从第一帧开始）和提前终止（ET，一句话：躯干或头部等部位触地即结束回合，之后奖励记为零）。在人形、Atlas 机器人、双足恐龙、龙等多种角色上展示行走、杂技和武术动作。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向「动作模仿」一支的起点：「参考动作 + 跟踪奖励 + RL」这一配方被后来的人形全身跟踪工作（如 [ExBody2](../arxiv-2412.13196/README.md)、[BeyondMimic](../arxiv-2508.08241/README.md)）延续。它的提前终止正是[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)第 8.1 条要核对的那类设定：倒地即终止时，训练数据里没有倒地之后的状态。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1804.02717
- 作者：Xue Bin Peng、Pieter Abbeel、Sergey Levine、Michiel van de Panne
- 全文：[arXiv PDF](https://arxiv.org/pdf/1804.02717)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
