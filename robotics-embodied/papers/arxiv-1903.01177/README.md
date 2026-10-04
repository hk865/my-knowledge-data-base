# PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1903.01177)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语义建图只给每个位置一个类别，分不清「这把椅子」和「那把椅子」；抓取、交互这类任务需要以单个物体为单位的地图。
- **核心方法**：相对 [SemanticFusion](../arxiv-1609.05130/README.md) 一类只融合类别的系统，改为全景标注（panoptic，一句话：背景区域 stuff 给类别，前景物体 things 给类别加实例编号）：每帧用 PSPNet 做语义分割、Mask R-CNN 做实例分割并合成全景标签，参照当前 3D 地图把帧间会变化的实例编号对齐，再融入基于 voxblox 的 TSDF 体素地图（截断符号距离场，一句话：每个体素存到最近表面的带符号距离，用于稠密重建）；另用全连接 CRF（条件随机场，一句话：让相邻且相似的位置倾向于取相同标签的概率模型）在线正则化地图。在 ScanNet v2 上，语义与实例分割结果优于或接近离线的 3D 网络方法。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向「语义建图」一支从类别走到实例的一步，位于 SemanticFusion 之后、借助视觉语言基础模型的 [FM-Fusion](../url-https-github.com-hkust-aerial-robotics-fm-fusion/README.md) 之前。优先级：存档。

## 身份信息

- 稳定标识：arxiv:1903.01177
- 作者：Gaku Narita、Takashi Seno、Tomoya Ishikawa、Yohsuke Kaji
- 全文：[arXiv PDF](https://arxiv.org/pdf/1903.01177)
- 发表：IROS 2019（arXiv 注释）
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)、[感知与传感器](../../fields/perception/README.md)
