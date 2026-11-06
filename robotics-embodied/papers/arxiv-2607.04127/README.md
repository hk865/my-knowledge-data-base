# Real-Time LiDAR Gaussian Splatting SLAM

> 状态：技术精读 · 2026 · [原文](https://arxiv.org/abs/2607.04127)

[返回领域目录](../../README.md) · [技术精读](reading.md) · [来源记录](source.json)

- **解决什么**：在资源有限时将 LiDAR 定位与高斯几何建图耦合。
- **核心方法**：复用配准中的局部几何初始化高斯，并用高斯几何反馈后续配准。
- **为什么在这个库里**：参考高斯 SLAM 如何避免重复几何计算。
