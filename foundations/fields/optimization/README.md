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

## 与其他概念的关系

概念地图写的是四篇讲义之间的特例与推广。本节写本分区的概念与其他分区的概念、与领域里正在使用的机制之间的关系。类型标注与[关系页](../../relations/README.md)相同：`[结构]` 数学上是同一结构或特例，推导在括号里的章节；`[经验]` 由实验发现，括号里给原文出处；`[历史]` 有作者自述或引用链。涉及具体模型的，写明版本与日期；各家为什么这样选，留在领域页。

### 反向传播：梯度怎样穿过时间与深度

- `[结构]` 沿时间的反向传播（BPTT）与最优控制里的伴随方程是同一个递推；RNN 的梯度消失与爆炸，是线性化状态方程的稳定性问题（[递推状态谱系](../../relations/recurrent-state.md)第 1 节，[RNN](../../lessons/12-rnn.md) 第 5 节）。
- `[历史]` LeCun（1988）用拉格朗日形式推导反向传播，自述受最优控制理论启发（同上第 1 节）。
- `[结构]` LSTM 的记忆通路与残差连接改的是同一个连乘：前者让每一步乘的是接近 1 的对角门值，后者在每层的导数里加一个恒等项 I（[LSTM](../../lessons/13-lstm.md) 第 4 节，[Attention 与 Transformer](../../lessons/14-attention-transformer.md)第 10.2 节）。
- `[经验]` 层归一化放在残差的哪一侧，决定要不要学习率预热：Xiong 等（2020）证明初始化时 Post-LN（归一化在残差相加之后）末层的梯度大，需要预热，Pre-LN（归一化在子层输入处）可以去掉预热（[训练科学](../../../cross-domain/fields/training-science/README.md)主线第 3 个节点）。

### 小批量与批量大小

- `[结构]` 数据并行与梯度累积都在计算同一个更大批量的平均梯度，一个在设备之间分摊，一个在时间上分摊（[分布式训练](../../lessons/05a-distributed-training.md)第 3–5 节）。
- `[经验]` 批量放大 k 倍时学习率也放大 k 倍，再配几轮渐进预热，ImageNet 上的 ResNet-50 可以把批量加到约 8k 而精度不降，再大误差开始上升（Goyal 等 2017，见[训练科学](../../../cross-domain/fields/training-science/README.md)主线第 3 个节点）。

### Adam、AdamW 与优化器状态

- `[结构]` Adam 的 m、v 各是一份与参数同样大的状态。P 个参数用 4 字节保存时，参数、梯度和这两份状态合计约 16P 字节，状态分片拆分的就是它们（[分布式训练](../../lessons/05a-distributed-training.md)第 8 节）。
- `[结构]` 后训练的强化学习与偏好优化改的是要最小化的损失，不是优化器：PPO 的代理损失、GRPO 与 DPO 的损失算出梯度之后，仍交给本分区的 Adam 一类优化器去更新（[强化学习](../../lessons/05b-reinforcement-learning.md)第 5–8 节）。所以优化器的超参与稳定性问题在后训练里照样存在。

### Muon：把矩阵当作矩阵来更新

- `[结构]` 符号下降与 Muon 是同一个问题在两种"步长尺子"下的答案。要求每个坐标的位移都不超过 η 时，让损失下降最多的一步是 −η·sign(g)，这就是 Adam 从零状态出发第一步的样子；要求更新矩阵的最大奇异值不超过 η 时，下降最多的一步是 −η·UVᵀ，其中 U、V 来自梯度（或动量）矩阵的奇异值分解 UΣVᵀ，这就是 Muon 正交化的理想结果（[Adam 与 AdamW](../../lessons/modules/optimization/adam.md)第 5–6 节，[Muon](../../lessons/modules/optimization/muon.md)第 3–4 节）。Moonlight 的讨论一节也把 Muon 解释为谱范数（矩阵的最大奇异值）下的最速下降（Liu 等 2025，§4）。
- `[经验]` 规模化需要本分区 AdamW 的那一项权重衰减。[Moonlight](../../../llm/papers/arxiv-2502.16982/README.md)（Kimi，2025-02）发现，Muon 在小规模上的优势在更大的模型、更多的 token 上会缩小，权重与层输出的 RMS 持续增长、超出 bf16 的高精度范围；加上 AdamW 式的解耦权重衰减，并按矩阵形状缩放更新、使更新的 RMS 与 AdamW 对齐（可直接沿用 AdamW 的超参）之后，在计算最优设定下，Muon 用约 52% 的训练 FLOPs 达到 AdamW 的损失（§1、§2.2、§3.2）。
- `[经验]` Muon 训练出的权重奇异值分布更分散：在 1.2T token 的检查点上，超过 90% 的权重矩阵 SVD 熵（奇异值分布的均匀程度）高于 AdamW，MoE 路由器权重上差距最大（Moonlight §3.4）。这与正交化"拉平各方向强弱"的设计意图一致（Muon 第 2 节）。
- `[经验]` Muon 会放大注意力分数。[Kimi K2](../../../llm/papers/arxiv-2507.20534/README.md)（2025-07）在中等规模训练中观察到注意力 logit 很快超过 1000；K2 用的 MLA（把 K、V 压成低维潜向量的注意力）推理时不显式构造 K，加不了在注意力里归一化 Q、K 的 QK-Norm，只好在优化器一侧补：每步更新后，若某个头的最大 logit 超过阈值，就按比例缩小这个头的 Q、K 投影权重，称为 QK-Clip（K2 §2.1，见[预训练方向](../../../llm/fields/pretraining/README.md)"损失稳定"与"优化器"两节）。
- `[经验]` "哪一块算一个矩阵"成了设计选择。[Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)（2026-07）把 Q、K、V 投影的动量矩阵按注意力头切开、逐块正交化，理由是整矩阵正交化时梯度大的头会主导共同的更新方向（K3 §2.5）；[DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)（2026-04）对多数模块用 Muon，嵌入、输出头、mHC 的静态偏置与门控、RMSNorm 的权重仍用 AdamW（V4 §2.4）。Muon 讲义第 9 节写的原始建议就是这条分界：隐藏层的二维权重交给 Muon，嵌入、输出层、偏置与归一化缩放交给 AdamW；V4 沿用了它，K3 则在二维矩阵内部再按头切分。
- `[结构]` Muon 与状态分片相互牵制：Newton–Schulz 迭代要用完整的矩阵，而状态分片正是把参数切开放在不同设备上。Moonlight 为此实现了 ZeRO-1 式的分布式 Muon（§2.3），DeepSeek-V4 设计了混合的 ZeRO 分桶策略（§3.4.1），Kimi K3 让每个设备只用点对点通信取回自己负责的那些矩阵的分片，再正交化（K3 §5.2.2）（分片见[分布式训练](../../lessons/05a-distributed-training.md)第 8 节）。
- `[经验]` 预训练与微调的优化器怎样搭配还没有定论：Moonlight 的讨论一节写到，实践中 AdamW 预训练的模型用 Muon 微调、或反过来，效果欠佳，并把它列为待解决的问题（§4）；它自己的对照里，Muon 预训练加 Muon 微调最好，在 AdamW 预训练的 Qwen2.5-7B 上改用 Muon 微调，结果只与 AdamW 微调持平（§3.5）。所以大量现成的 AdamW 检查点难以直接从 Muon 受益（微调见[迁移与元学习](../../lessons/05c-transfer-meta-learning.md)第 2–3 节）。

