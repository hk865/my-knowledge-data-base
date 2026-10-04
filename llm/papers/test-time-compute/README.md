# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

> 状态：技术精读 · 2024 · [原文](https://arxiv.org/abs/2408.03314)

[返回大语言模型目录](../../README.md)

- **解决什么**：给模型一份固定但不小的推理计算预算，它在难题上能提升多少，预算怎样分配最有效。
- **核心方法**：比较两类扩展推理计算的机制：用过程奖励模型（PRM：给推理的每一步打分的验证器）引导搜索，以及训练模型在旧答案上顺序修订。发现哪种更有效取决于题目难度，于是按估计的难度为每个提示自适应分配计算（compute-optimal）。相对 best-of-N（独立生成 N 个答案再选最好的），效率提高 4 倍以上；在 FLOPs 相同的比较中，对小模型已有一定成功率的题目，可以超过 14 倍大的模型。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)的核心基线，回答"推理计算能否替代预训练计算"。与 [Large Language Monkeys](../arxiv-2407.21787/README.md)（重复采样的覆盖率）、[s1](../arxiv-2501.19393/README.md)（控制思考长度）对照。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

[Language Models are Few-Shot Learners](../gpt3/README.md) → [Training language models to follow instructions with human feedback](../instructgpt/README.md) → 本篇（教学顺序，不表示直接继承）。

## 身份信息

- 稳定标识：arxiv:2408.03314 · [全文 PDF](https://arxiv.org/pdf/2408.03314v1) · 精读依据 v1
- 作者：Charlie Snell、Jaehoon Lee、Kelvin Xu、Aviral Kumar（UC Berkeley、Google DeepMind）
- 方向：llm/inference
