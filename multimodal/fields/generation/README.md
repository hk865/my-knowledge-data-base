# 视觉生成 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

视觉生成学习从条件与随机性产生图像或视频。扩散模型将生成分解为一系列去噪步骤；理解它需要把前向加噪、训练目标与反向采样区分开。

## 一个容易混淆的边界

重建示例或生成视频不是对真实未来的可靠预测。生成质量、条件遵循与物理一致性需要各自的评估。

## 入门任务

先用单个带噪样本说明DDPM的预测目标，再检查条件输入怎样改变采样过程。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/17-diffusion.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [Denoising Diffusion Probabilistic Models](../../papers/ddpm/README.md)
2. [Video Diffusion Models](../../papers/video-diffusion/README.md)
