# Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control

> 状态：技术精读 · 2018 · [原文](https://dspace.mit.edu/entities/publication/bc8c7e1e-5830-443f-a879-787947111fcf)

[返回机器人与具身目录](../../README.md)

- **解决什么**：四足的动态步态（有腾空或只有一两只脚支撑的步态）必须提前为未来做准备：非线性 MPC 能预测，但问题非凸，求解器不保证全局最优；凸的力分配 QP 快而可靠，却只顾当前一步、只适用准静态。
- **核心方法**：把机身近似为单刚体，预先给定接触时序与偏航，在横滚和俯仰较小时线性化转动方程，使未来最长 0.5 秒的地面反作用力规划变成凸二次规划：不到 1 ms 求出最优，每秒重算 20–30 次，同时保留三维运动。同一组增益和权重跑出站立、小跑、跳跃、溜蹄、三条腿步态和三维奔跑等多种步态，前进速度最高 3 m/s。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向的模型基线：后来的学习型控制（[RMA](../rma/README.md)、[Rudin 等 2021](../arxiv-2109.11978/README.md)）都要和"简化模型 + 滚动凸优化"这条路线比鲁棒性与精度。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

教学顺序：[ESKF 教程](../eskf/README.md)（机身状态怎样估计）→ 本篇。

## 身份信息

- 稳定标识：doi:10.1109/IROS.2018.8594448（Di Carlo、Wensing、Katz、Bledt、Kim；IROS 2018）
- 全文：[MIT DSpace 作者稿](https://dspace.mit.edu/server/api/core/bitstreams/474e8173-7b22-46e6-a51b-3d8e8a383357/content)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
