# How Cedar authorization works

> 状态：资料卡 · 动态文档 · [原文](https://docs.cedarpolicy.com/auth/authorization.html)

- **解决什么**：如何把“谁能对什么做什么”写成可执行的授权策略。
- **核心方法**：应用为 principal/action/resource/context 调用 authorizer；无匹配 permit 默认拒绝，匹配 forbid 优先，错误 policy 被跳过并回报 diagnostics。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：必读。
