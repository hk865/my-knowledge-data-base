# Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2102.05918)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视觉与视觉–语言表征依赖昂贵的人工清洗数据集（例如 Conceptual Captions），规模只有约千万对，限制了模型的扩大。
- **核心方法**：与 [CLIP](../clip/README.md) 同样是双塔加批内对比损失（EfficientNet-L2 图像塔、BERT-Large 文本塔，批 16384），差别在数据：放松 Conceptual Captions 的几乎全部清洗步骤，只做词频过滤，得到 18 亿对噪声 alt-text。零样本 ImageNet 76.4%（CLIP 76.2%）；消融显示同为 300 万对时噪声数据明显差于清洗数据，增加到 1200 万对时反超（Table 10），即规模可以弥补噪声。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 2 个节点、Baseline 页中与 CLIP 并列的基线，代表"最少过滤、靠规模"的数据选择；它自述的文本–文本相似度偏弱与人口分布偏斜，是后来数据整理研究的出发点之一。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2102.05918 · [全文 PDF](https://arxiv.org/pdf/2102.05918) · Google Research · ICML 2021
- 方向：multimodal/alignment、multimodal/visual-representation
