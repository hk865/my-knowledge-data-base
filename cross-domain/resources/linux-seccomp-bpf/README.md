# Seccomp BPF (SECure COMPuting with filters)

> 状态：资料卡 · 动态文档 · [原文](https://docs.kernel.org/userspace-api/seccomp_filter.html)

- **解决什么**：怎样缩小进程可调用的内核接口集合。
- **核心方法**：seccomp 以系统调用号/参数等元数据过滤调用，缩小暴露内核面；原文明说 syscall filtering 不是完整沙箱，逻辑行为与信息流还需其他加固/LSM。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
