# Gaussian Splatting SLAM

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2312.06741)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：稀疏 SLAM 的地图主要只能用于定位；网格占内存、分辨率有限，面元不连续，神经场需要昂贵的逐像素光线投射。
- **核心方法**：以 3D 高斯溅射为唯一表示做单目（也可 RGB-D）SLAM，推导位姿对高斯的李群解析雅可比用于直接跟踪，并用各向同性正则和几何校验控制高斯数量。TUM 单目无回环平均 3.96 cm（DROID-VO 7.73、DSO 11.0），渲染 769 FPS；约 3 fps。原文写明只在房间尺度测试、大场景漂移不可避免、没有回环；EuRoC 困难长序列 MH03–05 误差 2.2–4.5 m，ORB-SLAM3 为 0.02–0.09 m。补充实验显示 ORB-SLAM 位姿加离线 3DGS 的渲染指标与它没有显著差别。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 4 的单目 3DGS 节点，Imperial 稠密表示路线的一环。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2312.06741 · [全文 PDF](https://arxiv.org/pdf/2312.06741v2) · Hidenobu Matsuki、Riku Murai、Paul H. J. Kelly、Andrew J. Davison（Imperial College London）
- 发表：CVPR 2024 Highlight
- 方向：robotics/localization-mapping
