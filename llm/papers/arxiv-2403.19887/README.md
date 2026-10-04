# Jamba: A Hybrid Transformer-Mamba Language Model

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.19887)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Transformer 的 KV 缓存随上下文增长，长上下文时成为限制，每生成一个 token 都要读整段上下文；Mamba 这类状态空间模型推理省，但同规模下仍落后于 Transformer。此前把注意力与状态空间模型混合的尝试规模都很小（§1）。
- **核心方法**：每 8 层里 1 层注意力、7 层 Mamba，每隔一层把 MLP 换成 MoE（16 个专家选 2 个），总参数 52B、激活 12B，8 位权重时单张 80GB GPU 放得下。256K 上下文、16 位精度下 KV 缓存为 4GB，Mixtral 为 32GB，Llama-2 70B 为 128GB（Table 1）。消融中 1:3 与 1:7 的混合比几乎没有差别，都好于纯注意力与纯 Mamba；纯 Mamba 在 IMDB 上常常不按"Positive / Negative"的格式回答（1.3B 模型：纯 Mamba 48.8，纯注意力 84.1，混合 90.9，Table 6），作者推测纯 SSM 难以学会上下文学习，并在混合模型的注意力层里找到 12 个类似 induction head 的头。放大到 7B 级时 Mamba 层内部出现大激活值和损失尖峰，加 RMSNorm 后稳定（§6.4）。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"混合架构"一线第一个公开权重的生产级模型（Apache 2.0），把纯 Mamba 的几个坑（上下文学习、格式遵循、大规模稳定性）写成了实验。后续 [Kimi Linear](../arxiv-2510.26692/README.md) 把全注意力的比例定在 1/4。被混合的两方见 [Mamba 精读](../mamba/reading.md)与 [Transformer 精读](../transformer/reading.md)，induction head 的背景见[模型科学](../../../cross-domain/fields/model-science/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2403.19887 · [全文 PDF](https://arxiv.org/pdf/2403.19887) · AI21 Labs（模型发布在 Hugging Face 的 ai21labs 账号，arXiv 注释给出 ai21.com/jamba） · 权重以 Apache 2.0 许可发布（原文 §1）
- 方向：llm/architecture、llm/long-context
