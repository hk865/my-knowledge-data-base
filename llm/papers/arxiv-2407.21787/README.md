# Large Language Monkeys: Scaling Inference Compute with Repeated Sampling

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2407.21787)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：推理时通常只让模型对一个问题尝试一次；本篇把重复采样当作扩展推理计算的另一条轴，看收益怎样随样本数变化。
- **核心方法**：对同一问题独立采样大量候选。覆盖率（任一样本解出的题目比例）在四个数量级的样本数上持续增长，常呈对数线性，可用指数化的幂律拟合。在能自动验证的领域（代码、形式证明），覆盖率直接变成成绩：DeepSeek-Coder-V2-Instruct 在 SWE-bench Lite 上从 1 个样本的 15.9% 升到 250 个样本的 56%，高于当时单样本最好的 43%。没有自动验证器时，多数投票和奖励模型在几百个样本后就进入平台。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)中"验证器决定扩展上限"一问的核心证据：覆盖率与实际选中正确答案之间的差距，就是验证器的差距。与 [测试时计算预算](../test-time-compute/README.md) 的预算分配对照阅读。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2407.21787 · [全文 PDF](https://arxiv.org/pdf/2407.21787)
- 作者：Bradley Brown、Jordan Juravsky、Ryan Ehrlich、Ronald Clark、Quoc V. Le、Christopher Ré、Azalia Mirhoseini（斯坦福、牛津、Google DeepMind）
- 方向：llm/inference
