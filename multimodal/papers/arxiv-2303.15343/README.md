# Sigmoid Loss for Language Image Pre-Training

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2303.15343)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：批级 softmax 对比损失要对整批归一化，分布式实现需要汇集全部嵌入、生成整张相似度矩阵，效果又依赖很大的批。
- **核心方法**：把 CLIP 的批级 softmax 换成逐对 sigmoid：矩阵每一格独立判断"配不配"，加可学习偏置（初值 −10）抵消负样本远多于正样本的失衡，可分块计算不必拼出整张矩阵。批小于 16k 时明显好于 softmax；批加到 100 万，两种损失都在 32k 左右饱和；冻结图像塔的 SigLiT 用 4 块 TPUv4 两天达到零样本 ImageNet 84.5%；对人为加入的数据噪声更稳健。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md) Baseline 表"训练目标：sigmoid"一格；SigLIP 编码器后来被用作 VLA 与 VLM 的视觉塔（例如 [OpenVLA](../../../robotics-embodied/papers/openvla/reading.md)），续作是 [SigLIP 2](../arxiv-2502.14786/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2303.15343 · [全文 PDF](https://arxiv.org/pdf/2303.15343) · Google DeepMind, Zürich
- 方向：multimodal/alignment、multimodal/visual-representation
