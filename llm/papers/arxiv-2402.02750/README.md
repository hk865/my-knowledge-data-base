# KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.02750)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大批量、长上下文时 KV 缓存成为新的显存与速度瓶颈（原文举例：PaLM 540B 在批量 512、上下文 2048 时 KV 缓存约 3TB，是参数的 3 倍），而对 KV 缓存里数值分布的研究不足，量化不知道该按什么维度做（§1）。
- **核心方法**：非对称的 2 比特量化：Key 里有少数固定的大幅值通道，按通道量化能把误差关在单个通道里；Value 没有这种通道离群，按 token 量化能把误差关在单个 token 里；最近的 128 个 token 保留全精度。不需要微调。Llama-2-7B 上峰值显存（含权重）降低 2.6 倍，批量可放大 4 倍，吞吐提高 2.35–3.47 倍（§4.2.4）；Llama 与 Mistral 上精度最多下降约 2%，Falcon-7B（已用 MQA）需要 4 比特（Table 3）。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"推理效率"一节"降低 KV 缓存的存储精度"一格的代表，与减少 KV 头数的 [GQA](../arxiv-2305.13245/README.md) 是两件可以叠加的事；DeepSeek-V4 把 KV 缓存降到 FP8/FP4 属于同一方向（见[预训练方向](../../fields/pretraining/README.md)"数值精度"一节）。自述未来工作：降低 prefill 与解码阶段量化本身的开销。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2402.02750 · [全文](https://arxiv.org/pdf/2402.02750) · Rice University、Texas A&M University、CMU 等
- 方向：llm/inference
