# Taming Transformers for High-Resolution Image Synthesis

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2012.09841)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Transformer 没有局部性归纳偏置，计算量随序列长度平方增长，直接在像素上建模高分辨率图像算不起；此前在离散码上做自回归的方法只用很浅的量化，序列很长。
- **核心方法**：两阶段。先训练 VQGAN：卷积编码器把图像压成离散码本里的编号，重建损失由 L2 换成感知损失，并加一个局部块判别器做对抗训练，让码本在高压缩率下保住感知上重要的局部结构；再用 Transformer 自回归地预测这些编号，生成大图时用滑动窗口注意力。下采样倍数 f = 16 时一张 256×256 图只有 16×16 = 256 个 token（DALL·E 为 1024，VQVAE-2 为 5120）；f 小于 16 时生成的人脸结构不连贯，大于 16 时重建误差严重，作者写明重建能力是可达质量的上界。ImageNet 256×256 类条件 FID 15.78（不用拒绝采样），对照 ADM-G 4.59、BigGAN-deep 6.84；按分类器打分只保留 5% 的样本后为 5.20。代码与预训练模型公开。
- **为什么在这个库里**：[Baseline 页](../../fields/generation/BASELINES.md)部件 2"离散 token"一格的标准分词器。它的"感知损失 + 局部块判别器"自编码器训练法被同一团队直接用于 [LDM](../arxiv-2112.10752/README.md)（LDM 第 3.1 节引用），后来的视频 VAE（[Seedance 1.0](../arxiv-2506.09113/README.md)）也加判别器：这是 GAN 以部件身份留下来的主要路径。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2012.09841 · [全文 PDF](https://arxiv.org/pdf/2012.09841) · Heidelberg University IWR（Heidelberg Collaboratory for Image Processing）
- 名称：通称 VQGAN
- 方向：multimodal/generation
