# namespaces(7) — Linux manual page

> 状态：资料卡 · 动态文档 · [原文](https://man7.org/linux/man-pages/man7/namespaces.7.html)

- **解决什么**：如何让不同进程看到不同的系统资源视图。
- **核心方法**：namespace 将全局系统资源呈现为实例化视图；类型覆盖 PID、mount、network、user 等不同资源。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
