# Dynamic Visual SLAM using a General 3D Prior

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.06868)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：场景中的动态物体会严重破坏相机位姿估计；离线重建方法 MegaSaM 在 16 GB 显存内处理不完整序列。
- **核心方法**：以 DPV-SLAM 的块级 BA 为骨架，在前馈 3D 模型 π³ 上加运动物体分割头，剔除动态区域，并用它的深度预测按不确定度加强 BA。Bonn RGB-D Dynamic 上平均 2.20 cm，DROID-SLAM 4.91 cm，DynaSLAM 6.45 cm。原文写明每帧都要做多帧前馈推理，在 RTX 5000 上只有 2 fps。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)"动态物体"一行的最新修补。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2512.06868 · [全文 PDF](https://arxiv.org/pdf/2512.06868v1) · Xingguang Zhong、Liren Jin、Marija Popović、Jens Behley、Cyrill Stachniss（University of Bonn、TU Delft、Lamarr Institute）
- 发表：未见正式发表
- 方向：robotics/localization-mapping
