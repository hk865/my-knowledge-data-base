# Training Compute-Optimal Large Language Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2203.15556)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：给定一份训练算力，参数量与训练 token 数怎样分配才能让损失最低。Kaplan 等 2020 的配比主张算力增加时主要加参数（算力增加 10 倍，参数量加 5.5 倍、训练 token 只加 1.8 倍），此后的大模型大多只训练约 300B 个 token，作者认为它们训练不足。
- **核心方法**：相对 Kaplan 等 2020，把学习率余弦周期对齐到实际训练长度，并纳入更大的模型，在 400 多次训练（70M 到 16B 以上参数、5B 到 500B 个 token）上用三种方法重新拟合：固定模型大小、取不同训练长度的损失包络；固定算力的 IsoFLOP 曲线；参数化的损失函数拟合。三种方法都得到参数量与训练 token 数应按相同比例增长。按此训练的 Chinchilla（70B 参数、1.4T token）与算力相同的 Gopher（280B、300B token）相比，MMLU（57 个学科的多选题知识基准）5-shot 平均准确率为 67.6% 对 60.0%。
- **为什么在这个库里**：[训练科学方向](../../fields/training-science/README.md)主线节点 5“规模定律”的核心论文，也是“规模定律能外推多远”这一开放问题的入口：它说明拟合出的配比依赖学习率调度等实验协议，并自述只有两次大规模对照、高算力处最优参数量曲线有弯曲、分析只覆盖不超过一个 epoch 的训练。对照模型之一是 [GPT-3](../../../llm/papers/gpt3/reading.md)；配比怎样落到具体模型见[预训练方向](../../../llm/fields/pretraining/README.md)，规模化的跨领域论证见[观点：深度学习的规模化](../../../perspectives/scaling.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2203.15556 · [全文 PDF](https://arxiv.org/pdf/2203.15556)
- 方向：cross-domain/training-science
