# Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2502.18080)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：一味延长思维链（CoT）来扩展测试时计算，会不会反而损害推理表现。
- **核心方法**：在数学推理上发现，更长的 CoT 在某些领域确实降低表现，且最优的长度分布随领域而不同。据此提出 Thinking-Optimal Scaling：先用少量回答长度分布不同的种子数据（由 QwQ-32B-Preview 生成）教模型使用不同的推理强度，再让模型在更多问题上取各推理强度下最短的正确回答做自我改进。基于 Qwen2.5-32B-Instruct 的模型在多个数学基准上超过其他蒸馏得到的 32B o1 类模型，与种子数据的来源 QwQ-32B-Preview 相当。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"思考越长越好吗"一问的证据；与 [Do NOT Think That Much for 2+3=?](../url-https-proceedings.mlr.press-v267-chen25bx.html/README.md) 一起说明思考长度需要按问题分配。在[监督微调方向](../../fields/posttraining/sft/README.md)里属于自我改进式的数据构造。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2502.18080 · [全文 PDF](https://arxiv.org/pdf/2502.18080) · NeurIPS 2025
- 作者：Wenkai Yang、Shuming Ma、Yankai Lin、Furu Wei（中国人民大学高瓴人工智能学院、Microsoft Research）
- 方向：llm/inference、llm/posttraining/sft
