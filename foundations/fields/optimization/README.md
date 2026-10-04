# 优化与训练工程：让大规模训练可行、可预测

> 状态：领域入门页 · 试点 v2 · 依据 [synthesis-training.csv](synthesis-training.csv)（15 篇）

[回到基础模块](../../README.md) · [完整讲义目录](../../../docs/foundations/02-optimization.md) · [架构方向](../architectures/README.md)

## 这个领域在解决什么

拿一个标准的 Transformer 翻译模型，在 IWSLT14 德→英数据上用 Adam 训练。层归一化放在残差相加之后（Post-LN，原始 Transformer 的写法）、学习率一开始就取目标值时，BLEU（译文与参考译文的词组重合度，越高越好）只有 8.45；先用学习率预热（训练开头若干步把学习率从很小逐步升到目标值）再训练，同一个模型约为 34；把层归一化移到每个子层的输入（Pre-LN），去掉预热也能训到相当水平。数据、结构规模和目标都没变，变的是训练开始时梯度的大小。这个方向研究的就是这类问题：损失的梯度怎样穿过几十上百层到达每个参数，优化器面对的是什么样的损失地形，用什么配方（初始化、归一化、学习率、批大小、数值精度）让一次训练稳定跑完，给定算力能把损失降到多少，以及训练好的模型怎样适配新任务而保住原有能力。[判断] 这些研究把大规模训练从反复试错变成可以事先规划的工程，是 CNN 与 Transformer 两条线都能扩大规模的共同前提（两条线本身见[架构方向](../architectures/README.md)）。

## 主线历史

每个节点先写“上一个节点留下的问题”，再写它改变了什么。逐篇出处在综合表里。

