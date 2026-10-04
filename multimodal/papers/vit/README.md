# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

> 状态：逐步教学版精读 · 2020 · [原文](https://arxiv.org/abs/2010.11929)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：2020 年大规模图像识别的最好结果仍属于 ResNet 一类卷积网络；视觉里引入自注意力的工作要么与卷积结合，要么用专门设计的局部或稀疏注意力，难以在现代加速器上有效扩展。论文要回答：尽量不改标准 Transformer、不加图像专用的归纳偏置（一句话：结构里预先写入的规律假设，如卷积的局部性与平移等变性），靠更大的数据能否胜过卷积。
- **核心方法**：最接近的前作 Cordonnier 等只用 2×2 的小块做全局注意力，适用于小分辨率图像；ViT 把 224×224 的图切成 196 个 16×16 的块，每块经同一个线性投影变成向量，加一维可学习位置向量和 BERT 式 [class] token，直接送进标准 Transformer 编码器，增量在规模实验而不在新结构。只用 ImageNet 预训练时它不如同规模的 ResNet；在 3 亿张图的 JFT-300M 上预训练后，ViT-H/14 在 ImageNet 上达到 88.55%，预训练约 2.5k TPUv3 核·天，少于 BiT-L 的 9.9k（表 2）。
- **为什么在这个库里**：[视觉表征方向](../../fields/visual-representation/README.md)主线中"架构轴从 CNN 移到 Transformer"的节点，位于 [Baseline 页](../../fields/visual-representation/BASELINES.md)"架构 = 切块 Transformer"与"数据 = JFT-300M"两格，它的配方问题由同表"训练配方"的 [DeiT](../arxiv-2012.12877/README.md)、AugReg 两行修正。[MAE](../mae/README.md)、[DINO](../dino/README.md)、[CLIP](../clip/README.md) 都在这个骨干上换学习目标。优先级：必读。

## 阅读入口

- [逐步教学版精读](reading.md)：从切块手算到推理；"局限与后续"补了 DeiT、AugReg、Registers 等后续工作修正的结论
- [本篇图解与说明](figures/README.md)

## 可选的阅读顺序

[Attention Is All You Need](../../../llm/papers/transformer/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2010.11929 · Google Research（Brain Team） · ICLR 2021
- 年份：2020
- [官方原文页面](https://arxiv.org/abs/2010.11929)
- [官方全文入口](https://arxiv.org/pdf/2010.11929v2)
- 阅读版本：v2
- 方向：multimodal/alignment、multimodal/visual-representation、robotics/perception
