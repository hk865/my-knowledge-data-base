# Generalizing Manipulation Skills with a Local Coding Agent

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.26499)

- **解决什么**：本地运行的通用代码模型能否用少量程序技能和普通感知控制工具，适应操作任务的变化。
- **核心方法**：相对固定技能回放，让冻结Qwen模型读取手写技能、实时图像与状态，测量场景并编写调用九个机器人接口的程序。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中的本地冻结模型案例，同时提供“末端可达仍可能全身碰撞”的重要失败证据。优先级：选读。
