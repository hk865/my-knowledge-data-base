# SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks

> 状态：文献卡 · 2016 · [原文](https://arxiv.org/abs/1609.05130)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：稠密 SLAM（同时定位与建图，一句话：边估计相机位姿边构建环境地图）只给出几何形状，机器人还需要知道地图里每一处是什么类别的物体。
- **核心方法**：在 ElasticFusion（一种稠密 RGB-D SLAM 系统，用面元 surfel 表示表面，回环扫描时地图会随之形变，保持帧间的长期对应）之上接一个 CNN 逐帧做语义分割，再借 SLAM 提供的对应关系，把多个视角的类别预测按贝叶斯更新融合进每个面元的类别分布。在 NYUv2 上，融合后的地图投回 2D 时语义标注优于单帧 CNN；视角变化越大的序列提升越明显；系统约 25 Hz 实时运行。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向「语义建图」一支的起点：地图表示从纯几何扩展到带类别的几何。之后 [PanopticFusion](../arxiv-1903.01177/README.md) 加上物体实例，[FM-Fusion](../url-https-github.com-hkust-aerial-robotics-fm-fusion/README.md) 用视觉语言基础模型替换固定类别的 CNN。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1609.05130
- 作者：John McCormac、Ankur Handa、Andrew Davison、Stefan Leutenegger
- 全文：[arXiv PDF](https://arxiv.org/pdf/1609.05130)
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)、[感知与传感器](../../fields/perception/README.md)
