# DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1910.01108)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：BERT 这类大型预训练模型难以放到端侧设备上，也难以在有限的训练或推理预算下运行；需要一个通用的小模型，像大模型一样能再微调到各种任务，而不是每个任务各压缩一次。
- **核心方法**：此前的知识蒸馏（让小模型即学生去模仿大模型即教师的输出分布）大多在微调阶段为单个任务做；本篇把蒸馏挪到预训练阶段。学生沿用 BERT 的结构，层数减半，去掉 token-type 嵌入和 pooler，用掩码语言建模、蒸馏、隐状态余弦距离三项损失一起训练。摘要报告：参数比 BERT-base 少 40%，保留 97% 的语言理解能力，推理快 60%。
- **为什么在这个库里**：[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)里"预训练阶段的任务无关蒸馏"的早期代表，上承 [Hinton 等 2015](../../../cross-domain/papers/arxiv-1503.02531/README.md) 的软标签蒸馏；[MiniLM](../arxiv-2002.10957/README.md) 随后改为只蒸教师最后一层的自注意力。在[预训练方向](../../fields/pretraining/README.md)里，它是"用大模型教小模型"这一问的 BERT 时代参照。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1910.01108 · [全文 PDF](https://arxiv.org/pdf/1910.01108) · NeurIPS 2019 第 5 届 EMC² Workshop
- 作者：Victor Sanh、Lysandre Debut、Julien Chaumond、Thomas Wolf（Hugging Face）
- 方向：cross-domain/knowledge-distillation、llm/pretraining、llm/architecture
