# 优化与参数更新

[回到基础模块](../../README.md) · [完整讲义目录](../../lessons/02-optimization.md) · [跨模块关系页](../../relations/README.md)

## 这一分区回答什么

模型应当输出 3，却输出了 1。损失给这次错误打一个分数；反向传播算出每个参数对这个分数的影响，也就是梯度；优化器再决定沿梯度走多大一步、要不要参考过去几步。难处在于不同方向的尺度可能差得很远：对损失 ½(x² + 100y²) 用同一个学习率 η 做梯度下降，y 方向要求 η < 0.02 才不发散，x 方向于是每步最多只缩小约 2%（[梯度与 SGD](../../lessons/modules/optimization/gradient-sgd.md)第 7 节）。本分区的四篇讲义，是对"梯度怎样变成一次参数更新"的四种逐步加深的回答。

## 概念地图

| 模块 | 它解决的计算问题 | 先读 |
|---|---|---|
| [梯度、反向传播与 SGD](../../lessons/modules/optimization/gradient-sgd.md) | 把"给错误打分"变成每个参数的修改方向：链式法则把误差逐层分配给前面的参数，小批量样本给出梯度的廉价估计 | 无 |
| [动量与逐坐标自适应](../../lessons/modules/optimization/momentum.md) | 小批量梯度方向来回摆动、各参数的梯度尺度相差很大时，用历史信息平滑方向（动量），或为每个坐标单独定步长（Adagrad、RMSProp） | 梯度与 SGD 第 6–7 节 |
| [Adam 与 AdamW](../../lessons/modules/optimization/adam.md) | 把方向记忆和尺度记忆合在一起，修正两者从零开始造成的初期低估；AdamW 把权重衰减移到自适应缩放之外 | 动量与逐坐标自适应第 3、7 节 |
| [Muon](../../lessons/modules/optimization/muon.md) | 参数本来是矩阵时，按矩阵的奇异方向（矩阵把输入拉伸最多、最少的那些方向）而不是逐个元素整形更新：对动量矩阵做近似正交化 | 动量与逐坐标自适应第 3 节；奇异值分解在 Muon 第 3 节从头讲 |

四篇的依赖是一条直线，后一篇都在前一篇的更新式上加一层加工。它们之间的特例与推广关系如下，`[结构]` 表示数学上是同一结构或特例，推导在括号里的章节：

- **SGD**：θ ← θ − η·g。
  - **动量**：把 g 换成 m_t = βm_{t−1} + g_t，即过去梯度带符号、按 β 衰减的累积；持续同向的建议会累积，来回摆动的会抵消 `[结构]`（动量与逐坐标自适应第 3 节）。乘上 (1 − β) 就是滑动平均写法，两种写法只差一个常数倍，学习率要相应换算（同上第 4 节）。
  - **Adagrad、RMSProp**：把 g 逐坐标除以平方梯度累积量的平方根；RMSProp 用滑动平均让旧的尖峰逐渐被遗忘（同上第 6–7 节）。
    - **Adam**：分子是滑动平均写法的动量 m，分母是 RMSProp 式的平方梯度滑动平均的平方根 √v，再各自做偏差修正 `[结构]`（Adam 与 AdamW 第 2、4 节）。取 β₁ = 0 时 m 就是本次梯度，Adam 退化为带偏差修正的 RMSProp。
      - **符号下降**：从零状态出发的第一步、忽略 ε 时，m̂ = g、√v̂ = |g|，Adam 每个坐标的位移都是 ±η `[结构]`（同上第 5–6 节）。第二步起历史开始起作用，两者不再相同。
      - **Muon**：符号下降把每个元素的幅度归一；正交化把矩阵每个奇异方向的增益归一，理想结果是奇异值分解 UΣVᵀ 中的 UVᵀ `[结构]`（Muon 第 3–4 节）。两种归一在矩阵上给出不同结果，Muon 第 4 节有一个 2×2 的反例。
- **L2 惩罚与权重衰减**：对普通 SGD，在损失上加 λ‖θ‖²/2 等价于每步先把参数乘 (1 − ηλ) `[结构]`（Adam 与 AdamW 第 7 节，[参数正则化](../../lessons/modules/objectives/05-regularization.md)第 6 节）。对 Adam 两者不再等价，因为 λθ 会进入 m 和 v、被逐坐标缩放；AdamW 把衰减放回两本账之外。

