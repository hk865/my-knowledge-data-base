# Control Group v2

> 状态：资料卡 · 动态文档 · [原文](https://docs.kernel.org/admin-guide/cgroup-v2.html)

- **解决什么**：怎样限制任务占用的 CPU、内存等资源并组织层级预算。
- **核心方法**：cgroup 将进程分层组织，以 controller 分配/约束系统资源；下层不能取消上层资源限制。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
