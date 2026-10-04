# AM-RADIO: Agglomerative Vision Foundation Model -- Reduce All Domains Into One

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2312.06709)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CLIP（语言接地）、DINOv2（密集对应）、SAM（细致分割）的训练目标不同，各有长处也各有明显缺口，下游要么挑一个，要么同时跑几个编码器。
- **核心方法**：无标签的多教师蒸馏：只用 DataComp-1B 的图像，不用任何标注，让一个学生通过各自的适配头同时匹配 DFN CLIP、OpenAI CLIP、DINOv2-g、SAM-H 四个教师的摘要向量和逐块特征。ViT-H/16 学生在 ImageNet k 近邻（86.06 对 DINOv2 的 83.41）和 ADE20K 线性分割（51.34 对 48.68）上超过教师，零样本分类 82.93 略低于 DFN CLIP 的 83.90（Table 1）。另提出高吞吐的混合 CNN-Transformer 学生 E-RADIO。
- **为什么在这个库里**：多教师蒸馏的起点（[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 多教师蒸馏"一行），[C-RADIOv4](../arxiv-2601.17237/README.md) 与 [RADIO1D](../arxiv-2607.03624/README.md) 的前作；它把 [OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 式"拼接两个编码器"换成"蒸馏进一个"。结论写明"更好的教师得到更好的学生"。自述问题：低分辨率只训 CLIP 与 DINOv2、高分辨率才训 SAM，学生因此出现"模式切换"，输入到约 720 像素时特征突然变样（Fig.5），留待后续修复。代码已发布。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2312.06709（当前 v5，2024-04）· [全文 PDF](https://arxiv.org/pdf/2312.06709) · NVIDIA · CVPR 2024
- 方向：multimodal/visual-representation、cross-domain/knowledge-distillation
