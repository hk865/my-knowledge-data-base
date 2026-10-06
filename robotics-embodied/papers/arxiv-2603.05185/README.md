# Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2603.05185)

- **解决什么**：长程操作的高层子任务在失败或停滞后仍继续执行，怎样及时识别异常并触发恢复。
- **核心方法**：相对π0.5加入文字子任务生成，并训练Florence-2 critic持续判定进度、完成与异常，按事件触发高层重规划或状态重置。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中的执行监控与调度对照，帮助区分冻结通用LLM外挂与需训练的多模型系统。优先级：选读。
