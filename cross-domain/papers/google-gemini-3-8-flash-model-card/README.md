# Gemini 3.8 Flash Model Card

> 状态：文献卡 · 2026 · [原文](https://deepmind.google/models/model-cards/gemini-3-8-flash/)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Google DeepMind 2026-09-02 发布的 Gemini 3.8 Flash 的模型卡：用途、评测、已知局限与安全评估，面向"可规模化的生产级智能体"。
- **核心方法**：模型卡本身很短，结构、数据与训练细节都指向 Gemini 3.7 Flash 的模型卡。评测表与 Gemini 3.7 Flash、Claude Opus 5、Claude Sonnet 5、GPT-5.6 Sol、GPT-5.6 Terra 并列：Terminal-bench 2.1 上六个模型都在 80.4%–89.4%，Terminal-bench 4.0 上从 11.2% 到 51.8%（3.8 Flash 19.1%，Opus 5 51.8%）；DeepSWE v1.1 标为"长程软件工程"，3.8 Flash 73.7%。已知局限写明幻觉、偶发的变慢或超时、高努力档下为追求表现多用 token。安全一节有一项"语气"（Tone）自动评测，定义为"衡量回答的客观语气"，在敏感话题上与上一版比较，3.8 Flash 相对 3.7 Flash +0.2 个百分点；没有单列迎合（sycophancy）评测。
- **为什么在这个库里**：截至 2026-10-04，Gemini 最新的文本模型卡（模型卡列表中最新的 Pro 级卡片仍是 [Gemini 3.1 Pro](https://deepmind.google/models/model-cards/gemini-3-1-pro/)，2026-02-19，它的语气评测定义为"衡量拒答时的客观语气"）。在[思考笔记](../../../perspectives/notes/model-behavior.md)第 4 条里作为 Gemini 的官方对照；在[观点页](../../../perspectives/eval-shapes-models.md)里作为"短的终端 benchmark 已经分不开前沿模型、长的版本才拉开差距"的证据。优先级：选读。

## 身份信息

- 稳定标识：url:https://deepmind.google/models/model-cards/gemini-3-8-flash/ · [模型卡列表](https://deepmind.google/models/model-cards/)
- 作者：Google DeepMind（2026-09-02）
- 开放情况：官方模型卡，模型未开放；评测方法另见 deepmind.com/models/evals-methodology/gemini-3-8-flash（未打开）。
- 方向：cross-domain/evaluation、cross-domain/agents
