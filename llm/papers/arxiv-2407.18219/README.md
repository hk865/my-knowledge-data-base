# Recursive Introspection: Teaching Language Model Agents How to Self-Improve

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2407.18219)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：即使明确告诉模型"你错了"，最强的 LLM 也难以在多轮中持续改进自己的答案。
- **核心方法**：提出 RISE：把单轮提示的微调写成多轮马尔可夫决策过程（初始状态是提示，每一轮是一次新尝试），借鉴在线模仿学习与强化学习收集多轮数据，在模型先前失败的尝试之后提供改进后的回答作为监督，迭代微调，可选地加入环境反馈。在同等推理计算下，Llama2、Llama3、Mistral 在数学推理上随轮数增加而提高，优于几种单轮策略；能力更强的模型获益更大。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)中"顺序修订"一支的训练侧方法：[测试时计算预算](../test-time-compute/README.md)指出修订能力需要专门训练，RISE 给出一种训练办法。也属于[监督微调方向](../../fields/posttraining/sft/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2407.18219 · [全文 PDF](https://arxiv.org/pdf/2407.18219)
- 作者：Yuxiao Qu、Tianjun Zhang、Naman Garg、Aviral Kumar（CMU、UC Berkeley、MultiOn）
- 方向：llm/inference、llm/posttraining/sft、cross-domain/agents
