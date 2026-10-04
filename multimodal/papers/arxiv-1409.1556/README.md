# Very Deep Convolutional Networks for Large-Scale Image Recognition

> 状态：文献卡 · 2014 · [原文](https://arxiv.org/abs/1409.1556)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：AlexNet 之后的改进多在调第一层的感受野、步长，或做多尺度测试；网络深度本身对大规模图像识别有多大作用？
- **核心方法**：全部使用 3×3 卷积，把深度推到 16–19 个权重层。三层 3×3 卷积的感受野等于一层 7×7，却多了两次非线性，参数也更少（通道数为 C 时 27C² 对 49C²）。ILSVRC 2014 定位第一、分类第二；单网络 top-5 测试错误率 7.0%，比单个 GoogLeNet 低 0.9 个百分点，赛后两个模型集成降到 6.8%。公开了两个最好的模型，各配置参数量 1.33 亿到 1.44 亿。
- **为什么在这个库里**：[入门页](../../fields/visual-representation/README.md)主线第 3 个节点"架构轴在 CNN 内部加深"，[Baseline 页](../../fields/visual-representation/BASELINES.md)"架构 = 3×3 卷积堆深"一行。它作为预训练主干直接传到下游：[R-CNN](../arxiv-1311.2524/README.md) 把主干从 AlexNet 换成 VGG16 后，VOC2007 mAP 从 58.5% 升到 66.0%，代价是前向耗时约 7 倍。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1409.1556（当前 v6，2015-04）· [全文 PDF](https://arxiv.org/pdf/1409.1556) · University of Oxford（Visual Geometry Group）· ICLR 2015
- 方向：multimodal/visual-representation
