# git-worktree - Manage multiple working trees

> 状态：资料卡 · 动态文档 · [原文](https://git-scm.com/docs/git-worktree)

- **解决什么**：多个任务怎样在同一 Git 仓库中使用独立工作目录。
- **核心方法**：linked worktree 支持同一仓库多个工作目录，除 HEAD、index 等每工作树文件外仍共享仓库内容。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：必读。
