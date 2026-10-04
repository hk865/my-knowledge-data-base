# ImageNet Classification with Deep Convolutional Neural Networks

> 状态：文献卡 · 2012 · [原文](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在百万级图像、上千个类别上识别物体，需要容量足够大、又带有图像先验的模型；在此之前带标签的图像数据集只有数万张的量级，刚刚出现 ImageNet 这样的百万级数据。
- **核心方法**：5 个卷积层加 3 个全连接层、6000 万参数的卷积网络：用不饱和的 ReLU 加快训练，用 dropout 抑制全连接层的过拟合，把网络拆到两块 3GB 显存的 GTX 580 上并行，训练 5–6 天。ILSVRC-2010 测试集 top-1 / top-5 错误率 37.5% / 17.0%，此前最好的 SIFT 加 Fisher 向量为 45.7% / 25.7%；ILSVRC-2012 top-5 测试错误率 15.3%，第二名 26.2%（15.3% 是多个 CNN 的平均，其中两个先用额外的 ImageNet Fall 2011 数据预训练）。去掉任意一个中间层，top-1 约损失 2 个百分点。第一层学出对频率和方向有选择性的卷积核与颜色斑块。
- **为什么在这个库里**：[视觉表征方向](../../fields/visual-representation/README.md)主线第 1 个节点"数据轴与信号轴一起移动"的代表，[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 有标签监督加深层 CNN"一格；第一层卷积核是入门页"从内部看"一节的第一条证据。[判断] 改变局面的是数据、算力和 benchmark，卷积机制在 1998 年的 LeNet 中已经具备。作者自述没有用无监督预训练、并预计它会有帮助，这一步要到 2019 年的 [MoCo](../arxiv-1911.05722/README.md) 才在检测迁移上超过有监督预训练。优先级：必读。

## 身份信息

- 稳定标识：NeurIPS 2012（NIPS 25）论文集页面 · [全文 PDF](https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) · University of Toronto
- 方向：multimodal/visual-representation