1. **诊断训练困难：Glorot 与 Bengio（2010，Montréal）**。问题：2006 年以后，深网络要先做逐层无监督预训练等特殊初始化才能训好；同样的网络从标准随机初始化直接做梯度下降，效果差且原因不明。改变：把“难训”拆成可测量的量，即逐层激活是否饱和（落进 sigmoid、tanh 两端梯度接近 0 的平坦区）、反传梯度的方差怎样随层变化。他们在初始化处于线性区的假设下推导出：标准初始化使反传梯度方差逐层变化；按相邻两层宽度缩放初始权重（归一化初始化，后来常称 Xavier 初始化）能让激活和梯度的方差逐层大致保持。5 个隐藏层的 tanh 网络在 Shapeset-3×2 上，测试误差从 27.15% 降到 15.60%。
2. **优化地形：困住训练的主要是鞍点（Dauphin 等 2014；Choromanska、LeCun 等 2014）**。问题：初始化改善之后，训练仍会长时间停在平台上（损失几乎不降），通常的解释是陷进了坏的局部极小。改变：Dauphin 等（Montréal 与 Stanford）依据统计物理和随机矩阵理论论证，在高维问题中，误差远高于全局最小的临界点（梯度为 0 的点）以指数级的概率是鞍点（有的方向向上弯、有的方向向下弯），负曲率方向的比例随误差升高而增加；他们在小网络上测量了这一关系，用它解释平台期，并提出能逃离鞍点的 saddle-free Newton 方法。Choromanska 等在球面自旋玻璃模型的简化假设下得到：大网络的低临界值集中在全局最小之上的一条窄带内，带外局部极小的数目随网络规模指数减少。2018 年，Garipov 等（Cornell 与 Samsung AI 等）与 Draxler 等独立发现，分别训练得到的两个解之间存在一条训练损失和测试精度几乎不变的曲线（模式连通，mode connectivity）。
3. **ReLU 与更深的网络：He 初始化、批归一化与 Adam（2014–2015）**。问题：网络换成 ReLU、加到二三十层后，Glorot 推导依据的线性假设不再成立，He 等报告 30 层模型用 Xavier 初始化完全停滞；每层输入的分布随前面层的参数变化，迫使使用小学习率；不同参数的梯度尺度相差很大，一个全局学习率难以兼顾。改变：He 等（2015，Microsoft Research）针对 ReLU 推导出标准差为 √(2/n) 的初始化（n 为一个输出单元连接的输入个数），30 层模型可以收敛；Ioffe 与 Szegedy（2015，Google）的批归一化（BN：在一个 mini-batch 内把每个特征减均值、除标准差，再学一组缩放和平移）让 Google 的 Inception 分类网络的 BN-x5 变体达到原模型 72.2% 精度所需的训练步数少 14 倍；Kingma 与 Ba（ICLR 2015）的 Adam 为每个参数记录梯度的一阶、二阶矩估计并做偏差修正，按参数自适应步长（逐步计算见 [Adam 讲义](../../../docs/foundations/modules/optimization/adam.md)）。同年的 ResNet 用残差连接解决了更深网络训练误差反而上升的退化问题（[架构方向](../architectures/README.md) CNN 一线第 5 个节点）。
4. **扩到多机：大批量、预热与混合精度（2017）**。问题：上面的配方让单机训练稳定，但 ResNet-50 在 8 块 GPU 上训完 ImageNet 要 29 小时；扩到上百块 GPU，就要把 mini-batch 加大几十倍，而大 mini-batch 在训练早期造成优化困难。改变：Goyal 等（Facebook）提出线性缩放规则（mini-batch 乘以 k，学习率也乘以 k）和渐进预热（前 5 个 epoch 把学习率从 0.1 线性升到目标值）。mini-batch 8192 在 256 块 GPU 上 1 小时训完，top-1 错误率 23.74%，与 mini-batch 256 的 23.60% 相当；超过约 8k 后误差开始上升。同年 Micikevicius 等的混合精度训练用半精度（FP16）存储权重、激活和梯度，另存一份单精度主权重并对损失做缩放（防止小梯度在半精度下变成 0），内存消耗约减半。
5. **把归一化搬进 Transformer：Post-LN、预热与 Pre-LN（2016–2020）**。问题：BN 的统计量依赖 mini-batch 大小，难以用于循环网络和变长序列。改变：Ba、Kiros 与 Hinton（2016，Toronto）的层归一化（LN：在单个样本的一个向量内部求均值和方差）与批大小无关；原始 Transformer（2017）采用 Post-LN，并用 4000 步学习率预热加按步数 −1/2 次方衰减（[Transformer 精读](../../../llm/papers/transformer/reading.md)第 4 节）。GPT-2（2019）把 LN 移到每个子层的输入，并把残差层的初始权重按 1/√N 缩小（N 为残差层数）。Xiong 等（2020，中科院计算所、北京大学、Microsoft Research 等）给出解释：初始化时，Post-LN 最后一层参数的梯度上界与层数 L 无关，Pre-LN 的上界按 1/√L 缩小；Post-LN 一开始梯度过大，需要预热把步子压小，Pre-LN 可以去掉预热。
6. **从能训好到能预测：规模定律（2020–2022）**。问题：训练能稳定跑完以后，问题变成怎样花算力：给定预算，模型多大、数据多少，能把损失降到多少。改变：Kaplan 等（2020，OpenAI）发现，语言模型的测试交叉熵分别随参数量 N、数据量 D、算力 C 呈幂律下降（例如只受参数量限制时，损失正比于 N 的 −0.076 次方），跨越 7 个以上数量级，而与深宽比关系很弱；据此建议把增加的算力主要用于加大模型（最优参数量约随 C 的 0.73 次方增长），并在收敛前停止训练。Hoffmann 等（2022，DeepMind）用三种方法重新拟合，得到模型大小与训练 token 数应按相同比例增长；按此训练的 70B 参数 Chinchilla（1.4T token）与算力相同的 280B 参数 Gopher（300B token）相比，MMLU（覆盖多个学科的多选题知识基准）高 7 个百分点（[Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)）。作者把两家结论的差别归于两点：学习率余弦周期是否与训练 token 数匹配，以及拟合时是否纳入更大的模型。同一时期，Nakkiran 等（2019，Harvard 与 OpenAI）的双下降显示，在模型恰好能把训练误差压到 0 的临界规模附近，测试误差会随模型变大、训练变久甚至数据变多先升后降，有标签噪声时最明显。
7. **只改一小部分参数，保住已有能力（2017–2022）**。问题：一次预训练成本极高，下游任务却很多；全参数微调 GPT-3 175B，每个任务都要部署一份 175B 参数的副本。顺序训练还会出现灾难性遗忘：Kirkpatrick 等（2017，DeepMind）把它描述为学新任务时改动了对旧任务重要的权重，旧任务能力突然丢失；他们的 EWC 用 Fisher 信息（衡量参数变动对旧任务输出影响大小的量）给重要参数加二次惩罚。改变：Li 等（2018）把网络限制在一个随机子空间里训练，测出解出任务所需的最小子空间维数（本征维度），远小于参数量；Aghajanyan 等（2020，Facebook）在预训练语言模型上测到，RoBERTa-Large 在 MRPC 上只训练 200 个参数就达到全参数微调 90% 的效果，预训练会持续降低本征维度，相同预训练步数下模型越大本征维度越低。Hu 等（2021，Microsoft）的 LoRA 以这两篇为依据，假设微调时的权重变化是低秩的，冻结原权重，只训练两个小矩阵的乘积，可训练参数比全参数微调少约 10000 倍。InstructGPT（2022，OpenAI）在人类反馈强化学习中对 SFT 模型（先用人工示范答案监督微调得到的模型）加逐 token 的 KL 惩罚（KL 散度衡量两个输出分布的差异；作者写明加它是为了缓解对奖励模型的过度优化），并把预训练数据的似然梯度混进 PPO（一种限制每步策略改动幅度的强化学习算法）的更新（PPO-ptx），大幅收回了公开 NLP 基准上的能力回退（[InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 6、8、11 节）。

## 技术地基

- **梯度、反向传播与 SGD**：本页所有节点讨论的都是“梯度能否以合适的大小到达每个参数”。[梯度与 SGD 讲义](../../../docs/foundations/modules/optimization/gradient-sgd.md)。
- **动量、逐坐标自适应与 Adam/AdamW**：训练配方的核心部件，节点 3 的 Adam 和后来的权重衰减拆分都在这里。[动量讲义](../../../docs/foundations/modules/optimization/momentum.md)、[Adam 讲义](../../../docs/foundations/modules/optimization/adam.md)；把更新当作矩阵处理的新方向见 [Muon 讲义](../../../docs/foundations/modules/optimization/muon.md)。
- **残差连接与层归一化**：节点 3、5 的结构基础，决定梯度沿深度怎样传递。[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 10.2–10.4 节（含 pre-norm 块的写法）、[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节。
- **损失函数与交叉熵**：规模定律拟合的对象就是测试集上的交叉熵。[任务与训练目标模块](../../../docs/foundations/03-tasks-losses.md)。
- **数据并行、梯度累积与混合精度**：节点 4 的大批量训练建立在多卡合并梯度之上。[分布式训练讲义](../../../docs/foundations/05a-distributed-training.md)第 3、5、8 节。
- **微调与低秩适配**：节点 7 的 LoRA 从一个线性层推起。[迁移与元学习讲义](../../../docs/foundations/05c-transfer-meta-learning.md)第 2–6 节。

## 主要路线与团队偏好

- **让梯度传下去：初始化、归一化、残差**（Montréal 的 Glorot 与 Bengio；Microsoft Research 与 Facebook 的 He 一系；Google 的 Ioffe 与 Szegedy；Toronto 的 Ba 与 Hinton；Xiong 等）。押注：只要在训练开始时让激活和梯度的尺度逐层保持，深网络就能稳定训练。代价：每个方案都依赖特定假设，结构一换就要重新推导（Glorot 假设线性区，He 针对 ReLU，BN 依赖 batch 统计，LN 在卷积网络上不如 BN）；理论分析大多只覆盖初始化时刻。[判断] He 一系在 Delving Deep into Rectifiers、ResNet、大批量 SGD 三篇中都以 ImageNet 为目标，先暴露“规模加大后训练失败”的具体现象（30 层停滞、更深反而训练误差上升、大批量早期困难），再给出一条简单、可推导的规则（方差条件、残差、线性缩放加预热），而不提出新的优化器。
- **理解优化地形**（Montréal 的 Dauphin 等；Choromanska、LeCun 等；Cornell 的 Garipov、Wilson 等；Draxler 等）。押注：解释为什么非凸的深网络训练在实践中能成功，并据此设计方法（saddle-free Newton、快速几何集成）。代价：理论结论依赖强假设（随机高斯场、自旋玻璃、变量独立），经验测量多在小网络或 CIFAR 规模上完成。[判断] Bengio 所在的 Montréal 组在 2010 与 2014 两篇中都先测量训练中的统计量（逐层激活与梯度方差；临界点的误差与负曲率比例），再提出针对性的方法。
- **用规模定律做预算**（OpenAI 的 Kaplan 等；DeepMind 的 Hoffmann 等）。押注：在一系列较小的模型上拟合幂律，外推决定大模型的参数量与数据量。代价：拟合出的指数依赖实验协议，两家因学习率调度和规模范围不同得出不同配比；规律预测的是交叉熵，下游能力要另外验证。[判断] OpenAI 的 Scaling Laws 与 GPT-2 有多位共同作者，它把这个团队“decoder-only 加扩大规模”的押注（见[架构方向](../architectures/README.md)的路线一节）变成了可以计算的预算。
- **用少量参数适配、保住已有能力**（DeepMind 的 EWC；Facebook 的 Aghajanyan 等；Microsoft 的 LoRA；OpenAI 的 InstructGPT）。押注：已学到的能力集中在预训练权重里，适配只需在低维子空间里改动，或对偏离原模型的程度加约束。代价：LoRA 施加在哪些矩阵上主要凭经验；EWC 在 10 个 Atari 游戏上达不到分别训练 10 个 DQN 的总分；PPO-ptx 之后 DROP 仍比 GPT-3 低 1.93 F1（[InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 11 节）。同样的思路也体现在学习率上：BERT 预训练用 1e-4，微调推荐 5e-5、3e-5、2e-5。

## 用什么衡量进展

benchmark 的替换反映了这个方向目标的迁移：从“能不能训起来”，到“训多快”，到“能预测多少”，再到“改完之后还剩多少”。

- **能不能训起来（2010–2015）**：Shapeset-3×2、MNIST、CIFAR-10 上的测试误差，以及训练曲线是否停滞（Glorot、Dauphin、He 的 30 层实验）。这些数据集小，适合逐层测量梯度统计。
- **训多快（2015–2020）**：ImageNet top-1/top-5 错误率加上达到同一精度所需的训练步数或墙钟时间（BN 的 14 倍步数、Goyal 的 1 小时），翻译 BLEU（IWSLT14、WMT14，Xiong）。口径问题：步数倍数依赖选定的目标精度；“1 小时”依赖 256 块 GPU 的硬件条件。
- **能预测多少（2020 起）**：留出集上的交叉熵（每个 token 的 nats）对 N、D、C 的拟合，再用 MMLU、BIG-bench 等下游任务检验按预测训练出的模型（Chinchilla）。口径问题：Kaplan 的数据来自单一的 WebText2，Chinchilla 的分析假设只训练一个 epoch（交叉熵的平滑下降不直接等于下游能力的同步提升）。
- **改完之后还剩多少（2017 起）**：适配方法与全参数微调在 GLUE、E2E NLG、WikiSQL 等上的成绩对比，加上可训练参数量、显存和推理延迟（LoRA）；遗忘则看旧任务的回退，例如顺序学习的置换 MNIST 与 Atari（EWC），以及 RLHF 后 SQuAD、DROP、HellaSwag、WMT 法→英相对 GPT-3 的变化（InstructGPT）。

## 当前开放问题

- **“规模大了反而不容易陷入局部最优”的准确说法与证据边界。** 能被证据支持的说法是：在参数很多的网络里，阻碍训练的主要是鞍点和平台期，而不是损失明显更高的坏局部极小；训练得到的不同解损失相近，并由低损失的路径相连。证据分三层：Dauphin 等的理论来自随机场模型的结果，实测只在小网络上；Choromanska 等的“带外坏极小随规模指数减少”成立于自旋玻璃模型的简化假设下，“SGD 收敛到低值带”是猜想；Garipov 等与 Draxler 等在 CIFAR-10、CIFAR-100 上的现代卷积网络（ResNet、DenseNet 等）中观察到模式连通。边界：这里的“规模”指参数量或宽度（过参数化），与数据量和训练时长无关；对一般的非线性网络没有证明，Kawaguchi（2016）对深线性网络证明了每个局部极小都是全局极小，推广到非线性网络需要独立性假设；Safran 与 Shamir 用计算机辅助证明，两层 ReLU 网络在学生与教师宽度相同（6 到 20 个单元）时坏局部极小很常见，且命中概率随规模增加，轻度过参数化后才大幅减少。大模型训练的实际障碍随之转到数值稳定与超参数上（节点 4、5）。入口：[Dauphin 等](https://arxiv.org/abs/1406.2572)、[Choromanska 等](https://arxiv.org/abs/1412.0233)、[Garipov 等](https://arxiv.org/abs/1802.10026)、[Safran 与 Shamir](https://arxiv.org/abs/1712.08968)。
- **规模定律能外推多远？** Kaplan 等自己写明：这些规律没有可靠的理论解释；按其趋势外推，在约 10^12 参数、10^12 token、10^4 PF-day（每秒 10^15 次浮点运算持续一天为 1 PF-day）处 L(C) 与 L(D) 两条规律相互矛盾，规律必然在此之前失效；结论来自单一数据分布，学习率选择对结果敏感。Chinchilla 改变学习率调度、纳入更大模型后，最优配比就从“主要加参数”变成“参数与数据等比例”，说明拟合出的指数依赖实验协议；它自己也报告了高算力处最优参数量曲线的弯曲，以及单 epoch 假设（数据不够、需要重复使用时不在其覆盖范围内）。双下降则提示在临界规模附近测试误差可以非单调。另一条规模轴是推理时投入的算力，见 [Test-Time Compute 精读](../../../llm/papers/test-time-compute/reading.md)。入口：[Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)、[Kaplan 等](https://arxiv.org/abs/2001.08361)、[Nakkiran 等](https://arxiv.org/abs/1912.02292)。
- **少量参数为什么就够？** 这里有两种“低维”。数据一侧是流形假说（高维数据集中在低维结构附近）：Pope 等（ICLR 2021）估计常见自然图像数据集的本征维度远低于像素数，本征维度低的数据集更容易学、泛化更好。参数一侧是解空间的低维：Li 等与 Aghajanyan 等的本征维度、LoRA 的低秩增量，以及彩票假说（Frankle 与 Carbin，ICLR 2019：在 MNIST、CIFAR10 上的全连接和卷积网络里，找到只有原网络 10–20% 大小、保留原始初始化就能单独训到相当精度的子网络）。[判断] 两侧的低维是否同源，仍是开放问题。入口：[Aghajanyan 等](https://arxiv.org/abs/2012.13255)、[LoRA](https://arxiv.org/abs/2106.09685)、[OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)（LoRA 在机器人模型上的实际用法）。
- **后续训练阶段怎样保住已有能力？** InstructGPT 报告，单纯调大 KL 系数会显著降低验证奖励，且在 DROP、SQuAD 上始终收不回来，混入预训练梯度效果更好；EWC 在 Atari 上仍有差距。入口：[InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)、[Kirkpatrick 等](https://arxiv.org/abs/1612.00796)。

## 阅读顺序

1. [优化讲义目录](../../../docs/foundations/02-optimization.md)：先按梯度与 SGD、动量、Adam 的顺序走完手算，这是读懂本页每个节点的前提。
2. [Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 10 节：残差和 LN 怎样接成一个块，对应节点 3 和 5。
3. [Attention Is All You Need 精读](../../../llm/papers/transformer/reading.md)第 4 节：原始配方里的预热和衰减，是节点 5 中 Post-LN 问题的出发点。
4. [分布式训练讲义](../../../docs/foundations/05a-distributed-training.md)：大批量和混合精度的计算基础，对应节点 4。
5. [Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)，配合 Kaplan 等原文：节点 6，以及规模定律外推边界这个开放问题。
6. [迁移与元学习讲义](../../../docs/foundations/05c-transfer-meta-learning.md)第 4–6 节，再读 [InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 6、8、11 节：节点 7 的两种做法，低秩适配与对偏离加约束。

## 批注

**易误读**

- 开头例子中 8.45 对约 34 的 BLEU，比较的是同一个 Post-LN 模型在 IWSLT14 上用 Adam 时去掉与保留预热（Xiong 等 Sec.3.2）。原文报告的是效果很差，没有说训练数值发散。
- BN 原文用 internal covariate shift 解释其效果。Santurkar 等（NeurIPS 2018）认为层输入分布是否稳定与 BN 的效果关系不大，BN 主要让优化地形明显更平滑。
- Kaplan 等“主要加参数”的配比（N ∝ C^0.73）已被 Chinchilla 的等比例结论修正；引用时要注明是哪一篇、哪种学习率设定。
- Choromanska 等的结论建立在三个简化假设上（变量独立、参数化冗余、均匀性），见其摘要；“SGD 收敛到低值带”在原文中是猜想。
- Adam 原文的收敛分析只覆盖凸问题，非凸网络上的优势是经验结果（Sec.6.2）。
- 彩票假说的 10–20% 来自 MNIST、CIFAR10 上的较小网络，并依赖保留原始初始化；它说明的是存在可单独训练的稀疏子网络，与 LoRA 的低秩更新是不同的对象。
- InstructGPT 中 KL 惩罚针对 SFT 模型，作者写明的目的是缓解对奖励模型的过度优化；收回公开基准能力回退的主要手段是 PPO-ptx。

**判断的支撑论文**

- “训练工程是规模化的共同前提”：GPT-2 Sec.2.3（Pre-LN 与 1/√N 初始化）、Goyal 等 Sec.1、Kaplan 等 Sec.1、Hoffmann 等 Sec.1；与[架构方向](../architectures/README.md)主线中 ResNet、ViT、GPT-3 的节点对照。
- He 一系的偏好：Delving Deep into Rectifiers Fig.3（30 层 Xavier 停滞）、ResNet Sec.1（退化问题，见 architectures 方向的 synthesis-cnn.csv）、Goyal 等 Fig.1 与 Table（大批量）。
- Montréal 组的偏好：Glorot 与 Bengio Sec.3–4（逐层激活与梯度统计）、Dauphin 等的临界点测量。
- OpenAI 的押注延续：GPT-2 与 Kaplan 等的作者名单（Radford、Wu、Child、Amodei 同时出现在两篇中）。
- 数据侧与参数侧低维是否同源：Pope 等 2021 的摘要只讨论数据；Li 等 2018、Aghajanyan 等 2020 只讨论目标函数的解空间；目前没有看到把两者直接联系起来的原文。

**与其他论文的关联**

- [架构方向](../architectures/README.md)的 ResNet 节点与本页节点 3 是同一件事的两面：残差连接在那里是结构，在这里是让梯度传下去的手段。[结构] 残差块 y = x + F(x) 对 x 求导得到 I + ∂F/∂x，恒等项让梯度至少能原样传回上一层（[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 10.2 节）。
- [Transformer 精读](../../../llm/papers/transformer/reading.md)第 4 节的 4000 步预热，正是 Xiong 等要解释和去掉的那个阶段。[历史] Xiong 等在引言中直接以 Post-LN 需要预热为出发点。
- [GPT-3 精读](../../../llm/papers/gpt3/reading.md)：175B 的 GPT-3 是 Chinchilla 论文中的对照模型之一。
- [历史] LoRA 在引言中写明受 Li 等 2018 与 Aghajanyan 等 2020 的本征维度结果启发。
- [InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 6、8 节详细算过 KL 惩罚与 PPO-ptx，是本页节点 7 的展开。
- [Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)目前只有题录，精读时“它要解决的问题”应与本页节点 6 一致。

**综合表说明**

- 表中每行一篇，列为论文（路线）、年份、团队、要解决的问题、对照的 baseline、benchmark、自述局限、代码/数据是否开放、来源 URL。各格是原文的中文转述，注明节号、表号或图号。
- Glorot 与 Bengio、Adam 两篇从 PDF 全文逐字核对；其余各篇通过 ar5iv 页面，由摘要模型转述，表内标“ar5iv 转述”。
- 正文另用到的论文（未入表，只核对了 arXiv 摘要页或指定段落）：Choromanska 等 arXiv:1412.0233、Draxler 等 arXiv:1803.00885（ICML 2018）、Li 等 arXiv:1804.08838（ICLR 2018）、Frankle 与 Carbin arXiv:1803.03635、Kawaguchi arXiv:1605.07110（NIPS 2016）、Safran 与 Shamir arXiv:1712.08968、Pope 等 arXiv:2104.08894、Santurkar 等 arXiv:1805.11604、Micikevicius 等 arXiv:1710.03740（ICLR 2018）、GPT-2 原文 Sec.2.3（PDF 逐字核对）、BERT 附录 A.2–A.3、InstructGPT 引言与式 2。

**未核实 / 待验证**

- Choromanska 等的正式发表版本与作者单位；Safran 与 Shamir 的正式发表版本；Micikevicius 等的作者单位。正文因此未写这几项。
- Xiong 等 BERT 预训练的加速比例：ar5iv 转述的原句前后矛盾，未写入。
- 正文没有讨论训练中途的损失尖峰（loss spike）与大模型的训练不稳定，本轮没有选到对应的原文。
- GPT-3 的规模选择是否直接依据 Kaplan 等的配比，本轮未在 GPT-3 原文中核对；正文与关联中只写了 Chinchilla 把它作为对照。
