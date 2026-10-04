# mHC: Manifold-Constrained Hyper-Connections

> 状态：技术精读 · 2025 · [原文](https://arxiv.org/abs/2512.24880)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Hyper-Connections（HC，把残差流加宽成 n 条并行的流，并用可学习矩阵在层与层之间混合这些流）能提升性能，但混合矩阵没有约束，多层连乘以后不再保持恒等映射（浅层信号原样传到深层的性质），信号会被放大或衰减。作者在 27B 模型上观察到，HC 在约第 12k 步出现损失突升，同时梯度范数异常；按行和、列和衡量的复合映射最大增益（Amax Gain Magnitude）峰值达到 3000，理想值为 1。
- **核心方法**：用 Sinkhorn-Knopp 迭代把残差混合矩阵投影到双随机矩阵（元素非负、每行每列之和都为 1）构成的集合上。这类矩阵的谱范数不超过 1，相乘后仍是双随机矩阵，所以任意多层的复合映射都不会放大信号；n = 1 时退化为普通残差连接。配合算子融合与重计算，扩展倍数 n = 4 时额外训练时间为 6.7%。27B 模型上，mHC 的 BBH 为 51.0、DROP 为 53.9，HC 为 48.9、51.6，无扩展的基线为 43.8、47.0；3B、9B、27B 的计算缩放曲线显示，相对基线的损失优势随规模基本保持。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"支持更深更大的网络"中残差流一线的代表；[DeepSeek-V4](../arxiv-2606.19348/README.md) 把它用进 1.6T 参数的模型。Kimi 的 [Attention Residuals](../arxiv-2603.15031/README.md) 从另一侧处理同一个问题（把残差的固定求和换成跨层注意力），并在原文表 2 中把 mHC 列为对照，两篇可以对照着读。残差连接的基础见 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.2 节。[DeepSeek-V4.1-Flash](../arxiv-2609.19969/README.md) 又把它改成单次遍历的 Single-Pass mHC，读写量从 V4 实现的 20d 降到 10d。优先级：必读。

## 阅读入口

- [技术精读](reading.md)（前作 [Hyper-Connections](../arxiv-2409.19606/README.md) 在精读中一并讲清）
- [图解与说明](figures/README.md)
- [证据档案](evidence.json)
- [原文版本与阅读记录](source.json)
- 基础：[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10 节（残差与归一化）、[RNN 讲义](../../../foundations/lessons/12-rnn.md)第 5、7 节（连乘与稳定性）

## 身份信息

- 稳定标识：arxiv:2512.24880 · [全文 PDF](https://arxiv.org/pdf/2512.24880) · DeepSeek-AI
- 方向：llm/pretraining、llm/architecture
