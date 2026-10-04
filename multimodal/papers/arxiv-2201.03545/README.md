# A ConvNet for the 2020s

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2201.03545)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：分层视觉 Transformer（如 Swin）重新引入了卷积的先验，才成为检测、分割的通用主干，但它的效果常被归功于 Transformer 本身。纯卷积网络在同样的配方下到底能做到多好？
- **核心方法**：从 ResNet-50 出发，逐步借用视觉 Transformer 的设计并记录每一步的效果：先只换成 Transformer 式训练配方，结构不变，ImageNet 就从 76.1% 升到 78.8%；再改阶段比例、切块式输入层、深度可分离卷积、倒瓶颈、7×7 大核、LayerNorm、GELU 等。得到的纯卷积 ConvNeXt 在相近计算量下，ImageNet 分类、COCO 检测、ADE20K 分割持平或超过 Swin；ImageNet-22K 预训练的 ConvNeXt-XL 在 384 分辨率下达到 87.8%。
- **为什么在这个库里**：[入门页](../../fields/visual-representation/README.md)主线第 6 个节点"对 ViT 的四种回答"之一，[Baseline 页](../../fields/visual-representation/BASELINES.md)"架构 = 现代化 CNN"与"训练配方"两行；[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md) 的主要证据；[DINOv3](../arxiv-2508.10104/README.md) 也蒸馏出 ConvNeXt 版本。自述局限：多模态学习中跨注意力可能更适合建模模态间的交互，Transformer 在离散、稀疏或结构化输出的任务上可能更灵活。代码已发布。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2201.03545（当前 v2，2022-03）· [全文 PDF](https://arxiv.org/pdf/2201.03545) · Facebook AI Research（FAIR）、UC Berkeley · CVPR 2022
- 方向：multimodal/visual-representation
