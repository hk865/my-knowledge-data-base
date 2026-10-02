# 评估与监督可靠性：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

评估先定义想测的能力、任务分布和错误代价，再选择指标或评审者。自动裁判能扩展比较规模，但需要检查位置偏差、长度偏差和与人类判断的一致程度。

## 第二步：沿具体文章拆机制

[Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../../papers/llm-judge/README.md) → [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](../../../llm/papers/test-time-compute/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

交换两份回答的顺序重复评判，记录翻转率，再阅读LLM-as-a-Judge的偏差分析。

## 第四步：保留边界

裁判偏好、模型正确性和用户效用不是完全相同的目标；相关性也不足以证明没有系统性偏差。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