还有两个问题贯穿四篇，它们决定优化器拿到的梯度是否可用：

- **尺度不一与预条件**：狭长山谷中，同一个学习率无法兼顾陡、缓两个方向。先按方向缩放梯度再更新，叫预条件。完整曲率太贵，动量和自适应方法用更便宜的历史统计改善这个问题（梯度与 SGD 第 7 节）。
- **梯度过小**：梯度接近 0 可能是到了最低点，也可能是鞍点（有的方向向上弯、有的方向向下弯），或者是多层局部导数连乘后变小（梯度与 SGD 第 8 节）。连乘问题在 [RNN](../../lessons/12-rnn.md) 第 5 节表现为梯度消失与爆炸，[LSTM](../../lessons/13-lstm.md) 第 4 节和残差连接（[Attention 与 Transformer](../../lessons/14-attention-transformer.md)第 10.2 节）都在结构上改这个连乘。

## 与其他分区和关系页的连接

- [递推状态谱系](../../relations/recurrent-state.md)：RNN 的梯度消失与爆炸，是线性化状态方程的稳定性问题；BPTT（沿时间展开的反向传播）的反向递推与最优控制中的伴随方程是同一个递推。
- [架构分区](../architectures/README.md)：残差连接与 LayerNorm 决定梯度沿深度怎样传递（[Attention 与 Transformer](../../lessons/14-attention-transformer.md)第 10.2–10.4 节）。
- [目标分区](../objectives/README.md)：优化器最小化的对象就是损失；[参数正则化](../../lessons/modules/objectives/05-regularization.md)第 6–7 节从目标一侧讲 L2 与权重衰减的同一个区别。
- [进阶分区](../advanced/README.md)：数据并行在各卡上算局部梯度再求平均，等于一次更大批量的 SGD；Adam 的 m、v 两份状态要占显存，是状态分片要拆分的对象（[分布式训练](../../lessons/05a-distributed-training.md)第 3–5、8 节）。LoRA 限定哪些参数参与更新（[迁移与元学习](../../lessons/05c-transfer-meta-learning.md)第 4–6 节）。

## 阅读顺序

1. [梯度、反向传播与 SGD](../../lessons/modules/optimization/gradient-sgd.md)：手算一次两层反传，再看狭长山谷（第 7 节）和梯度过小的几种原因（第 8 节）。
2. [动量与逐坐标自适应](../../lessons/modules/optimization/momentum.md)。
3. [Adam 与 AdamW](../../lessons/modules/optimization/adam.md)：两本账的逐步计算，以及第 6 节为什么 Adam 不等于取符号。
4. [Muon](../../lessons/modules/optimization/muon.md)。
5. [参数正则化](../../lessons/modules/objectives/05-regularization.md)第 6–7 节：从目标一侧再看一次 AdamW。
6. [RNN](../../lessons/12-rnn.md) 第 5 节与 [Attention 与 Transformer](../../lessons/14-attention-transformer.md)第 10 节：梯度怎样穿过时间和深度。
7. [分布式训练](../../lessons/05a-distributed-training.md)第 3–5、8 节：多卡上的同一次更新、梯度累积与混合精度。

## 往哪里去

- 初始化、归一化、学习率预热、大批量训练、规模定律、本征维度与遗忘，这些让大规模训练稳定、可预测的研究：[训练科学](../../../cross-domain/fields/training-science/README.md)。
- 原始 Transformer 的学习率预热与衰减配方：[Attention Is All You Need 精读](../../../llm/papers/transformer/reading.md)第 4 节。
- 对后续训练阶段偏离程度加约束（KL 惩罚）：[InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 6 节。
- 跨领域的论证：[深度学习的规模化](../../../perspectives/scaling.md)。

## 批注

**易误读**

- Adam 的 v 记录的是梯度平方的滑动平均，衡量近期梯度的幅度，不是二阶导数，也不是方差（Adam 与 AdamW 第 3 节）；"逐坐标预条件"指的是这种用梯度统计代替曲率的缩放。
- Muon 的正交化在实现中用少量 Newton–Schulz 型矩阵迭代近似，讲义里的更新式是去掉前瞻、形状缩放和衰减后的教学骨架（Muon 第 5–6 节）。
