# FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.04555)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：依赖有监督目标检测器的语义建图对图像分布敏感，换到真实环境后检测与分割性能大幅下降。
- **核心方法**：改用视觉语言基础模型（官方代码用 RAM 识别标签、GroundingDINO 开放词表检测、SAM 分割）产生开放集检测，用概率标签融合把开放集标签测量映射成闭集语义类别，再用实例细化模块合并因分割不一致造成的过分割实例，从 RGB-D 序列增量重建实例级语义地图。ScanNet（室内 RGB-D 扫描数据集）零样本语义实例分割达到 40.3 mAP，明显优于传统语义建图方法。
- **为什么在这个库里**：[感知与传感器](../../fields/perception/README.md)方向"语义地图"一支进入基础模型时代的节点：[SemanticFusion](../arxiv-1609.05130/README.md) → [Pixel-Voxel](../doi-10.3390-s18093099/README.md) → [PanopticFusion](../arxiv-1903.01177/README.md) → 本篇。优先级：存档。

## 身份信息

- 稳定标识：url:https://github.com/HKUST-Aerial-Robotics/FM-Fusion（论文 arxiv:2402.04555；Liu、Wang、Shi、Qiao、Shen；IEEE RA-L 第 9 卷第 3 期 2232–2239，2024-03）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2402.04555) · 代码：[HKUST-Aerial-Robotics/FM-Fusion](https://github.com/HKUST-Aerial-Robotics/FM-Fusion)
- 方向：[感知与传感器](../../fields/perception/README.md)（另见[状态估计与建图](../../fields/localization-mapping/README.md)）
