# Gemini: A Family of Highly Capable Multimodal Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2312.11805)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：构建能同时处理文本、图像、音频、视频并在各模态上都强的模型家族（Ultra、Pro、Nano）。
- **核心方法**：官方报告只写到：基于 Transformer 解码器，32K 上下文；视觉编码借鉴 Flamingo、CoCa 与 PaLI，区别是模型"从一开始就是多模态"，能用离散图像 token 直接输出图像；视频按帧序列放入长上下文；支持可变输入分辨率；音频直接取 16kHz 的 USM 特征。Nano（1.8B、3.25B）由大模型蒸馏并 4 比特量化。Gemini Ultra 的 MMMU 为 62.4%，作者称比此前最好高 5 个百分点以上。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)"早融合与从一开始就多模态"一支的官方来源；参数量、视觉部件结构与训练数据都未公开，只能按报告原话引用。长上下文的后续版本见 [Gemini 1.5](../../../llm/papers/arxiv-2403.05530/README.md)。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2312.11805（Gemini Team 等 1351 位作者；当前 v5，2025-05）· [全文 PDF](https://arxiv.org/pdf/2312.11805v5) · Google（Gemini Team）
- 方向：[视觉语言模型](../../fields/vlm/README.md)
