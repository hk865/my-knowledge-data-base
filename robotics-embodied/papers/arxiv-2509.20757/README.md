# MASt3R-Fusion: Integrating Feed-Forward Visual Model with IMU, GNSS for High-Functionality SLAM

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2509.20757)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：前馈点图流水线丢掉了概率多传感器融合的优势；纯视觉方法有尺度歧义，在视觉退化环境中性能下降。
- **核心方法**：把 MASt3R 两视图回归得到的 Sim(3) 视觉约束以 Hessian 形式放进公制尺度的 SE(3) 因子图，分层为实时滑窗 VIO 与带回环和 GNSS 的全局层。KITTI-360 带回环的全局误差为轨迹长度的 0.05%，ORB-SLAM3 0.63%，VGGT-Long 2.91%；原文称 8 GB 显存可处理任意长序列。原文没有专门的局限节，§III-B 指出大尺度户外长时间前向运动时远近深度的不确定性带来显著误差。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 5 中"给前馈前端补公制尺度"的代表，也是学习式前端与概率估计器结合的开放问题入口。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2509.20757 · [全文 PDF](https://arxiv.org/pdf/2509.20757v3) · Yuxuan Zhou、Xingxing Li、Shengyu Li、Zhuohao Yan、Chunxi Xia等（武汉大学测绘学院）
- 发表：未见正式发表
- 方向：robotics/localization-mapping
