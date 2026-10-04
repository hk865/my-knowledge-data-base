# Video Diffusion Models

> 状态：技术精读 · 2022 · [原文](https://arxiv.org/abs/2204.03458)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：DDPM 已让扩散在图像上追平 GAN，此前的视频生成主要用自回归、VAE、GAN 和流模型。把扩散搬到视频有两个困难：加速器内存一次只够训练约 16 帧；生成更长或更清晰的视频需要条件生成，为每种条件单独训练一个模型成本高。
- **核心方法**：扩散形式基本照搬 DDPM（改为连续时间与余弦日程），把一整块 16 帧视频一起加噪、去噪，增量在三处：图像 U-Net 改成时空分解的 3D U-Net，卷积和空间注意力只在帧内做，另插只沿帧轴的时间注意力；屏蔽时间注意力后同一网络就是图像模型，于是可以图像–视频联合训练；用重建引导（一句话：沿"让模型能重建已知部分"的梯度修正其余部分）从无条件模型做条件采样。每段视频加 8 张单帧，验证 FVD（生成视频与真实视频在 I3D 特征空间里的分布距离，越低越好）从 205.42 降到 60.72（表 4）；16 帧模型延长到 64 帧时，重建引导为 134.55，旧的替换法为 436.16（表 6）。
- **为什么在这个库里**：[视觉生成方向 Baseline 页](../../fields/generation/BASELINES.md)中部件 3"时空分解 3D U-Net"、部件 4"v 预测"、部件 5"预测–校正"与部件 8"整块视频联合去噪 + 分块延长"几格的代表，[入门页](../../fields/generation/README.md)阅读顺序第 4 篇。后来的视频模型逐个替换了它的部件，留下的是图像–视频联合训练与整块联合去噪，这条线也接到[视频与时序方向](../../fields/video-temporal/README.md)。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：时空分解 3D U-Net 与重建引导；"局限与后续"对照 Imagen Video、HunyuanVideo、Wan、Seedance 的选择
- [本篇图解与说明](figures/README.md)

## 可选的阅读顺序

[Denoising Diffusion Probabilistic Models](../ddpm/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2204.03458 · Google（论文首页只给出 google.com 邮箱）
- 年份：2022
- [官方原文页面](https://arxiv.org/abs/2204.03458)
- [官方全文入口](https://arxiv.org/pdf/2204.03458v2)
- 阅读版本：v2
- 方向：multimodal/generation、multimodal/video-temporal
