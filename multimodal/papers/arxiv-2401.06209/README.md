# Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2401.06209)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多模态大模型的视觉部分通常只依赖 CLIP，它们在简单的视觉问题上系统性出错：问题出在视觉、语言还是对齐？
- **核心方法**：找"CLIP 盲对"：CLIP ViT-L/14 嵌入余弦相似度超过 0.95、DINOv2 嵌入相似度低于 0.6 的图片对，据此出 150 对、300 道题（MMVP）。人类 95.7%，GPT-4V 38.7%，LLaVA-1.5 24.7%（随机 25%）；归纳出朝向、计数、视角等 9 类模式，其中 7 类任何规模的 CLIP 都解决不了，CLIP 失败的模式与 VLM 失败的模式强相关。把 CLIP 与 DINOv2 的逐块特征交错送入 VLM（I-MoF），视觉定位明显变好而指令遵循不掉。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 7 个节点：对比目标的盲区怎样随视觉塔传进 VLM，是本方向交给 [VLM 方向](../../fields/vlm/README.md)的接口；与 [视觉表征方向](../../fields/visual-representation/README.md)"按性质组合多种表征"的判断一致。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2401.06209 · [全文 PDF](https://arxiv.org/pdf/2401.06209) · New York University、FAIR Meta、UC Berkeley
- 方向：multimodal/alignment、multimodal/vlm、multimodal/visual-representation
