# NICE-SLAM: Neural Implicit Scalable Encoding for SLAM

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2112.12130)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有神经隐式 SLAM 重建过平滑、难以扩展到大场景：iMAP 的单个 MLP 只能全局更新，在多房间公寓上重建与跟踪都显著变差。
- **核心方法**：改用多分辨率层次特征网格加预训练的小解码器，只更新视锥内的网格，只优化与当前帧重叠的关键帧。ScanNet 上轨迹误差 9.63，复现的 iMAP 为 36.67；动态数据集 Co-Fusion 上 1.6 cm，iMAP 复现为 7.8 cm。原文写明预测能力受粗网格尺度限制、不做回环，TUM 上 ORB-SLAM2 与 BAD-SLAM 仍更好。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 4 神经地图的节点。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2112.12130 · [全文 PDF](https://arxiv.org/pdf/2112.12130v2) · Zihan Zhu、Songyou Peng、Viktor Larsson、Weiwei Xu、Hujun Bao等（浙江大学、ETH Zurich、MPI-IS、Lund University、University of Amsterdam、Microsoft）
- 发表：CVPR 2022
- 方向：robotics/localization-mapping
