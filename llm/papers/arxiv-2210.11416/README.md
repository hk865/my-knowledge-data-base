# Scaling Instruction-Finetuned Language Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2210.11416)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：指令微调在任务数、模型规模和思维链数据三个方向上继续扩大，收益是否还在。
- **核心方法**：把指令微调扩大到 1,836 个任务（473 个数据集），覆盖 PaLM、T5、U-PaLM；Flan-PaLM 540B 平均比 PaLM 540B 高 9.4 个百分点，五样本 MMLU 达到 75.2%（该数字用了思维链与自洽采样）。关键发现：不含思维链（CoT，一句话：先写出中间推理再给答案）数据的指令微调会损害思维链推理，只加入 9 个思维链数据集就能在所有评测上改善。公开了 Flan-T5 权重。
- **为什么在这个库里**：[SFT Baseline 表](../../fields/posttraining/sft/BASELINES.md)"数据配比"一格的早期证据：示范里有没有推理过程，决定 SFT 之后推理能力保不保得住；2025 年长思维链冷启动数据是这一点的延续。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2210.11416 · [全文 PDF](https://arxiv.org/pdf/2210.11416) · Google
- 方向：llm/posttraining/sft
