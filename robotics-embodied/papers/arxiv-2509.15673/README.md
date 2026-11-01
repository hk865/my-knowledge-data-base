# Omni-LIVO: Robust RGB-Colored Multi-Camera Visual-Inertial-LiDAR Odometry via Photometric Migration and ESIKF Fusion

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2509.15673)

- **解决什么**：扩大视觉覆盖范围，并在图像质量变化时调节视觉融合贡献。
- **核心方法**：扩展 FAST-LIVO2 的多相机直接对齐；公开实现根据各相机的光度残差及观测数调整视觉协方差。
- **为什么在这个库里**：提供相机级规则调权的强基线，用来检验学习观测级可靠性是否必要。优先级：必读。

[官方代码](https://github.com/elon876/Omni-LIVO)
