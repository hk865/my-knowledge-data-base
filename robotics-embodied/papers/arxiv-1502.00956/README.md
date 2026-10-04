# ORB-SLAM: a Versatile and Accurate Monocular SLAM System

> 状态：文献卡 · 2015 · [原文](https://arxiv.org/abs/1502.00956)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：PTAM 只能在小场景中运行，缺回环和遮挡处理，重定位对视角变化不鲁棒，还需要人工初始化。
- **核心方法**：在 PTAM 的架构上从头重写为跟踪、局部建图、回环三线程，所有环节统一使用 ORB 特征；用共视图把优化限制在局部，回环后在 Essential Graph 上做 7 自由度位姿图优化，并自动在单应与基础矩阵之间选择初始化模型。TUM 的 16 条序列上 PTAM 跟丢 8 条；有人走动的 fr3_walking_xyz 上重定位召回 77.9%，PTAM 为 0。原文写明的失败：KITTI 01 高速公路无法处理，KITTI 08 无回环时尺度漂移 46.58 m，NewCollege 反向大环未检出。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 2 的核心节点，ORB-SLAM2/3 的前作。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1502.00956 · [全文 PDF](https://arxiv.org/pdf/1502.00956v2) · Raúl Mur-Artal、J. M. M. Montiel、Juan D. Tardós（Universidad de Zaragoza I3A）
- 发表：IEEE T-RO 2015
- 方向：robotics/localization-mapping
