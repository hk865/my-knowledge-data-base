# LAION-5B: An open large-scale dataset for training next generation image-text models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2210.08402)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CLIP、ALIGN、BASIC 等模型依赖数亿到数十亿对的图文数据，但此前没有这一规模的公开数据集，研究集中在少数工业实验室。
- **核心方法**：从 Common Crawl 出发，用 OpenAI 的 CLIP ViT-B/32 给每对图文打分，英文对余弦相似度低于 0.28、其他语言低于 0.26 的丢掉，约 500 亿张图中去掉约 90%，得到 58.5 亿对（英文 23.2 亿），附 NSFW、水印分数与最近邻索引；用它复现了 CLIP，并训练或微调 GLIDE、Stable Diffusion。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 5 个节点、Baseline 表"数据：CLIP 打分过滤并公开"一格；后续 OpenCLIP 缩放定律、[DataComp](../arxiv-2304.14108/README.md) 都建立在它之上，Stable Diffusion 的训练数据也来自它（见[视觉生成方向](../../fields/generation/README.md)）。自述用小 CLIP 过滤会继承其偏差；LAION 官方 2024 年发布 Re-LAION-5B 删除不安全链接。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2210.08402 · [全文 PDF](https://arxiv.org/pdf/2210.08402) · LAION、UC Berkeley、TU Darmstadt、University of Washington、Stability AI、Jülich 等
- 方向：multimodal/alignment、multimodal/generation
