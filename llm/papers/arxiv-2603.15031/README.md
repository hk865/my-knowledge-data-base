# Attention Residuals

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2603.15031)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：预归一化（PreNorm，先归一化再进子层）的残差连接把所有层的输出以相同的权重 1 累加，隐藏状态的幅度随层数 L 按 O(L) 增长，每一层的相对贡献被逐渐稀释，早期层的信息埋在总和里，无法被后面的层有选择地取回。
- **核心方法**：作者把"残差沿深度累加"看作与"RNN 沿时间递推"对偶的结构：Transformer 当年用注意力取代了时间上的递推，这里用注意力取代深度上的累加。每层有一个可学习的伪查询向量，对前面各层的输出做 softmax 加权求和（Full AttnRes）。为降低大规模训练中的显存与流水线通信，把层分成约 8 个块，只对块级表示做注意力（Block AttnRes）。五种规模的规模定律拟合中，Block AttnRes 的损失相当于基线多用 1.25 倍算力；在 Kimi Linear 结构（48B 总参数、3B 激活，1.4T token）上，各层输出幅度保持有界，梯度在各层分布更均匀，下游评测全部提升。原文表 2 把 mHC 列为参照：Full AttnRes 优于 mHC，Block AttnRes 与之相当，每层访存更少（5.5d 对 34d）。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"支持更深更大的网络"中残差流一线的 Kimi 方案，与 DeepSeek 的 [mHC](../arxiv-2512.24880/README.md) 处理同一个问题而数学手段不同。实验骨架是 [Kimi Linear](../arxiv-2510.26692/README.md)，[Kimi K3](../arxiv-2607.24653/README.md) 采用了它。残差连接的基础见 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.2 节。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2603.15031 · [全文 PDF](https://arxiv.org/pdf/2603.15031) · Kimi Team（Moonshot AI）
- 方向：llm/pretraining、llm/architecture
