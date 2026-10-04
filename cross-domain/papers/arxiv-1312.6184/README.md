# Do Deep Nets Really Need to be Deep?

> 状态：文献卡 · 2013 · [原文](https://arxiv.org/abs/1312.6184)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：深网络在语音和视觉上领先，这个优势来自深度本身、更多的参数，还是现有训练方法更适合深结构？作者用模型压缩做检验：一个只有一层隐藏层的浅网络，能不能学到深网络学到的函数。
- **核心方法**：沿用 [Model Compression](../url-cornell-compression.kdd06/README.md) 的"教师打标签、学生模仿"，改动在目标上：浅学生用 L2 损失回归教师 softmax 之前的 logit，而不是概率或硬标签，理由是 logit 保留了各类之间的相对大小，经过 softmax 会被压平（§2.2）；输入与非线性隐藏层之间插一层线性层，只为加快训练（§2.3）。TIMIT 音素识别上，教师是 9 个 CNN 的集成（音素错误率 PER 18.5%）。直接训练的浅网络 PER 为 23.0%–23.6%，单个 CNN 为 19.5%；模仿训练后，8k 隐藏单元的浅网络为 21.6%，略好于参数量相近的三层 DNN（21.9%），400k 隐藏单元的为 20.0%，接近 CNN（Table 1）。
- **为什么在这个库里**：[知识蒸馏方向](../../fields/knowledge-distillation/README.md)阶段 2 与 [Baseline 页](../../fields/knowledge-distillation/BASELINES.md)"传什么 = 回归教师 logit"一格的代表；[Hinton 等](../arxiv-1503.02531/README.md)证明，高温极限下温度蒸馏就等价于这种 logit 匹配（Hinton 等 §2.1）。它最早写出"迁移数据不够"这个失败条件：TIMIT 没有额外的无标签数据，只能把训练集本身当迁移集，教师在训练点上过拟合，师生差距随之拉大（§3.2）；CIFAR-10 上不带卷积的网络多深都学不好，浅学生只能先加一层卷积与池化（§4.1）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1312.6184 · [全文 PDF](https://arxiv.org/pdf/1312.6184) · Lei Jimmy Ba（University of Toronto）、Rich Caruana（Microsoft Research） · NIPS 2014
- 方向：cross-domain/knowledge-distillation
