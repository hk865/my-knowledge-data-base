# Scaling Text-to-Image Diffusion Transformers with Representation Autoencoders

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.16208)

- **解决什么**：RAE（冻结表征编码器、训练重建解码器的表示自编码器）在 ImageNet 类条件生成上的收益，能否迁移到自由文本、复杂画面和文字渲染仍未确定。
- **核心方法**：扩大冻结 SigLIP 2（用图文匹配学习视觉语义）编码器对应解码器的数据与训练规模，检验 RAE 与 FLUX VAE（FLUX 文生图模型的变分自编码器）；保留维度相关噪声调度，同时重新检验宽扩散头与噪声增强解码的必要性。
- **为什么在这个库里**：是 [RAE](../arxiv-2510.11690/README.md)走向自由文本生成的直接后继，展示规模放大后哪些设计可以简化。优先级：选读。
