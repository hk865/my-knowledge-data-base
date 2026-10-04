# GAIA: a benchmark for General AI Assistants

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.12983)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：AI benchmark 追逐对人越来越难的任务；GAIA 反其道而行：选对人概念上简单、对最强的 AI 仍困难的真实问题（摘要、§3.1）。
- **核心方法**：466 道需要检索、浏览、读文件、多步推理与工具组合的问题，按步骤数与工具数分三级；答案是简短、无歧义的事实，按类型归一化后近似精确匹配判分（§3.2）。只公开 166 道带答案的开发集，其余 300 道的答案保留，用于排行榜（§1）。人类 92%，配插件的 GPT-4 约 15%（摘要；后者由人工挑选插件得到，作者称不可精确复现）；最难一级 GPT-4 为 0%。自述局限（§6）：不评估得出答案的过程；仍有歧义；只有英文；会随预训练数据污染与网页消失而衰减（§5）。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"真实环境 benchmark"阶段的通用助手评测；答案隐藏的测试集是"评测数据被藏起来以防被优化"的典型做法，与[评估方向](../../fields/evaluation/README.md)讨论的隐藏数据相呼应。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2311.12983 · [全文 PDF](https://arxiv.org/pdf/2311.12983)
- 作者：Grégoire Mialon、Clémentine Fourrier、Craig Swift、Thomas Wolf、Yann LeCun、Thomas Scialom（Meta（FAIR、GenAI）、Hugging Face、AutoGPT）
- 开放情况：开发集公开（Hugging Face gaia-benchmark，门控）；测试集答案不公开。
- 方向：cross-domain/agents、cross-domain/evaluation
