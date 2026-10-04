# OLMo: Accelerating the Science of Language Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.00838)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：最强的语言模型越来越封闭，训练数据、架构和开发细节不公开，研究者无法科学地研究这些模型及其偏差与风险。
- **核心方法**：相对大多只发布权重和推理代码的开放模型，本篇把训练数据（Dolma）、训练与评估代码、训练日志和数百个中间检查点一起公开。发布 7B 规模的四个变体（架构、优化器、训练硬件不同）和一个 1B 模型，都训练了至少 2T token。
- **为什么在这个库里**：[训练科学方向](../../../cross-domain/fields/training-science/README.md)与[预训练方向](../../fields/pretraining/README.md)的实验材料来源：中间检查点让"训练过程中模型发生了什么"可以直接研究。例如 [How Do Large Language Models Acquire Factual Knowledge During Pretraining?](../../../cross-domain/papers/arxiv-2406.11813/README.md) 就是从 OLMo 的中途检查点续训来追踪事实知识。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2402.00838 · [全文 PDF](https://arxiv.org/pdf/2402.00838)
- 作者：Dirk Groeneveld、Iz Beltagy、Pete Walsh、Akshita Bhagia 等 43 位（Allen Institute for AI 为主，另有华盛顿大学、耶鲁、NYU、CMU 作者）
- 方向：llm/pretraining、cross-domain/training-science、cross-domain/model-science
