# OpenVINS: A Research Platform for Visual-Inertial Estimation

> 状态：文献卡 · 2020 · [原文](https://pgeneva.com/downloads/papers/Geneva2020ICRA.pdf)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：现有开源 VINS 难以扩展、缺少文档，研究者难以在同一平台上比较滤波式 VIO 的设计。
- **核心方法**：在 MSCKF 上做成模块化开源平台：流形上的滑窗 EKF、带 FEJ 的 SLAM 路标、在线标定内外参与相机-IMU 时间偏移、仿真器与评估工具。仿真中初值较差时，开启在线标定的位置 NEES 约 2.0，不标定时达到 1045、轨迹误差 508.7 m。
- **为什么在这个库里**：[Baseline 页](../../fields/localization-mapping/BASELINES.md)"状态参数化 + 标定"一格；EqVIO、学习式 IMU 偏置预测都以它的 MSCKF 实现为对照。优先级：选读。

## 身份信息

- 稳定标识：url:https://pgeneva.com/downloads/papers/Geneva2020ICRA.pdf · [全文 PDF](https://pgeneva.com/downloads/papers/Geneva2020ICRA.pdf) · Patrick Geneva、Kevin Eckenhoff、Woosik Lee、Yulin Yang、Guoquan Huang（University of Delaware RPNG）
- 发表：ICRA 2020（据其他论文的参考文献，PDF 页面未印会议名）
- 方向：robotics/localization-mapping
