# A Programming Paradigm for Spatiotemporal Composability

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2608.25512)

- **解决什么**：动态软件组件怎样在卸载时清理自身影响，并在依赖变化时正确启停。
- **核心方法**：将可撤销 effect（组件产生且可清理的作用）、响应式 coeffect（随外部依赖变化的需求）和统一 context（中介组件交互的上下文）组成动态组件演算，并由 Cordis 实现。
- **为什么在这个库里**：补充[权限、隔离与协作](../../fields/agents/permissions-isolation-collaboration.md)的运行时组件生命周期视角；DeepSeek Harness 官方说明由 Cordis 驱动，这一关联不把该论文变成长程记忆算法。优先级：选读。
