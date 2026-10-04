# Repeat After Me: Transformers are Better than State Space Models at Copying

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.01032)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：状态空间模型、线性注意力、RNN 这类推理时状态大小固定的模型（作者统称"广义状态空间模型"GSSM）在困惑度上已接近 Transformer，但不清楚它们为效率牺牲了什么（§1）。
- **核心方法**：理论上证明两层 Transformer 能复制长度随头数指数增长的字符串，而 GSSM 无法准确复制比状态比特数更长的串。实验上，学会复制长度 300 的串，Transformer 所需样本比最好的 GSSM 少 100 倍，并能外推到更长的串。在 Pile 上预训练、Mamba 困惑度更低的同规模模型之间对比：电话簿查找（给一份"姓名：号码"列表再问某人的号码）在列表足够长时，最小的 Pythia-410M 也超过最大的 Mamba-2.8B；SQuAD 上 Mamba 的成绩随段落变长下降得更快（§5）。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"线性注意力与状态空间做不好的场景"的直接证据：困惑度更低不等于能用好上下文。与 [Based](../arxiv-2402.18668/README.md) 的召回–状态下界、[Jamba](../arxiv-2403.19887/README.md) 的格式失败一起读；被比较的模型见 [Mamba 精读](../mamba/reading.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2402.01032 · [全文 PDF](https://arxiv.org/pdf/2402.01032) · ICML 2024 · Harvard University（Kempner Institute、CMSA）
- 方向：llm/architecture
