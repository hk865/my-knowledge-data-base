# Agent approvals & security

> 状态：资料卡 · 动态文档 · [原文](https://learn.chatgpt.com/docs/agent-approvals-security)

- **解决什么**：Agent 的执行沙箱、动作审批和网络入口各自覆盖什么。
- **核心方法**：本地 OS 沙箱与动作审批分别约束技术执行面和审批流程；文档明确 command-network 控制自身不关闭 hosted web search、apps 或 MCP。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
