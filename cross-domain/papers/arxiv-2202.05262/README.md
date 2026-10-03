# Locating and Editing Factual Associations in GPT

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2202.05262)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自回归语言模型中的事实关联（例如"某地标—所在城市"）存放在哪里，能否直接改写。
- **核心方法**：先用因果追踪（破坏输入中的主语，再把某一层某个位置的激活恢复成干净值，看正确答案的概率恢复多少）在 GPT-2 XL 中定位到：中间层的 FFN 在处理主语 token 时有一组决定性的计算步骤；再据此提出 ROME（Rank-One Model Editing），对单个中层 FFN 的权重做一次秩一更新（只加上一个外积矩阵）来改写某条事实。相对已有编辑方法，ROME 在 zsRE 编辑任务上效果相当，在作者新建的反事实数据集 CounterFact 上同时保持特异性与泛化，其他方法只能顾及其一。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 5 节节点：上一节点 [FFN 键值记忆](../arxiv-2012.14913/README.md) 把 FFN 读作键值表，本篇把这种读法变成可干预的定位与编辑，是"FFN 偏向知识"的直接证据；下一节点 [Dissecting Recall](../arxiv-2304.14767/README.md) 补上事实被注意力读出的路径，并把存储的重点前移到更低层的 MLP。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2202.05262 · [全文 PDF](https://arxiv.org/pdf/2202.05262)
- 方向：cross-domain/interpretability
