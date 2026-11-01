# FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual Odometry

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2408.14035)

- **解决什么**：让相机、LiDAR 与 IMU 在实时计算预算内共同估计自身运动。
- **核心方法**：在统一体素地图上构造点云几何与图像光度约束，以误差状态迭代卡尔曼滤波顺序更新状态。
- **为什么在这个库里**：作为动态可靠性研究的同基座对照，先保留估计器，再替换观测可靠性模块。优先级：必读。

[官方代码](https://github.com/hku-mars/FAST-LIVO2)
