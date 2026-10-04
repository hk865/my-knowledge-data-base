# Learning Latent Dynamics for Planning from Pixels

> 状态：文献卡 · 2018 · [原文](https://arxiv.org/abs/1811.04551)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：能否只从像素学到环境动力学，并在潜空间里快速在线规划。
- **核心方法**：提出 RSSM（同时含确定的循环状态与随机潜变量的状态空间模型）和潜变量多步预测训练目标（latent overshooting），用 CEM 在潜空间规划（视野 12、1000 个候选、10 轮）。在 DeepMind Control 上用远少于无模型方法的回合数达到相近水平。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)主线第 2 步：Dreamer 一线的 RSSM 从这里来；部署时规划的早期代表。优先级：选读。
