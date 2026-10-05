# SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.28434)

- **解决什么**：长程编码任务中的交互历史越来越长，固定时机和粒度的压缩容易丢掉关键材料。
- **核心方法**：让智能体学习何时、压缩哪段以及怎样压缩，结合合成轨迹与记忆感知的 GRPO（组内相对策略优化，以同组候选的相对表现更新策略）联合训练记忆管理和任务解决。
- **为什么在这个库里**：对应[工程记忆闭环](../../fields/agents/memory-evidence-loop.md)中的工作上下文管理；它主要研究任务内压缩，跨会话事件记录与跨项目经验迁移需要另行评价。优先级：选读。
