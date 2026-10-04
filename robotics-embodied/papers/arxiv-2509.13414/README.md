# MapAnything: Universal Feed-Forward Metric 3D Reconstruction

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2509.13414)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：[VGGT](../arxiv-2503.11651/README.md) 一类前馈重建只吃图像，输出没有公制尺度；机器人上往往还有相机内参、里程计或 IMU 给的位姿、深度传感器，这些几何信息前馈模型用不上。
- **核心方法**：Meta Reality Labs 与 CMU 的 Transformer（DINOv2 ViT-G 编码器 + 交替注意力），输入一张或多张图像，可选地加入内参、位姿、深度或部分重建；输出分解成每视图深度、局部射线图、相机位姿和一个全局公制尺度因子，尺度分支与几何分支之间阻断梯度。一个模型同时做 SfM、多视图立体、单目深度、相机定位和深度补全。作者表中，同样只给图像时多视图点图误差低于 VGGT；加入内参、位姿、深度后误差继续下降。作者写明不建模几何输入的噪声与不确定性，不处理动态运动与场景流，输入像素与输出逐一对应的设计限制了大场景应用。
- **为什么在这个库里**：[定位与建图方向](../../fields/localization-mapping/README.md)阶段 5"单目没有公制尺度"的另一种修法：[MASt3R-Fusion](../arxiv-2509.20757/README.md) 在后端加 IMU 与 GNSS 因子，MapAnything 把已有的几何量直接喂进前馈模型。3DV 2026。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2509.13414（Meta Reality Labs、Carnegie Mellon University，Keetha 等 17 位作者；当前 v3，2026-01-23；3DV 2026）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2509.13414) · [项目页](https://map-anything.github.io/)
- 方向：[定位与建图](../../fields/localization-mapping/README.md)（另见[感知](../../fields/perception/README.md)）
