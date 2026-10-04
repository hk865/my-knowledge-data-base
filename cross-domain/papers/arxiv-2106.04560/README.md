# Scaling Vision Transformers

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2106.04560)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言 Transformer 的规模定律已有研究，Vision Transformer（ViT）怎样随模型、数据、算力扩展还不清楚。
- **核心方法**：在私有的 JFT-3B（近 30 亿张弱标注图像）与公开的 ImageNet-21k 上，把 ViT 从 5M 参数扩到 2B、数据从 1M 张扩到 3B 张，拟合 ImageNet 微调与 10-shot 线性评测的错误率与算力的关系：前沿近似"双饱和幂律"，算力最大时错误率趋向一个非零下限，算力最小时最小的模型也有非零准确率。小模型（如 Ti/16）加数据没有收益，大模型在 30M–300M 张图上仍受数据限制；大模型更省样本。顺带改进架构与训练以省显存，训出 2B 参数的 ViT-G/14，ImageNet top-1 90.45%，每类只用 10 张样本时 84.86%。
- **为什么在这个库里**：[训练科学方向](../../fields/training-science/README.md)"不同模态的差异"一节中判别式视觉一侧的证据：它拟合的是错误率，曲线形状与 [Henighan 等](../arxiv-2010.14701/README.md)交叉熵的"幂律加常数"不能直接比较；它也说明视觉规模定律依赖非公开数据。与 [ViT](../../../multimodal/papers/vit/README.md) 一起读，可看到"ViT 需要大数据"在规模上的完整版本（见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2106.04560 · [全文 PDF](https://arxiv.org/pdf/2106.04560) · Google Research, Brain Team（苏黎世）· CVPR 2022
- 作者：Xiaohua Zhai、Alexander Kolesnikov、Neil Houlsby、Lucas Beyer
- 方向：cross-domain/training-science、multimodal/visual-representation
