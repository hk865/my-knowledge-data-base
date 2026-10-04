# VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2307.05973)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言条件的机器人操作依赖预定义的运动原语，限制了能做的任务。
- **核心方法**：LLM 写代码调用 VLM 获取物体位置，在三维体素上组合出可供性与约束的价值图，作为运动规划器的目标函数，零样本合成轨迹，不需要原语。5 个真实任务平均 88%，LLM + 原语基线 24%；接触丰富的任务仍需要动力学模型。
- **为什么在这个库里**：[具身 Agent](../../fields/embodied-agents/README.md)主线第 3 步与 Baseline 页"技能库 + 可行性"一行：绕过固定技能库的代表。优先级：必读。
