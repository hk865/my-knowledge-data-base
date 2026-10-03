# Dissecting Recall of Factual Associations in Auto-Regressive Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2304.14767)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已知事实性知识可以定位到语言模型的中层 MLP（见 [ROME](../arxiv-2202.05262/README.md)），但模型在推理时怎样把它取出来、交到预测位置，此前并不清楚。
- **核心方法**：在 GPT-2（1.5B）和 GPT-J（6B）上用"注意力敲除"（逐层切断最后位置对主语或关系位置的注意力边，看预测概率掉多少）追踪信息流，得到三步机制：较早层的 MLP 把大量属性写进主语最后一个 token 的表示；关系信息传到预测位置；上层注意力头再从主语表示中"查询"出属性，这些头的参数本身也常编码主语到属性的映射（约 70% 的预测符合这一模式）。相对 ROME，它补上了"读出"这一半，并把重点从中层 MLP 前移到更低层的 MLP 与注意力参数。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)中"注意力参与读出事实"的直接证据，使那条链的结论成为"事实主要存于 MLP，由注意力读出"。优先级：选读。
