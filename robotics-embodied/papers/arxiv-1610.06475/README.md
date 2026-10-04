# ORB-SLAM2: an Open-Source SLAM System for Monocular, Stereo and RGB-D Cameras

> 状态：文献卡 · 2016 · [原文](https://arxiv.org/abs/1610.06475)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：单目 SLAM 有尺度漂移，探索中纯旋转会失败，初始化需要多视图。
- **核心方法**：在 ORB-SLAM 上加双目与 RGB-D：区分近点与远点（40 倍基线为界），回环后在单独线程做全局 BA，并提供只定位不建图的模式。原文写明 EuRoC V2_03 因严重运动模糊跟丢、KITTI 09 末尾的回环未检出；TUM 对比中补偿了 fr2 深度 4% 的尺度偏差，作者承认这可能部分解释了它更好的结果。
- **为什么在这个库里**：[Baseline 页](../../fields/localization-mapping/BASELINES.md)"传感器配置"一格；后来的稠密与学习式 SLAM 在 TUM 上最常引用的对照。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1610.06475 · [全文 PDF](https://arxiv.org/pdf/1610.06475v2) · Raúl Mur-Artal、Juan D. Tardós（Universidad de Zaragoza I3A）
- 发表：IEEE T-RO 2017
- 方向：robotics/localization-mapping
