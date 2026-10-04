# Language Models are Few-Shot Learners

> 状态：技术精读 · 2020 · [原文](https://arxiv.org/abs/2005.14165)

[返回大语言模型目录](../../README.md)

- **解决什么**：预训练后仍要为每个任务准备成千上万条标注做微调；人只看几个例子或一句说明就能做新任务。
- **核心方法**：沿用 GPT-2 式的自回归 Transformer，把规模扩到 175B（共训练 8 个规模），评测时完全不更新参数，只在输入里放任务说明和 0 个、1 个或少量示例（上下文学习：模型从提示中的示例推断任务，权重不变）。少样本设置在翻译、问答、完形填空等任务上有时接近此前微调的最好结果，同时报告了仍然吃力的数据集，以及网页训练数据带来的测试污染问题。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"预训练学到了什么"的历史起点：规模扩大后，任务可以写进提示。它的目标只是续写、不对齐用户意图，这一局限直接引出 [InstructGPT](../instructgpt/README.md)。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

[Attention Is All You Need](../transformer/README.md)（自回归 Transformer 的结构）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2005.14165 · [全文 PDF](https://arxiv.org/pdf/2005.14165v4) · 精读依据 v4
- 作者：Tom B. Brown、Benjamin Mann、Nick Ryder、Melanie Subbiah、Jared Kaplan 等 31 位（OpenAI）
- 方向：llm/pretraining、llm/architecture、cross-domain/model-science、cross-domain/agents
