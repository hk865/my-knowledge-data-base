# FAST-LIO2: Fast Direct LiDAR-inertial Odometry

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2107.06829)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：点云量大与机载算力矛盾；基于平滑度的特征提取在缺少大平面、长边或小视场固态激光雷达下特征太少。
- **核心方法**：在前作 FAST-LIO 的迭代 EKF 上去掉特征提取，原始点直接对地图做点到平面配准，用增量 k-d 树 ikd-Tree 维护地图，并在线标定激光-IMU 外参。19 条序列中 18 条最好，比 LIO-SAM 快约 10 倍，ARM 板上 10 Hz。原文写明地图超过 2000 m 后精度不再提升（漂移导致误配旧点），本身是纯里程计、没有回环。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 1 中滤波式激光惯性的代表。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2107.06829 · [全文 PDF](https://arxiv.org/pdf/2107.06829v1) · Wei Xu、Yixi Cai、Dongjiao He、Jiarong Lin、Fu Zhang（University of Hong Kong）
- 发表：未核实（arXiv 无 journal-ref）
- 方向：robotics/localization-mapping
