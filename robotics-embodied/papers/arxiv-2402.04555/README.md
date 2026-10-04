# FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.04555)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：基于监督检测器的语义建图对图像分布敏感，不微调部署到新场景时性能严重下降；基础模型在视角变化时给出不一致的实例掩码，造成过分割。
- **核心方法**：RAM 打标签、Grounding DINO 按标签检测、SAM 出掩码，增量融合进实例级语义地图；用概率标签融合把开放集标签转成闭集类别，并合并被切碎的实例。ScanNet 30 个验证场景 mAP50：未微调的 Mask R-CNN 接 Kimera 5.4，微调后 25.9，FM-Fusion 40.3。每帧 1039.6 ms（SAM 464.4 ms），原文写明还不是实时系统；相机位姿由数据集提供。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 6 的核心节点，"站在现在看过去"表中"固定类别换场景就掉点"的依据；代码仓库另有[资料卡](../url-https-github.com-hkust-aerial-robotics-fm-fusion/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2402.04555 · [全文 PDF](https://arxiv.org/pdf/2402.04555v2) · Chuhao Liu、Ke Wang、Jieqi Shi、Zhijian Qiao、Shaojie Shen（HKUST、长安大学）
- 发表：IEEE RA-L vol. 9, no. 3, 2024
- 方向：robotics/perception、robotics/localization-mapping
