# MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.03192)

- **解决什么**：语义相似的旧经验可能无助于当前行动，需要知道哪些经验实际有用。
- **核心方法**：在冻结模型权重的条件下保存意图、经验、效用三元组，在语义召回之后结合效用选择，再用环境反馈更新记忆效用。
- **为什么在这个库里**：对应[工程记忆闭环](../../fields/agents/memory-evidence-loop.md)的经验选择环节；效用衡量任务帮助程度，事实可信度仍需证据，多条经验的信用分配仍有歧义。优先级：选读。
