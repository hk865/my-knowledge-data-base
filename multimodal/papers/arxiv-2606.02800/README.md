# Cosmos 3: Omnimodal World Models for Physical AI

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.02800)

- **解决什么**：视觉推理、视频模拟与机器人动作原本分属不同模型，接口与训练目标难以共同扩展。
- **核心方法**：用 Mixture-of-Transformers 双流结构耦合自回归推理与扩散生成；通过对视频或动作 token 分别加噪，把正向动力学、逆动力学和联合视频–动作生成写成同一条件建模问题。
- **为什么在这个库里**：为 [世界模型基线](../../fields/world-models/BASELINES.md)补上“模型怎样直接接动作”的统一接口，承接 [Cosmos-Predict2.5](../arxiv-2511.00062/README.md)。优先级：必读。
