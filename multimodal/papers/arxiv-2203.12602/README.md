# VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2203.12602)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视频 Transformer 离不开大规模图像预训练，从零训练效果差；视频帧冗余、帧间相关，按图像 MAE 的方式随机遮蔽时，被遮的块常能在相邻帧找到未遮的副本，模型学到的是难以泛化的捷径。
- **核心方法**：把 [MAE](../mae/README.md) 搬到视频：16 帧切成 2×16×16 的立方块，按"管道"遮蔽（所有帧遮同一位置），遮蔽率 90%–95%，编码器只处理可见块、解码器重建像素。ViT-B 在 SSv2 上 69.6%（从零训练 32.6%，ImageNet-21K 有监督预训练 61.8%）；只用 3.5k 段视频也能预训练。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 5 步、[Baseline 表](../../fields/video-temporal/BASELINES.md)"预训练信号 = 遮蔽像素重建"一格。作者自述 Kinetics 视频大多静止、与场景相关，时间建模的作用不明显；SSv2 上 42k 段视频预训练好于 24 万段 Kinetics 预训练（68.7% 对 68.5%），说明数据与目标任务的匹配比数量重要。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2203.12602 · [全文 PDF](https://arxiv.org/pdf/2203.12602) · 南京大学、腾讯 AI Lab、上海人工智能实验室
- 方向：multimodal/video-temporal、multimodal/visual-representation
- NeurIPS 2022（arXiv 注释）
