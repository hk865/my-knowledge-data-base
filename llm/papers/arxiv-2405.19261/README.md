# Faster Cascades via Speculative Decoding

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.19261)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：级联（只把"难"的输入交给大模型）与投机解码（大模型并行验证小模型的草稿）各有长处：前者在经验上成本—质量权衡更好，后者在理论上保证质量不变；能否兼得。
- **核心方法**：用投机执行来实现级联的延迟规则（deferral rule：决定何时交给大模型）：把要精确采样的目标从大模型分布 p 换成小模型分布 q 与 p 按延迟规则组合的分布 π，用 min(1, π/q) 接受、从 max(π−q, 0) 补采。作者刻画了最优延迟规则，并用 plug-in 近似实现。在 Gemma 和 T5 上，成本—质量权衡优于级联和投机解码基线。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"精确采样混合分布"一格：精确采到的是 π，一般不等于大模型分布。与 [Leviathan 等的投机解码](../arxiv-2211.17192/README.md)（精确保证）和 [BiLD](../arxiv-2302.07863/README.md)（阈值近似）一起读，可分清三类保证。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2405.19261 · [全文 PDF](https://arxiv.org/pdf/2405.19261)
- 作者：Harikrishna Narasimhan、Wittawat Jitkrittum、Ankit Singh Rawat、Seungyeon Kim、Neha Gupta、Aditya Krishna Menon、Sanjiv Kumar（Google Research）
- 方向：llm/inference
