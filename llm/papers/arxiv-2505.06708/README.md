# Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2505.06708)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：门控在 LSTM、状态空间模型、线性注意力里用得很多，但它在标准 softmax 注意力中具体起什么作用，缺少系统研究；与此相关的两个现象也缺少简单的解释和缓解办法：注意力汇聚（attention sink，大量注意力分数集中在开头的 token 上）和训练中的损失尖峰。
- **核心方法**：在 15B MoE（2.54B 激活）与 1.7B 稠密模型上，用最多 3.5T token 比较 30 多种门控变体，发现在缩放点积注意力（SDPA）的输出之后加一个逐头、依赖输入的 sigmoid 门效果最好。作者把原因归于两点：给注意力中由 V 投影与输出投影构成的低秩线性映射加上非线性，以及按查询产生的稀疏门值。基线模型平均 46.7% 的注意力落在第一个 token 上（第 21 层达 83%），加门后降到 4.8%；门控还压低了大激活值，基线在调高学习率时出现收敛问题，门控模型可以用更大的学习率。把上下文用 YaRN 从 32K 扩到 128K 后，RULER 在 128K 上基线为 31.65，门控为 58.82；在原训练长度 32K 以内，两者相差很小。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"注意力不丢失"一节的核心证据，它把注意力汇聚、大激活值、训练稳定与长度外推连在一起。[DeepSeek-V4](../arxiv-2606.19348/README.md) 走了另一条路，在 softmax 分母中显式加入可学习的 sink 项；[Kimi K3](../arxiv-2607.24653/README.md) 的 MLA 输出门引用了这一类门控。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2505.06708 · [全文 PDF](https://arxiv.org/pdf/2505.06708) · 阿里巴巴 Qwen 团队（另有 University of Edinburgh、Stanford、MIT、清华大学作者）
- 方向：llm/pretraining、llm/architecture
