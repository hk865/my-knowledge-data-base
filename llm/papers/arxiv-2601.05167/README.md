# RelayLLM: Efficient Reasoning via Collaborative Decoding

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.05167)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大模型推理成本高、延迟大，小模型推理能力不够；已有的级联或路由把整个查询交给大模型，粒度太粗，小模型能完成的大部分步骤也被浪费。
- **核心方法**：提出 token 级的协作解码：小模型做主控，需要时输出特殊命令 `<call>n</call>` 暂停，由大模型续写 n 个 token 后交还（大模型也可提前结束）；用预热加 GRPO（组相对策略优化，一种不需要价值网络的强化学习算法）两阶段训练小模型，平衡独立生成与适时求助。六个基准的平均准确率为 49.52%，大模型只生成了全部 token 的 1.07%，与表现相当的随机路由器相比成本降低 98.2%。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"大小模型协作与关键段接管"一格：大模型真正生成关键片段，而不是批量验证草稿；只有经验上的准确率—成本折中，没有分布保证。与 [Faster Cascades](../arxiv-2405.19261/README.md)、[BiLD](../arxiv-2302.07863/README.md) 对照。优先级：选读。

## 批注

**易误读**
- 1.07% 是大模型生成的 token 占比，不等于端到端节省的时间比例；训练与评测集中在数学推理基准。

## 身份信息

- 稳定标识：arxiv:2601.05167 · [全文 PDF](https://arxiv.org/pdf/2601.05167)
- 作者：Chengsong Huang、Tong Zheng、Langlin Huang、Jinyuan Li、Haolin Liu、Jiaxin Huang（圣路易斯华盛顿大学、马里兰大学、弗吉尼亚大学）
- 方向：llm/inference
