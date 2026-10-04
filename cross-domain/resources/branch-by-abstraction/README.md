# Branch By Abstraction

> 状态：资料卡 · 2014 · [原文](https://martinfowler.com/bliki/BranchByAbstraction.html)

- **解决什么**：大型替换怎样在保持系统可运行的同时逐步完成。
- **核心方法**：先用抽象层承接旧实现，再使新旧实现共存，逐段切换并最终删除旧实现；全过程保持可构建、可运行、可发布，降低一次性替换风险。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：看迁移中间态如何保持功能，而非只画最终目标结构。优先级：选读。
