# 评估与监督可靠性 阅读导航

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

评估先定义想测的能力、任务分布和错误代价，再选择指标或评审者。自动裁判能扩展比较规模，但需要检查位置偏差、长度偏差和与人类判断的一致程度。

## 一个容易混淆的边界

裁判偏好、模型正确性和用户效用不是完全相同的目标；相关性也不足以证明没有系统性偏差。

## 入门任务

交换两份回答的顺序重复评判，记录翻转率，再阅读LLM-as-a-Judge的偏差分析。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/modules/data/01-data-contracts.md)。

## 从已有讲解开始

1. [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../../papers/llm-judge/README.md)
2. [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](../../../llm/papers/test-time-compute/README.md)
