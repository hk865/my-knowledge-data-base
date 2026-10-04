# LiT: Zero-Shot Transfer with Locked-image text Tuning

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2111.07991)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：从头训练两座塔的 CLIP、ALIGN 很贵，而网页图文数据未必足够干净，学不出最好的图像表征。
- **核心方法**：相对 CLIP、ALIGN 只改图像塔：用一个已在干净的（半）人工标注数据上预训练好的图像塔（ViT-g/14，JFT-3B 预训练），训练时冻结，只训练文本塔去"读出"图像表征。零样本 ImageNet 85.2%、ObjectNet 82.5%；作者发现解冻图像塔会让它在对齐数据上损失更低、在分布外数据上更差（Fig.4）。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md) Baseline 表"图像塔：冻结预训练"一格；与 [SigLIP](../arxiv-2303.15343/README.md)、[SigLIP 2](../arxiv-2502.14786/README.md) 同一组作者，是"Google Zürich 追求更省、更好用"这一团队偏好的第一篇。自述检索上优势不明显。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2111.07991 · [全文 PDF](https://arxiv.org/pdf/2111.07991) · Google Research, Brain Team, Zürich
- 方向：multimodal/alignment
