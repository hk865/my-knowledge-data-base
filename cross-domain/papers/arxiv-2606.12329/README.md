# PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.12329)

- **解决什么**：跨会话开发怎样保留失败尝试、设计理由及旧决策被替代的历史。
- **核心方法**：相对单份不断改写的项目摘要，用本地只追加事件保存问题、尝试、修复、决策和笔记，确定性生成摘要，按文件提供编辑前历史警告，并显式记录决策替代。
- **为什么在这个库里**：是[工程记忆闭环](../../fields/agents/memory-evidence-loop.md)的持久记录参照；v2 属可行性研究，编辑前检查提供历史提示，尚未证明能减少重复失败。优先级：选读。
