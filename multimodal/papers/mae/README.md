# Masked Autoencoders Are Scalable Vision Learners

> 状态：技术精读 · 2021 · [原文](https://arxiv.org/abs/2111.06377)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言已经靠"遮住再预测"摆脱了标注，视觉里的去噪自编码一直落后：ViT 自己试过的遮蔽块预测在 ImageNet 上只到 79.9%，比大规模有监督预训练低约 4 个百分点，BEiT 预测离散视觉 token 又要先用额外数据训练分词器。作者把差距归到两点：图像空间冗余大，少量缺失块能从邻居插值出来；输出像素的解码器怎么设计，决定编码器学到的语义层次。
- **核心方法**：相对 ViT 与 BEiT 的遮蔽预测，MAE 把遮挡比例提到 75%，标准 ViT 编码器只处理可见块，遮挡标记（一句话：占住被遮位置的共享可学习向量）只在一个很小的解码器入口才插入，重建目标直接是像素，不需要外部分词器。ViT-L 上，编码器不处理遮挡标记时微调 84.9、线性评测 73.5，处理时为 84.2、59.6，计算量还多 3.3 倍（表 1c）；只用 ImageNet-1K，ViT-H 在 448 分辨率微调达到 87.8%（表 3）。
- **为什么在这个库里**：[视觉表征方向 Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 遮蔽 75% 的块重建像素"一行，与 [DINO](../dino/README.md) 相邻，是[入门页](../../fields/visual-representation/README.md)"对 ViT 的四种回答"中只换训练信号的一种；它"微调强、冻结特征弱"的协议差异是入门页"从测量看"一节的例子，视频一侧的 VideoMAE 也沿用它的训练信号（[视频与时序方向](../../fields/video-temporal/README.md)）。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：高遮挡率与非对称编码器的计算账；"局限与后续"补了 DINOv2、Web-SSL、I-JEPA 的对照
- [本篇图解与说明](figures/README.md)

## 可选的阅读顺序

[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../vit/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2111.06377 · Facebook AI Research（FAIR）
- 年份：2021
- [官方原文页面](https://arxiv.org/abs/2111.06377)
- [官方全文入口](https://arxiv.org/pdf/2111.06377v3)
- 阅读版本：v3
- 方向：multimodal/visual-representation
