# Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents

> 状态：逐步教学版 · 2026 · [原文](https://arxiv.org/abs/2609.37810)

[返回机器人与具身目录](../../README.md)

- **解决什么**：通用多模态 Agent 能零样本解机器人任务，但每次都从头推理、从头探索物理世界，执行成本高。
- **核心方法**：提出 RoboSkill 的"探索—执行—演化"循环：探索收集任务信息，执行时按反馈调整，再按执行记录更新技能库，下一轮复用技能来指导探索和执行；用触觉补充视觉以减少接触时的不确定性，用可复用代码补充文字指导以减少复用时的推理开销。LIBERO-10（LIBERO 桌面操作仿真基准中的长时程子集）上首回合成功率提高 12.5–25.0 个百分点，四种 Agent 的平均运行时间降低 7.6%–72.4%。相对 [SayCan](../saycan/README.md) 的固定技能库，技能库随执行经验增长。
- **为什么在这个库里**：[具身 Agents](../../fields/embodied-agents/README.md)方向"技能库怎样增长"一格。优先级：选读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:2609.37810（Xie、Chen、Cao、Lu、Wu、Jiang；v1，2026-09）
- 全文：[arXiv PDF v1](https://arxiv.org/pdf/2609.37810v1)
- 方向：[具身 Agents](../../fields/embodied-agents/README.md)（跨领域另见[智能体](../../../cross-domain/fields/agents/README.md)）
