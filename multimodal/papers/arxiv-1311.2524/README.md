# Rich feature hierarchies for accurate object detection and semantic segmentation

> 状态：文献卡 · 2013 · [原文](https://arxiv.org/abs/1311.2524)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：PASCAL VOC 检测在 2010–2012 年进展停滞，最好的方法是组合多种低层手工特征与上下文的复杂集成系统。ImageNet 分类上学到的 CNN 特征能不能用于检测，检测标注又很少，怎么训？
- **核心方法**（R-CNN）：用选择性搜索给出约 2000 个与类别无关的候选区域，每个区域缩放后送进 CNN 抽特征，再用线性 SVM 分类。关键是两段训练：先在 ILSVRC 分类数据上有监督预训练，再在检测数据上微调。VOC2012 mAP 53.3%，比此前最好结果相对提高 30% 以上；VOC2007 从 HOG-DPM 的 33.7% 升到 54.2%，其中微调贡献 8.0 个百分点，加边框回归到 58.5%，2014 年 10 月版把主干换成 VGG16 后到 66.0%。ILSVRC2013 的 200 类检测上 31.4%，OverFeat 为 24.3%。代价是每张图约 13 秒（GPU）。
- **为什么在这个库里**：[入门页](../../fields/visual-representation/README.md)主线第 2 个节点，"预训练加微调"这一使用方式的起点，[Baseline 页](../../fields/visual-representation/BASELINES.md)"读出接口 = 检测数据上微调整个主干"一行；从它开始，表征的好坏用迁移到下游任务的效果来衡量。主干换成 [VGG](../arxiv-1409.1556/README.md) 后的提升，说明主干变强会直接传到下游。代码已发布。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1311.2524（当前 v5，2014-10，CVPR 2014 论文的扩展版）· [全文 PDF](https://arxiv.org/pdf/1311.2524) · UC Berkeley
- 方向：multimodal/visual-representation、robotics/perception
