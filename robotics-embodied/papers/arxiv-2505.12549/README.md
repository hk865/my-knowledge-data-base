# VGGT-SLAM: Dense RGB SLAM Optimized on the SL(4) Manifold

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2505.12549)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VGGT 一次能处理的帧数受显存限制（RTX 4090 约 60 帧）；不标定时前馈重建存在射影歧义，用相似变换对齐子图不够。
- **核心方法**：用 VGGT 对关键帧窗口生成子图，相邻子图之间估计 15 自由度单应，在 SL(4) 流形上做因子图优化并加回环。TUM 不标定时 0.053 m，MASt3R-SLAM 0.060 m，DROID-SLAM 0.158 m；7-Scenes 上与 MASt3R-SLAM 持平。原文写明平面点下单应估计退化（TUM floor 序列不稳定），对外点敏感，回环间隔长时漂移还包括透视。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 5 表中的一行；它的平面退化与漂移由 VGGT-SLAM 2.0 修正。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2505.12549 · [全文 PDF](https://arxiv.org/pdf/2505.12549v2) · Dominic Maggio、Hyungtae Lim、Luca Carlone（MIT）
- 发表：NeurIPS 2025（官方 GitHub）
- 方向：robotics/localization-mapping
