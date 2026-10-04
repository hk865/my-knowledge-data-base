# ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM

> 状态：技术精读 · 2020 · [原文](https://arxiv.org/abs/2007.11898)

[返回机器人与具身目录](../../README.md)

- **解决什么**：视觉惯性系统多数只用最近几秒的观测，误差随路程累积；能复用地图的视觉惯性 SLAM 初始化 IMU 又慢又脆弱，跟踪一丢就只能重定位或从头开始。
- **核心方法**：在同一团队纯视觉的 ORB-SLAM2 之上，加入完全基于最大后验估计（连 IMU 初始化阶段也是）的紧耦合视觉惯性 SLAM；再用召回率更高的新地点识别方法支撑多地图系统 Atlas：跟踪丢失时另起新图，重访时与旧图无缝合并，使时间上相隔很远、甚至来自上一次运行的共视关键帧也进入光束法平差（bundle adjustment，一句话：联合优化相机位姿与三维点、使重投影误差最小）。摘要称在各种传感器配置下精度比此前方法高 2–5 倍。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向的视觉惯性 SLAM 系统基线，单目、双目、RGB-D 与鱼眼都支持，源码开放。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

教学顺序：[ESKF 教程](../eskf/README.md)（IMU 积分与误差状态）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2007.11898（Campos、Elvira、Gómez Rodríguez、Montiel、Tardós；IEEE T-RO 2021，DOI 10.1109/TRO.2021.3075644）
- 全文：[arXiv PDF v2](https://arxiv.org/pdf/2007.11898v2)
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)（另见[感知与传感器](../../fields/perception/README.md)、[世界模型与行动预测](../../fields/world-models/README.md)）