### 一次更新能走多远

- `[结构]` LoRA 把一处权重的更新限制为两个小矩阵的乘积 BA，秩至多为 r；优化器只更新 A、B 的参数，原权重不动（[迁移与元学习](../../lessons/05c-transfer-meta-learning.md)第 4–5 节）。`[历史]` LoRA 原文以本征维度研究为依据：预训练语言模型解出下游任务所需的自由度远小于参数量（[训练科学](../../../cross-domain/fields/training-science/README.md)主线第 6 个节点）。
- `[结构]` 学习率在参数空间里限制一步走多远；PPO 的裁剪在输出分布上限制新旧策略一步相差多少，RLHF 的 KL 惩罚限制整个训练离参考模型多远（[强化学习](../../lessons/05b-reinforcement-learning.md)第 7、9 节）。三者都是对"更新幅度"的约束，量的对象不同，所以调大学习率不能代替 KL 惩罚。

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
- Muon 怎样从研究原型变成旗舰模型的优化器，以及 QK-Clip、FP8/FP4 这些配套的数值约束：[预训练方向](../../../llm/fields/pretraining/README.md)"优化器"与"数值精度"两节，[Moonlight 文献卡](../../../llm/papers/arxiv-2502.16982/README.md)。
- 裁剪与 KL 在后训练里的用法：[强化学习后训练](../../../llm/fields/posttraining/rl/README.md)"技术地基"。

## 批注

**易误读**

- Adam 的 v 记录的是梯度平方的滑动平均，衡量近期梯度的幅度，不是二阶导数，也不是方差（Adam 与 AdamW 第 3 节）；"逐坐标预条件"指的是这种用梯度统计代替曲率的缩放。
- Muon 的正交化在实现中用少量 Newton–Schulz 型矩阵迭代近似，讲义里的更新式是去掉前瞻、形状缩放和衰减后的教学骨架（Muon 第 5–6 节）。
- 符号下降与 Muon 的"最速下降"对应只描述理想的更新方向。实际的 Adam 从第二步起有历史统计参与，Muon 经过 Newton–Schulz 近似与形状缩放，都不再是严格的最速下降（Adam 与 AdamW 第 6 节、Muon 第 5–6 节）。
- Moonlight 的"约 52% 训练 FLOPs"是在计算最优设定下、按规模定律拟合曲线比较得到的（§3.2），对照是作者调过参的 AdamW，不是任何设定下的固定倍数；Muon 训练的注意力 logit 超过 1000 是 K2 中等规模实验里的观察（K2 §2.1）。

**与其他论文的关联**

- [Moonlight](../../../llm/papers/arxiv-2502.16982/README.md)（权重衰减与更新 RMS 匹配）→ [Kimi K2](../../../llm/papers/arxiv-2507.20534/README.md)（QK-Clip）→ [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)（Muon 与 AdamW 按模块分工、混合 ZeRO）→ [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)（按头正交化）：四篇按时间连成 Muon 规模化的路径，每一步都在补上一步留下的数值或工程问题。
- [递推状态谱系](../../relations/recurrent-state.md)第 1 节：BPTT 与伴随方程的推导，以及 Pascanu 等 2013 的梯度消失条件。

**未核实 / 待验证**

- Goyal 等 2017、Xiong 等 2020、LoRA 与本征维度两篇的结论取自[训练科学](../../../cross-domain/fields/training-science/README.md)页，本轮未重新打开原文。
- Muon 原作者的博客（Jordan 等 2024）未打开，原始参数分组建议的转述取自 Muon 讲义第 9 节。
