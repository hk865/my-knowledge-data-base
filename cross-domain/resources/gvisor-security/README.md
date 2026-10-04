# Security Model

> 状态：资料卡 · 动态文档 · [原文](https://gvisor.dev/docs/architecture_guide/security/)

- **解决什么**：怎样减少不可信应用对宿主内核接口的直接接触。
- **核心方法**：Sentry 重实现应用可见 System API，减少对宿主 API 的直接暴露；VM 则通过 guest OS/虚拟设备改变边界；资源耗尽仍依赖宿主 cgroup，网络策略需另施加；硬件侧信道不是其一般防护保证。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
