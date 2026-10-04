# git-worktree - Manage multiple working trees

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://git-scm.com/docs/git-worktree
- 类型：官方技术文档，非论文
- 日期：动态资料，无固定发表日期
- 日期依据：页面标注 manual last updated in 2.56.0，版本日期 2026-09-28；这不是 worktree 发明/论文发布日期
- [原文入口](https://git-scm.com/docs/git-worktree)
- 阅读版本：2.56.0
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

linked worktree 支持同一仓库多个工作目录，除 HEAD、index 等每工作树文件外仍共享仓库内容。

- 实际阅读范围：name_description_commands_shared_repository
- 证据边界：由共享语义可推断：worktree 解决开发并行/文件冲突组织，单独使用不能构成进程、身份或网络安全隔离。 该安全结论是由官方共享语义作出的工程推论，不是手册声称的安全保证。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)

只保留公开原文链接，不镜像第三方全文。
