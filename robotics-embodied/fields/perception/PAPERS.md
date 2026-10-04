# 机器人感知：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

以下每项链接到唯一的单篇目录，按[入门页](README.md)主线历史的阶段分组。跨方向出现是交叉引用，不重复计算资源。

## 单帧检测与分割

- [You Only Look Once: Unified, Real-Time Object Detection](../../papers/arxiv-1506.02640/README.md) · 2015 · 文献卡
- [Mask R-CNN](../../papers/arxiv-1703.06870/README.md) · 2017 · 文献卡
- [Segment Anything](../../papers/arxiv-2304.02643/README.md) · 2023 · 文献卡

## 跨时间融合与语义地图

- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](../../papers/arxiv-1609.05130/README.md) · 2016 · 文献卡
- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](../../papers/doi-10.3390-s18093099/README.md) · 2018 · 文献卡
- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](../../papers/arxiv-1903.01177/README.md) · 2019 · 文献卡
- [ConceptFusion: Open-set Multimodal 3D Mapping](../../papers/arxiv-2302.07241/README.md) · 2023 · 文献卡
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](../../papers/arxiv-2402.04555/README.md) · 2024 · 文献卡
- [FM-Fusion 代码仓库](../../papers/url-https-github.com-hkust-aerial-robotics-fm-fusion/README.md) · 代码仓库卡，不计为论文

## 深度与 3D 几何

- [Digging Into Self-Supervised Monocular Depth Estimation](../../papers/arxiv-1806.01260/README.md) · 2018 · 文献卡
- [PointPillars: Fast Encoders for Object Detection from Point Clouds](../../papers/arxiv-1812.05784/README.md) · 2018 · 文献卡
- [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](../../papers/arxiv-2401.10891/README.md) · 2024 · 文献卡
- [Depth Anything V2](../../papers/arxiv-2406.09414/README.md) · 2024 · 文献卡

## 多传感器融合与评测

- [nuScenes: A multimodal dataset for autonomous driving](../../papers/arxiv-1903.11027/README.md) · 2019 · 文献卡
- [BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation](../../papers/arxiv-2205.13542/README.md) · 2022 · 文献卡

## 感知到控制（与运动控制方向共享）

- [Learning robust perceptive locomotion for quadrupedal robots in the wild](../../papers/arxiv-2201.08117/README.md) · 2022 · 文献卡
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md) · 2022 · 文献卡
- [MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion](../../papers/doi-10.1002-advs.202524345/README.md) · 年份见原文 · 文献卡（原文未打开）

## 上游与表征（交叉引用）

- [ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](../../papers/orb-slam3/README.md) · 2020 · 技术精读（位姿来源，见[定位与建图](../localization-mapping/README.md)）
- [Quaternion kinematics for the error-state Kalman filter](../../papers/eskf/README.md) · 2017 · 技术精读（融合的统计基础）
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../../../multimodal/papers/vit/README.md) · 2020 · 精读（编码器结构，见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)）
- [Learning Transferable Visual Models From Natural Language Supervision](../../../multimodal/papers/clip/README.md) · 2021 · 精读（开放词汇语义的来源）
