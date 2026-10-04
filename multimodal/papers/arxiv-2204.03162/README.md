# Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2204.03162)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视觉–语言模型在许多任务上表现很好，但能否理解"树在购物车里"与"购物车在树上"这种词相同、顺序不同的组合差别并不清楚。
- **核心方法**：400 组专家手工构造的题目：两张图、两句用词完全相同只是顺序不同的话，要求正确配对；分别算文本得分、图像得分和两者都对的组得分，并带细粒度语言与视觉标签。CLIP ViT-B/32 的三项得分为 30.75%、10.50%、8.00%，随机水平 25%、25%、16.67%，众包人类 89.50%、88.50%、85.50%，所有模型的组得分都低于随机。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 4 个节点：评测目标从"检索得准"迁到"组合得对"的起点；与 [ARO](../arxiv-2210.01936/README.md)、[SugarCrepe](../arxiv-2306.14610/README.md) 对照阅读。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2204.03162 · [全文 PDF](https://arxiv.org/pdf/2204.03162) · Hugging Face、Facebook AI Research、University of Waterloo、University College London
- 方向：multimodal/alignment、multimodal/vlm
