# BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2205.13542)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：点级融合有损：激光雷达投到相机造成几何畸变，相机投到激光点在语义上有损，32 线激光雷达下只有约 5% 的相机特征能找到对应点，难以做鸟瞰地图分割。
- **核心方法**：相机特征按深度分布抬升到鸟瞰网格，与激光雷达特征在同一网格上卷积融合，接检测与地图分割多任务头；把 BEV 池化从 500 ms 以上优化到 12 ms。nuScenes 测试集 NDS 72.9、每帧 119.2 ms（RTX 3090）；雨天检测 mAP 69.9，纯激光雷达的 CenterPoint 为 59.2；夜间地图分割 mIoU 43.6，纯相机版本 30.8。原文写明预计算依赖内外参固定，深度不准会使 BEV 特征错位；没有标定误差实验。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 4 跨传感器融合的节点，[Baseline 页](../../fields/perception/BASELINES.md)"融合空间"一格。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2205.13542 · [全文 PDF](https://arxiv.org/pdf/2205.13542v3) · Zhijian Liu、Haotian Tang、Alexander Amini、Xinyu Yang、Huizi Mao等（MIT、OmniML）
- 发表：ICRA 2023
- 方向：robotics/perception
