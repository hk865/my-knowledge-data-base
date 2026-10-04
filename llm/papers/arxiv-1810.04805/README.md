# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> 状态：文献卡 · 2018 · [原文](https://arxiv.org/abs/1810.04805)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：GPT 这类从左到右的语言模型做预训练时，每个 token 只能看见前文，作者认为这对句子级任务不是最优，对问答这类需要两侧上下文的逐 token 判断更不利；需要一种能双向预训练、再加一个输出层就能微调到各种任务的表示。
- **核心方法**：相对 GPT 的单向语言模型，改用遮蔽语言模型（一句话：随机遮住输入中 15% 的 token，让模型根据两侧上下文猜回原词）训练双向 Transformer 编码器；被选中的位置 80% 换成 [MASK]、10% 换随机词、10% 保持不变，以减轻预训练有 [MASK]、微调没有的不一致。另加下一句预测任务（判断句子 B 是否紧接句子 A）。BERT-base 有 110M 参数（与 GPT 同尺寸以便对照），BERT-large 有 340M。摘要报告 11 项 NLP 任务刷新纪录，GLUE 80.5（绝对提高 7.7 个百分点）、SQuAD v1.1 测试 F1 93.2。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)主线第 1 个节点中 encoder-only 一路的代表，也是 STYLE §3.3"路线为什么收敛"示例里与 GPT、T5 对照的一方；遮蔽目标的机制见[自监督与生成目标讲义](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)。在[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)里，它是 [DistilBERT](../arxiv-1910.01108/README.md)、[TinyBERT](../arxiv-1909.10351/README.md)、[MiniLM](../arxiv-2002.10957/README.md) 共同的教师，BERT 时代压缩工作的起点。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1810.04805 · [全文 PDF](https://arxiv.org/pdf/1810.04805) · Google AI Language · NAACL-HLT 2019 · 代码与预训练模型开放（google-research/bert）
- 作者：Jacob Devlin、Ming-Wei Chang、Kenton Lee、Kristina Toutanova
- 方向：llm/pretraining、llm/architecture、cross-domain/knowledge-distillation
