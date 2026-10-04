# Code as Policies: Language Model Programs for Embodied Control

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2209.07753)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让语言模型不只是选技能，而是直接写出调用感知与控制接口的机器人策略。
- **核心方法**：相对 SayCan 从固定技能库中打分选择，改为让 LLM 生成 Python 代码：调用物体检测与控制原语，使用 NumPy 等库做空间推理，遇到未定义函数就递归生成（分层代码生成）。RoboCodeGen 上分层生成 95%，平铺 81%；受限于感知 API 能描述什么、有哪些控制原语。
- **为什么在这个库里**：[具身 Agent](../../fields/embodied-agents/README.md)主线第 3 步与 Baseline 页"技能接口"一行。优先级：必读。
