# Bridging Semantics and Physics with Constrained LLMs for Safe and Trustworthy Robotic Manipulation

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2608.29379)

- **解决什么**：LLM的语义选择怎样在执行前经过参数、运动学与碰撞检查，减少自然语言与物理动作之间的错配。
- **核心方法**：相对无约束语言到动作映射，把对象绑定和有限技能调用通过MCP（模型调用外部工具的通信协议）的结构化参数检查，再由固定状态机与MoveIt Task Constructor（运动规划任务构造器）生成并验证轨迹。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中的有类型工具和几何检查参照，明确通用模型能决定什么以及执行器还需验证什么。优先级：选读。
