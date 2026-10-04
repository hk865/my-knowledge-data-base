# PointPillars: Fast Encoders for Object Detection from Point Clouds

> 状态：文献卡 · 2018 · [原文](https://arxiv.org/abs/1812.05784)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VoxelNet 每帧 225 ms（4.4 Hz），SECOND 达到 20 Hz 但仍保留昂贵的 3D 卷积，跟不上车载激光雷达的帧率。
- **核心方法**：用 PointNet 把点云按竖直柱体编码成伪图像，之后只用 2D 卷积。KITTI 鸟瞰检测 66.19 mAP（中等难度）、62 Hz，每帧 16.2 ms（1080Ti）。原文写明行人与骑车人常互相误分，行人易与电线杆、树干混淆；KITTI 只用前视相机视野内约 10% 的点，实车要处理整圈点云，嵌入式 GPU 吞吐可能更低。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 3 的激光雷达节点，[Baseline 页](../../fields/perception/BASELINES.md)几何一侧的参照。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1812.05784 · [全文 PDF](https://arxiv.org/pdf/1812.05784v2) · Alex H. Lang、Sourabh Vora、Holger Caesar、Lubing Zhou、Jiong Yang等（nuTonomy（APTIV））
- 发表：CVPR 2019
- 方向：robotics/perception
