# Generalizing Verifiable Instruction Following

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2507.02833)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：精确指令遵循（满足"只回答是或否""某个词至少出现 3 次"这类可程序验证的输出约束）的主流评测 IFEval 只有 25 种约束模板，很快被做满：模型学会的是遵循约束，还是只学会了这 25 种？
- **核心方法**：IFBench 用 58 种新的、域外的可验证约束（计数、格式、句子/单词/字符操作、复制等）测泛化：GPT-4.1、Claude 3.7 Sonnet 等领先模型在 IFEval 上都很高，在 IFBench 上低于 50%，作者据此认为多数模型过拟合了 IFEval 的约束集。训练侧为每种约束写验证函数做可验证奖励的强化学习（IF-RLVR，用 GRPO），另发布 29 种新的训练约束：同样数据、同样起点下 GRPO 一致优于 DPO；IF-RLVR 同时提升 IFEval 与 IFBench，但略微损害 AlpacaEval 2 这类对话评测。§5 讨论约束与主任务冲突时（例如要求单句摘要的每个词首字母依次递增）模型怎样取舍，即奖励黑客与指令层级问题。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"指令与格式遵循"一节：可验证约束既是评测又是奖励，换一组约束分数就掉，是"评测一旦成为训练目标就会被过拟合"的干净例子。与同团队的 [Tulu 3](../../../llm/papers/arxiv-2411.15124/README.md)（RLVR 用于约束遵循，降低 KL 惩罚后出现只为满足约束的怪异输出）连读。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2507.02833 · [全文 PDF](https://arxiv.org/pdf/2507.02833) · Allen Institute for AI、University of Washington
- 发表：NeurIPS 2025 Datasets and Benchmarks
- 方向：cross-domain/evaluation、llm/posttraining/rl
