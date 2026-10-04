# SlowFast Networks for Video Recognition

> 状态：文献卡 · 2018 · [原文](https://arxiv.org/abs/1812.03982)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：3D 卷积把时间和空间对称处理，但视频里类别语义（"手""人"）变化慢、动作（拍手、挥手）变化快；双流方法要预先算光流，两路结构也相同。
- **核心方法**：两条路径并行：Slow 路以低帧率、全通道看语义；Fast 路帧率高 α = 8 倍、通道只有 β = 1/8，约占总计算 20%，不做时间下采样；侧向连接把 Fast 的特征注入 Slow，端到端从原始像素训练、不用光流。Fast 路单独只有 51.7%，加到 Slow 上提升 3.0 个百分点；AVA 时空动作检测从 Slow-only 的 19.0 升到 24.2 mAP，拍手（+27.7 AP）、游泳（+27.4）等动态类别提升最大。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 3 步、[Baseline 表](../../fields/video-temporal/BASELINES.md)"时间算子 = 双速率"一格。它把"推理时用 100 多个视图的成本长期被忽视"写进正文；[LLaVA-Video](../arxiv-2410.02713/README.md) 的"慢帧多 token、快帧少 token"直接借用它的思路。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1812.03982 · [全文 PDF](https://arxiv.org/pdf/1812.03982) · Facebook AI Research（FAIR）
- 方向：multimodal/video-temporal
