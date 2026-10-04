# DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

> 状态：技术精读 · 2026 · [原文](https://arxiv.org/abs/2606.19348)

[返回大语言模型目录](../../README.md)

- **解决什么**：推理模型靠更长的思考过程提升能力（测试时扩展），长程智能体任务又需要很长的上下文，而原始注意力的计算量随序列长度平方增长，成为百万 token 上下文的主要瓶颈。
- **核心方法**：保留 [DeepSeekMoE](../arxiv-2401.06066/README.md) 与多 token 预测（MTP），改动三处。注意力改为两种压缩注意力交错：CSA 先沿序列把 KV 压缩（压缩率 4），再用 DeepSeek 稀疏注意力只读其中 top-k 个条目；HCA 压缩率 128，但保持稠密；两者都加一条 128 token 的滑动窗口分支、对 Q 与压缩后的 KV 做 RMSNorm，并在 softmax 分母里加可学习的 sink 项，使一个头的注意力总量可以小于 1。残差连接改为 [mHC](../arxiv-2512.24880/README.md)。多数矩阵参数改用 [Muon](../arxiv-2502.16982/README.md) 优化器（嵌入、输出头、RMSNorm 仍用 AdamW），因为 Q、KV 已做归一化，没有采用 Kimi K2 的 QK-Clip。V4-Pro 为 1.6T 总参数、49B 激活，训练 33T token；V4-Flash 为 284B、13B，32T token；序列长度从 4K 逐步加到 16K、64K、1M；V4-Flash 前 1T token 用稠密注意力预热（V4-Pro 的稠密阶段更长），64K 时转为稀疏。1M 上下文下，V4-Pro 的单 token 推理 FLOPs 为 V3.2 的 27%，KV 缓存为 10%。报告写明训练中出现了明显的损失尖峰，回滚只能暂时恢复；作者把尖峰追到 MoE 层的离群值，用 Anticipatory Routing（用若干步之前的参数计算路由，只在检测到尖峰时启用）和 SwiGLU 截断压住，并承认原理尚未理解。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"问题与手段"表中几乎每一行都有它的条目：长上下文（CSA/HCA）、更深的网络（mHC）、优化器（Muon）、稳定性（两种新技巧）、课程（稠密预热后转稀疏）。上一代是 [DeepSeek-V3](../arxiv-2412.19437/README.md)；它采用的 Muon 来自 Kimi 的工作，体现了两家路线的交汇。优先级：必读。精读给出了 V3 → V3.2 → V4 的部件变化表和三代 KV 字节的手算。

## 阅读入口

- [技术精读](reading.md)
- [证据档案](evidence.json)
- [原文版本与阅读记录](source.json)

## 阅读顺序

[DeepSeek-V2 精读](../deepseek-v2/reading.md)（MLA）→ [DeepSeek-V3](../arxiv-2412.19437/README.md) → [NSA](../arxiv-2502.11089/README.md) → [DeepSeek-V3.2](../arxiv-2512.02556/README.md)（DSA）→ [mHC](../arxiv-2512.24880/README.md) → 本篇 → [DeepSeek-V4.1-Flash](../arxiv-2609.19969/reading.md)。

## 身份信息

- 稳定标识：arxiv:2606.19348 · [全文 PDF](https://arxiv.org/pdf/2606.19348) · DeepSeek-AI · 原文称这是 V4 系列的预览版
- 方向：llm/pretraining、llm/architecture、llm/long-context
