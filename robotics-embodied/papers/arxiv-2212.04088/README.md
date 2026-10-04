# LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2212.04088)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有具身指令跟随方法需要大量标注数据，样本效率低。
- **核心方法**：用 GPT-3 做少样本高层规划：kNN 检索上下文示例，输出子目标序列交给已有的低层模型（HLSM）；执行失败或超时时把检测到的物体列表放回提示重新规划。ALFRED 上只用 100 条示例成功率 16.42%，全量数据的 HLSM 为 20.27%。
- **为什么在这个库里**：[具身 Agent](../../fields/embodied-agents/README.md)主线第 2 步：在长程基准上量化少样本 LLM 规划，并暴露低层检测的瓶颈。优先级：选读。
