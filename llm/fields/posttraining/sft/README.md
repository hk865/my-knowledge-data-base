# 监督微调 SFT 阅读导航

[返回领域总目录](../../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

监督微调用示范告诉模型在什么上下文里产生什么回应。理解它时要同时看数据的角色标记、损失掩码、示范质量和部署任务，而不能只把它当成继续训练若干轮。

## 一个容易混淆的边界

SFT拟合示范；偏好学习利用回答之间的比较。两者可以顺序组合，但监督对象不同。

## 入门任务

给一个多轮对话标出仅对回答计算损失的token，再对照InstructGPT的SFT阶段。

## 具体讲解入口

[打开已有独立讲解](../../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)。

## 从已有讲解开始

1. [Language Models are Few-Shot Learners](../../../papers/gpt3/README.md)
2. [Training language models to follow instructions with human feedback](../../../papers/instructgpt/README.md)
