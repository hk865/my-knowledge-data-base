# MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2002.10957)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：BERT 类模型有数亿参数，微调和线上服务受延迟与容量限制；需要一种任务无关的压缩方法，且学生模型的层数和宽度可以自由选择。
- **核心方法**：TinyBERT 等前作逐层对齐教师与学生，需要设计层与层的映射；本篇只蒸馏教师最后一层 Transformer 的自注意力模块。蒸馏目标除了注意力分布（query 与 key 的缩放点积），还新加入 value 之间的缩放点积（value 关系）。教师很大时，先蒸到一个中等大小的助教模型再蒸到学生。摘要报告：学生用教师 50% 的参数和计算量，在 SQuAD 2.0 和若干 GLUE 任务上保留 99% 以上的准确率。
- **为什么在这个库里**：[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)中"用中间表示做监督"的代表：蒸馏的对象可以是注意力内部的关系，而不只是输出分布。与 [DistilBERT](../arxiv-1910.01108/README.md) 同属 BERT 时代的预训练模型压缩，两者对照可看出"蒸什么"的选择。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2002.10957 · [全文 PDF](https://arxiv.org/pdf/2002.10957) · 代码与模型在 microsoft/unilm 仓库
- 作者：Wenhui Wang、Furu Wei、Li Dong、Hangbo Bao、Nan Yang、Ming Zhou（Microsoft Research）
- 方向：cross-domain/knowledge-distillation、llm/pretraining、llm/architecture
