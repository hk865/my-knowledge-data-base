# Self-Instruct: Aligning Language Models with Self-Generated Instructions

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2212.10560)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：指令微调依赖人写的指令数据，数量、多样性和创造性都有限。
- **核心方法**：让 GPT-3 从 175 个人写种子任务出发，自己生成指令、输入和输出，过滤无效或过于相似的样本后得到约 5.2 万条指令，再用它们微调 GPT-3 自身；在 Super-NaturalInstructions 上比原模型绝对提高 33%，与用私有用户数据和人工标注训练的 InstructGPT001 相当。作者自述：方法继承语言模型自身的局限，收益多集中在预训练中常见的用法上，长尾情形可能收益很小，并可能强化模型已有的偏见（§8）。
- **为什么在这个库里**：[SFT Baseline 表](../../fields/posttraining/sft/BASELINES.md)中"数据来源 = 模型自生成"一格的起点；此后 Alpaca、Llama 3 的合成数据、R1 的蒸馏数据都是"让模型写示范"这条线的延伸。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2212.10560 · [全文 PDF](https://arxiv.org/pdf/2212.10560) · 华盛顿大学、AI2 等 · ACL 2023
- 方向：llm/posttraining/sft
