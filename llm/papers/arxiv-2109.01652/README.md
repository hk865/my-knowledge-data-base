# Finetuned Language Models Are Zero-Shot Learners

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2109.01652)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让预训练语言模型不靠提示里的示例，也能完成训练时没见过的任务类型（zero-shot）。
- **核心方法**：把 60 多个 NLP 数据集改写成自然语言指令模板，对 137B 的 LaMDA-PT 做指令微调（instruction tuning，一句话：在"指令 + 答案"格式的多任务数据上继续训练），按任务簇留出评测；在 25 个数据集中 20 个上超过 zero-shot 的 175B GPT-3。作者写明两处做不好：任务本身就是续写句子时（常识推理、指代消解），7 个任务中只在 3 个上超过未微调的 LaMDA-PT；8B 及更小的模型上，指令微调反而损害没见过任务上的表现，作者推测小模型的容量被训练任务占满（§4.2）。
- **为什么在这个库里**：[SFT Baseline 表](../../fields/posttraining/sft/BASELINES.md)中"数据来源 = 公开 NLP 任务改写"一格的起点。InstructGPT 用 FLAN 数据微调的 175B GPT-3 作对照，在真实 API 提示上偏好胜率低于 InstructGPT，说明公开任务的分布与用户请求不同。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2109.01652 · [全文 PDF](https://arxiv.org/pdf/2109.01652) · Google Research · ICLR 2022
- 方向：llm/posttraining/sft
