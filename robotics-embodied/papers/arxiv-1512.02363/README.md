# On-Manifold Preintegration for Real-Time Visual-Inertial Odometry

> 状态：文献卡 · 2017 · [原文](https://arxiv.org/abs/1512.02363)

- **解决什么**：减少高频 IMU 在非线性优化中被反复积分的计算开销。
- **核心方法**：在旋转流形上把关键帧间 IMU 测量汇成相对运动约束，给出雅可比及事后偏置修正。
- **为什么在这个库里**：支撑离线短窗口数据包的预积分缓存设计。优先级：必读。
