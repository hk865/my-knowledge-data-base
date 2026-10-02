# 架构与效率：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

架构决定信息怎样流动以及计算、显存随序列长度怎样增长。注意力、状态空间和稀疏专家分别改变不同部分，比较时应固定任务、训练预算和推理条件。

## 第二步：沿具体文章拆机制

[Attention Is All You Need](../../papers/transformer/README.md) → [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](../../papers/mamba/README.md) → [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../papers/deepseek-v2/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

先画出一次注意力的信息路由，再分别列出Mamba、DeepSeek-V2试图改变的计算或缓存瓶颈。

## 第四步：保留边界

MoE的总参数、激活参数、KV缓存和训练吞吐不是同一指标；架构名不能替代测量。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
