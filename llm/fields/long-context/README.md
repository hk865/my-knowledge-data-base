# 长上下文与记忆 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

长上下文同时涉及位置表示、训练课程、推理内存和信息利用。能接收很长的输入，只说明接口容量；真正的问题是远处信息能否在目标任务中被正确使用。

## 一个容易混淆的边界

上下文窗口、长距离检索、长文理解和持久记忆是不同能力，不能只用单一检索题替代全部评估。

## 入门任务

从Transformer出发，逐项检查Qwen2.5-1M如何处理训练长度、推理成本与长文任务。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/14-attention-transformer.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [Attention Is All You Need](../../papers/transformer/README.md)
2. [Qwen2.5-1M Technical Report](../../papers/qwen2.5-1m/README.md)
