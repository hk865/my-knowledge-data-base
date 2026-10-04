# You Only Look Once: Unified, Real-Time Object Detection

> 状态：文献卡 · 2015 · [原文](https://arxiv.org/abs/1506.02640)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：R-CNN 类检测是多阶段流水线，慢且难优化，因为每个部件要分别训练。
- **核心方法**：把检测写成一次回归：整张图输入，直接在 7×7 网格上输出框和类别。VOC2007 上 63.4 mAP、45 fps（Titan X），同表 Faster R-CNN（VGG-16）73.2 mAP、7 fps。原文写明主要误差来源是定位不准（定位误差占 19.0%，Fast R-CNN 为 8.6%），难处理成群的小物体。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 1 的节点，[Baseline 页](../../fields/perception/BASELINES.md)"预测网络"一格；速度与精度并列报告的早期例子。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1506.02640 · [全文 PDF](https://arxiv.org/pdf/1506.02640v5) · Joseph Redmon、Santosh Divvala、Ross Girshick、Ali Farhadi（University of Washington、Allen Institute for AI、FAIR）
- 发表：未核实（arXiv 页与 PDF 首页未印会议名）
- 方向：robotics/perception
