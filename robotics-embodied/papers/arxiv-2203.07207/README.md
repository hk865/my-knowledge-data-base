# A Self-Supervised, Differentiable Kalman Filter for Uncertainty-Aware Visual-Inertial Odometry

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2203.07207)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：滤波或优化式 VIO 在剧烈光照变化、快速运动、低纹理图像下容易发散；纯学习式 VIO 在正常条件下又不如经典方法。
- **核心方法**：把两者接成可微卡尔曼滤波器：过程模型由 IMU 驱动，观测模型是神经网络给出的相对位姿及其不确定性，整个滤波器端到端训练，损失是自监督的（不需要真值位姿），比类似的监督方法更好，还能在线再训练。在人为退化的 EuRoC 序列上，经典估计器持续发散的情况下本方法精度没有明显下降；借助 IMU 的度量信息还能恢复场景尺度，这是其他单目自监督 VIO 做不到的。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向「学习 + 滤波」混合路线的代表，回答「网络放在滤波器的哪个位置」：这里网络只替换观测模型，过程模型与不确定性传播仍由卡尔曼滤波完成。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2203.07207
- 作者：Brandon Wagstaff、Emmett Wise、Jonathan Kelly
- 全文：[arXiv PDF](https://arxiv.org/pdf/2203.07207)
- 发表：AIM 2022（arXiv 注释）
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)
