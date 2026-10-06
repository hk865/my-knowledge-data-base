# StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2603.20659)

- **解决什么**：VLA在熟悉任务中会因无关物体或遮挡失败，怎样利用成功经验先把环境整理到策略较擅长的状态。
- **核心方法**：相对直接在扰乱场景执行VLA，让冻结VLM推断待移除物体，再经SAM3、三维定位和逆运动学原语完成环境整理，最后调用原策略。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中“初始环境干预”的代表；它把感知和控制工具接给通用模型，而非修改VLA轨迹。优先级：选读。
