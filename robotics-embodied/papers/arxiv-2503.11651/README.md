# VGGT: Visual Geometry Grounded Transformer

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.11651)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多视图重建依赖逐场景优化，速度慢。
- **核心方法**：一个前馈 Transformer 一次从一到数百张图直接输出相机参数、深度图、点图和三维轨迹，坐标系取第一台相机。H100 上 100 帧 3.12 s、21.15 GB 显存，200 帧 8.75 s、40.63 GB。原文写明不支持鱼眼与全景图，极端旋转下性能下降，大的非刚性形变会失败。
- **为什么在这个库里**：[Baseline 页](../../fields/localization-mapping/BASELINES.md)"前端 → 前馈多视图模型"一格；VGGT-SLAM、VGGT-Long 都从它的显存帧数上限出发。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2503.11651 · [全文 PDF](https://arxiv.org/pdf/2503.11651v1) · Jianyuan Wang、Minghao Chen、Nikita Karaev、Andrea Vedaldi、Christian Rupprecht等（Oxford VGG、Meta AI）
- 发表：CVPR 2025
- 方向：robotics/localization-mapping
