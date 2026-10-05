# MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2608.13883)

- **解决什么**：在相同任务与执行框架下，替换记忆后端会怎样改变后续行动效果。
- **核心方法**：在 MemoryArena 的五个评测域，以相同框架、请求模型别名、样本和评分代码比较 MemoryLake、Mem0、向量检索增强生成与长上下文。
- **为什么在这个库里**：对应[工程记忆讲义](../../fields/agents/memory-evidence-loop.md)的对照设计：整套后端同时改变写入、检索、预算和提示组装，结果不能单独归因于图结构，实验也未匹配成本。优先级：选读。
