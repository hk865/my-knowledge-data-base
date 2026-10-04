# 架构与信息流

[回到基础模块](../../README.md) · [完整讲义目录](../../lessons/01-architectures.md) · [跨模块关系页](../../relations/README.md)

## 这一分区回答什么

给一张 224×224 的照片判断是猫还是狗，给一句英文生成法文译文，给一团随机噪声生成一张图片。三件事都要先决定：输入的哪些部分之间交换信息，哪些计算共用同一组参数。图像里相邻像素关系最紧，卷积只看一个小窗口，并在所有位置共用同一个小核；句子里相关的词可能隔得很远，注意力按内容决定每个位置去读哪里；传感器读数要带着过去走，循环网络把历史压进一个状态。生成任务还多一层选择：怎样从噪声或隐藏变量得到样本，与内部用哪种网络做计算，是两个独立的决定。

## 概念地图

本分区的八篇讲义回答两个问题：信息在位置之间怎样流动，以及怎样生成样本。下面两张表给出每个模块解决的计算问题和需要先读的内容；第三部分写模块之间谁是谁的特例或推广。

### 信息在位置之间怎样流动

| 交换方式 | 模块 | 它解决的计算问题 | 先读 |
|---|---|---|---|
| 固定的局部邻居 | [CNN](../../lessons/11-cnn.md) | 同一个图案出现在图像任何位置，都能用同一个小核检测出来；参数量与图像大小无关，多层叠加后看到的区域逐层变大 | 无 |
| 经过一个状态 | [RNN](../../lessons/12-rnn.md) | 只看当前输入不够时，把任意长的历史压进固定大小的状态，每一步用同一套参数更新它 | 无；第 5 节的梯度部分可先读[梯度与 SGD](../../lessons/modules/optimization/gradient-sgd.md) |
| 经过一个状态 | [LSTM](../../lessons/13-lstm.md) | 让一条线索在状态里跨很多步保留下来：用门决定保留、改写和读出，使记忆通路上每一步乘的因子可以接近 1 | RNN 第 5 节 |
| 按内容读取任意位置 | [Attention 与 Transformer](../../lessons/14-attention-transformer.md) | 每个位置在一步之内按内容读取其他任何位置；用 mask（规定哪些位置可读的 0/1 表）控制可见范围，使下一词预测的训练可以并行 | 无 |
| 按内容读取任意位置 | [QKV](../../lessons/15-qkv-deep-dive.md) | 为什么要把"和谁匹配"（Q、K）与"读到什么内容"（V）分开，两个匹配投影能否合并成一个矩阵 | Attention 与 Transformer 第 3–6 节 |
| 线性状态、给定的图、按条件选参数 | [SSM、GNN 与 MoE](../../lessons/18-ssm-gnn-moe.md) | SSM（状态空间模型）：把递推改成线性，长序列就能按卷积或并行 scan（把逐步递推改写成可并行的前缀运算）计算；GNN（图神经网络）：在任意给定的图上让节点与邻居交换信息；MoE（混合专家）：参数很多，但每个 token（模型处理的基本单位，例如一个词或词片段）只调用其中几组 | SSM 先读 RNN 第 7 节；GNN 先读 QKV 第 4 节；MoE 先读 Attention 与 Transformer 第 10.1 节 |

### 怎样生成样本

| 模块 | 它解决的计算问题 | 先读 |
|---|---|---|
| [VAE](../../lessons/16-vae.md) | 用一个隐藏变量产生多个不同的合理样本；真实后验（看到数据后对隐藏变量的判断）算不出来时，用编码器近似它，并优化变分下界 ELBO（对数似然的一个可计算下界） | [概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)第 8 节的 KL |
| [Diffusion](../../lessons/17-diffusion.md) | 把生成拆成从纯噪声出发的逐级去噪；训练时任取一个噪声强度一步加噪，让网络回归加进去的噪声 | VAE 第 4 节 |

### 谁是谁的特例或推广

