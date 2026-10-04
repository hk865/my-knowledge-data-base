# Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.09078)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CoT 与 ToT（思维树：把推理展开成树并搜索）通常只做一遍推理，走错的路径难以回头修正。
- **核心方法**：相对单棵 ToT，并行构建多棵推理树做集体决策：用稀疏激活只保留最相关的推理路径，加入实时的动态自我纠错，并用共识引导的决策在正确率与计算量之间权衡。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)中"搜索结构"一支的组合式变体，可与 [Large Language Monkeys](../arxiv-2407.21787/README.md) 的简单重复采样对照，看结构化搜索在同等预算下多出多少。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2412.09078 · [全文 PDF](https://arxiv.org/pdf/2412.09078) · 预印本（v5）
- 作者：Zhenni Bi、Kai Han、Chuanjian Liu、Yehui Tang、Yunhe Wang（华为诺亚方舟实验室）
- 方向：llm/inference
