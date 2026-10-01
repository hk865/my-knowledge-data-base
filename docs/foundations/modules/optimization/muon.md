# Muon 与矩阵更新正交化

[返回优化目录](../../02-optimization.md) · [返回总导读](../../00-learning-navigation.md)

## 先读两分钟

本模块把 Muon 从名字拆成实际操作：先产生带动量的矩阵更新，再对它的奇异方向尺度做近似重整，最后更新权重。它不把网络权重强制变成正交矩阵，也不保证在所有任务上超过 AdamW。

## 一张图建立整体印象

![Muon 与矩阵更新正交化浓缩总图](../../../../assets/foundations/02d-overview.svg)

## Muon 把矩阵更新当成一个整体处理

这里把你提到的“Moen”按 **Muon** 解释；你此前也明确问过 Muon。其全称是 MomentUm Orthogonalized by Newton-Schulz。Keller Jordan 等人的 2024 年公开说明与实现是主要原始来源，这些资料将贡献归于具体作者与开放协作，不能简单写成“OpenAI 发明”。[作者说明及贡献名单](https://kellerjordan.github.io/posts/muon/)

Adam 主要逐坐标调整尺度。Muon 则保留隐藏层权重的矩阵结构：先形成带动量的更新矩阵 M，再用 Newton–Schulz 矩阵迭代对更新做近似正交化，最后加到权重上。第 t 次梯度 Gₜ 在旧权重 Wₜ₋₁ 处计算。省略 Nesterov、尺寸缩放和衰减细节时，其骨架是：

Mₜ = μMₜ₋₁ + Gₜ

Oₜ ≈ Ortho(Mₜ)

Wₜ = Wₜ₋₁ − ηₜOₜ

“正交化”究竟是什么？把 M 做只保留非零奇异值的紧致分解 M = UΣVᵀ，U、V 描述两个坐标系之间的方向，Σ 的对角线描述各奇异方向的强弱。理想操作以 UVᵀ 代替 UΣVᵀ：保留方向结构，让非零奇异方向的尺度更接近。直观例子是 diag(100,1) 理想地变成 diag(1,1)。满秩方阵的理想结果是正交矩阵；满秩长方阵对应行或列正交的半正交矩阵。

这里被处理的是 **M，即更新矩阵，而不是参数 W 本身**。所以不能说“Muon 强制网络每层权重正交”。实际实现采用少量多项式矩阵迭代而非完整 SVD，也不要求输出精确等于 UVᵀ；精确为零的奇异方向不会由这种迭代凭空产生信号。[Muon 官方实现](https://github.com/KellerJordan/Muon/blob/master/muon.py)

原始推荐分工是：隐藏层的二维权重矩阵用 Muon；embedding、输出头、bias、归一化缩放等用 AdamW。卷积核可按实现要求展平为矩阵，因此“二维参数”不等于“只有全连接层能用”。实际版本还会调整不同形状矩阵的更新尺度，不能直接照搬别的优化器的学习率。额外成本来自多次矩阵乘法；好处能否抵消单步开销，取决于矩阵尺寸、batch、设备和分布式实现。[作者的使用边界](https://kellerjordan.github.io/posts/muon/)

2025 年的扩展工作研究了大规模语言模型训练中的权重衰减、更新尺度对齐和分布式实现。这说明 Muon 已超出最初的小模型实验，但不证明它对所有模型、数据、微调或强化学习任务都更强。公平比较需要给两者调参，并比较相同数据预算、训练时间和验证指标，不能只看“训练若干 step 后哪个 loss 低”。[Muon is Scalable for LLM Training](https://arxiv.org/abs/2502.16982)

## 第一步 用一个矩阵看清改动对象

![Muon矩阵更新分解](../../../../assets/foundations/02d-matrix-step.svg)

图 1 取 M = diag(100,1)，只是为了让 U、V 的旋转部分不挡住直觉。理想输出 diag(1,1) 与逐元素归一化恰好容易混淆，但对一般非对角矩阵，UVᵀ 并不是逐元素取符号。它同时利用行列构成的线性变换结构。

所谓“弱方向”指 M 的小奇异值对应方向，不一定是某个单独神经元，也不意味着这个方向必然是有价值的特征。把它们放大是算法动机，效果需要实验。若矩阵秩亏，保留非零奇异值的紧致分解只处理已有非零子空间；多项式迭代不会无中生有补出零方向。

## 第二步 近似迭代为何无需完整 SVD

![NewtonSchulz奇异值迭代](../../../../assets/foundations/02d-newton-schulz.svg)

图 2 按原实现的系数计算：先归一化 M，再迭代 X新 = aX + b(XXᵀ)X + c(XXᵀ)²X。对于 X = UΣVᵀ，这相当于把每个奇异值 s 变为 φ(s) = as + bs³ + cs⁵，同时保留奇异向量方向。a、b、c 分别为 3.4445、−4.775、2.0315。

因此本例较小的奇异值从约 0.01 逐步增大；第五步时两个值约为 0.6965 与 0.6989，而非精确的 1。这里展示的是高精度数学映射，没有模拟 bfloat16 舍入。这恰好说明“approximate orthogonalization”的含义：少量 GPU 友好的矩阵乘法换取有用的尺度变换，不承诺精确求出极分解。

## 关联原文与代码精读

### 原作者说明中应区分定义和假说

阅读 [Muon 原作者说明](https://kellerjordan.github.io/posts/muon/) 的 Definition、The design of Muon 和 Empirical considerations。定义告诉你动量之后做什么；“较弱方向可能仍有用”的解释属于动机与经验理解，不是证明所有任务更优的定理。阅读时把这两层分开，也不要把页面中的早期训练成绩当成普适性能保证。

### 从官方实现追踪每一个对象

在 [muon.py](https://github.com/KellerJordan/Muon/blob/master/muon.py) 中依次找 muon_update、zeropower_via_newtonschulz5 和参数更新。检查输入究竟是梯度、动量还是参数；看四维卷积更新如何展平；再看矩阵长宽比例如何影响缩放。源码注释明确说明所选少步多项式不必精确输出 UVᵀ。把“理想 SVD 操作”与“实际数值实现”分开，就不会误把图 2 的约 0.7 当作算法失败。

### 扩展到大规模训练补了什么

阅读 [Muon is Scalable for LLM Training](https://arxiv.org/html/2502.16982v1) 的 Methods，重点找权重衰减、更新 RMS 对齐和分布式实现。这里研究的不只是单个小矩阵如何变化，还包括不同形状参数的学习率可比性，以及额外矩阵计算如何分布到设备上。扩展论文的实验证据属于其模型和训练设置，不能外推为“Muon 总比 AdamW 快”。

## 如何决定是否值得试

先确认哪些参数适合使用 Muon，哪些继续由 AdamW 处理，再对两种方案分别调学习率与衰减。比较同样验证目标的训练耗时，或者相同资源预算下的验证质量；额外的 Newton–Schulz 计算、临时矩阵内存和通信都应算进成本。单看 step 数不够，单看更新算子的 FLOPs 也不够。[PyTorch Muon 参数与缩放选项](https://docs.pytorch.org/docs/2.14/generated/torch.optim.Muon.html)

自检：Muon 对 M 做近似正交化后，W新 是否一定正交？不一定，因为 W新 = W旧 − ηO。正交更新与正交权重约束是两件事。

回到 [Adam 与 AdamW](adam.md) 比较逐坐标缩放；训练不稳定时先查 [梯度模块的诊断表](gradient-sgd.md)，不要把换优化器当成万能恢复。
