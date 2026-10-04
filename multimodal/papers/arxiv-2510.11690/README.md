# Diffusion Transformers with Representation Autoencoders

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.11690)

- **解决什么**：潜空间扩散沿用重建型 VAE，语义弱、潜空间维度受限；换成表征编码器后又面临高维扩散训练问题。
- **核心方法**：冻结 DINO、SigLIP 或 MAE 等表征编码器，训练解码器组成表示自编码器 RAE，再调整噪声尺度与扩散网络以适应高维语义潜空间。
- **为什么在这个库里**：连接 [视觉表征](../../fields/visual-representation/README.md)与[视觉生成](../../fields/generation/README.md)，让“理解用的特征”成为生成空间。优先级：必读。
