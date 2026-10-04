# Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.05271)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源多模态模型在性能和效率上仍落后 GPT-4o、Claude-3.5-Sonnet；视觉编码器、语言模型、数据规模和推理时计算各自怎样影响表现，缺系统研究。
- **核心方法**：沿用 InternVL 1.5 的 ViT–MLP–LLM 结构（InternViT-6B 或 300M，448 切块，pixel unshuffle 每块 256 token），研究扩展规律。三个发现：大视觉编码器减少对数据的依赖，配 6B 视觉编码器的 78B 模型约用 120B token，作者对比 Qwen2-VL 累计的 1.4T；数据质量重要，LLM 对数据噪声远比视觉编码器敏感，微调数据中区区几千条重复样本就让模型在长输出和 CoT 中陷入循环；测试时扩展有益，MMMU 用 CoT 达 70.1%，比直接回答高 3.7，是第一个过 70% 的开源模型。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 7 个节点与团队竞争的证据（用 Qwen2-VL 的训练 token 作对比）。复读问题与 [DeepSeek LLM](../../../llm/papers/arxiv-2401.02954/README.md) 的"SFT 数据越多越容易重复"同源。自述过滤不能根除复读，长回答中仍有幻觉；OpenCompass 只覆盖 8 个学术 VQA。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2412.05271（Zhe Chen 等 42 位作者；当前 v5，2025-09）· [全文 PDF](https://arxiv.org/pdf/2412.05271v5) · 上海人工智能实验室 OpenGVLab 等
- 方向：[视觉语言模型](../../fields/vlm/README.md)
