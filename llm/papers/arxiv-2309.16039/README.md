# Effective Long-Context Scaling of Foundation Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.16039)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：缺少公开、可复现的长上下文训练配方；当时的开源长上下文模型评测不充分，扩长之后又难以保住短任务表现（§1）。
- **核心方法**：从 Llama 2 检查点继续预训练 400B token（7B/13B 用 32,768 长度，34B/70B 用 16,384），并把 RoPE 的基频从 10,000 提高到 500,000（ABF，Adjusted Base Frequency，§2.1、§4.1）；长指令数据由 Llama 2 Chat 自动生成，不需要人工标注。§4.2 的数据消融结论是：调整预训练数据的长度分布没有明显收益，提升主要来自数据质量，很少的长文本也能训出长上下文能力；§4.4 显示从短上下文模型继续训练比从头用长序列训练约省 40% FLOPs。70B 的短任务没有退化反而上升（MMLU 71.7 对 Llama 2 的 68.9）；ZeroSCROLLS 平均 37.7，高于 gpt-3.5-turbo-16k 的 36.7、低于 Claude 的 39.1。
- **为什么在这个库里**：[长上下文方向](../../fields/long-context/README.md)"数据与课程"一环的公开配方，"提高 RoPE 基频 + 在预训练末段继续训练"后来被 Qwen 系列（ABF）沿用。自述局限：没有针对广泛的长上下文应用微调、分词器比 GPT-3.5 多用约 10% 的 token、幻觉。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2309.16039 · [全文](https://arxiv.org/pdf/2309.16039) · Meta（GenAI）
- 方向：llm/long-context、llm/pretraining
