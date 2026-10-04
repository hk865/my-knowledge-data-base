# Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models

> 状态：技术精读 · 2026 · [原文](https://arxiv.org/abs/2601.07372)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：混合专家（MoE）用条件计算扩充容量，但 Transformer 没有原生的"按键查知识"操作，只能用多层计算去模拟检索，效率低。
- **核心方法**：在 MoE 的条件计算之外加一条"条件记忆"稀疏轴：把经典的 N-gram（连续 N 个 token 组成的片段）嵌入现代化为 Engram 模块，用当前 token 与前几个 token 组成的 N-gram 做哈希，以常数时间从大嵌入表中取出向量，经门控加回残差流（各层逐层累加更新的主表示）。在总参数与每 token 计算量都固定的条件下，验证损失随稀疏参数在 MoE 专家与 Engram 表之间的分配比例呈 U 形；按这一规律扩展到 27B 的 Engram 模型，优于参数量和计算量都相同的 MoE 基线。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 8 节"Engram"节点：它把不依赖上下文的静态模式从计算中移到查表里，关掉 Engram 后事实知识类基准大幅下降、阅读理解类基本保留。上一节点是 [Switch Transformer](../arxiv-2101.03961/README.md) 与 [DeepSeekMoE](../arxiv-2401.06066/README.md) 代表的 MoE；相关工作一节直接引用 [FFN 键值记忆](../../../cross-domain/papers/arxiv-2012.14913/README.md)；下一节点 [Tokenizer-Agnostic Engram Module](../arxiv-2607.29065/README.md) 与 [Frozen Memory Is Not Enough](../arxiv-2608.17050/README.md) 把它的嵌入表当作可移植部件。[DeepSeek-V4](../arxiv-2606.19348/README.md) 没有采用它，[DeepSeek-V4.1-Flash](../arxiv-2609.19969/README.md) 接入了 196B 参数的 Engram。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [证据档案](evidence.json)
- [原文版本与阅读记录](source.json)
- 关系页：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 8–9 节

## 身份信息

- 稳定标识：arxiv:2601.07372 · [全文 PDF](https://arxiv.org/pdf/2601.07372)
- 方向：llm/pretraining、llm/architecture
