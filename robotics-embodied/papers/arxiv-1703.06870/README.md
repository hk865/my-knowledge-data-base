# Mask R-CNN

> 状态：文献卡 · 2017 · [原文](https://arxiv.org/abs/1703.06870)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Faster R-CNN 不是为输入输出的像素对齐设计的，RoIPool 做粗糙的空间量化，无法直接产生精确的实例掩码。
- **核心方法**：在 Faster R-CNN 上并行加一个掩码分支，用 RoIAlign（双线性插值取特征、不取整）替换 RoIPool，掩码与类别解耦。COCO test-dev 实例分割 mask AP 37.1（FCIS+++ 33.6）；每张图 195 ms（Tesla M40），约 5 fps，作者写明设计未针对速度优化；Cityscapes 中样本少的类别存在领域偏移。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)的单帧基线，[Baseline 页](../../fields/perception/BASELINES.md)中"一张图进，框、类别、掩码出"的接口；PanopticFusion 用它做实例分割。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1703.06870 · [全文 PDF](https://arxiv.org/pdf/1703.06870v3) · Kaiming He、Georgia Gkioxari、Piotr Dollár、Ross Girshick（Facebook AI Research）
- 发表：未核实（arXiv 页与 PDF 首页未印会议名）
- 方向：robotics/perception
