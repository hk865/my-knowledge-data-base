# ViViT: A Video Vision Transformer

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2103.15691)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视频切成 token 后序列很长；Transformer 一般只在大数据上有效，而视频数据集较小。
- **核心方法**：用时空管道（例如 16×16×2 像素×帧）切块并线性嵌入；比较四种结构：全时空注意力、先逐帧空间编码再在帧特征上做时间编码（分解编码器）、分解自注意力、分解点积注意力；用中心帧初始化管道嵌入，加正则化并借用预训练图像模型，使它能在小数据集上训练。ViViT-B 在 K400 上全时空 80.0%，逐帧编码后直接平均池化 75.8%；JFT 预训练的 ViViT-H 达 84.9%。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 4 步，与 TimeSformer 并列。"先逐帧编码、再在帧特征上建模时间"的分解编码器，与后来视频大模型"图像编码器逐帧编码、语言模型处理帧序列"同构；作者自述 SSv2 上细粒度运动仍是短板，并观察到此前方法在 SSv2 与 Kinetics 上的相对表现呈反相关。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2103.15691 · [全文 PDF](https://arxiv.org/pdf/2103.15691) · Google Research
- 方向：multimodal/video-temporal
- ICCV 2021（arXiv 注释）
