# 偏好学习与奖励模型：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

偏好数据通常比较同一问题的多个回答。研究重点是把比较转成可优化目标，并检查偏好来自谁、比较条件是否一致、奖励是否偏向长度或表达方式。

## 第二步：沿具体文章拆机制

[Training language models to follow instructions with human feedback](../../../papers/instructgpt/README.md) → [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](../../../papers/dpo/README.md) → [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../../../../cross-domain/papers/llm-judge/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

在同一问题的两份回答上计算相对概率变化，比较奖励模型加PPO与DPO分别更新哪些对象。

## 第四步：保留边界

偏好分数不等于客观真值；奖励模型的好坏和最终策略表现也应分别评估。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
