# 语言模型强化学习 阅读导航

[返回领域总目录](../../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

强化学习把生成过程与奖励连接起来。先区分策略、参考策略、价值估计和奖励来源，再问采样数据怎样影响更新，以及奖励怎样分配给一串token。

## 一个容易混淆的边界

生成更长的回答不自动等于更好的推理。PPO的截断比值也不是对任何规模更新都有效的硬性保证。

## 入门任务

用一次短轨迹说明观察、动作、回报和优势，随后核对PPO中的概率比值与InstructGPT的训练角色。

## 具体讲解入口

[打开已有独立讲解](../../../../foundations/lessons/05b-reinforcement-learning.md)。

## 从已有讲解开始

1. [Proximal Policy Optimization Algorithms](../../../papers/ppo/README.md)
2. [Training language models to follow instructions with human feedback](../../../papers/instructgpt/README.md)
