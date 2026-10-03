# DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2401.06066)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：GShard 这类常规混合专家（MoE）架构从 N 个专家中激活得分最高的 K 个，难以做到专家专门化（每个专家掌握互不重叠、聚焦的知识）。
- **核心方法**：相对 GShard 做两处改动：把专家细分成 mN 个、每个 token 激活其中 mK 个，让被激活专家的组合更灵活；再隔离出 K_s 个所有 token 共用的共享专家，承担通用知识、减少路由专家之间的冗余。2B 规模下，DeepSeekMoE 与专家参数和计算量都是其 1.5 倍的 GShard 2.9B 性能相当。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 7 节"MoE"节点：论文把"用 MoE 层替换 Transformer 中的 FFN"作为常规做法，每个专家与标准 FFN 结构相同，并直接用"知识混杂"与"知识冗余"描述要解决的问题。同一节点里，[Switch Transformer](../arxiv-2101.03961/README.md) 把路由简化到 1 个专家，本篇把专家切细；[DeepSeek-V2](../deepseek-v2/README.md) 在整个模型中采用本篇架构；下一节点 [Engram](../arxiv-2601.07372/README.md) 与本篇共享多位 DeepSeek-AI 作者，在 MoE 之外增加查表式的条件记忆。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2401.06066 · [全文 PDF](https://arxiv.org/pdf/2401.06066)
- 方向：llm/pretraining、llm/architecture
