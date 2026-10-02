# 图文对齐 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

图文对齐让两种模态的表示在某种任务上可比较。以对比学习为例，一批配对图文同时提供正样本与负样本，训练后的相似度还能用于检索和候选标签排序。

## 一个容易混淆的边界

相似度排序不是自然语言生成，也不保证模型理解空间关系或精细计数。

## 入门任务

亲手构造一个小批次相似度矩阵，分别沿图到文与文到图计算匹配目标。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../../papers/vit/README.md)
2. [Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md)
