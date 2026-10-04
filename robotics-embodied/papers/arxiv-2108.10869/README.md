# DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2108.10869)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：现有 SLAM 鲁棒性不足，失败形式包括特征轨迹丢失、优化发散和漂移累积；此前的深度 SLAM 缺少回环与全局 BA。
- **核心方法**：在光流网络 RAFT 上把"迭代更新光流"改成"迭代更新所有像素的深度与相机位姿"，每一步由可微稠密 BA 层完成；后端在全部关键帧上做全局 BA 并加长程边实现回环；只用合成数据 TartanAir 单目训练。TUM fr1 的 9 条单目序列上 ORB-SLAM2 失败 6 条、ORB-SLAM3 失败 5 条，DROID-SLAM 全部成功；EuRoC 单目只比较 ORB-SLAM3 成功的序列时误差低 43%。原文写明资源需求是最大局限：实时运行需两张 RTX 3090，长序列需 24 GB 显存。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 4 学习式对应的核心节点，MASt3R-SLAM、VGGT-SLAM 等最常用的学习式对照。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2108.10869 · [全文 PDF](https://arxiv.org/pdf/2108.10869v2) · Zachary Teed、Jia Deng（Princeton University）
- 发表：NeurIPS 2021（官方 GitHub）
- 方向：robotics/localization-mapping
