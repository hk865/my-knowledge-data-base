# DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.10302)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：前作 DeepSeek-VL 的混合编码器固定在 384 和 1024 两种分辨率，在大图、极端长宽比、信息图、稠密 OCR 和精细定位上吃亏；稠密语言模型推理成本高。
- **核心方法**：视觉侧改为动态切块：单个 SigLIP-SO400M-384 按长宽比把图切成最多 9 块（候选分辨率 m×384 by n×384、mn ≤ 9）加全局缩略图；语言侧换成带 MLA（压缩 KV 缓存的多头潜在注意力）的 DeepSeekMoE，3B、16B、27B 三档，激活 1.0B、2.8B、4.5B。数据约 70% 视觉语言、30% 纯文本；对齐阶段训练视觉编码器与适配器、冻结 LLM，预训练阶段全部解冻。新增定位与 GUI 感知能力。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 5 个节点切块一路与"语言侧走向 MoE"的代表；[Kimi-VL](../arxiv-2504.07491/README.md) 以它的固定尺寸编码器和 4K 上下文为出发点。自述局限：每次对话只能放少量图片；模糊图像与未见过的物体仍有困难；推理能力待加强。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2412.10302（Zhiyu Wu 等 27 位作者；当前 v1，2024-12）· [全文 PDF](https://arxiv.org/pdf/2412.10302v1) · DeepSeek-AI
- 方向：[视觉语言模型](../../fields/vlm/README.md)
