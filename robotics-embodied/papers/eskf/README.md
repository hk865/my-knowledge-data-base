# Quaternion kinematics for the error-state Kalman filter

> 状态：技术精读 · 2017 · [原文](https://arxiv.org/abs/1711.02508)

[返回机器人与具身目录](../../README.md)

- **解决什么**：IMU 驱动的状态估计里，姿态活在三维旋转群上：直接对四元数或旋转矩阵做卡尔曼滤波会碰到约束、奇异，以及左乘右乘、局部全局扰动等约定混乱，实现很难逐项核对。
- **核心方法**：这是教程而不是新方法：系统整理四元数与旋转的约定、旋转群的李结构、旋转扰动、导数与积分，再导出误差状态卡尔曼滤波（ESKF，一句话：大运动由名义状态积分，小误差在三维切空间里用卡尔曼滤波估计）的完整链条：名义状态传播、误差协方差传播、观测更新、注入、重置，并给出局部误差与全局误差两套成套公式。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向的数学底座；[ORB-SLAM3](../orb-slam3/README.md) 的视觉惯性部分、[学习 IMU 零偏](../arxiv-2505.06748/README.md)这类工作的公式，都可以对照它核对约定。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:1711.02508（Joan Solà；v1，2017-11）
- 全文：[arXiv PDF v1](https://arxiv.org/pdf/1711.02508v1)
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)（另见[感知与传感器](../../fields/perception/README.md)、[运动控制与腿足运动](../../fields/control-locomotion/README.md)）
