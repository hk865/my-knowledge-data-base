# How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.16821)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源模型与 GPT-4V 等闭源模型差在三处：视觉编码器只有约 300M；固定 336 或 448 分辨率，看不清文档；训练以英文为主，非英文场景与 OCR 弱。
- **核心方法**：ViT–MLP–LLM 结构：InternViT-6B 持续学习后经 MLP 接 InternLM2-20B，pixel shuffle 把视觉 token 减到四分之一（每块 448×448 得 256 个）；动态高分辨率按长宽比把图切成 1–40 块（最高约 4K）并加一张缩略图；收集中英双语数据并用开源 LLM 翻译扩展。在 18 个 benchmark 中 8 个达到当时最好，OCR 类（TextVQA、ChartQA、DocVQA）上超过 GPT-4V 等闭源模型。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 5 个节点"切块"一路的代表，也是 InternVL 系列放弃 [InternVL 1](../arxiv-2312.14238/README.md) 大号中间件、改用 MLP 的转折点。此后 [InternVL 2.5](../arxiv-2412.05271/README.md) 与 [InternVL3](../arxiv-2504.10479/README.md) 都沿用这一结构。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2404.16821（Zhe Chen 等 35 位作者；当前 v2，2024-04）· [全文 PDF](https://arxiv.org/pdf/2404.16821v2) · 上海人工智能实验室 OpenGVLab 等
- 方向：[视觉语言模型](../../fields/vlm/README.md)
