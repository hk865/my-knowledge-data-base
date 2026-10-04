# Learning Transferable Visual Models From Natural Language Supervision

> 状态：逐步教学版精读 · 2021 · [原文](https://arxiv.org/abs/2103.00020)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：传统分类器把类别含义存在分类头的权重里，新增或更换类别就要重新标注、重新训练；此前用网页文字做监督的工作规模太小，Visual N-Grams 的零样本 ImageNet 只有 11.5%。CLIP 要回答：网上天然配对的图文能否代替人工类别标签，并直接给出一个用语言指定任务的接口。
- **核心方法**：结构上是从头训练的简化版 ConVIRT（在医学图像与报告上做图文对比学习的前作），增量在数据与规模：自建 4 亿对网上图文，图像塔和文本塔各输出一个单位向量，在每批 32,768 对里同时训练"图找文"与"文找图"的批内对比（一句话：每个样本要从同批全部候选中认出自己的配对）。使用时把类别名写成"a photo of a {类别}."交给文本塔，得到的向量就是分类器权重；不用 ImageNet 的训练图，零样本 ImageNet 76.2%（表 1），与原始的有监督 ResNet-50 相当。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)的[基线](../../fields/alignment/BASELINES.md)，也是[视觉表征方向 Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 图文对比"一行与"冻结的大编码器"基线之一；它在读出接口上的问题由同表 [LLaVA](../llava/README.md)、Perception Encoder 两行接上，图像塔也由此成为视觉语言模型的常用视觉塔。优先级：必读。

## 阅读入口

- [逐步教学版精读](reading.md)：从批内配对手算到零样本推理；"局限与后续"补了 MetaCLIP、DataComp、SigLIP、ARO 等后续工作修正的结论
- [本篇图解与说明](figures/README.md)

## 可选的阅读顺序

[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../vit/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2103.00020 · OpenAI
- 年份：2021
- [官方原文页面](https://arxiv.org/abs/2103.00020)
- [官方全文入口](https://arxiv.org/pdf/2103.00020v1)
- 阅读版本：v1
- 方向：multimodal/alignment、multimodal/vlm、robotics/perception
