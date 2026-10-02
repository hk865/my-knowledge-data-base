# 世界模型：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

世界模型用观察与动作预测未来状态、潜在表示或回报，从而支持学习或规划。核心是预测目标、状态表示、动作条件与使用方式，不是所有视频生成器都天然适合决策。

## 第二步：沿具体文章拆机制

[Mastering Diverse Domains through World Models](../../papers/dreamerv3/README.md) → [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../../../robotics-embodied/papers/zero-wam/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

在DreamerV3中分清真实经验、后验状态、先验预测和想象轨迹，再与Zero-WAM的动作条件任务比较。

## 第四步：保留边界

训练内的预测误差、规划后的回报和现实中的安全性是三个不同证据层。想象训练也不能绕过模型误差。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
