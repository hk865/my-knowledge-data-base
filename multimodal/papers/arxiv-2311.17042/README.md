# Adversarial Diffusion Distillation

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.17042)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：扩散模型的迭代采样步数多，阻碍实时应用；GAN 一步出图，但扩到大数据集后样本质量常不及扩散模型。
- **核心方法**：把预训练扩散模型（例如 SDXL）蒸馏成 1–4 步的学生：一路用分数蒸馏，以冻结的教师扩散模型给出去噪目标；一路用判别器损失，判别器建在冻结的 DINOv2 ViT-S 特征上，并以文本与图像为条件。人评中单步 ADD-XL 胜过 4 步的 LCM-XL，4 步在多数比较中胜过 50 步的 SDXL 教师。作者自述与观察：真实感提升以多样性略降为代价；单步时人评仍不及 50 步 SDXL；FID 与人评不一致（SDXL 的 FID 更高，人评的画质与对齐却更好）。代码与权重公开。
- **为什么在这个库里**：[Baseline 页](../../fields/generation/BASELINES.md)部件 5"对抗蒸馏"一格，GAN 判别器以部件身份回到主流的直接证据；与 [Seedance 1.0](../arxiv-2506.09113/README.md) 的多阶段蒸馏、[Genie 2](../genie-2-blog/README.md) 的蒸馏实时版（画质下降）对照着读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2311.17042 · [全文 PDF](https://arxiv.org/pdf/2311.17042) · Stability AI
- 方向：multimodal/generation
