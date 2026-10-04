# Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.19309)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：标准投机解码只接受与目标模型分布对齐的草稿 token，很多客观上正确的续写也被拒绝；即使用 GPT-4o 或人写的文本做草稿，接受率也不高，加速上限因此受限。
- **核心方法**：借鉴 LLM 当评审（LLM-as-a-judge）的思路，相对标准投机解码（小模型先草拟、大模型并行验证的加速解码）的验证规则，在冻结的目标模型最后一层隐状态上训练一个小的线性"评审"头，判断当前草稿 token 是否正确；标准接受与评审接受任一成立即接受。在 Llama-3.1 系列上，8B/405B-Judge 比 Llama-405B 快约 9 倍，并在多项基准上保持质量。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"放宽验证"一格：以经验上的质量保持换接受率，不再保证目标分布。与 [Leviathan 等的投机解码](../arxiv-2211.17192/README.md) 的精确保证对照。优先级：选读。

## 批注

**易误读**
- 约 9 倍的加速以 HuggingFace 实现为基线；在优化过的 GPT-fast 框架下对照，加速约 3.9 倍，两组数字不能混用（§5.1、Table 1）。评审头可能误接受，所以论文要求同时测生成质量。

## 身份信息

- 稳定标识：arxiv:2501.19309 · [全文 PDF](https://arxiv.org/pdf/2501.19309) · ICLR 2025
- 作者：Gregor Bachmann、Sotiris Anagnostidis、Albert Pumarola、Markos Georgopoulos、Artsiom Sanakoyeu、Yuming Du、Edgar Schönfeld、Ali Thabet、Jonas Kohler（Meta GenAI、ETH Zürich）
- 方向：llm/inference
