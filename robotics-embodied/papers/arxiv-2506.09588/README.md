# Attention-Based Map Encoding for Learning Generalized Legged Locomotion

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2506.09588)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：腿足机器人在可落脚区域稀疏的地形上既要精确落脚，又要扛住不确定性：模型规划控制器精确但怕真实扰动，学习控制器鲁棒但在稀疏地形上不够准，两者结合的混合方法计算量大，且受规划器本身限制。
- **核心方法**：不再外接落脚点规划器，而是在端到端 RL 策略里加入以本体感知为条件的注意力地图编码，随策略一起训练；训练后网络把注意力集中在未来落脚的可踩区域，注意力权重也成了解释策略如何"看"地形的窗口。分别为 12 自由度四足和 23 自由度人形训练控制器，在室内外多种地形（含训练未见过的）实机测试。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向"外部感知怎样进入策略"一格；对照 [Miki 等 2022](../arxiv-2201.08117/README.md)（注意力循环编码器融合高程图与本体感知）读，后续版本是 [AME-2](../arxiv-2601.08485/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2506.09588（He、Zhang、Jenelten、Grandia、Bächer、Hutter；v1，2025-06，arXiv 注明为同行评审前的原稿；后续论文 AME-2 称本篇为 AME-1，并引作 Science Robotics 2025）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2506.09588)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
