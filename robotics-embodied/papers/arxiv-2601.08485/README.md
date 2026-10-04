# Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.08485)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：跑酷式的敏捷运动多依赖端到端感知运动模型，泛化和可解释性有限；面向通用地形的方法又不够敏捷，并且在视觉遮挡下表现差。
- **核心方法**：在 [AME-1](../arxiv-2506.09588/README.md) 的注意力地图编码器上增加全局特征，并用它给局部特征加权，使运动模式能随地形变化；另配一套学习式建图流程，用神经网络把深度观测转成带不确定度的局部高程，再与里程计融合，并接入并行仿真，训练时策略看到的就是在线建图的输出，以帮助 sim-to-real（一句话：仿真中训练、直接部署到真机）。在 ANYmal-D 四足和 LimX TRON1 双足上验证。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向"外部感知怎样进入策略"一格的较新版本，同时处理建图噪声与遮挡；与 [Extreme Parkour](../arxiv-2309.14341/README.md) 这类深度图端到端策略对照读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2601.08485（Zhang、Klemm、Yang、Hutter；当前 v3，2026-09；arXiv 注明被 IEEE T-RO 有条件接收，曾用名 AME-2）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2601.08485)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
