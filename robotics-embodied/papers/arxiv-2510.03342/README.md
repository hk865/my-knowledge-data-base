# Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.03342)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：上一代 [Gemini Robotics](../arxiv-2503.20020/README.md) 在双臂 Franka 与 Apollo 人形上是逐本体后训练的专用模型，作者写明它们几乎不能泛化到训练任务的变体之外（§3.1 脚注 2）；长时程任务需要规划、成功判定与执行分工。
- **核心方法**：Google DeepMind 的官方技术报告。两个模型分工：Gemini Robotics 1.5（VLA）在输出动作前先用自然语言写"思考"，把任务拆成几秒长的片段，再拆成"把夹爪向左移"这类原语；Motion Transfer（新架构加训练配方，让多种机器人的数据形成统一的运动理解，报告未给机制）使一个 checkpoint 同时控制 ALOHA、双臂 Franka 和 Apollo 人形。Gemini Robotics-ER 1.5（VLM）作编排器，负责任务分解、成功判定与调用工具，把 VLA 当作工具调用。真机基准 230 个任务，开发期 90% 以上的评测在 MuJoCo 仿真中完成（§2.3）。长时程 agent 实验中，用 ER 1.5 编排的总失败率 22%，用 Gemini 2.5 Flash 编排为 44.5%（Table 1）。
- **为什么在这个库里**：[VLA Baseline 表](../../fields/vla/BASELINES.md)中"任务条件 = 先写思考或子任务再出动作"与"数据 = 多本体统一"两格，是 Google DeepMind 从 RT 系列走到 Gemini 的当前节点。自述局限：灵巧度与上一代持平（§7）；本体差异很大（人形）时 Motion Transfer 的增益较弱（§3.2）；单独的 Thinking VLA 做复杂长时程任务不够（§5）。报告未写参数量、动作表示、延迟与是否在云端运行。优先级：选读。
