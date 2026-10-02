# 架构与效率 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

架构决定信息怎样流动以及计算、显存随序列长度怎样增长。注意力、状态空间和稀疏专家分别改变不同部分，比较时应固定任务、训练预算和推理条件。

## 一个容易混淆的边界

MoE的总参数、激活参数、KV缓存和训练吞吐不是同一指标；架构名不能替代测量。

## 入门任务

先画出一次注意力的信息路由，再分别列出Mamba、DeepSeek-V2试图改变的计算或缓存瓶颈。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/15-qkv-deep-dive.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [Attention Is All You Need](../../papers/transformer/README.md)
2. [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](../../papers/mamba/README.md)
3. [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../papers/deepseek-v2/README.md)
