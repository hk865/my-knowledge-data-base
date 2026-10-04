# Building multi-agent systems: When and how to use them

> 状态：资料卡 · 2026 · [原文](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)

- **解决什么**：哪些任务值得增加 Agent，怎样划出有效的上下文边界。
- **核心方法**：多Agent的明确收益来自上下文隔离、可独立并行工作、专门工具或领域上下文；按上下文边界拆任务；同一功能的实现和测试通常共享上下文，黑盒核验可独立；核验须有明确标准并检查边界/失败场景，防止过早宣告通过。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：先定位单Agent瓶颈，再证明新增协调边界值得；干净API边界比角色名称更重要。优先级：必读。
