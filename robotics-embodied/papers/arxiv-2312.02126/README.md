# SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2312.02126)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：显式表示的跟踪依赖丰富的几何特征与高帧率，隐式神经表示计算低效、难编辑、有灾难性遗忘，逐光线采样又限制了效率。
- **核心方法**：用各向同性的 3D 高斯作地图，通过可微溅射对全部像素计算光度与深度损失，并用渲染出的轮廓掩码决定跟踪用哪些像素、在哪里新增高斯。低纹理的 ScanNet++ 上误差 1.2 cm，ORB-SLAM3 因缺特征反复重新初始化、误差 158.2 cm；TUM 上 5.48 cm，ORB-SLAM2 为 1.98 cm。每帧跟踪约 1 秒、建图约 1.4 秒（3080 Ti）；原文写明对运动模糊、大深度噪声和激进旋转敏感，需要已知内参和稠密深度。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 4 的 3DGS 节点，低纹理场景"站在现在看过去"表的证据。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2312.02126 · [全文 PDF](https://arxiv.org/pdf/2312.02126v3) · Nikhil Keetha、Jay Karhade、Krishna Murthy Jatavallabhula、Gengshan Yang、Sebastian Scherer等（CMU、MIT）
- 发表：CVPR 2024
- 方向：robotics/localization-mapping
