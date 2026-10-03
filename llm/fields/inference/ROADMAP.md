# 推理时计算：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

推理时计算是在已有模型之上使用额外预算，例如多次采样、验证、搜索或修订。重要问题是预算分配给谁、验证器是否可靠，以及延迟、token和正确率怎样一起衡量。

## 第二步：沿具体文章拆机制

[Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](../../papers/test-time-compute/README.md) → [ReAct: Synergizing Reasoning and Acting in Language Models](../../../cross-domain/papers/react/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

固定一个任务和总预算，分别定义单次生成、best-of-N和修订流程的成本与停止条件。

## 第四步：保留边界

更多采样与更大的模型不是可直接互换的预算；验证器误差可能让更大的搜索放大错误。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。

## 2026年10月3日：精确验证与近似协作

先读[草拟—验证机制导读](draft-verification-guide.md)及Leviathan/Chen，再对照BiLD、RelayLLM和Judge Decoding的保证变化。EAGLE-3、DFlash与DFlash2改变草拟器；Faster Cascades精确保持的是定义的混合分布，不能默认为大模型分布。用同一任务、采样设置、硬件及延迟口径比较，关注拒绝重算、调用预算与质量。
