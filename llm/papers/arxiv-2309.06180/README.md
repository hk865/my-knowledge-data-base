# Efficient Memory Management for Large Language Model Serving with PagedAttention

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.06180)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：服务大语言模型时，每个请求的 KV 缓存（生成时保存的历史 Key、Value）很大，而且随生成动态增长；已有系统把它放在连续显存里，按最大长度预留，产生大量碎片，又无法在请求之间共享，于是一批能同时处理的请求数受限，吞吐上不去。原文测得已有系统的 KV 缓存显存中只有 20.4%–38.2% 真正存着 token 状态（§1、Fig.2）。
- **核心方法**：PagedAttention：借用操作系统的分页虚拟内存，把每个请求的 KV 缓存切成固定大小的块，块在显存里可以不连续，按需分配，并允许多个采样分支或共享前缀共用同一块（写时复制）。在此之上实现服务系统 vLLM。KV 缓存的有效占比提高到 96.3%（Fig.2）；同等延迟下吞吐比 FasterTransformer 和 Orca 高 2–4 倍，ShareGPT 负载上可承受的请求率比 Orca（Oracle）高 1.7–2.7 倍（§6.2）；beam 宽度为 6 时提升到 2.3 倍（§6.3）。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"推理效率"一节中"批处理与显存管理"的代表：推理时多采样、长思考都要靠它把一张卡上的并发做大；best-of-N 与 beam 搜索的共享前缀正是它的分页共享最省的场景。自述局限：分页对训练这类张量形状固定的负载、或计算受限的服务未必有利，attention kernel 本身比 FasterTransformer 慢 20%–26%（§7–8）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2309.06180 · [全文](https://arxiv.org/pdf/2309.06180) · UC Berkeley、Stanford、UC San Diego 等
- 方向：llm/inference
