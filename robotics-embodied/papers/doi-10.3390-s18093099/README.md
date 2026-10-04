# Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network

> 状态：文献卡 · 2018 · [原文](https://doi.org/10.3390/s18093099)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：ElasticFusion 等稠密 3D 建图只有几何、没有语义；语义分割网络效果好但太慢，难以接进实时机器人系统。
- **核心方法**：PixelNet 从 RGB 图像学全局上下文，VoxelNet 从点云学局部几何形状，再用 softmax 加权融合层按各自置信度自适应合并两路得分（此前的融合多为等权，或门控融合至多两种模态），并与 RGB-D SLAM 集成，单块 Titan X 上约 13 Hz。相对 [SemanticFusion](../arxiv-1609.05130/README.md) 等"单张图像分割、再按多帧贝叶斯更新"的做法，网络直接同时使用图像与点云。
- **为什么在这个库里**：[感知与传感器](../../fields/perception/README.md)方向"语义地图"一支 2018 年的节点，位于 SemanticFusion 与 [PanopticFusion](../arxiv-1903.01177/README.md)、[FM-Fusion](../url-https-github.com-hkust-aerial-robotics-fm-fusion/README.md)（基础模型、开放词表）之间。优先级：存档。

## 身份信息

- 稳定标识：doi:10.3390/s18093099（Zhao、Sun、Purkait、Duckett、Stolkin；Sensors 第 18 卷第 9 期 3099，2018-09）
- 全文：[PMC 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6164553/)
- 方向：[感知与传感器](../../fields/perception/README.md)（另见[状态估计与建图](../../fields/localization-mapping/README.md)）
