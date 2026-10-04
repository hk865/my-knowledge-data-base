# cuVSLAM: CUDA accelerated visual odometry and mapping

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2506.04359)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：机器人的传感器组合千差万别（1 到 32 个相机、有没有深度、有没有 IMU），SLAM 还要在 Jetson 这类边缘设备上实时运行、只占很少一部分算力。
- **核心方法**：NVIDIA 用 CUDA 实现一套经典视觉 SLAM：前端是 Shi-Tomasi 角点加金字塔 Lucas-Kanade 光流跟踪（每一层用归一化互相关验证），局部是异步的滑窗稀疏 BA，全局是位姿图优化加回环；多相机之间用"视锥相交图"自动找重叠视野。Jetson AGX Orin 上双目每帧 1.8 ms、双目惯性 3.8 ms；作者表中 EuRoC 双目、KITTI 上的相对平移误差略低于 ORB-SLAM3（0.17% 对 0.21%、0.27% 对 0.31%）。作者写明多双目需要硬件同步；快速六自由度运动（TartanAir V2 Hard）误差变大；720p 单目加深度模式在 Orin 上 37.7 ms，超过 30 fps 的帧间隔。
- **为什么在这个库里**：[定位与建图方向](../../fields/localization-mapping/README.md)的工业界参照：NVIDIA 在 GR00T N1.6 的仿真到真机流程（2026-01 技术博客）里用的定位栈是 cuVSLAM 加 cuVGL 全局定位、[FoundationStereo](../arxiv-2501.09898/README.md) 深度和 nvblox，也就是产品一侧仍选"特征法 + BA + 位姿图"，前馈 3D 模型还在研究一侧。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2506.04359（NVIDIA，Korovko、Slepichev 等 8 位作者；当前 v3，2025-07-08）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2506.04359)
- 方向：[定位与建图](../../fields/localization-mapping/README.md)
