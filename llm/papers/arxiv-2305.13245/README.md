# GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2305.13245)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自回归解码每一步都要从显存读出全部权重和历史 K、V，速度受显存带宽限制；多查询注意力（MQA，所有查询头共用一组 K、V）读得少，但原文写明它会降低质量、训练也不稳定（§1、附录 A）。
- **核心方法**：分组查询注意力（GQA）：把查询头分成 G 组，每组共用一组 K、V 头，G=1 退化为 MQA，G 等于头数时就是普通多头注意力。已有的多头模型可以"升级训练"：把各头的 K、V 投影取平均合并，再用原预训练算力的 5% 继续训练（§2.1）。T5-XXL 上 8 组的 GQA 推理时间 0.28（MQA 0.24、多头 1.51），平均分 47.1，接近多头的 47.2（Table 1）。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"推理效率"一节"减少每个 token 的 KV 缓存"一格的代表，[Qwen2.5-1M](../qwen2.5-1m/reading.md) 等模型沿用；更激进的压缩是 [DeepSeek-V2](../deepseek-v2/reading.md) 的 MLA。机制见 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 14.3 节。自述局限：只在 encoder–decoder 模型上评估，没有和从头训练的 GQA 对比。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2305.13245 · [全文](https://arxiv.org/pdf/2305.13245) · Google Research
- 方向：llm/inference、llm/architecture
