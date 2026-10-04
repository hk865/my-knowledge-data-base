# VGGT-SLAM 2.0: Real-time Dense Feed-forward Scene Reconstruction

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.19887)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VGGT-SLAM 的 15 自由度对齐在回环之间快速漂移、使场景严重变形，在平面场景中退化，因子图只估计子图间单应。
- **核心方法**：放弃 SL(4)：利用重叠帧必须有相同位姿与内参这一约束，只解标定对齐和一个尺度；发现 VGGT 某一层的注意力可免训练地用于回环验证，既拒绝误匹配、又补出更多回环。TUM 不标定时 0.041 m（v1 为 0.053 m）；RTX 3090 上 8.4 fps，接入 CLIP 开放集检测时 6.3 fps，Jetson Thor 上 3.5 fps。原文写明白墙等无纹理场景会发散，后端只优化位姿不优化点。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 5 中同一团队修自家 v1 的例子。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2601.19887 · [全文 PDF](https://arxiv.org/pdf/2601.19887v2) · Dominic Maggio、Luca Carlone（MIT LIDS）
- 发表：RSS 2026（官方 GitHub）
- 方向：robotics/localization-mapping