每条带关系类型：`[结构]` 数学上是同一种结构或一个是另一个的特例，推导在括号里的讲义章节；`[历史]` 有作者自述或原文引用。

- **状态递推** s_t = f(s_{t−1}, u_t)：用上一步的状态和本步输入算出新状态。
  - RNN：f 可学习并带 tanh 非线性 `[结构]`（RNN 第 7.1 节）。梯度消失与爆炸，就是这个系统线性化之后的稳定性问题。
    - LSTM：记忆沿 c_t = f_t⊙c_{t−1} + … 传递，梯度在这条通路上每步乘对角的门值 diag(f_t)，而不是满矩阵 `[结构]`（LSTM 第 4 节）。GRU 是遗忘门与写入门之和恒为 1 的特例（LSTM 第 6.3 节）。
  - SSM：去掉非线性、转移变成线性的 RNN，因此可以展开成长卷积或用并行 scan 计算 `[结构]`（RNN 第 7.3 节，SSM、GNN 与 MoE 第 2.2 节）。
    - Mamba：转移随输入变化。取 N=1、A=−1、B=1 时，选择性 SSM 退化为 h_t = (1−g_t)h_{t−1} + g_t x_t，也就是 GRU 形式的门控 RNN `[结构]`（LSTM 第 6.4 节，原文定理 1）。
    - 线性注意力：状态是矩阵，T_t = T_{t−1} + φ(k_t)v_tᵀ，转移固定为单位阵 `[结构]`（QKV 第 10.1 节）。
- **消息传递**：每个节点从邻居收集消息、汇总后更新自己（SSM、GNN 与 MoE 第 3.2 节）。
  - CNN：规则网格图上的消息传递，按相对位移选择权重 `[结构]`（同上第 3.5 节）。
  - 自注意力：全连接图上的消息传递，权重由 Q、K 匹配给出；GAT（图注意力网络）把同一机制限制在图的邻居上 `[结构]`（同上第 3.6 节）。
- **键值读取** Σ_i w(q, k_i)·v_i：用查询和每个键的匹配程度给值加权求和。
  - 注意力：键和值来自输入，权重是 softmax(qKᵀ/√d_k)（softmax 把一组分数变成非负、和为 1 的权重）。单个查询的注意力就是以指数点积为核的 Nadaraya–Watson 核回归（用相似度给已知样本加权、平均它们的结果） `[结构]`（QKV 第 8 节）。
  - FFN（Transformer 中逐位置的两层前馈网络）：FFN(x) = f(xW_1)W_2 = Σ_i f(x·k_i)v_i，W_1 的列是键、W_2 的行是值，都是固定参数 `[结构]`（Attention 与 Transformer 第 10.4、17 节）。
    - MoE：把 FFN 切成多个专家，路由器按打分只读其中几个；路由打分与注意力打分形式相同 `[结构]`（SSM、GNN 与 MoE 第 4.3、4.5 节）。
- **卷积的特例**
  - FFN 是核大小为 1 的卷积：令卷积公式中的核高、核宽为 1，每个位置的输出就是 XW + b `[结构]`（Attention 与 Transformer 第 17 节）。
  - ViT（把图像切成小块、每块当作一个 token 交给 Transformer 的视觉模型）的切块嵌入是核大小与步幅都等于块边长的卷积：把每块展平后乘同一个矩阵 E，E 的每一列重排后就是一个卷积核 `[结构]`（同上第 17 节）。
- **潜变量模型与变分下界**
  - VAE：编码器 q_φ(z|x) 可学习。
  - 扩散模型：编码器固定为逐步加高斯噪声的马尔可夫链、潜变量与数据同维的多层 VAE，训练优化的仍是变分下界 `[结构]`（VAE 与 Diffusion 的"与其他概念的关系"）。去噪网络可以是卷积 U-Net（先逐级缩小、再逐级放大并跨层拼接的编码–解码网络），也可以是 Transformer。

几种部件在多个模块里重复出现：

