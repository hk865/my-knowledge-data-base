# GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction

> 状态：技术精读 · 2025 · [原文](https://arxiv.org/abs/2503.10170)

[返回领域目录](../../README.md) · [技术精读](reading.md) · [来源记录](source.json)

- **解决什么**：在自由轨迹下联合恢复可渲染场景和精确表面。
- **核心方法**：先以 LiDAR 训练 SDF，再让二维高斯面片整体贴近连续表面，并以图像监督外观。
- **为什么在这个库里**：为 LiDAR 几何与高斯重建结合提供参考。
