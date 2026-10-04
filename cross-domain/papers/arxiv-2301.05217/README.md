# Progress Measures for Grokking via Mechanistic Interpretability

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2301.05217)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：grokking（训练集早已拟合、测试精度很久之后才突然上升）这类看似不连续的训练现象，能否找到连续变化、并与它有因果联系的进度指标。
- **核心方法**：把在模加法上训练的小 Transformer 完整逆向：它用离散傅里叶变换和三角恒等式把加法变成圆上的旋转，并在激活、权重和傅里叶空间的消融上验证。据此定义进度指标，把训练分成连续的三段：记忆、电路形成、清理。电路在测试精度上升之前早已形成，测试精度的“突然”上升来自权重衰减清除记忆成分；没有权重衰减或其他正则时，这些网络在该任务上不出现 grokking。
- **为什么在这个库里**：[训练科学方向](../../fields/training-science/README.md#与模型科学的关系)对照表中“机制解释训练动态”的例子，与 [Induction Heads](../arxiv-2209.11895/README.md) 同属“训练中的突变对应到一个电路的形成”。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2301.05217 · [全文 PDF](https://arxiv.org/pdf/2301.05217)
- 方向：cross-domain/model-science
