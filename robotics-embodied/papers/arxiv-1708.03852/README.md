# VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator

> 状态：文献卡 · 2017 · [原文](https://arxiv.org/abs/1708.03852)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：单目加低成本 IMU 是能估计公制 6 自由度位姿的最小传感器组合，但缺少直接测距，使初始化、外参标定和非线性优化都很困难。
- **核心方法**：先做纯视觉 SfM，再与 IMU 预积分对齐，恢复尺度、重力、速度和陀螺偏置；之后用紧耦合滑窗优化融合视觉与 IMU，在线估计外参，DBoW2 回环后做 4 自由度位姿图（横滚和俯仰由重力可观）。约 700 m 室内外轨迹上 OKVIS 漂移 2.36%，VINS-Mono 不开回环 0.88%；滑窗优化 50 ms（10 Hz）。原文写明初始化需要加速度激励、不能从静止开始，剧烈光照变化与激进运动仍会失败，纯旋转无法三角化。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 3 的核心节点，与 ORB-SLAM3 同为优化式 VIO 的常用对照。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1708.03852 · [全文 PDF](https://arxiv.org/pdf/1708.03852v1) · Tong Qin、Peiliang Li、Shaojie Shen（HKUST）
- 发表：IEEE T-RO 2018
- 方向：robotics/localization-mapping
