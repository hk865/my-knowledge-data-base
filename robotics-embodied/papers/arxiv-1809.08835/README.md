# Crowd-Robot Interaction: Crowd-aware Robot Navigation with Attention-based Deep Reinforcement Learning

> 状态：文献卡 · 2018 · [原文](https://arxiv.org/abs/1809.08835)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：机器人在人群中导航时，把人当静态障碍或只做反应式避障，会产生不安全、不自然的行为。
- **核心方法**：相对 CADRL、LSTM-RL，显式建模人与机器人、人与人之间的交互，用自注意力汇聚周围行人的状态，再用价值网络规划（SARL）。在 ORCA 控制行人的仿真中，机器人对人不可见时成功率 100%、碰撞 0%，ORCA 为 43% 与 57%。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 2 步与 Baseline 页"局部执行"一行：动态障碍从反应式避障走向学习交互的代表。优先级：选读。
