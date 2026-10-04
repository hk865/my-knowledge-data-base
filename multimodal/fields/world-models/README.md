# 世界模型 阅读导航

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

世界模型用观察与动作预测未来状态、潜在表示或回报，从而支持学习或规划。核心是预测目标、状态表示、动作条件与使用方式，不是所有视频生成器都天然适合决策。

## 一个容易混淆的边界

训练内的预测误差、规划后的回报和现实中的安全性是三个不同证据层。想象训练也不能绕过模型误差。

## 入门任务

在DreamerV3中分清真实经验、后验状态、先验预测和想象轨迹，再与Zero-WAM的动作条件任务比较。

## 具体讲解入口

[打开已有独立讲解](../../../foundations/lessons/16-vae.md)。

## 从已有讲解开始

1. [Mastering Diverse Domains through World Models](../../papers/dreamerv3/README.md)
2. [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../../../robotics-embodied/papers/zero-wam/README.md)
