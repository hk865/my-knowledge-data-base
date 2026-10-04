# Kimi Linear: An Expressive, Efficient Attention Architecture

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.26692)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：线性注意力（用固定大小的递推状态代替随长度增长的 KV 缓存）计算和显存都省，但表达力有限，作者写明长上下文检索是纯线性结构的主要瓶颈；以往把线性注意力与全注意力混合的模型，规模小、评测也不全面。
- **核心方法**：提出 Kimi Delta Attention（KDA），在 Gated DeltaNet 的基础上把逐头的遗忘门改成逐通道的门，让每个特征维度有自己的遗忘速率。模型每 3 层 KDA 接 1 层全注意力 MLA，MLA 层不用位置编码（NoPE），位置与近因偏好全部交给 KDA，这样扩展上下文时也不必调整 RoPE。在 1.4T token、相同训练配方的对照下，48B 总参数、3B 激活的 Kimi Linear 在短上下文、长上下文和强化学习评测上都超过全 MLA 基线，KV 缓存最多减少 75%，1M 长度下解码吞吐最多提高 6 倍。混合比例的消融显示，7:1 的训练损失相近，但在分布不同的验证集上明显变差；1:1 验证损失相近，推理开销更大。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"更长更大的注意力"中"用线性注意力替换大部分全注意力"一条路线的代表，接在[递推状态谱系](../../../foundations/relations/recurrent-state.md)的线性注意力节点之后。[Attention Residuals](../arxiv-2603.15031/README.md) 在它的结构上做实验，[Kimi K3](../arxiv-2607.24653/README.md) 沿用 3:1 的 KDA–MLA 混合。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2510.26692 · [全文 PDF](https://arxiv.org/pdf/2510.26692) · Kimi Team（Moonshot AI）
- 方向：llm/pretraining、llm/architecture、llm/long-context
