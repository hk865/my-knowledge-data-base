# Learning Interactive Real-World Simulators

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.06114)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：不同数据集分别富含物体、动作、运动信息，难以合成一个统一的、可交互的真实世界模拟器。
- **核心方法**：把多源数据训练成动作条件的视频模拟器（UniSim），在其中训练高层 VLM 规划器和低层 RL 策略：RL 让成功率从 58% 升到 81%，两者零样本迁移到真实 Language Table。自述会对不现实的动作编造结果、记忆短、对未见形态泛化差、只模拟视觉。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)用法 (c)"当仿真器训练策略"的代表。优先级：必读。
