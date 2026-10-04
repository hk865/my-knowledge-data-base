# Gemma 2: Improving Open Language Models at a Practical Size

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2408.00118)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：小模型的进步主要靠加长训练，但收益只随数据量对数增长（最新的小模型要训练到 15T token，才能把最好成绩提高不到 1%–2%），作者认为这说明小模型仍训练不足，于是寻找不靠继续堆 token 的提升办法。
- **核心方法**：2B 与 9B 模型不再以下一个真实 token 为目标，而以大模型（教师）给出的下一词分布为目标做知识蒸馏，在超过计算最优量 50 倍的 token 上训练，用来模拟在多于现有数据的 token 上训练；27B 模型从头训练（13T token）。结构上每隔一层交替使用局部滑动窗口注意力（窗口 4096）与全局注意力（跨度 8192），用 GQA（分组查询注意力），并对注意力层与最终层的 logit 做软截断（logit soft-capping，按 soft_cap·tanh(logits/soft_cap) 把 logit 限制在 ±soft_cap 内，注意力层取 50、最终层取 30）。消融中，从 7B 教师蒸馏的 2B 模型优于从头训练的同尺寸模型。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)两处的起点："更多知识"一节里蒸馏作为小模型的训练目标，"更长更大的注意力"一节里局部/全局交错（1:1）。它的 logit 软截断在 [Gemma 3](../arxiv-2503.19786/README.md) 中被 QK-Norm 取代。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2408.00118 · [全文 PDF](https://arxiv.org/pdf/2408.00118) · Google DeepMind（Gemma Team）
- 方向：llm/pretraining、llm/architecture
