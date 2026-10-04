# A Survey of World Models for Autonomous Driving

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.11260)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：梳理自动驾驶世界模型的研究，给出分类和技术路线图。
- **核心方法**：三层分类：未来物理世界的生成（按图像、BEV、占据、点云四种表示，多用扩散模型与 4D 占据预测）；智能体的行为规划（规则驱动与学习驱动，代价图优化与强化学习生成轨迹）；预测与规划的交互（潜空间扩散、带记忆的结构，用于多智能体协同决策）。另分析自监督、多模态预训练、生成式数据增强等训练范式，并比较场景理解与运动预测上的表现。
- **为什么在这个库里**：驾驶方向的入口综述，供[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)批注中的驾驶对照项查文献；本库没有单独的驾驶方向页。它是持续更新的项目（arXiv 注明，另有论文列表与 benchmark 仓库），本卡依据 2025 年 9 月的 v4。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2501.11260 · [全文 PDF](https://arxiv.org/pdf/2501.11260) · 浙江大学人工智能协同创新中心（CCAI） · 持续更新的综述（v4，2025-09）
- 方向：multimodal/world-models、robotics/navigation-planning
