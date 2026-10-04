# Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2301.04213)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：ROME、MEMIT 依据因果追踪把事实定位到中层 MLP，并据此选择编辑哪一层；定位结果是否真能告诉我们该改哪里，此前没有检验。
- **核心方法**：在 GPT-J 与 CounterFact 上逐条比较因果追踪效应与在各层编辑的成功率：相当一部分事实的追踪峰值落在 ROME/MEMIT 编辑的层范围之外，追踪效应与编辑成功率的相关接近 0（ROME、MEMIT 与 Adam 微调都是如此）；编辑哪一层本身比定位结果更能预测编辑效果。
- **为什么在这个库里**：[模型科学方向](../../fields/model-science/README.md)主线节点 ROME 的“做不好的场景”：理解模型怎样存储，不一定直接告诉我们怎样改它。也是[训练科学](../../fields/training-science/README.md#与模型科学的关系)中“哪些参数重要”两种定义的对照。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2301.04213 · [全文 PDF](https://arxiv.org/pdf/2301.04213)
- 方向：cross-domain/model-science
