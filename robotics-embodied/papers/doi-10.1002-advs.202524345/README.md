# MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion

> 状态：文献卡 · 2026 · [原文](https://doi.org/10.1002/advs.202524345)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：基于感知的四足深度强化学习控制器难以同时做到跨地形通用和跨机型迁移，深度图渲染计算开销大，策略对传感器噪声敏感。
- **核心方法**：用 NVIDIA Warp 并行计算深度图降低训练开销；以对比学习从深度图和高度图中提取低维地形特征，并显式做深度去噪，使感知模型与动力学解耦、可在不同四足机型上快速微调；再用按地形特征调节惩罚强度的奖励，让攀爬、跳跃、钻爬、挤过窄缝等技能在一个训练阶段学会。相对 [Agarwal 等 2022](../url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md) 那种"先用特权地形信息训练、再蒸馏到深度策略"的两阶段做法，本篇不需要蒸馏。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向"外部感知怎样进入策略"一格中深度路线的一个变体，关注训练成本与跨机型复用。优先级：存档。

## 身份信息

- 稳定标识：doi:10.1002/advs.202524345（Dong 等 10 位作者；Advanced Science 第 13 卷第 34 期 e24345，2026 年 4 月在线发表）
- 全文：[Wiley 官方页面](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202524345) · 代码：[arclab-hku/MGDP](https://github.com/arclab-hku/MGDP)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
