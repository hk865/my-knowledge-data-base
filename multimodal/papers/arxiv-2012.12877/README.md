# Training data-efficient image transformers & distillation through attention

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2012.12877)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：ViT 的好结果依赖 3 亿张非公开图像（JFT-300M）和大型算力，原文的结论是数据不足时泛化差，多数团队用不上这样的条件。
- **核心方法**：结构与 ViT-B 相同，只用 ImageNet-1K，在一台 8 卡机器上预训练 53 小时。增量全在训练配方：AdamW、RandAugment、Mixup、CutMix、随机擦除、随机深度、重复增强。DeiT-B 在 224 分辨率 81.8%，384 分辨率微调后 83.1%。消融显示配方极其敏感：去掉随机擦除或随机深度，训练不收敛（4.3%、3.4%）；同时去掉 Mixup 与 CutMix 降到 75.8%；优化器换成 SGD 降到 74.5%（Table 8）。另加一个"蒸馏 token"，向 CNN 教师（RegNetY-16GF，82.9%）的预测标签学习，最好 85.2%，比 JFT 预训练的 ViT-B（384 分辨率 84.15%）高约 1 个百分点；CNN 当教师比 Transformer 当教师效果更好，作者推测是学生继承了卷积的归纳偏置。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练配方"一行的第一篇：它说明 ViT"需要大数据"的结论有很大一部分是配方问题（[ViT 精读](../vit/reading.md)"局限与后续"第 1 条）；只用 ImageNet 的 DeiT-B 也是 BEiT 等同骨干比较中的有监督对照，Registers 分析的 DeiT-III 是它的续作。作者自述：配方沿用了为卷积网络设计的增强与正则，更适合 Transformer 的增强还会带来提升。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2012.12877 · [全文 PDF](https://arxiv.org/pdf/2012.12877) · Facebook AI、Sorbonne University · ICML 2021
- 方向：multimodal/visual-representation
