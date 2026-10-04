# GPQA: A Graduate-Level Google-Proof Q&A Benchmark

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.12022)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：可扩展监督（scalable oversight：人怎样监督在某领域超过自己的模型）的实验需要一类题：领域专家知道答案，而有能力、有动机、能上网的非专家也做不出（§1）。
- **核心方法**：生物、物理、化学的博士（含在读）出题，经"专家验证 → 修改 → 第二位专家验证 → 三位非专家验证"四步；非专家是其他领域的博士，平均每题花 37 分钟、可用除 LLM 以外的任何网络资源。主集 448 题，筛选更严的 Diamond 子集 198 题。专家准确率 65%（扣除事后承认的明显失误为 74%），非专家 34%，GPT-4 few-shot CoT 39%（随机为 25%）。作者请求不要在网上以明文或图片公开题目，并在数据中加入 canary 字符串（一段特殊标记，供训练语料过滤）。自述局限：只有 448 题，要 50%→60% 这种量级的差别才有 80% 的统计功效；专家来自 Upwork，不代表科研实践中的题目分布。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)主线中"难到网上搜不到"的一步，Diamond 子集后来成为推理模型发布的常用指标；它的出发点是监督而不是排名，与本库的 [weak judging strong](../arxiv-2407.04622/README.md) 同属可扩展监督问题。"小题集的统计功效"和"公开时防泄漏"两个口径都以它为例。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2311.12022 · [全文 PDF](https://arxiv.org/pdf/2311.12022) · New York University、Cohere、Anthropic
- 发表：arXiv 预印本（v1）
- 方向：cross-domain/evaluation、cross-domain/model-science
