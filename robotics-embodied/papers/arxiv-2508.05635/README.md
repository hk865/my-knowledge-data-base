# Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2508.05635)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：机器人操作的数据采集、训练与评估是割裂的流水线，拖慢迭代、掩盖失败模式。
- **核心方法**：在约 3000 小时、100 万回合的 AgiBot-World-Beta 上训练指令条件的多视角视频扩散模型 GE-Base，接 160M 参数的流匹配动作头 GE-Act，做成动作条件神经仿真器 GE-Sim 用于闭环评估，并提出 EWMBench；每个新本体只用 1 小时遥操作数据适配。只用自家数据，只覆盖平行夹爪的桌面操作。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)用法 (d)(e)：世界基础模型平台的代表，主线第 5 步。优先级：选读。
