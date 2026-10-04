# ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1912.01734)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：把自然语言与带状态变化的交互动作联系起来，超越静态图像上的视觉语言任务。
- **核心方法**：在 AI2-THOR 中给出 7 类家务、8,055 条专家示范、25,743 条指令，平均每个任务 50 步，指令描述不完整、部分动作不可逆。端到端 Seq2Seq 基线在未见测试集上任务成功率 0.4%，人类 91%。
- **为什么在这个库里**：[具身 Agent](../../fields/embodied-agents/README.md)主线起点：说明端到端模型做不了长程任务，此后的 LLM-Planner、EmbodiedBench 都在它上面测。优先级：选读。
