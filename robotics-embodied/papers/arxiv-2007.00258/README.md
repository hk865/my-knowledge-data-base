# LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2007.00258)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LOAM 把数据存在全局体素地图里，难以加入回环与绝对测量，大场景会漂移，IMU 只是松耦合。
- **核心方法**：用 GTSAM 因子图紧耦合四类因子：IMU 预积分、激光里程计、GPS、回环；新关键帧只与固定数量的子关键帧局部地图配准。自采 Campus 数据集上 LOAM 终点误差 192.43 m，LIO-SAM 0.12 m；建图每帧 58.4 ms，LOAM 253.6 ms（只用 CPU）。原文写明回环只用欧氏距离检测，GPS 只修水平方向。
- **为什么在这个库里**：[Baseline 页](../../fields/localization-mapping/BASELINES.md)"估计器"一格的激光惯性代表，用来对照 FAST-LIO2 的滤波做法。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2007.00258 · [全文 PDF](https://arxiv.org/pdf/2007.00258v3) · Tixiao Shan、Brendan Englot、Drew Meyers、Wei Wang、Carlo Ratti等（MIT、Stevens Institute of Technology）
- 发表：IROS 2020
- 方向：robotics/localization-mapping
