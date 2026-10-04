# Training Agents Inside of Scalable World Models

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2509.24527)

- **解决什么**：DreamerV3 一类在线世界模型难以拟合复杂视频，而可交互视频模型的速度与动作精度又不足以承载大量想象训练。
- **核心方法**：Dreamer 4 用因果视频分词器与 Transformer 动力学替代循环状态模型；shortcut forcing 把少步生成和带噪历史训练结合，再用离线数据学出的奖励与策略头进行想象强化学习。
- **为什么在这个库里**：接上 [DreamerV3](../dreamerv3/reading.md) 到可扩展视频动力学的直接后继，也把 [世界模型基线](../../fields/world-models/BASELINES.md)中的表示、动力学与数据来源三格一起改掉。优先级：必读。
