# MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning

> 状态：逐步教学版 · 2026 · [原文](https://arxiv.org/abs/2607.14252)

[返回机器人与具身目录](../../README.md)

- **解决什么**：具身 Agent 怎样把不断积累的第一人称经历，变成以后推理和规划时用得上的持久记忆。
- **核心方法**：设计"形成—巩固—检索"的记忆生命周期，按环境、实体、活动、知识四类存储组织经历；在线编辑随新证据修正记忆，离线巩固把重复模式抽象成可复用的流程与偏好。在 45 小时第一人称视频基准上同时测回溯问答和前瞻规划，分布外任务规划最多提升 16.6%，并在实机上验证：从人类视频得到的记忆能让规划用上特定人的偏好和物品。相对 [SayCan](../saycan/README.md) 这类只看当前状态的语言—技能系统，补的是跨经历记忆。
- **为什么在这个库里**：[具身 Agents](../../fields/embodied-agents/README.md)方向"记忆"一格。优先级：选读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:2607.14252（Yu、Yuan、Zhang；v1 2026-07 为 RSS 2026 FM4RoboPlan 研讨会口头报告，v2 2026-08 注明被 EMNLP 2026 接收）
- 全文：[arXiv PDF v2](https://arxiv.org/pdf/2607.14252v2)
- 方向：[具身 Agents](../../fields/embodied-agents/README.md)（跨领域另见[智能体](../../../cross-domain/fields/agents/README.md)）
