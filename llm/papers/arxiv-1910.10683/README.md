# Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1910.10683)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：迁移学习（先在数据丰富的任务上预训练，再在下游任务上微调）的方法五花八门，难以分辨哪些因素真正重要。
- **核心方法**：把所有文本任务统一成"输入文本 → 输出文本"的格式，在同一框架下系统比较预训练目标、架构、无标注数据、迁移方式等因素，并发布约 750GB 的清洗网页语料 C4。架构比较（§3.2.4，计算量相同、先预训练再微调）中，encoder-decoder 加去噪目标（遮掉文本片段让模型还原）在全部任务上最好，GLUE 为 83.28，同样用去噪目标的 decoder-only 语言模型为 74.70；去噪目标总体优于语言建模目标。综合这些结论并把模型扩大到 11B 参数，在摘要、问答、文本分类等多个 benchmark 上达到当时最好。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"主线历史"第 1 阶段"配方收敛到 decoder-only"这一判断的反面证据：它的结论限定在先预训练再微调的设定下，评测转向不微调的 few-shot 之后，结论翻转（见 [GPT-3 精读](../gpt3/reading.md)与 [PaLM](../arxiv-2204.02311/README.md)）。作者在展望中也怀疑去噪这种简单目标不是教模型通用知识的高效方式。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1910.10683 · [全文 PDF](https://arxiv.org/pdf/1910.10683) · Google · 正式版发表于 JMLR 21 (2020)；C4 数据、预训练模型与代码公开
- 方向：llm/pretraining
