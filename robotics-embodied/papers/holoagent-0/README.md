# HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory

> 状态：逐步教学版 · 2026 · [原文](https://arxiv.org/abs/2606.23565)

[返回机器人与具身目录](../../README.md)

- **解决什么**：LLM Agent 在数字环境里"推理—调用工具—看反馈—修正"的循环，很难直接搬到实体机器人：物理执行是连续的、依赖本体、不确定，还受安全约束；现有具身能力多是孤立模块或松散耦合的决策循环。
- **核心方法**：相对 [ReAct](../../../cross-domain/papers/react/README.md) 式的数字 Agent 循环，加入三层耦合结构：Embodied AgentOS 把语言指令转成可执行技能图、调度机器人资源、监控执行，并根据运行反馈触发澄清或重新规划；3D 空间记忆负责把指令落到物理世界；具身技能负责动作。在实机上评测空间记忆、长程导航和闭环执行（动作生成、找物、多机协作、移动操作）。
- **为什么在这个库里**：[具身 Agents](../../fields/embodied-agents/README.md)方向"空间记忆"一格；与 [MEMORA](../memora/README.md)（经历记忆）对照读。优先级：选读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:2606.23565（Zhou 等 12 位作者；v1，2026-06）
- 全文：[arXiv PDF v1](https://arxiv.org/pdf/2606.23565v1)
- 方向：[具身 Agents](../../fields/embodied-agents/README.md)（跨领域另见[智能体](../../../cross-domain/fields/agents/README.md)）
