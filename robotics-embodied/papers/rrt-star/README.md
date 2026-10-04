# Sampling-based Algorithms for Optimal Motion Planning

> 状态：技术精读 · 2011 · [原文](https://arxiv.org/abs/1105.1186)

[返回机器人与具身目录](../../README.md)

- **解决什么**：PRM、RRT 等采样规划器概率完备，但返回路径的代价随采样增多几乎必然收敛到非最优值。
- **核心方法**：提出 PRM*、RRG 和 RRT*：每个新点只连接半径按 γ(log n / n)^(1/d) 收缩的邻域；RRT* 为新点选代价最低的父节点，再把能因此变便宜的邻居重连过来。每步计算量只比原算法多常数倍，却获得渐近最优性；证明借助随机几何图理论。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)方向采样规划的基线（"渐近最优"一格）。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:1105.1186（Karaman、Frazzoli；International Journal of Robotics Research，2011）
- 全文：[arXiv PDF v1](https://arxiv.org/pdf/1105.1186v1)
- 方向：[导航与规划](../../fields/navigation-planning/README.md)（另见[运动控制与腿足运动](../../fields/control-locomotion/README.md)）
