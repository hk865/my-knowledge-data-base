# PaLI: A Jointly-Scaled Multilingual Language-Image Model

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2209.06794)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：此前的大容量视觉语言模型中，语言骨干远大于视觉骨干；怎样用一个"图像加文字进、文字出"的接口覆盖描述、问答、读字等任务，并扩展到 100 多种语言？
- **核心方法**：encoder–decoder 结构：复用 13B 的 mT5-XXL，另训 4B 的 ViT-e，视觉约占 PaLI-17B 参数的 25%；所有任务写成"图像 + 查询 → 文字答案"。新建 WebLI（100 亿张图、覆盖 100 多种语言，按图文匹配分取前 10% 约 10 亿对）。主预训练在 224 分辨率上冻结 ViT、只更新语言部分（附录消融显示冻结略好），最大模型再用 588 分辨率全参数训练 1 万步。VQAv2 84.3%，COCO 描述 CIDEr 149.1；作者结论是扩大视觉侧的回报（每参数、每 FLOP 的提升）更高。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 1 个节点中 Google 的另一条路线（encoder–decoder、平衡两侧参数），也是 [RT-2](../../../robotics-embodied/papers/arxiv-2307.15818/README.md) 所用 PaLI-X 的前身。自述局限：多物体复杂场景描述不全、英文微调后丢失多语言能力、开放词表生成的同义答案被判错。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2209.06794（Xi Chen 等 29 位作者；当前 v4，2023-06）· [全文 PDF](https://arxiv.org/pdf/2209.06794v4) · Google Research · ICLR 2023
- 方向：[视觉语言模型](../../fields/vlm/README.md)
