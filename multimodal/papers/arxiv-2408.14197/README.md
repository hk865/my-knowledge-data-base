# Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2408.14197)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有的驾驶世界模型多用来生成数据或做预训练，很少直接服务端到端规划。
- **核心方法**：以相机为输入的 4D 占据预测世界模型：记忆模块用"语义与运动条件归一化"累积历史 BEV（鸟瞰图特征）嵌入，世界解码器预测未来占据与运动流；把速度、转向角、轨迹、高层指令等动作条件注入模型，实现可控生成；规划器用基于占据的代价函数在候选轨迹中选最优。在 nuScenes、nuScenes-Occupancy、Lyft-Level5 上评测，nuScenes 规划 L2 在 1/2/3 秒上比 UniAD 相对降低 33%、22%、9.7%（UniAD 的评测口径）。
- **为什么在这个库里**：与 [OccWorld](../arxiv-2311.16038/README.md) 同属[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)批注中的驾驶对照项；它把"动作条件"做成可插拔的多种控制信号，对应操作世界模型拆分表里的"③ 动作条件"。`[判断]` 它相对 UniAD 的优势随预测时距拉长而缩小（33% → 9.7%），与操作世界模型"多步预测会漂"的现象一致。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2408.14197 · [全文 PDF](https://arxiv.org/pdf/2408.14197) · 浙江大学、华为 · AAAI 2025
- 方向：multimodal/world-models、robotics/navigation-planning
