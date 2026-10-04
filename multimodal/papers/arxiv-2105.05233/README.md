# Diffusion Models Beat GANs on Image Synthesis

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2105.05233)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：扩散模型在 CIFAR-10 上已最好，在 LSUN、ImageNet 上仍不及 BigGAN-deep。作者假设差距来自两点：GAN 的结构被反复打磨过；GAN 能用多样性换保真度（例如截断），扩散模型没有对应的旋钮。
- **核心方法**：一轮 U-Net 结构消融（加深加宽、更多注意力头、在 32/16/8 三个分辨率加注意力、BigGAN 式残差块做上下采样、用时间步与类别调制组归一化的 AdaGN），再加分类器引导：在带噪图像上单独训练一个分类器，采样时用它对目标类别的梯度推动样本。ImageNet 256×256 类条件 FID 4.59，BigGAN-deep 为 6.95；128×128 为 2.97；只用 25 次前向即可追平 BigGAN-deep；与上采样扩散模型结合后 256×256 为 3.94。作者自述多步采样仍比 GAN 慢，分类器引导只适用于有标注的数据，并提出可以用带噪的 CLIP 按文字引导生成。代码公开。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 5 个节点，[Baseline 页](../../fields/generation/BASELINES.md)部件 3"主干"（U-Net 消融）与部件 6"分类器引导"两格。benchmark 主战场从 CIFAR-10 移到 ImageNet 类条件生成从这里开始；DiT 统计的像素空间 ADM 每次前向约 1120 Gflops，是潜空间方案要省掉的部分。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2105.05233 · [全文 PDF](https://arxiv.org/pdf/2105.05233) · OpenAI
- 方向：multimodal/generation
