# Gemma 3 Technical Report

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.19786)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：给 Gemma 增加视觉理解、更多语言和至少 128K 的上下文，同时控制长上下文下急剧增长的 KV 缓存显存。
- **核心方法**：局部与全局注意力层的比例从 Gemma 2 的 1:1 改为 5:1，局部窗口从 4096 缩到 1024；消融中比例改到 7:1、窗口缩小，验证困惑度的变化都很小。32K 上下文下，只用全局注意力的配置让 KV 缓存带来约 60% 的额外显存，局部层更多、窗口 1024 的配置降到 15% 以下（原文图 5）。用 QK-Norm 替代 Gemma 2 的 logit 软截断。长上下文不从头用 128K 训练：先用 32K 序列预训练，到预训练末段把全局层的 RoPE 基频从 10K 提到 1M（局部层保持 10K），再按 8 倍缩放扩到 128K（1B 模型只到 32K）。所有模型都用蒸馏训练，每个 token 按教师概率采样 256 个 logit 作为学习目标；27B 模型训练 14T token。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"损失稳定"（QK-Norm 替代软截断）与"更长更大的注意力"（局部/全局交错的第二代）两处的证据，也是 Google 开放模型"交错注意力加蒸馏"这一偏好的中间一环。前一代是 [Gemma 2](../arxiv-2408.00118/README.md)；下一代 Gemma 4 保持 5:1，并让全局层的 key 兼作 value。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2503.19786 · [全文 PDF](https://arxiv.org/pdf/2503.19786) · Google DeepMind（Gemma Team）
- 方向：llm/pretraining、llm/architecture、llm/long-context
