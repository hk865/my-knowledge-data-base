# Dynamic-LIVO: A Dynamic-Aware LiDAR-Inertial-Visual Odometry System Using Spatio-Temporal Normals

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.19336)

- **解决什么**：在动态环境中避免运动物体污染 LIVO 位姿估计和静态彩色地图。
- **核心方法**：通过时空法向量识别运动点，将分类共享给 LiDAR 与视觉更新；对观测不足的点延迟判定。
- **为什么在这个库里**：作为同传感器模态、同基座附近的几何动态剔除对照。优先级：必读。
