# Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

> 状态：逐步教学版 · 2022 · [原文](https://arxiv.org/abs/2204.01691)

[返回机器人与具身目录](../../README.md)

- **解决什么**：大语言模型能写出听起来合理的任务步骤，却不知道当前这台机器人、在当前环境里，哪一步真的做得到。
- **核心方法**：给机器人一组预训练技能，每一步把两件事相乘：语言模型判断"这个技能对完成指令有没有用"，技能的价值函数估计"现在执行能不能成功"；选乘积最高的技能执行，执行后再重新打分。机器人充当语言模型的"手和眼"，在移动操作机器人上完成长时程、抽象的自然语言指令。
- **为什么在这个库里**：[具身 Agents](../../fields/embodied-agents/README.md)方向的入门基线；后续的 [EmbodiedSkills](../embodiedskills/README.md)、[RoboSkill](../roboskill/README.md)、[MEMORA](../memora/README.md) 分别补执行验证、技能增长和跨经历记忆。优先级：必读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:2204.01691（Ahn 等 45 位作者；当前 v2，2022-08，增加 PaLM 结果与开源仿真环境）
- 全文：[arXiv PDF v2](https://arxiv.org/pdf/2204.01691v2)
- 方向：[具身 Agents](../../fields/embodied-agents/README.md)（跨领域另见[智能体](../../../cross-domain/fields/agents/README.md)）
