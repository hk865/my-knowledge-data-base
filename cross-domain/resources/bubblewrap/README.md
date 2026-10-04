# Bubblewrap

> 状态：资料卡 · 动态文档 · [原文](https://github.com/containers/bubblewrap)

- **解决什么**：怎样把 namespace、挂载和其他系统机制组装为应用沙箱。
- **核心方法**：bubblewrap 是构建沙箱的低层工具；保护范围取决于调用参数，策略由包装它的框架决定；暴露的 socket/挂载也可能扩大权限。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
