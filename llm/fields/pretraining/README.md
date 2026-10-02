# 预训练 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

预训练把大量序列转成可迁移的预测能力。先分清输入怎样分词、哪些位置计算损失、数据怎样混合，再讨论参数规模与训练计算量；只知道模型有多少参数，还不足以比较两个训练方案。

## 一个容易混淆的边界

few-shot上下文示例、参数更新和持续预训练是不同操作。规模报告中的数据量、token数和计算预算也不是一个量。

## 入门任务

用一段短文本标出输入token、预测目标和参与损失的位置，再读GPT-3的数据与few-shot评估设置。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [Language Models are Few-Shot Learners](../../papers/gpt3/README.md)
2. [Qwen2.5-1M Technical Report](../../papers/qwen2.5-1m/README.md)
