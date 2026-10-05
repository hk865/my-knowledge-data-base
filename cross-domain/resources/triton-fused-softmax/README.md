# Fused Softmax

> 状态：资料卡 · 动态文档（main） · [原文](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)

- **解决什么**：怎样让 softmax（把一组数变成和为 1 的非负权重）减少中间结果在显存与计算单元之间的搬运。
- **核心方法**：把求最大值、指数、求和与归一化融合进一个 kernel（执行具体计算的实现），在 GPU 片上存储中完成中间计算；示例根据行宽和设备资源安排执行配置。
- **为什么在这个库里**：接在 [PyTorch 分发器](../pytorch-dispatcher/README.md)之后，理解“算什么”与“怎样在硬件上算”的关系。优先级：选读。

## 批注

- **适用边界**：示例面向每行能放入 GPU 片上存储的矩阵，性能取决于输入形状和设备条件。
- **[判断] 何时改实现**：任务更换后若仍使用受支持的 softmax，运算定义可以沿用；硬件或形状变化时先检查已有实现的适用范围与配置，超出支持范围时再考虑换用或补充实现。融合保留目标运算，但浮点计算仍需验证误差。
- **实现入口**：若以后需要接入 PyTorch，先按 [PyTorch Custom Operators](https://docs.pytorch.org/tutorials/advanced/custom_ops_landing_page.html) 判断内置算子组合是否已经够用。
