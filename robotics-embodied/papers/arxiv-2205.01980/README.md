# EqVIO: An Equivariant Filter for Visual Inertial Odometry

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2205.01980)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：标准 EKF 式 VIO 存在不一致性（一句话：滤波器报告的协方差小于实际误差，即过度自信）和较大的线性化误差。
- **核心方法**：为 VIO 问题构造一个新的李群对称性，并套用等变滤波器（EqF，一句话：利用系统的对称性选择误差坐标，使误差动力学的线性化更准确的一类滤波器）。这一对称性与 VIO 参考系的不变性相容，带来更好的一致性；无偏置的 IMU 动力学是群仿射的，线性化误差只取决于偏置估计误差和测量噪声；视觉测量对该对称性等变，可以用更高阶的输出近似减小更新方程中的近似误差。在 EuRoC 与 UZH FPV 数据集上，速度和精度都优于其他先进 VIO。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向「滤波器几何结构」一支：用对称性而不是更多传感器去改善一致性，可与同从不变性出发的 [PLV-IEKF](../arxiv-2311.04477/README.md)、[学习 IMU 偏置的不变 VIO](../arxiv-2505.06748/README.md) 对照。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2205.01980
- 作者：Pieter van Goor、Robert Mahony
- 全文：[arXiv PDF](https://arxiv.org/pdf/2205.01980)
- 发表：IEEE Transactions on Robotics, vol. 39, no. 5, 2023（arXiv 期刊信息）
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)
