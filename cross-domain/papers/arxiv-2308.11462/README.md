# LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2308.11462)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LLM 能做哪些类型的法律推理？缺少由法律专业人士设计、法律界与 ML 界都能使用的测量工具。
- **核心方法**：协作构建 162 个任务，按美国法学教育常用的 IRAC 框架分为六类法律推理：识别争点、回忆规则、适用规则、得出结论、解释（合同条款等文本）、理解修辞。分类任务用精确匹配与平衡准确率，抽取任务用 F1；"适用规则"任务要求写出推理过程，由受过法律训练的人按公开的评分指南人工评分，只评了 GPT-4、GPT-3.5、Claude-1。评测 20 个开源与商用模型：GPT-4 各类最好，但它的"回忆规则"只有 59.2，远低于"得出结论"的 89.9。作者说明提示没有精调，结果是下限。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"法律"一节：规则回忆（最接近"凭记忆引用法条和判例"、也最容易幻觉的一类）是所有模型的短板；任务按推理类型拆开，比单一的律师考试分数更能看出差在哪里。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2308.11462 · [全文 PDF](https://arxiv.org/pdf/2308.11462) · Stanford 牵头，40 位作者来自法学院、律所与 ML 团队
- 发表：NeurIPS 2023 Datasets and Benchmarks（Advances in Neural Information Processing Systems 36）
- 方向：cross-domain/evaluation
