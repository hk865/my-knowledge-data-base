# V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2506.09985)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：能否从互联网视频和少量机器人交互中学到能理解、预测并用于规划的世界模型。
- **核心方法**：先在大规模视频上做 JEPA 式自监督预训练（预测被遮住部分的特征而非像素），再用 DROID 中约 62 小时无标注机器人视频后训练动作条件预测器（V-JEPA 2-AC），以图像为目标在特征空间规划。两个实验室的 Franka 零样本抓放 80%/65%，每个动作规划 16 秒（Cosmos 4 分钟）；对相机位置敏感，长程误差累积。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)主线第 4 步：在预训练特征上规划的代表，与 [DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md) 对照。优先级：必读。
