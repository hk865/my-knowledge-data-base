# How to train your ViT? Data, Augmentation, and Regularization in Vision Transformers

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2106.10270)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：ViT 的归纳偏置比 CNN 弱，小数据上更依赖正则与数据增强（作者合称 AugReg）；但训练数据量、AugReg、模型大小与计算预算之间怎样权衡，没有系统研究，各论文实现细节不同，结果也难以互相比较。
- **核心方法**：用统一设置在 ImageNet-1K、ImageNet-21K、JFT-300M 上训练大量不同大小的 ViT（含与 ResNet 的混合结构），扫描增强与正则强度，再做迁移评测，发布 5 万多个模型。主要结论：合适的 AugReg 加更多计算，效果约等于训练数据扩大 10 倍，在公开的 ImageNet-21K 上训练的 ViT 追平或超过 JFT-300M 上的同规模模型，但两条路花的计算差不多；增强比正则更常有用，在 ImageNet-21K 上正则几乎总是有害，计算固定为 30 epoch 时任何 AugReg 都伤害除最大模型以外的模型；在只有约 3000 张图的 Pet37 上，从零训练怎样搜索都达不到迁移的效果；性能相近的预训练模型之间，迁移时优先选数据更多的，而不是增强更多的。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"数据"与"训练配方"两行：Google 自己对"ViT 依赖 JFT"的修正，与 [DeiT](../arxiv-2012.12877/README.md) 一起把架构差异与配方、数据差异分开（[ViT 精读](../vit/reading.md)"局限与后续"第 1–2 条）。它还提醒不要只用 ImageNet-1K 验证集挑模型：在 1K 上预训练会抬高这个验证集的分数。自述局限：只研究原始 ViT 结构，不含 ResNet 与后来的 ViT 变体，主要是分类任务。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2106.10270 · [全文 PDF](https://arxiv.org/pdf/2106.10270) · Google Research, Brain Team（Zürich） · TMLR 2022（05/2022）
- 方向：multimodal/visual-representation
