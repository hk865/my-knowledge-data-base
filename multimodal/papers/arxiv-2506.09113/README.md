# Seedance 1.0: Exploring the Boundaries of Video Generation Models

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2506.09113)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：现有视频基础模型难以同时兼顾提示遵循、运动合理和画质，而且推理慢。
- **核心方法**：在扩散 Transformer + 流匹配的主流骨架上，把空间层与时间层解耦（空间层沿用 SD3 的 MMDiT 让文本与图像 token 双向交互），文本到视频与图像到视频联合训练并原生支持多镜头；后训练用三类奖励模型（基础、运动、美学）做 RLHF；再用多阶段蒸馏（含判别器）把推理加速约 10 倍。VAE 训练和蒸馏都用了判别器损失。
- **为什么在这个库里**：[观点页：生成收敛](../../../perspectives/generative-convergence.md)阶段四表中字节跳动 Seed 一行的依据，也是 [视觉生成领域页](../../fields/generation/README.md)"GAN 退为部件"的直接证据（VAE 与蒸馏中的判别器）；它把视频生成的竞争重心从结构转到后训练与加速。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2506.09113 · [全文 PDF](https://arxiv.org/pdf/2506.09113) · 字节跳动 Seed
- 方向：multimodal/generation、multimodal/video-temporal
