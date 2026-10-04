# A Multi-State Constraint Kalman Filter for Vision-aided Inertial Navigation

> 状态：文献卡 · 2007 · [原文](https://www-users.cse.umn.edu/~stergios/papers/ICRA07-MSCKF.pdf)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：相机加 IMU 的实时导航：EKF-SLAM 要维护相机位姿与数千个特征的相关性，计算量随特征数平方增长。
- **核心方法**：状态只保留 IMU 状态和滑窗内最多 Nmax 个相机位姿克隆，特征不进状态；一个特征的轨迹结束后先三角化，再把残差投影到消掉特征误差的方向上做 EKF 更新，复杂度对特征数线性。车载 3.2 km、1598 帧上终点误差约 10 m（行驶距离的 0.31%，由地图推算，无 GPS 真值），单核 14 Hz。原文写明多数特征只能跟踪几帧，运动平行光轴，车辆、行人、树叶靠马氏距离检验剔除，没有回环。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)滤波路线的起点，[Baseline 页](../../fields/localization-mapping/BASELINES.md)中滤波式基线之一；后来的 OpenVINS、EqVIO、PLV-IEKF、学习式 IMU 偏置预测都以它为骨架或对照，它的不一致问题由 FEJ 与不变滤波修正。优先级：必读。

## 身份信息

- 稳定标识：url:https://www-users.cse.umn.edu/~stergios/papers/ICRA07-MSCKF.pdf · [全文 PDF](https://www-users.cse.umn.edu/~stergios/papers/ICRA07-MSCKF.pdf) · Anastasios I. Mourikis、Stergios I. Roumeliotis（University of Minnesota）
- 发表：ICRA 2007（据其他论文的参考文献，PDF 页面未印会议名）
- 方向：robotics/localization-mapping
