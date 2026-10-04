# TinyBERT: Distilling BERT for Natural Language Understanding

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1909.10351)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：BERT 这类预训练语言模型计算代价高，难以在资源受限的设备上高效运行；已有的 BERT 蒸馏只用输出或部分隐状态，且多只在一个阶段做。
- **核心方法**：相对 [DistilBERT](../arxiv-1910.01108/README.md) 只在预训练阶段用软标签和隐状态余弦，本篇为 Transformer 设计逐层蒸馏：学生的嵌入层、每层的注意力矩阵与隐状态、最后的预测层分别对齐教师的对应层；并在两个阶段都蒸馏：先在通用语料上做通用蒸馏，再用微调过的 BERT 作教师、在扩充过的任务数据上做任务蒸馏，扩充用 BERT 与 GloVe 做词替换。4 层的 TinyBERT4 有 14.5M 参数，比 BERT-base 小 7.5 倍、推理快 9.4 倍，GLUE 测试集平均 77.0，教师 79.5，同尺寸的 DistilBERT4 为 71.9（Table 1）。
- **为什么在这个库里**：[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)主线阶段 4 的三种做法之一（逐层对齐），与 [MiniLM](../arxiv-2002.10957/README.md) 的"只蒸最后一层"对照着读，后者正是为省去 TinyBERT 这类层映射而提出。它也给出了这一阶段做不好的场景：所有 4 层学生在 CoLA 上都与教师差距很大（TinyBERT4 44.1、教师 52.8）；去掉任务阶段的数据增强，四项平均从 75.6 降到 68.4（Table 2）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1909.10351 · [全文 PDF](https://arxiv.org/pdf/1909.10351) · 华为诺亚方舟实验室、华中科技大学 · Findings of EMNLP 2020 · 代码与模型开放（huawei-noah/Pretrained-Language-Model）
- 作者：Xiaoqi Jiao、Yichun Yin、Lifeng Shang、Xin Jiang、Xiao Chen、Linlin Li、Fang Wang、Qun Liu
- 方向：cross-domain/knowledge-distillation、llm/pretraining
