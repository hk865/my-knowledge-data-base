# 优化与训练基础模块导航

[返回总导读](00-learning-navigation.md)

## 先读两分钟

损失负责评价，反向传播负责求导，优化器把梯度变成更新，验证集检查是否真正有用。优化器的主要困难是噪声、尺度、曲率、稳定性和计算预算，不能只用“局部最优还是全局最优”解释。

本轴按四个可独立阅读的概念模块组织；每个模块都有一张浓缩总图、至少两张分步图、详细推导、关键原论文或实现精读，以及自检题。

1. [梯度 反向传播与 SGD](modules/optimization/gradient-sgd.md)：链式法则、mini-batch、病态山谷、鞍点边界和训练故障诊断
2. [动量与逐坐标自适应](modules/optimization/momentum.md)：Momentum、Nesterov、Adagrad 与 RMSProp 如何处理方向和尺度
3. [Adam 与 AdamW](modules/optimization/adam.md)：一阶二阶矩、偏差修正、L2 与解耦衰减为什么不同
4. [Muon 与矩阵更新正交化](modules/optimization/muon.md)：矩阵奇异方向、Newton–Schulz、参数分组与实际成本

建议顺序是 1 → 2 → 3 → 4。遇到 loss 突然变大可直接看模块 1 的诊断表；已熟悉 Adam 的读者可直接进入 Muon。所有手算和曲线都是标明假设的教学计算，不是性能基准。
