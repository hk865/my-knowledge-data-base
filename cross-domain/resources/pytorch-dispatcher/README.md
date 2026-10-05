# Registering a Dispatched Operator in C++

> 状态：资料卡 · 2020 · [原文](https://docs.pytorch.org/tutorials/advanced/dispatcher.html)

- **解决什么**：同一个算子（规定输入怎样变成输出的运算，例如加法）怎样根据设备和求导需求调用合适的代码。
- **核心方法**：把运算接口与 kernel（执行具体计算的实现）分开注册；dispatcher（分发器）根据张量参数和运行状态选择相应实现，同一加法可以有 CPU 与 CUDA 两套代码。
- **为什么在这个库里**：为“运算是什么、由哪段代码完成”建立区分，再用 [Fused Softmax](../triton-fused-softmax/README.md) 理解实现怎样利用硬件。优先级：选读。

## 批注

- **版本边界**：本教程自 PyTorch 2.4 起弃用；当前实现入口是 [PyTorch Custom Operators](https://docs.pytorch.org/tutorials/advanced/custom_ops_landing_page.html)。该入口建议，能由内置算子组合表达的运算直接写成 Python 函数。
- **[判断] 调度的层次**：这里的分发决定调用哪个实现；线程如何并行、片上存储如何使用，需要继续看具体实现。已有后端能够支持时，更换设备可以沿用运算接口；缺少后端支持时，需要补充对应实现。
