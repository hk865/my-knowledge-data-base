# Revisiting Feature Prediction for Learning Visual Representations from Video

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.08471)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：检验"预测特征"能否单独作为从视频无监督学习的目标：不用预训练图像编码器、文本、负样本、像素重建或任何人工标注。
- **核心方法**：V-JEPA：从视频中遮掉大块连续的时空区域（平均遮蔽约 90%），预测器根据可见部分，在另一个编码器（参数取滑动平均、不回传梯度）给出的特征空间里预测被遮区域的表示，用 L1 损失；在约 200 万段公开视频（VideoMix2M）上训练，评测时冻结主干、只训练注意力探针。ViT-H/16 冻结评测 K400 82.0%、SSv2 71.4%；图像模型 DINOv2 在 K400 上 83.4% 反而更高，在 SSv2 上只有 50.6%。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 5 步、[Baseline 表](../../fields/video-temporal/BASELINES.md)"预训练信号 = 特征预测"一格；后续 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) 在它之上加动作条件预测器做机器人规划。消融里"只用前几帧预测后面"（因果遮蔽）的特征不如在整段视频中遮块，VideoMAE 式管道遮蔽配特征预测效果最差。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2404.08471 · [全文 PDF](https://arxiv.org/pdf/2404.08471) · Meta FAIR、Inria、ENS、Université Gustave Eiffel、NYU
- 方向：multimodal/video-temporal、multimodal/visual-representation、multimodal/world-models
- 通称 V-JEPA；与 2025 年的 V-JEPA 2 是两篇论文