- **权重共享**：CNN 在空间上共享卷积核，RNN 在时间上共享 W_h、W_x，两者的参数量都与输入长度无关 `[结构]`（CNN 第 9 节）。
- **残差通路**：y = x + F(x) 对 x 求导得 I + ∂F/∂x，恒等项给梯度留出一条不经过 F 的路。ResNet（残差网络）用它解决网络加深后训练误差反而上升的问题（CNN 第 6 节）；Transformer 每个子层都加残差连接，原文直接引用 ResNet `[历史]`（Attention 与 Transformer 第 10.2、17 节）；LSTM 中 f=1 的记忆通路起同样的作用 `[结构]`（LSTM 的"与其他概念的关系"）。
- **看到多大范围**：L 层 3×3、步幅 1 的卷积，每层向外多看 1 个像素，感受野（能影响一个输出的输入区域）是 (2L+1)×(2L+1)，靠堆层和下采样扩大（CNN 第 4 节）；自注意力在第一层就让每个位置读取全部位置（Attention 与 Transformer 第 2 节）。这一差别在不同数据规模下的后果，见[观点页](../../../perspectives/cnn-vs-transformer.md)。

## 与其他分区和关系页的连接

- [递推状态谱系](../../relations/recurrent-state.md)：把 RNN、LSTM、SSM、Mamba、线性注意力串成一条链，核心问题是状态转移怎样同时做到稳定、按内容选择、可以并行。
- [注意力与 FFN 的分工谱系](../../relations/attention-ffn-division.md)：从注意力的 A 与 V 走到 FFN 键值记忆、MoE 与 Engram（把静态模式改成查表的记忆模块），说明读取位置与存放知识怎样在模块之间分工。
- 只涉及两个模块的关系写在各篇末尾：[CNN](../../lessons/11-cnn.md#9-与其他概念的关系)、[RNN](../../lessons/12-rnn.md#与其他概念的关系)、[LSTM](../../lessons/13-lstm.md#与其他概念的关系)、[Attention 与 Transformer](../../lessons/14-attention-transformer.md#17-与其他概念的关系)、[QKV](../../lessons/15-qkv-deep-dive.md#与其他概念的关系)、[VAE](../../lessons/16-vae.md#与其他概念的关系)、[Diffusion](../../lessons/17-diffusion.md#与其他概念的关系)、[SSM、GNN 与 MoE](../../lessons/18-ssm-gnn-moe.md#与其他概念的关系)。
- [优化分区](../optimization/README.md)：梯度沿深度或时间传递时要连乘每层的局部导数（[梯度与 SGD](../../lessons/modules/optimization/gradient-sgd.md)第 8 节），RNN 第 5 节、LSTM 第 4 节和残差通路都是在改这个连乘。
- [目标分区](../objectives/README.md)：架构决定网络怎样计算，训练目标决定让它做什么题。因果 mask 让同一个 Transformer 可以用下一词目标并行训练（[自监督与生成目标](../../lessons/modules/objectives/03-pretraining-objectives.md)第 2–4 节）。
- [进阶分区](../advanced/README.md)：LoRA 加在 Transformer 的线性层上；上下文学习发生在注意力的计算里，不改权重（[迁移与元学习](../../lessons/05c-transfer-meta-learning.md)第 4、10 节）。
- [数据分区](../data/README.md)：Transformer 的 padding mask 与文本实验中的 masked mean pooling 用的是同一种 0/1 掩码。

## 阅读顺序

1. [CNN](../../lessons/11-cnn.md) 第 1–5 节：从一个 [−1,0,1] 核理解卷积、通道、感受野与汇聚。
2. [RNN](../../lessons/12-rnn.md) 第 1–5 节，再读第 7 节的状态方程视角；接着读 [LSTM](../../lessons/13-lstm.md)。
3. [Attention 与 Transformer](../../lessons/14-attention-transformer.md) 第 1–12 节：手算一次注意力，再看 mask、多头、FFN、残差与归一化怎样接成一个块；第 13 节区分 encoder 与 decoder。
4. [QKV](../../lessons/15-qkv-deep-dive.md)：匹配与内容为什么分开，以及注意力与核回归、线性注意力的关系。
5. [SSM、GNN 与 MoE](../../lessons/18-ssm-gnn-moe.md)：读完 2 和 4 再读，三节分别接回 RNN、注意力和 FFN。
6. [VAE](../../lessons/16-vae.md)，再读 [Diffusion](../../lessons/17-diffusion.md)。这条生成线与 1–5 互不依赖，可以单独先读。
7. 两张关系页：[递推状态谱系](../../relations/recurrent-state.md)、[注意力与 FFN 的分工谱系](../../relations/attention-ffn-division.md)。
8. 对照原文看机制：[Attention Is All You Need 精读](../../../llm/papers/transformer/reading.md)、[ViT 精读](../../../multimodal/papers/vit/reading.md)（切块嵌入）、[DDPM 精读](../../../multimodal/papers/ddpm/reading.md)、[Mamba 精读](../../../llm/papers/mamba/reading.md)。

## 往哪里去

- 卷积网络在视觉中的发展（ImageNet → ResNet → 自监督视觉 → ViT 与 ConvNeXt）：[视觉表征](../../../multimodal/fields/visual-representation/README.md)。
- Transformer 在语言中的发展（BERT、T5、GPT 的路线收敛）：[预训练](../../../llm/fields/pretraining/README.md)。
- 生成模型的发展（GAN → DDPM → LDM → DiT）：[视觉生成](../../../multimodal/fields/generation/README.md)。
- 注意力的成本、MoE 与 SSM 在大模型里的用法：[架构与效率](../../../llm/fields/architecture/README.md)、[长上下文与记忆](../../../llm/fields/long-context/README.md)。
- FFN 键值记忆、事实定位等对模型内部的研究：[模型科学](../../../cross-domain/fields/model-science/README.md)。
- 残差、归一化与规模定律怎样让深网络可训练、可预测：[训练科学](../../../cross-domain/fields/training-science/README.md)。
- 扩散与 flow matching（直接回归把噪声推向数据的速度场）用于生成机器人动作：[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)；VAE 式潜变量用于预测未来：[世界模型](../../../multimodal/fields/world-models/README.md)。
- 跨领域的论证：[深度学习的规模化](../../../perspectives/scaling.md)、[Transformer 为什么成为通用主干，CNN 仍在哪里占优](../../../perspectives/cnn-vs-transformer.md)、[语言、图像、视频的生成为何收敛到相近的配方](../../../perspectives/generative-convergence.md)。

## 批注

**易误读**

- 残差一条的导数 I + ∂F/∂x 针对纯加法形式。原始 Transformer 把 LayerNorm（在一个向量内部减均值、除标准差的归一化）放在加法之后（Post-LN），恒等通路要经过 LayerNorm；Pre-LN 把它移进分支（Attention 与 Transformer 第 10.4 节）。
- 线性注意力与 Mamba 同属线性递推，区别在于线性注意力的转移固定为单位阵，没有随输入变化的遗忘（SSM、GNN 与 MoE 的"与其他概念的关系"）。
- 卷积是网格图上的消息传递，这是结构对应；GNN 的历史来源有多条，不只来自 CNN（SSM、GNN 与 MoE 的批注）。

**与其他论文的关联**

- Mamba 定理 1 的门控形式与推导见 [Mamba 精读](../../../llm/papers/mamba/reading.md)；LRU 从 RNN 出发、经线性化与对角化追平 S4，见[递推状态谱系](../../relations/recurrent-state.md)第 3 节。
- FFN 作为键值记忆的实验证据见 [Geva 等 2021 文献卡](../../../cross-domain/papers/arxiv-2012.14913/README.md)；MoE 替换 FFN 的实例见 [Switch Transformer 文献卡](../../../llm/papers/arxiv-2101.03961/README.md)。
