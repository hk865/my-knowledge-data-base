# 推理时计算 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

推理时计算是在已有模型之上使用额外预算，例如多次采样、验证、搜索或修订。重要问题是预算分配给谁、验证器是否可靠，以及延迟、token和正确率怎样一起衡量。

## 一个容易混淆的边界

更多采样与更大的模型不是可直接互换的预算；验证器误差可能让更大的搜索放大错误。

## 入门任务

固定一个任务和总预算，分别定义单次生成、best-of-N和修订流程的成本与停止条件。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/05-advanced-bridges.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](../../papers/test-time-compute/README.md)
2. [ReAct: Synergizing Reasoning and Acting in Language Models](../../../cross-domain/papers/react/README.md)

## 大小模型协作：先分清验证保证

[两图机制导读与手算示例](draft-verification-guide.md)覆盖精确目标分布、近似协作及关键片段接管；这是方向导读，不增加单篇全文精读计数。

[本轮文献卡](PAPERS.md)逐条标记实际核验版本、方法段和限制。
