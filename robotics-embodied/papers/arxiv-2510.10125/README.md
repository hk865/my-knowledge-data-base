# Ctrl-World: A Controllable Generative World Model for Robot Manipulation

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.10125)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：通用机器人策略在新物体与新指令上的评估需要大量真机 rollout，改进又需要额外的专家纠正数据。
- **核心方法**：在 1.5B 的 Stable Video Diffusion 上微调多视角联合预测、逐帧动作条件、位姿条件记忆检索的世界模型，在 DROID 上训练；用它评估 π0、π0-FAST、π0.5，并把想象中筛出的成功轨迹用于微调 π0.5，新物体与新指令上 38.7% → 83.4%。碰撞、滑动、旋转等物理仍有差距，成功轨迹靠人挑。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)用法 (c)(d)：为 VLA 做评估与合成数据的代表。优先级：选读。
