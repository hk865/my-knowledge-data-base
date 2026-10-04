# Scaling Behavior Foundation Model for Humanoid Robots

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.15163)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：行为基础模型被寄望于靠规模提升人形控制能力，但学习范式、行为数据和模型结构三者怎样配合才能有效扩展，并不清楚。
- **核心方法**：让三件事协同：用全局坐标系下的整体动作跟踪统一各种人形控制问题；平衡同策略采样量与参考动作多样性；提出可扩展的 Humanoid Transformer 结构。摘要报告测试集 MPKPE（平均关键点位置误差）相对现有人形控制器在局部模式降低 10% 以上、全局模式降低 82%，并做了实机部署。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向人形分支"规模化"一问的实证：动作跟踪范式（见 [BeyondMimic](../arxiv-2508.08241/README.md)）在数据和模型放大后怎样变化；背景见 [BFM 综述](../arxiv-2506.20487/README.md)。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2607.15163（Zeng 等 18 位作者；v1，2026-07）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2607.15163)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
