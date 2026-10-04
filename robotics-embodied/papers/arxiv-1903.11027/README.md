# nuScenes: A multimodal dataset for autonomous driving

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1903.11027)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：缺少带完整 360° 多传感器配置（相机、雷达、激光雷达）的自动驾驶感知数据集与评测。
- **核心方法**：1000 个 20 秒场景、5.5 小时、140 万个 3D 框；6 相机、5 雷达、1 台 32 线 20 Hz 激光雷达，相机曝光在激光雷达扫过相机视场中心时触发；定义 NDS，一半看检测 mAP，一半看位置、尺寸、朝向、速度和属性的误差。测试集上 PointPillars 为 NDS 45.3，纯图像的 MonoDIS 为 38.4。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)"用什么衡量进展"中 benchmark 从 KITTI 迁移到全向多传感器的节点；BEVFusion 的主要评测集。优先级：存档。

## 身份信息

- 稳定标识：arxiv:1903.11027 · [全文 PDF](https://arxiv.org/pdf/1903.11027) · Holger Caesar、Varun Bankiti、Alex H. Lang、Sourabh Vora、Venice Erin Liong等 10 人（nuTonomy（APTIV））
- 发表：CVPR 2020（arXiv comments，v5）
- 方向：robotics/perception
