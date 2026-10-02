# 偏好学习与奖励模型 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

偏好数据通常比较同一问题的多个回答。研究重点是把比较转成可优化目标，并检查偏好来自谁、比较条件是否一致、奖励是否偏向长度或表达方式。

## 一个容易混淆的边界

偏好分数不等于客观真值；奖励模型的好坏和最终策略表现也应分别评估。

## 入门任务

在同一问题的两份回答上计算相对概率变化，比较奖励模型加PPO与DPO分别更新哪些对象。

## 具体讲解入口

[打开已有独立讲解](../../../../docs/foundations/modules/objectives/02-classification-probabilities.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [Training language models to follow instructions with human feedback](../../../papers/instructgpt/README.md)
2. [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](../../../papers/dpo/README.md)
3. [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../../../../cross-domain/papers/llm-judge/README.md)
