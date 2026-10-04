# DeepSeek-VL: Towards Real-World Vision-Language Understanding

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.05525)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源模型把算力花在指令阶段、靠学术数据刷分，真实使用体验差；多在 336 或 448 的低分辨率上运行；长时间多模态训练后语言能力退化。
- **核心方法**：SigLIP-L（384）负责语义、SAM-B（1024）负责细节，两路混合编码把 1024×1024 的图压成 576 个 token；三段训练：只训适配器 → 联合视觉语言预训练（训练 LLM 与适配器）→ SFT。两个发现：加大"只训适配器"阶段的数据没有收益甚至更差；直接用多模态数据训练 LLM 时语言指标急剧下降，作者归因于多模态语料过于简单且与语言数据竞争，于是保留至少 70% 纯文本，并从文本为主逐步提高多模态比例（"模态预热"）。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)"保住语言能力"一线的证据，与 [LLM 后训练](../../../llm/fields/posttraining/README.md)中的对齐税同源。自述 MathVista 36.1 落后 GPT-4V 的 47.8；结论中承诺的 MoE 在 [DeepSeek-VL2](../arxiv-2412.10302/README.md) 兑现，固定 1024 输入也在那里被切块取代。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2403.05525（Haoyu Lu 等 15 位作者；当前 v2，2024-03）· [全文 PDF](https://arxiv.org/pdf/2403.05525v2) · DeepSeek-AI
- 方向：[视觉语言模型](../../fields/vlm/README.md)
