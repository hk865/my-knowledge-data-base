# Is Space-Time Attention All You Need for Video Understanding?

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2102.05095)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：卷积核只看局部时空邻域，超出感受野的依赖要靠层层聚合；深层 3D CNN 在高分辨率、长视频上训练很贵。能否完全用自注意力搭视频模型。
- **核心方法**：TimeSformer 把 ViT 扩到视频：每帧切 16×16 的块；每个 Transformer 块里先做时间注意力（只看其他帧同一位置的块），再做空间注意力（只看本帧的块），每个块要比较的对象从 NF + 1 个降到 N + F + 2 个（N 为每帧块数，F 为帧数）。K400 78.0%，视频训练 416 V100 小时（SlowFast 用 3840 小时达 75.6%）；只做空间注意力时 K400 仍有 76.9%，SSv2 只有 36.6%（分开时空注意力为 59.5%）。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 4 步、[Baseline 表](../../fields/video-temporal/BASELINES.md)"时间算子 = 分开的时空注意力"一格。只做空间注意力的对照是"Kinetics 几乎不需要时间、SSv2 离不开时间"最干净的证据；视频生成模型的"空间层与时间层解耦"是同一种分解。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2102.05095 · [全文 PDF](https://arxiv.org/pdf/2102.05095) · Facebook AI、Dartmouth College
- 方向：multimodal/video-temporal
- ICML 2021（arXiv 注释）
