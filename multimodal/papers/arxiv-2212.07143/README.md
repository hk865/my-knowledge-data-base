# Reproducible scaling laws for contrastive language-image learning

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2212.07143)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：缩放定律研究多用私有数据和模型，或只研究单模态；对比图文学习的缩放规律缺少可复现的系统研究。
- **核心方法**：用公开的 LAION（最多 20 亿对）和 OpenCLIP 代码，按模型、数据、看过的样本数三条轴训练到 340 亿个样本，拟合零样本分类、检索、线性探针与微调的幂律。同为 ViT-L/14，OpenAI CLIP ImageNet 零样本 75.5%、COCO 文到图 R@5 61.1%，LAION-2B 上为 75.2%、71.1%：WIT 训练的模型在分类上随规模提升更快，LAION 训练的在检索上更快，作者归因于训练数据分布。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 5 个节点，"数据分布决定缩放曲线"的直接证据；也是 LAION 与华盛顿大学一系"公开数据加受控测量"偏好的中间一篇（前接 [LAION-5B](../arxiv-2210.08402/README.md)，后接 [DataComp](../arxiv-2304.14108/README.md)）。规模化总线见[观点页](../../../perspectives/scaling.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2212.07143 · [全文 PDF](https://arxiv.org/pdf/2212.07143) · LAION、UC Berkeley、HuggingFace、University of Washington、Jülich Supercomputing Center
- 方向：multimodal/alignment
