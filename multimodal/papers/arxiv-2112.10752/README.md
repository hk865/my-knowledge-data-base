# High-Resolution Image Synthesis with Latent Diffusion Models

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2112.10752)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：像素空间扩散训练常需 150–1000 个 V100 日，在一张 A100 上采样 5 万张约要 5 天；而大部分计算花在肉眼几乎看不出的细节上。
- **核心方法**：两阶段：先训练一个自编码器（感知损失加局部块判别器，轻度 KL 或 VQ 正则；第 3.1 节写明基于 VQGAN）把图像压到低维潜空间，再在潜空间里训练扩散模型；U-Net 仍以二维卷积为主，加交叉注意力接入文本、布局等条件。下采样倍数 f 是关键旋钮：同样训练 200 万步后，像素扩散（f = 1）与 f = 8 的 FID 相差 38，f 过大则压缩丢信息、质量停滞，f = 4 和 8 最均衡。ImageNet 类条件 LDM-4-G FID 3.60（用系数 1.5 的无分类器引导）；在 LAION-400M 上训练了 1.45B 参数的文本到图像模型。作者自述顺序采样仍比 GAN 慢；需要像素级精度时自编码器的重建会成为瓶颈，超分辨率模型已受此限制。代码与预训练模型公开。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 6 个节点，[Baseline 页](../../fields/generation/BASELINES.md)现代配方中"潜空间"部件的出处；[DiT](../arxiv-2212.09748/README.md) 直接用它的 VAE，并把它作为 Stable Diffusion 的出处引用。Rombach、Blattmann、Esser 后来在 Stability AI 写了 [SD3](../arxiv-2403.03206/README.md) 与 [ADD](../arxiv-2311.17042/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2112.10752 · [全文 PDF](https://arxiv.org/pdf/2112.10752) · LMU Munich 与 Heidelberg University IWR、Runway ML · CVPR 2022
- 方向：multimodal/generation
