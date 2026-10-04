# Landlock: unprivileged access control

> 状态：资料卡 · 动态文档 · [原文](https://docs.kernel.org/userspace-api/landlock.html)

- **解决什么**：普通进程怎样主动收紧自己及后代的资源访问权限。
- **核心方法**：Landlock 是可叠加 LSM，允许非特权进程收紧自身及后代的访问；路径须同时通过全部 Landlock 层、DAC 和其他 LSM 控制。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
