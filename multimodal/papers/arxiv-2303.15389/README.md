# EVA-CLIP: Improved Training Techniques for CLIP at Scale

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2303.15389)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CLIP 训练计算成本高，扩大规模时训练不稳定，并依赖很大的批。
- **核心方法**：相对 OpenCLIP 改图像塔初始化与训练技巧：图像塔用遮蔽图像建模预训练过的 EVA 初始化（作者称它结合了图文对比的高层语义与遮蔽建模捕获的几何结构），文本塔用 OpenAI CLIP 或 OpenCLIP 初始化，配合 LAMB 优化器、训练时随机丢掉 50% 图像块与 flash attention。EVA-02-CLIP-L/14 看 40 亿样本 ImageNet 零样本 79.8%，同尺寸 OpenCLIP 看 320 亿样本为 74.0%。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md) Baseline 表"图像塔：遮蔽建模初始化"一格，说明对比学习与视觉自监督（[MAE](../mae/README.md) 一类）可以串联；它也出现在 SigLIP 2 的对照表中。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2303.15389 · [全文 PDF](https://arxiv.org/pdf/2303.15389) · 北京智源研究院（BAAI）、华中科技大学
- 方向：multimodal/alignment
