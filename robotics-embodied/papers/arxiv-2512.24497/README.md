# What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.24497)

- **解决什么**：[DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md) 与 [V-JEPA 2](../arxiv-2506.09985/README.md) 都能在特征空间规划，但骨干、训练展开和规划器的收益混在一起。
- **核心方法**：统一动作条件的特征预测配方，分别比较视觉编码器、本体状态、多步训练、上下文和优化器；结果随任务而变，真实图像与简单仿真偏好的编码器也不同。
- **为什么在这个库里**：在[机器人世界模型](../../fields/world-models/README.md)里从“选哪个模型”转到“哪项设计值得消融”，比继续堆模型名更适合作为复现入口。优先级：必读（潜空间规划支线）；选定任务上的经验配方不构成通用最优性保证。
