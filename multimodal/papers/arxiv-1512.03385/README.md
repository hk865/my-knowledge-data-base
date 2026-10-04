# Deep Residual Learning for Image Recognition

> 状态：文献卡 · 2015 · [原文](https://arxiv.org/abs/1512.03385)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：网络加深时出现"退化"：精度先饱和、随后下降，而且更深的模型训练误差反而更高，所以不是过拟合；作者用 BN 确认前向信号和反向梯度都没有消失。
- **核心方法**：让每两到三层只学相对输入的修正量 F(x)，输出 x + F(x)，恒等捷径不增加参数。ImageNet 验证集上 34 层普通网络 top-1 错误率 28.54%，比 18 层的 27.94% 还高；加上捷径后 34 层为 25.03%，低于 18 层的 27.88%。最深 152 层（VGG 的 8 倍深，计算量却更低），集成模型 ILSVRC 2015 top-5 测试错误率 3.57%；只换成更深的主干，COCO 检测相对提升 28%。作者自述：深层普通网络为什么难优化留待研究；1202 层的网络测试结果比 110 层差，归因于过拟合。
- **为什么在这个库里**：[视觉表征方向](../../fields/visual-representation/README.md)主线第 3 个节点"架构轴在 CNN 内部加深"的终点。ImageNet 有监督 ResNet-50 是 [Baseline 页](../../fields/visual-representation/BASELINES.md)的第一个基线：MoCo、SimCLR、DINO 的线性评测表都以它为对照，ConvNeXt 从它出发检验训练配方。残差连接后来成为 Transformer 的标准部件（[CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节）。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1512.03385 · [全文 PDF](https://arxiv.org/pdf/1512.03385) · Microsoft Research · CVPR 2016
- 方向：multimodal/visual-representation
