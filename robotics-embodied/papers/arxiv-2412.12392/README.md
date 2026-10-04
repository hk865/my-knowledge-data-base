# MASt3R-SLAM: Real-Time Dense SLAM with 3D Reconstruction Priors

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.12392)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：SLAM 还不是即插即用的算法，需要硬件经验与标定；单视图深度先验有歧义、跨视角不一致。
- **核心方法**：以双视图 3D 重建先验 MASt3R 为前端：点图迭代投影匹配、基于射线误差的跟踪、局部融合、检索回环和 Sim(3) 二阶全局优化，对相机只假设有唯一光心。TUM 上标定时 0.030 m（DROID-SLAM 0.038 m），不标定时 0.060 m；约 15 fps（RTX 4090）。原文写明全局优化不精化全部几何，MASt3R 只在针孔图像上训练、畸变越大越差，全分辨率解码器是瓶颈；EuRoC 上 0.041 m 输给 DROID-SLAM。VGGT-Long 报告它在 KITTI 上约 100 帧后跟丢。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 5 的起点，前馈 3D 先验当前端的第一个实时系统。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2412.12392 · [全文 PDF](https://arxiv.org/pdf/2412.12392v2) · Riku Murai、Eric Dexheimer、Andrew J. Davison（Imperial College London）
- 发表：CVPR 2025 Highlight
- 方向：robotics/localization-mapping
