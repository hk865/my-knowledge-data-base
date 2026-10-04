# Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2408.15664)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：混合专家模型（MoE，每个 token 只送到少数几个专家 FFN 计算）需要各专家的负载大致均衡，否则会出现路由坍缩（少数专家吃掉大部分 token）。常用的负载均衡辅助损失（GShard、Switch Transformer 的做法）陷入两难：系数小了均衡不住，系数大了会引入与语言建模目标冲突的梯度，拉低模型质量。
- **核心方法**：去掉辅助损失，在 top-K 选择之前给每个专家的路由分数加一个偏置，按上一批的负载调整（负载重就调低，负载轻就调高）。偏置只决定选谁，不进入门控权重和梯度；它依据的是历史负载，因此不会像 Expert Choice 那样用到同一序列中未来 token 的信息。在 1B 与 3B 的 MoE（最多 200B token）上，验证困惑度分别从 9.56 降到 9.50、从 7.97 降到 7.92，衡量全局负载偏离的 MaxVio 从 0.72、0.52 降到 0.04（对照组为系数 0.001 的辅助损失）。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"支持更深更大的网络"一节中负载均衡的代表。[DeepSeek-V3](../arxiv-2412.19437/README.md) 把它用到 671B 模型上并做了消融，[Kimi K3](../arxiv-2607.24653/README.md) 在近千个专家时改用按分位数直接设定偏置的做法。MoE 本身见 [DeepSeekMoE](../arxiv-2401.06066/README.md) 与[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 7 节。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2408.15664 · [全文 PDF](https://arxiv.org/pdf/2408.15664) · DeepSeek-AI 与北京大学
- 方向：llm/pretraining、llm/architecture
