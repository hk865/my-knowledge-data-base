# Fast Transformer Decoding: One Write-Head is All You Need

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1911.02150)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Transformer 训练时整段序列可以并行，自回归生成却只能一个 token 一个 token 地算，每一步都要从显存重新读出整段历史的 K、V（KV 缓存，生成时为复用而保存的历史键值）。作者的分析是，这一步的速度受显存带宽限制而不是算力限制，序列越长越严重（§2.4.1）。
- **核心方法**：相对 [Transformer](../transformer/README.md) 的多头注意力只改一处：保留多个查询头，让所有头共用同一组 K、V，称为多查询注意力（MQA），KV 缓存因此缩小为原来的 1/h（h 为头数）。WMT14 英→德的 6 层 encoder–decoder（2.11 亿参数，8 个头）上，解码器每个 token 的推理时间从 46 μs 降到 3.8 μs（TPUv2，Table 2），开发集 BLEU 从 26.7 降到 26.5；Billion-Word 语言模型的开发集困惑度从 29.9 升到 30.2，好于"直接减少头数或头维度"的各种替代（30.9–31.2，Table 3）。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"注意力变体"一线的起点，也是"KV 缓存"这个部件第一次被单独当作设计目标。站在现在看，它的质量损失被小模型上的 BLEU 与困惑度低估了：[GQA](../arxiv-2305.13245/README.md) 附录 A 报告从头训练的 MQA 频繁出现损失尖峰、在长输入任务上微调时直接发散；[DeepSeek-V2](../deepseek-v2/reading.md) 附录 D.1 的 7B 稠密模型上，MMLU 多头 45.2、GQA 41.2、MQA 37.9。机制见 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 14.3 节。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1911.02150 · [全文 PDF](https://arxiv.org/pdf/1911.02150) · Google · 单作者技术报告，原文写明实验配置"发表前补充"
- 方向：llm/architecture、llm/inference
