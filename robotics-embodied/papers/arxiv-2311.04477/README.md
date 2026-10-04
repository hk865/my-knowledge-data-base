# PLV-IEKF: Consistent Visual-Inertial Odometry using Points, Lines, and Vanishing Points

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.04477)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：EKF 式 VIO 常有系统不一致和角度漂移；人造环境中的直线和消失点能提供方向约束，但加入后还要保持一致性。
- **核心方法**：以右不变 EKF（IEKF，一句话：在李群上定义与状态无关的误差，使误差传播不依赖当前估计值）融合点、线、消失点三类特征；证明点特征的常规加性误差定义与不变误差定义在测量模型上数学等价、同样保持一致性，线特征有类似结论；再做基于不变滤波的可观性分析，证明消失点测量能自然保持系统的不可观方向。用仿真与实测验证位姿精度和一致性。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向不变滤波 VIO 的特征扩展，与 [EqVIO](../arxiv-2205.01980/README.md) 都从对称性出发处理一致性，区别在于本篇靠增加结构化特征提高方向可观性。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2311.04477
- 作者：Tong Hua、Tao Li 等（共 7 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2311.04477)
- 发表：ROBIO 2023（arXiv 注释）
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)
