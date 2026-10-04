# Docker Engine security

> 状态：资料卡 · 动态文档 · [原文](https://docs.docker.com/engine/security/)

- **解决什么**：容器怎样限制进程，又在哪些地方仍依赖宿主和部署配置。
- **核心方法**：Docker 组合 namespace、cgroup、capabilities 与内核安全机制；cgroup 主要计量/限制资源，不能据此认定跨容器数据访问被授权隔离；daemon 控制权和主机挂载本身是关键风险面。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
