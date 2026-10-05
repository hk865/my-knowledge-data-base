# MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2602.16313)

- **解决什么**：评价 Agent 是否真正利用前几次会话的信息完成后续行动。
- **核心方法**：把显式相互依赖的任务放入跨会话的记忆—智能体—环境循环，在购物、旅行计划、渐进搜索和数理推导中比较记忆方案及长上下文对照。
- **为什么在这个库里**：是[工程记忆讲义](../../fields/agents/memory-evidence-loop.md)的评测入口，联合观察任务成功、子任务进度与延迟；作者结果显示记忆收益随任务和依赖深度变化。优先级：必读。
