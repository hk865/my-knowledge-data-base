# Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.04546)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：动作条件世界模型能让机器人不经实际交互就预测候选动作的后果，用于策略评估、规划和数据增强；但灵巧手的动作有 23 维，真实数据少，整体式模型学不到逐个关节的动作效果。
- **核心方法**：把像素预测拆成两段：动力学模型由过去的分割掩码和 23 维动作（6 维末端位姿加 17 个手部关节位置）预测未来的掩码；渲染模型用加了 ControlNet 的 Stable Video Diffusion 把掩码画成逼真的 RGB。分割空间里的仿真—真实差距更小，所以动力学模型可以先在 50 多小时的仿真数据上预训练，再用不到 2.5 小时的真实示范微调。在灵巧抓放基准上，掩码条件与仿真预训练都是让 23 个自由度逐维可控的必要条件；整体式基线只能反映手和末端的大致轨迹。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"①②"一行：用中间表示（分割掩码）把仿真数据接进视频世界模型，回答"真实数据不够时怎么训动作条件世界模型"；作者把它定位为把 [Ctrl-World](../../../robotics-embodied/papers/arxiv-2510.10125/README.md) 一类做法（从 Stable Video Diffusion 初始化，面向平行夹爪）扩展到高维的灵巧手。做不好的场景：没有深度信息，手遮挡时会丢物体；长时预测中按颜色类别画的掩码不绑定物体身份，会漂；合成数据覆盖不了自然的操作动作；假设相机固定（Limitations 段）；定量实验只在一个灵巧抓放基准上。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2607.04546 · [全文 PDF](https://arxiv.org/pdf/2607.04546) · 苏黎世联邦理工学院（ETH Zurich）软体机器人实验室
- 方向：multimodal/world-models
