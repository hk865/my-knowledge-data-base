# Learned IMU Bias Prediction for Invariant Visual Inertial Odometry

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2505.06748)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：视觉惯性里程计（VIO，一句话：融合相机与 IMU 估计位置、速度和姿态）用不变扩展卡尔曼滤波（invariant EKF，一句话：利用位姿与速度的李群结构，使误差传播不依赖当前估计值）可以改善收敛和鲁棒性，但 IMU 零偏一放进滤波状态，就破坏了这种李群对称性。
- **核心方法**：不再把零偏当作滤波状态去估计，而是训练一个神经网络，从过去一段 IMU 读数直接预测零偏，滤波器因此保持不变形式；滤波器本体是不变的 MSCKF（一句话：把最近若干帧相机位姿放进状态、用多帧共视特征做更新的滤波器）。实机实验中，视觉长时间缺失、只能依赖 IMU 时，估计仍然稳健。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向里"零偏怎样建模"这一处的学习化改动，与库内的 [EqVIO](../arxiv-2205.01980/README.md)、[PLV-IEKF](../arxiv-2311.04477/README.md) 同属利用对称性的滤波一支；对照 [ESKF 教程](../eskf/README.md)中把零偏放进误差状态的标准做法读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2505.06748（Altawaitan、Stanley、Ghosal、Duong、Atanasov；当前 v2，2025-10；arXiv 注明已投 IEEE）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2505.06748)
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)
