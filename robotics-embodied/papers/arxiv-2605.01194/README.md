# VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2605.01194)

- **解决什么**：每一步都增加VLA采样会浪费计算，怎样识别不确定时刻，并用较轻的模型选出更好的动作块。
- **核心方法**：相对直接执行π0.5，先以动作差异判断是否值得多采样，再用训练过的相对动作critic成对比较候选、淘汰选优。
- **为什么在这个库里**：[动作模型干预讲义](../../fields/embodied-agents/action-model-intervention.md)中的“小模型工具”对照：改候选选择与推理预算，需另训练critic。优先级：选读。
