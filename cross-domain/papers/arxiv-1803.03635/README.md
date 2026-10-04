# The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1803.03635)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：剪枝能在训练后去掉大部分参数而不损精度，但剪出来的稀疏结构从头训练往往训不好；稀疏网络能否一开始就训练。
- **核心方法**：迭代剪枝找出子网络后，把剩余权重重置回原始初始化再单独训练。在 MNIST、CIFAR10 上的全连接与卷积网络中，找到只有原网络 10–20% 大小、训练后精度相当的子网络（“中奖彩票”）；换成随机重新初始化后效果变差。
- **为什么在这个库里**：[训练科学方向](../../fields/training-science/README.md)“少量参数为什么就够”与“与模型科学的关系”两处的证据，对照训练后整层冗余的 [ShortGPT](../../../llm/papers/arxiv-2403.03853/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1803.03635 · [全文 PDF](https://arxiv.org/pdf/1803.03635)
- 方向：cross-domain/training-science
