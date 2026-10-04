# 训练科学：把训练过程本身当作研究对象

> 状态：领域入门页 · v1 · 依据 [synthesis.csv](synthesis.csv)（15 篇）
>
> 速览：
> - 训练科学把训练过程本身当作测量对象：先测训练中的统计量（激活、梯度方差、曲率、损失曲线），再据此改配方；Glorot 与 Bengio（2010）是起点。
> - 主线是一条问题链：能不能训起来（初始化、优化地形）→ 怎样在大规模上训（批量、预热、归一化的位置）→ 好多少、预算怎么分（双下降、规模定律）→ 改多少就够、怎样不毁掉已有能力（本征维度、LoRA、遗忘）。
> - 每条规律都有失效的边界：线性缩放在批量超过约 8k 后失效，Kaplan 的配比被 Chinchilla 修正，地形结论多在小网络上测得。
> - 训练科学与模型科学研究同一批参数：induction head 的形成正对应损失曲线上的鼓包，grokking 的“突然泛化”在机制层面是连续的三段，ROME 的秩一编辑与秩为 1 的 LoRA 形式相同（见“与模型科学的关系”）。

[返回跨方向目录](../../README.md) · [论文目录](PAPERS.md) · [综合表](synthesis.csv) · [基础分区：优化（机制怎么算）](../../../foundations/fields/optimization/README.md) · [模型科学（训练出来的模型里有什么）](../model-science/README.md) · [观点：深度学习的规模化](../../../perspectives/scaling.md)

## 这个领域在解决什么

DeepMind 手里有一份固定的训练算力，已经用它训出了 280B 参数、看过 300B 个 token 的 Gopher。同样的算力，换成 70B 参数、1.4T 个 token，训出的 Chinchilla 在 MMLU（由 57 个学科考试题组成的多选题知识基准）上 5-shot 平均准确率 67.6%，Gopher 是 60.0%。结构、数据来源和优化器都没换，换的只是“参数多少、数据多少”这一个配比，而这个配比是从 400 多次小规模训练的损失曲线里拟合出来的。训练科学研究的就是这类问题：训练过程本身有哪些可以测量、可以预测的规律。具体包括优化器面对的损失地形长什么样，学习率、批大小、预热这些配方背后有什么经验规律，损失怎样随模型、数据、算力变化（规模定律），模型变大时测试误差为什么会先升后降（双下降），训练实际用到了多少自由度（本征维度），以及分阶段训练时后一阶段怎样不毁掉前一阶段学到的能力（灾难性遗忘）。

初始化、归一化、Adam、学习率调度这些机制怎么计算，属于基础层，见[基础分区：优化](../../../foundations/fields/optimization/README.md)；本页只在需要时用一句话提到它们。训练好的模型内部有什么（注意力头、FFN 中的知识、层的冗余），属于[模型科学](../model-science/README.md)。

## 主线历史

节点按问题链排列，年份有交叠。每个节点先写上一个节点留下的问题，再写它改变了什么；逐篇出处在[综合表](synthesis.csv)。

1. **把训练当成测量对象：Glorot 与 Bengio（2010，Montréal）**。问题：2006 年以后，深网络要先做逐层无监督预训练等特殊初始化才能训好；同样的网络从标准随机初始化直接做梯度下降，效果差且原因不明。改变：把“难训”拆成训练中可以测量的量，即逐层激活是否饱和（落进 sigmoid、tanh 两端梯度接近 0 的平坦区）、反传梯度的方差怎样随层变化，再据此推出让方差逐层大致保持的初始化尺度（推导见[优化讲义目录](../../../foundations/lessons/02-optimization.md)）。5 个隐藏层的 tanh 网络在 Shapeset-3×2 上，测试误差从 27.15% 降到 15.60%。从这里起，研究训练的方式变成：先测量训练中的统计量，再针对性地改配方。**做不好的场景**：推导假设激活在 0 附近近似线性，换成 ReLU 后这个假设不成立，He 等（2015）报告 30 层 ReLU 网络用这种初始化完全停滞（见节点 3）。
2. **优化地形：困住训练的主要是鞍点，各个解之间彼此相连（2014–2018）**。问题：初始化改善之后，训练仍会长时间停在平台上（损失几乎不降），通常的解释是陷进了坏的局部极小。改变：Dauphin 等（2014，Montréal 与 Stanford）依据统计物理和随机矩阵理论论证，在高维问题中，误差远高于全局最小的临界点（梯度为 0 的点）以指数级的概率是鞍点（有的方向向上弯、有的方向向下弯，见[梯度与 SGD 讲义](../../../foundations/lessons/modules/optimization/gradient-sgd.md)第 8 节），负曲率方向的比例随误差升高而增加；他们在小网络上测量了这一关系，用它解释平台期，并提出能逃离鞍点的 saddle-free Newton 方法。同年 Choromanska、LeCun 等在球面自旋玻璃模型的简化假设下得到：大网络的低临界值集中在全局最小之上的一条窄带内，带外局部极小的数目随网络规模指数减少。2018 年，Garipov 等（Cornell 与 Samsung AI 等）与 Draxler 等独立发现，分别训练得到的两个解之间存在一条训练损失和测试精度几乎不变的曲线（模式连通，mode connectivity）。**做不好的场景**：理论结论依赖随机场、自旋玻璃等简化假设，实测集中在小网络和 CIFAR 规模；Safran 与 Shamir 用计算机辅助证明，两层 ReLU 网络在学生与教师宽度相同（6 到 20 个单元）时坏局部极小很常见，轻度过参数化之后才大幅减少（证据分层见“当前开放问题”第一条）。
3. **训练配方的经验规律：先在更大规模上暴露失败，再给出简单规则，之后才被解释（2015–2020）**。问题：地形研究解释了训练为什么通常能找到低损失的解，但没有回答网络变深、批量变大、换成 Transformer 时，初始化和学习率该怎样定。改变：几条经验规律先后出现。He 等（2015，Microsoft Research）报告 30 层 ReLU 网络用 Xavier 初始化完全停滞，按 ReLU 重推方差条件后可以收敛；Goyal 等（2017，Facebook）提出线性缩放规则（mini-batch 乘以 k，学习率也乘以 k）加 5 个 epoch 的渐进预热（学习率从小值逐步升到目标值），ResNet-50 以 mini-batch 8192 在 256 块 GPU 上 1 小时训完 ImageNet，top-1 错误率 23.74%，与 mini-batch 256 的 23.60% 相当，超过约 8k 后误差开始上升。解释往往晚于规则：原始 Transformer（2017）用 4000 步预热，是一条经验配方；Xiong 等（2020，中科院计算所、北京大学、Microsoft Research 等）证明，初始化时层归一化放在残差相加之后（Post-LN）的末层梯度上界与层数 L 无关，放在子层输入处（Pre-LN）的上界按 1/√L 缩小，所以 Post-LN 一开始梯度过大、需要预热，Pre-LN 可以去掉预热。IWSLT14 德→英翻译上，同一个 Post-LN 模型用 Adam 时，去掉预热 BLEU（译文与参考译文的词组重合度）只有 8.45，保留预热约 34。**做不好的场景**：每条规则只在自己的假设内成立，线性缩放在 mini-batch 超过约 8k 后误差上升，Xiong 等的理论只覆盖初始化时刻；训练中途的损失尖峰本页还没有对应的原文（见批注）。（批归一化、层归一化与 Adam 各自怎么算，见[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.2–10.4 节与 [Adam 讲义](../../../foundations/lessons/modules/optimization/adam.md)。）
4. **双下降：参数远多于样本的模型为什么还能泛化（2019）**。问题：配方让更大的模型训得动，实践中模型也往往越大越好；这与经典的偏差–方差权衡（模型过大会过拟合）相矛盾。改变：Nakkiran 等（Harvard 与 OpenAI）用有效模型复杂度（训练过程能把训练误差压到约 0 的最大样本数）统一两种说法：在它约等于训练样本数的临界区附近，测试误差随模型变大先升后降；同样的非单调也出现在训练轮数上，甚至出现在样本数上（更多数据反而变差），有标签噪声时最明显。这一现象在 CIFAR 上的 ResNet18 与 5 层 CNN、IWSLT'14 与 WMT'14 上的 Transformer 中都出现。**做不好的场景**：作者自述这一假说是非正式的，“训练误差约 0”的阈值凭经验取 0.1，临界区的宽度依赖数据分布和训练过程，原因尚未完全理解（Nakkiran 等 §2）；在临界区内，加数据或加大模型都可能让测试误差变差，所以它解释了现象，却不能事先告诉你临界区在哪里。
5. **规模定律：从“越大越好”到“好多少、预算怎么分”（2020–2022）**。问题：双下降说明临界区之外“更大更好”，但没有给出好多少，也没有说一笔算力该花在参数上还是数据上。改变：Kaplan 等（2020，OpenAI）发现，语言模型的测试交叉熵分别随参数量 N、数据量 D、算力 C 呈幂律下降（例如只受参数量限制时，损失正比于 N 的 −0.076 次方），跨越 7 个以上数量级，而与深宽比关系很弱；据此建议把增加的算力主要用于加大模型（算力增加 10 倍时，参数量加 5.5 倍、训练 token 只加 1.8 倍），并在收敛前停止训练。Hoffmann 等（2022，DeepMind）训练 400 多个从 70M 到 16B 以上参数的模型、用三种方法重新拟合，得到模型大小与训练 token 数应按相同比例增长；按此训练的 Chinchilla 就是开头的例子（[Chinchilla 文献卡](../../papers/arxiv-2203.15556/README.md)）。作者把两家结论的差别归于两点：学习率余弦周期是否与训练 token 数匹配，以及拟合时是否纳入更大的模型。**做不好的场景**：Kaplan 等写明规律没有可靠的理论解释，并在约 10^12 参数处两条规律相互矛盾；拟合对象是交叉熵，下游能力要另外验证；Chinchilla 的分析假设训练不超过一个 epoch，数据需要重复使用时不在覆盖范围内（详见“当前开放问题”）。
6. **本征维度：训练实际用到多少自由度（2018–2021）**。问题：规模定律讲的是从头训练；预训练之后，下游任务常常只有几百到几千条标注，微调数亿参数却不明显过拟合（这正是 Aghajanyan 等引言提出的问题）。改变：Li 等（2018）把网络限制在一个随机子空间里训练，测出解出任务所需的最小子空间维数（本征维度），远小于参数量；Aghajanyan 等（2020，Facebook）在预训练语言模型上测到，RoBERTa-Large 在 MRPC 上只训练 200 个参数（再随机投影回全参数空间），就达到全参数微调 90% 的效果；预训练会持续降低本征维度，相同预训练步数下模型越大本征维度越低。Hu 等（2021，Microsoft）的 LoRA 以这两篇为依据，假设微调时的权重变化是低秩的，冻结原权重、只训练两个小矩阵的乘积，可训练参数比全参数微调少约 10000 倍（从一个线性层推导 LoRA，见[迁移与元学习讲义](../../../foundations/lessons/05c-transfer-meta-learning.md)第 4–5 节）。**做不好的场景**：LoRA 自述两点，把两个小矩阵合并进原权重以消除推理延迟之后，就不便在同一次前向计算中批处理不同任务的输入（§4.2）；施加在哪些权重矩阵上主要凭经验（§8），原文只改注意力权重、冻结 MLP。
7. **灾难性遗忘与分阶段训练：后一阶段怎样保住前一阶段的能力（2017–2022）**。问题：适配只需改动少量自由度，但顺序训练仍会冲掉已有能力；大模型的训练又恰好分成多个阶段（预训练 → 监督微调 → 人类反馈强化学习）。改变：Kirkpatrick 等（2017，DeepMind）把灾难性遗忘描述为学新任务时改动了对旧任务重要的权重，他们的 EWC 用 Fisher 信息（衡量参数变动对旧任务输出影响大小的量）给重要参数加二次惩罚。InstructGPT（2022，OpenAI）在人类反馈强化学习中对 SFT 模型（先用人工示范答案监督微调得到的模型）加逐 token 的 KL 惩罚（KL 散度衡量两个输出分布的差异；作者写明加它是为了缓解对奖励模型的过度优化），并把预训练数据的似然梯度混进 PPO（一种限制每步策略改动幅度的强化学习算法）的更新，称为 PPO-ptx，由它大幅收回公开 NLP 基准上的能力回退（[InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 6、8、11 节）。**做不好的场景**：EWC 在 10 个 Atari 游戏上达不到分别训练 10 个 DQN 的总分；InstructGPT 单纯调大 KL 系数收不回 DROP、SQuAD 上的回退，PPO-ptx 之后 DROP 仍比 GPT-3 低 1.93 F1。

## 技术地基

- **梯度、SGD 与 Adam**：本页的经验规律（学习率随批量缩放、预热、调度）都是关于这些优化器在大规模下怎样表现的规律。[梯度与 SGD 讲义](../../../foundations/lessons/modules/optimization/gradient-sgd.md)、[Adam 讲义](../../../foundations/lessons/modules/optimization/adam.md)；整个分区的概念地图见[基础分区：优化](../../../foundations/fields/optimization/README.md)。
- **曲率、Hessian 与鞍点**：Hessian（损失对参数的全部二阶偏导排成的矩阵）的特征值有正有负的临界点就是鞍点，节点 2 的地形研究统计的正是这些特征值。[梯度与 SGD 讲义](../../../foundations/lessons/modules/optimization/gradient-sgd.md)第 7–8 节。
- **残差连接与层归一化**：节点 3 中 Post-LN 与 Pre-LN 的差别，就在归一化放在残差支路的哪一侧。[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.2–10.4 节。
- **交叉熵**：规模定律拟合的对象是留出集上每个 token 的交叉熵。[任务与训练目标模块](../../../foundations/lessons/03-tasks-losses.md)。
- **数据并行与混合精度**：节点 3 的大批量训练建立在多卡合并梯度之上。[分布式训练讲义](../../../foundations/lessons/05a-distributed-training.md)第 3、5、8 节。
- **微调与低秩适配**：节点 6、7 讨论的对象。[迁移与元学习讲义](../../../foundations/lessons/05c-transfer-meta-learning.md)第 2–6 节。

## 主要路线与团队偏好

- **解释训练为什么能成功：地形与泛化**（Montréal 的 Dauphin 等；Choromanska、LeCun 等；Cornell 的 Garipov、Wilson 等；Draxler 等；Harvard 与 OpenAI 的 Nakkiran 等）。押注：非凸的深网络训练在实践中能成功、过参数化的模型还能泛化，背后有可以测量的几何与统计规律，理解了它就能设计方法（saddle-free Newton、快速几何集成）。代价：理论结论依赖强假设（随机高斯场、自旋玻璃、变量独立），经验测量多在小网络或 CIFAR 规模上完成；双下降的“临界区宽度”没有形式定义。[判断] Bengio 所在的 Montréal 组在 2010 与 2014 两篇中都先测量训练中的统计量（逐层激活与梯度方差；临界点的误差与负曲率比例），再提出针对性的方法。
- **在规模上找配方的经验规律**（Microsoft Research 与 Facebook 的 He 一系；Google 的 Ioffe 与 Szegedy；Xiong 等）。押注：把规模加大后训练失败的具体现象暴露出来，就能找到一条简单、可推导的规则。代价：每条规则依赖特定假设，结构一换就要重新找（Glorot 假设线性区，He 针对 ReLU，线性缩放在 mini-batch 超过约 8k 后失效）；理论解释大多只覆盖初始化时刻。[判断] He 一系在 Delving Deep into Rectifiers、ResNet、大批量 SGD 三篇中都以 ImageNet 为目标，先暴露“规模加大后训练失败”的现象（30 层停滞、更深反而训练误差上升、大批量早期困难），再给出简单规则（方差条件、残差、线性缩放加预热），而不提出新的优化器。
- **用规模定律做预算**（OpenAI 的 Kaplan、Henighan 等；DeepMind 的 Hoffmann 等；Google Brain 的 Zhai 等）。押注：在一系列较小的模型上拟合幂律，外推决定大模型的参数量与数据量。代价：拟合出的指数依赖实验协议，Kaplan 与 Chinchilla 因学习率调度和规模范围不同得出不同配比；规律预测的是交叉熵或某个迁移任务的错误率，其他下游能力要另外验证。[判断] OpenAI 在 Kaplan 等（语言）与 Henighan 等（图像、视频、图文、数学）两篇中用同一套方法拟合规模定律，两篇共享 Kaplan、McCandlish、Henighan、Amodei 等作者；Kaplan 等又与 GPT-2 有多位共同作者，它把这个团队“decoder-only 加扩大规模”的押注变成了可以计算的预算（路线本身见[预训练方向](../../../llm/fields/pretraining/README.md)）。
- **只改少量自由度、保住已有能力**（DeepMind 的 EWC；Facebook 的 Aghajanyan 等；Microsoft 的 LoRA；OpenAI 的 InstructGPT）。押注：已学到的能力集中在预训练权重里，适配只需在低维子空间里改动，或对偏离原模型的程度加约束。代价：LoRA 施加在哪些矩阵上主要凭经验；EWC 在 10 个 Atari 游戏上达不到分别训练 10 个 DQN 的总分；PPO-ptx 之后 DROP 仍比 GPT-3 低 1.93 F1（[InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 11 节）。

## 用什么衡量进展

benchmark 的替换反映了这个方向目标的迁移：从“能不能训起来”，到“训多快”，到“能预测多少”，再到“改完之后还剩多少”。

- **能不能训起来（2010–2015）**：Shapeset-3×2、MNIST、CIFAR-10 上的测试误差，以及训练曲线是否停滞（Glorot、Dauphin、He 的 30 层实验）。这些数据集小，适合逐层测量梯度统计和临界点的曲率。
- **训多快（2015–2020）**：ImageNet top-1/top-5 错误率加上达到同一精度所需的训练步数或墙钟时间（批归一化让 Inception 变体所需步数少 14 倍、Goyal 的 1 小时），翻译 BLEU（IWSLT14、WMT14，Xiong）。口径问题：步数倍数依赖选定的目标精度；“1 小时”依赖 256 块 GPU 的硬件条件。
- **能预测多少（2020 起）**：留出集上的交叉熵（每个 token 的 nats）对 N、D、C 的拟合，再用 MMLU、BIG-bench 等下游任务检验按预测训练出的模型（Chinchilla）。口径问题：Kaplan 的数据来自单一的 WebText2，Chinchilla 的分析假设训练不超过一个 epoch；交叉熵的平滑下降不直接等于下游能力的同步提升。
- **改完之后还剩多少（2017 起）**：适配方法与全参数微调在 GLUE、E2E NLG、WikiSQL 等上的成绩对比，加上可训练参数量、显存和推理延迟（LoRA）；遗忘则看旧任务的回退，例如置换 MNIST 序列与 Atari（EWC），以及人类反馈强化学习后 SQuAD、DROP、HellaSwag、WMT 法→英相对 GPT-3 的变化（InstructGPT）。

## 不同模态的差异

本页的综合表以语言和图像分类为主。下表对照每个研究对象在各模态上的证据来自哪里。

| 研究对象 | 语言 | 视觉 | 其他模态 |
|---|---|---|---|
| 规模定律 | Kaplan 等：WebText2 上的交叉熵；Chinchilla：MassiveText，附录 C 在 C4 与 GitHub 代码上的 IsoFLOP 结果相近（前提是不超过一个 epoch） | Henighan 等 2020：自回归图像生成的交叉熵；Zhai 等（CVPR 2022，Google Brain）：ViT 在 JFT-3B 上有监督预训练后的 ImageNet 迁移错误率，并在公开的 ImageNet-21k 上复核 | Henighan 等：视频、图文双向生成、数学解题 |
| 训练配方的经验规律 | Xiong 等：Post-LN、预热与 Pre-LN | Goyal 等：线性缩放与预热；ConvNeXt：只把 ResNet-50 换成 Transformer 式训练配方（300 epoch、AdamW、Mixup/CutMix 等数据增强），ImageNet-1K 精度从 76.1% 升到 78.8% | — |
| 优化地形 | Dauphin 等的 Penn Treebank 循环网络 | Dauphin 等：降采样 MNIST、CIFAR-10 上的小 MLP；Garipov 等：CIFAR 与 ImageNet 上的 VGG、ResNet、Wide ResNet | — |
| 双下降 | Nakkiran 等：IWSLT'14、WMT'14 上的 Transformer | Nakkiran 等：CIFAR 上的 ResNet18、5 层 CNN | — |
| 本征维度与低秩适配 | Aghajanyan 等；LoRA | 数据一侧的本征维度：Pope 等 2021 | 机器人：OpenVLA 用 LoRA 微调（[OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)） |
| 遗忘与分阶段训练 | InstructGPT | EWC：置换 MNIST | EWC：Atari 强化学习 |

从这张表可以读出三点差别。

- **规模定律测的量不同。** 语言和生成式模型拟合交叉熵，Henighan 等发现图像、视频、图文、数学都服从“幂律加常数”（常数对应数据本身不可约的熵），而且最优参数量都约随算力的 0.7 次方增长，与 Kaplan 在语言上的结果接近。判别式视觉拟合的是迁移错误率：Zhai 等发现错误率随算力的前沿在两端都饱和（双饱和幂律）——算力最大时错误率趋向一个非零值，算力最小时连最小的模型也有非零准确率。错误率有上下界，交叉熵没有，所以两类曲线的形状不能直接比较。
- **训练信号与数据的可得性不同。** Zhai 等在引言中写明，视觉中最成功的预训练是有监督的，NLP 是无监督的；视觉规模定律的主要证据依赖非公开的 JFT 数据集（ViT 依赖 JFT-300M，Zhai 等依赖 JFT-3B）。数据规模在视觉里还决定架构比较的结论：ViT 在 JFT-300M 的 9M 张子集上不如计算量相近的 ResNet，90M 张以上反超（见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)）。
- **地形证据集中在图像分类和小网络上。** 综合表中的地形测量来自 CIFAR、ImageNet 上的卷积网络和小 MLP，语言一侧只有一个 Penn Treebank 循环网络；Transformer 语言模型上的地形测量，综合表中还没有对应的论文。

由此留下两个开放问题：

- [判断] Henighan 等的“各模态最优配比相近”沿用了 Kaplan 的方法，Chinchilla 修正的正是这套方法在语言上的配比；其他模态的配比是否也要按 Chinchilla 的方式修正，目前没有看到原文检验。Chinchilla 作者在结论中只写了“预期其他模态也有类似权衡”。Zhai 等的结果（小模型加数据无益，大模型从 10 亿张到 30 亿张仍在受益）在方向上与“模型与数据一起加”一致。
- 鞍点、模式连通这类地形结论能否推广到大规模 Transformer 语言模型，需要新的测量。

## 与模型科学的关系

训练科学从训练过程问“参数怎样被用上、何时用上”，[模型科学](../model-science/README.md)从训练结果问“参数里存了什么、怎样起作用”。两边研究同一批参数，假说可以互相检验：训练曲线上的突变需要内部机制来解释，内部机制需要训练动态来说明它何时、为何形成。下表把两边对照起来。

| 训练科学的假说或现象 | 模型科学的发现 | 关系 | 两边怎样互相解释 |
|---|---|---|---|
| 训练早期损失曲线上的一个鼓包：上下文学习能力在约 25 亿到 50 亿 token 之间骤升 | [Induction head](../../papers/arxiv-2209.11895/README.md)：前一层的“前一 token 头”与后一层的复制头组成电路，完成 [A][B] … [A] → [B] 的续写 | `[经验]` | Olsson 等（2022，Anthropic）发现 induction head 形成的时刻，正是损失曲线出现鼓包、上下文学习骤升的时刻；只有一层的模型两者都不出现。改架构让 induction head 更容易形成（smeared key：每个头的 key 可以混入前一个 token 的 key）之后，一层模型也出现了上下文学习，两层以上的模型骤升提前。损失曲线上的一个形状由此对应到一个具体电路 |
| grokking：训练集早已拟合，测试精度很久之后才突然上升 | [Nanda 等](../../papers/arxiv-2301.05217/README.md)（ICLR 2023）把在模加法上训练的小 Transformer 完整逆向：它用离散傅里叶变换和三角恒等式把加法变成圆上的旋转 | `[经验]` | 用这个机制定义的进度指标，把训练分成连续的三段：记忆、电路形成、清理。电路在测试精度上升之前早已形成，“突然”来自权重衰减把记忆成分清除；没有权重衰减或其他正则时，这些网络在该任务上不出现 grokking。看似不连续的训练现象，在机制层面是连续的 |
| 本征维度与低秩更新：微调只需改动很少的自由度（节点 6）；LoRA 在 GPT-3 上秩取 1 就足以适配 WikiSQL 与 MultiNLI | [ROME](../../papers/arxiv-2202.05262/README.md)：一条事实可以用一次秩一更新写进一层 MLP | `[结构]` | ROME 的更新 Ŵ = W + Λ(C⁻¹k\*)ᵀ 是一个列向量乘一个行向量；LoRA 的 ΔW = BA 取秩 r = 1 时，B 是一列、A 是一行，形式相同。差别在求法与位置：ROME 按键值记忆的读法用闭式解一次算出，key 由主语决定，改的是 MLP；LoRA 在任务数据上用梯度学，原文只改注意力权重。[判断] 键值记忆的读法给“低秩更新为什么够用”提供了一种解释：写入或改动少量键值对，本来只需要低秩的权重变化；它能否解释 LoRA 在一般任务上的效果，没有看到原文检验 |
| 过参数化与彩票假说：训练出的网络有大量冗余，存在可单独训练的稀疏子网络 | [ShortGPT](../../../llm/papers/arxiv-2403.03853/README.md)：大模型许多层的输入与输出几乎相同，按层的重要性删掉 25% 的层，LLaMA 2-13B 的 MMLU 只从 55.0 降到 52.2 | `[判断]` | 两边都在说“参数没有被同等用上”，对象却不同：[彩票假说](../../papers/arxiv-1803.03635/README.md)针对初始化时的稀疏连接，在 MNIST、CIFAR10 的小网络上成立；ShortGPT 针对训练后的整层，在 7B–13B 的语言模型上成立。两者能否互相推出，没有直接证据。冗余也有边界：删掉 25% 的层后，Llama2-7B 与 Baichuan2-7B 在 XSum、C3 等生成任务上的成绩接近 0（ShortGPT §5） |
| 知识在预训练中怎样形成：[Chang 等](../../papers/arxiv-2406.11813/README.md)（NeurIPS 2024）在 OLMo 的中途检查点上注入新事实，发现事实知识是每见一次概率小幅上升、随后被遗忘稀释的累积过程；遗忘与训练步数呈幂律，重复数据遗忘更快，更大的批量更抗遗忘 | 事实写在哪里：ROME 的因果追踪指向中间层 MLP；[Dissecting Recall](../../papers/arxiv-2304.14767/README.md) 指向较早层 MLP 把属性写进主语表示、再由上层注意力读出 | `[判断]` | 前者回答“何时、以什么节奏写进去”，后者回答“写在哪里、怎样读出”。Chang 等用累积–遗忘过程解释长尾知识表现差与语料去重有益；这些知识写进了哪几层、是否就是因果追踪定位到的那几层，没有看到同时测两者的原文 |
| 灾难性遗忘：EWC 用 Fisher 信息衡量参数对旧任务的重要性，给重要参数加惩罚（节点 7） | 因果追踪按“恢复激活后正确答案的概率恢复多少”定位事实；[Hase 等](../../papers/arxiv-2301.04213/README.md)（NeurIPS 2023）在 GPT-J 上发现，追踪效应与在该层编辑的成功率相关接近 0 | `[判断]` | “哪些参数重要”有两种定义：对损失的敏感度（Fisher 信息）和对输出的因果效应（因果追踪）。Hase 等的结果说明，后者定位到的位置不直接告诉我们该改哪里；两种定义在同一模型上是否一致，没有看到原文比较 |

这张表读出三点。

- [判断] 前两行两边对得上：训练中的突变都被追溯到一个电路的形成，而机制层面的指标能把看似突然的变化拆开（grokking 一例中，电路比测试精度的上升早得多）。训练科学的宏观曲线可以用模型科学的部件来分解。
- 第三行在形式上对得上（`[结构]`），解释力还没有检验。
- [判断] 后三行两边各测各的：训练科学测自由度、冗余和遗忘速度，模型科学测位置和因果效应，还没有原文在同一个模型上同时测量两者。这是两个方向最直接的合作点；训练数据、代码和中途检查点都公开的模型（例如 Chang 等使用的 [OLMo](../../../llm/papers/arxiv-2402.00838/README.md)）让这种测量可以做。

## 当前开放问题

- **“规模大了反而不容易陷入局部最优”的准确说法与证据边界。** 能被证据支持的说法是：在参数很多的网络里，阻碍训练的主要是鞍点和平台期，而不是损失明显更高的坏局部极小；训练得到的不同解损失相近，并由低损失的路径相连。证据分三层：Dauphin 等的理论来自随机场模型的结果，实测只在小网络上；Choromanska 等的“带外坏极小随规模指数减少”成立于自旋玻璃模型的简化假设下，“SGD 收敛到低值带”在原文中是猜想；Garipov 等与 Draxler 等在 CIFAR-10、CIFAR-100 上的现代卷积网络（ResNet、DenseNet 等）中观察到模式连通。边界：这里的“规模”指参数量或宽度（过参数化），与数据量和训练时长无关；对一般的非线性网络没有证明，Kawaguchi（2016）对深线性网络证明了每个局部极小都是全局极小，推广到非线性网络需要独立性假设；Safran 与 Shamir 用计算机辅助证明，两层 ReLU 网络在学生与教师宽度相同（6 到 20 个单元）时坏局部极小很常见，且命中概率随规模增加，轻度过参数化后才大幅减少。大模型训练的实际障碍随之转到数值稳定与超参数上（节点 3）。入口：[Dauphin 等](https://arxiv.org/abs/1406.2572)、[Choromanska 等](https://arxiv.org/abs/1412.0233)、[Garipov 等](https://arxiv.org/abs/1802.10026)、[Safran 与 Shamir](https://arxiv.org/abs/1712.08968)。
- **规模定律能外推多远？** Kaplan 等自己写明：这些规律没有可靠的理论解释；按其趋势外推，在约 10^12 参数、10^12 token、10^4 PF-day（每秒 10^15 次浮点运算持续一天为 1 PF-day）处 L(C) 与 L(D) 两条规律相互矛盾，规律必然在此之前失效；结论来自单一数据分布，学习率选择对结果敏感。Chinchilla 改变学习率调度、纳入更大模型后，最优配比就从“主要加参数”变成“参数与数据等比例”，说明拟合出的指数依赖实验协议；它自己也报告了高算力处最优参数量曲线的弯曲，以及单 epoch 假设（数据不够、需要重复使用时不在其覆盖范围内）。双下降则提示在临界规模附近测试误差可以非单调。另一条规模轴是推理时投入的算力，见 [Test-Time Compute 精读](../../../llm/papers/test-time-compute/reading.md)；规模化作为跨领域现象的论证见[观点：深度学习的规模化](../../../perspectives/scaling.md)。入口：[Chinchilla 文献卡](../../papers/arxiv-2203.15556/README.md)、[Kaplan 等](https://arxiv.org/abs/2001.08361)、[Nakkiran 等](https://arxiv.org/abs/1912.02292)。
- **少量参数为什么就够？** 这里有两种“低维”。数据一侧是流形假说（高维数据集中在低维结构附近）：Pope 等（ICLR 2021）估计常见自然图像数据集的本征维度远低于像素数，本征维度低的数据集更容易学、泛化更好。参数一侧是解空间的低维：Li 等与 Aghajanyan 等的本征维度、LoRA 的低秩增量，以及[彩票假说](../../papers/arxiv-1803.03635/README.md)（Frankle 与 Carbin，ICLR 2019：在 MNIST、CIFAR10 上的全连接和卷积网络里，找到只有原网络 10–20% 大小、保留原始初始化就能单独训到相当精度的子网络）。[判断] 两侧的低维是否同源，仍是开放问题。入口：[Aghajanyan 等](https://arxiv.org/abs/2012.13255)、[LoRA](https://arxiv.org/abs/2106.09685)、[OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)（LoRA 在机器人模型上的实际用法）。
- **后续训练阶段怎样保住已有能力？** InstructGPT 报告，单纯调大 KL 系数会显著降低验证奖励，且在 DROP、SQuAD 上始终收不回来，混入预训练梯度效果更好；EWC 在 Atari 上仍有差距。入口：[InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)、[Kirkpatrick 等](https://arxiv.org/abs/1612.00796)、[后训练：强化学习方向](../../../llm/fields/posttraining/rl/README.md)。

## 阅读顺序

1. [基础分区：优化](../../../foundations/fields/optimization/README.md)与[梯度与 SGD 讲义](../../../foundations/lessons/modules/optimization/gradient-sgd.md)第 7–8 节：先掌握优化器怎么算、曲率和鞍点是什么，本页每个节点都把它们当作研究对象。
2. [Dauphin 等](https://arxiv.org/abs/1406.2572)与 [Garipov 等](https://arxiv.org/abs/1802.10026)：节点 2，地形研究怎样从“测量临界点”走到“发现解之间相连”。
3. [Attention Is All You Need 精读](../../../llm/papers/transformer/reading.md)第 4 节，再读 [Xiong 等](../../../llm/papers/arxiv-2002.04745/README.md)：节点 3，一条经验配方（预热）怎样在三年后得到解释。
4. [Chinchilla 文献卡](../../papers/arxiv-2203.15556/README.md)，配合 [Kaplan 等](https://arxiv.org/abs/2001.08361)原文：节点 5，以及规模定律外推边界这个开放问题；读完可接[预训练方向](../../../llm/fields/pretraining/README.md)，看这些配比怎样落到具体模型上。
5. [迁移与元学习讲义](../../../foundations/lessons/05c-transfer-meta-learning.md)第 4–6 节，再读 [InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 6、8、11 节：节点 6、7 的两种做法，低秩适配与对偏离加约束。

## 批注

**易误读**

- 开头例子中 Chinchilla 的 MMLU 成绩，摘要写作 67.5%，正文 Sec.4.2.2 与 Table 6 为 67.6%（5-shot，57 个任务的平均）；与 Gopher 的 60.0% 相比高 7.6 个百分点。
- 节点 3 中 8.45 对约 34 的 BLEU，比较的是同一个 Post-LN 模型在 IWSLT14 上用 Adam 时去掉与保留预热（Xiong 等 Sec.3.2）。原文报告的是效果很差，没有说训练数值发散。
- 批归一化原文用 internal covariate shift 解释其效果。Santurkar 等（NeurIPS 2018）认为层输入分布是否稳定与批归一化的效果关系不大，它主要让优化地形明显更平滑。
- Kaplan 等“主要加参数”的配比（N ∝ C^0.73）已被 Chinchilla 的等比例结论修正；引用时要注明是哪一篇、哪种学习率设定。Henighan 等在各模态上得到的约 0.7 次方，沿用的也是 Kaplan 的方法。
- Choromanska 等的结论建立在三个简化假设上（变量独立、参数化冗余、均匀性），见其摘要；“SGD 收敛到低值带”在原文中是猜想。
- Adam 原文的收敛分析只覆盖凸问题，非凸网络上的优势是经验结果（Sec.6.2）。
- 彩票假说的 10–20% 来自 MNIST、CIFAR10 上的较小网络，并依赖保留原始初始化；它说明的是存在可单独训练的稀疏子网络，与 LoRA 的低秩更新是不同的对象。
- InstructGPT 中 KL 惩罚针对 SFT 模型，作者写明的目的是缓解对奖励模型的过度优化；收回公开基准能力回退的主要手段是 PPO-ptx。
- Zhai 等的双饱和幂律描述的是错误率，与 Henighan 等交叉熵的“幂律加常数”是不同的量；Zhai 等在结论中写明其结论不一定推广到所研究的规模与 ViT 家族之外。

**判断的支撑论文**

- Montréal 组的偏好：Glorot 与 Bengio Sec.3–4（逐层激活与梯度统计）、Dauphin 等的临界点测量。
- He 一系的偏好：Delving Deep into Rectifiers Fig.3（30 层 Xavier 停滞）、ResNet Sec.1（退化问题，见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)）、Goyal 等 Fig.1 与 Table（大批量）。
- OpenAI 的押注延续：GPT-2 与 Kaplan 等的作者名单（Radford、Wu、Child、Amodei 同时出现在两篇中）；Kaplan 等与 Henighan 等的作者名单（Kaplan、McCandlish、Henighan、Brown、Gray、Radford、Amodei 同时出现在两篇中），Henighan 等 Table 1 中语言一行的最优参数量直接取自 Kaplan 等。
- 其他模态的配比是否需要 Chinchilla 式修正：Henighan 等 Sec.1（N_opt ∝ C^0.7 适用于所有模态）、Chinchilla Sec.5（“预期其他模态也有类似权衡”）与附录 C（C4、GitHub 代码上的 IsoFLOP 结果）、Zhai 等 Sec.2.1（小模型加数据无益、大模型 1B→3B 张仍受益）。反例或边界：Zhai 等测的是错误率而不是交叉熵，两者的最优配比不能直接对照。
- 机制层面的指标能分解训练曲线：Olsson 等 Argument 1–2（鼓包与 induction head 同时出现；smeared key 改变形成时刻后骤升随之移动）、Nanda 等摘要与 §5（记忆、电路形成、清理三段，权重衰减的作用）。反例或边界：Olsson 等在带 MLP 的大模型上只有相关性证据；Nanda 等只研究了单一电路解决的模加法任务，作者在局限中写明大模型与真实任务另需验证。
- 键值记忆的读法解释低秩更新：ROME 式 (2) 与 Appendix A（秩一闭式解）、LoRA §4.1 与 §7.2（ΔW = BA，Table 6 中 r = 1 足以适配 W_q、W_v）。反例或边界：LoRA 原文只改注意力权重、冻结 MLP，ROME 改的是 MLP，两者作用的矩阵不同；Hase 等发现因果追踪定位的层不能预测编辑效果，说明“键值记忆写在哪里”这一层解释本身还不稳。
- 两边“各测各的”：Chang 等只测事实的对数概率随训练步数的变化，不定位层；ROME、Dissecting Recall、Hase 等只分析训练结束后的模型；ShortGPT 只分析训练后的层，Frankle 与 Carbin 只分析初始化与剪枝。反例或边界：本轮只检索了这几篇，可能存在同时测量两者的工作未被收录。
- 数据侧与参数侧低维是否同源：Pope 等 2021 的摘要只讨论数据；Li 等 2018、Aghajanyan 等 2020 只讨论目标函数的解空间；目前没有看到把两者直接联系起来的原文。

**与其他论文的关联**

- [Transformer 精读](../../../llm/papers/transformer/reading.md)第 4 节的 4000 步预热，正是 Xiong 等要解释和去掉的那个阶段。[历史] Xiong 等在引言中直接以 Post-LN 需要预热为出发点。
- [GPT-3 精读](../../../llm/papers/gpt3/reading.md)：175B 的 GPT-3 是 Chinchilla 论文中的对照模型之一，也是“约 300B token 训练”这一做法的代表（Chinchilla Sec.1、Table 1）。[历史] GPT-3 的规模选择依据了 Kaplan 等的规模定律：原文图 2.2 写明按其分析训练更大的模型、用更少的 token，作者贡献一节写明 Kaplan 与 McCandlish 用规模定律指导了模型与数据规模的决定（见[预训练方向](../../../llm/fields/pretraining/README.md)）。
- [历史] LoRA 在引言中写明受 Li 等 2018 与 Aghajanyan 等 2020 的本征维度结果启发。
- [InstructGPT 精读](../../../llm/papers/instructgpt/reading.md)第 6、8 节详细算过 KL 惩罚与 PPO-ptx，是本页节点 7 的展开。
- [ViT 精读](../../../multimodal/papers/vit/reading.md)：数据规模决定 ViT 与 ResNet 胜负的实验（Sec.4.3–4.4），是视觉一侧“规模与训练配方”的证据；ConvNeXt 的配方对照见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。
- [模型科学](../model-science/README.md)研究训练出来的模型内部有什么；两边的对照见正文“与模型科学的关系”。[Induction Heads](../../papers/arxiv-2209.11895/README.md) 与 [Nanda 等](../../papers/arxiv-2301.05217/README.md)是“机制解释训练动态”的两例，[ROME](../../papers/arxiv-2202.05262/README.md) 与 LoRA 之间是秩一更新的结构对应。
- [Chinchilla 文献卡](../../papers/arxiv-2203.15556/README.md)目前没有精读，精读时“它要解决的问题”应与本页节点 5 一致。

**综合表说明**

- 表中每行一篇，列为论文（路线）、年份、团队、要解决的问题、对照的 baseline、benchmark、自述局限、代码/数据是否开放、来源 URL。各格是原文的中文转述，注明节号、表号或图号。
- Glorot 与 Bengio、Adam 两篇从 PDF 全文逐字核对；其余各篇通过 ar5iv 页面，由摘要模型转述，表内标“ar5iv 转述”。
- 正文另用到的论文（未入表，只核对了 arXiv 摘要页或指定段落）：Choromanska 等 arXiv:1412.0233、Draxler 等 arXiv:1803.00885（ICML 2018）、Li 等 arXiv:1804.08838（ICLR 2018）、Frankle 与 Carbin arXiv:1803.03635、Kawaguchi arXiv:1605.07110（NIPS 2016）、Safran 与 Shamir arXiv:1712.08968、Pope 等 arXiv:2104.08894、Santurkar 等 arXiv:1805.11604、GPT-2 原文 Sec.2.3、InstructGPT 引言与式 2。“不同模态的差异”一节另用到 Henighan 等 arXiv:2010.14701（PDF 全文：摘要、Sec.1、Table 1、Fig.2）、Zhai 等 arXiv:2106.04560（PDF 全文：Sec.1、Sec.2.1–2.2、结论与局限）、Chinchilla Sec.1、Sec.5 与附录 B、C（PDF 全文），以及 ViT、ConvNeXt 的数字（取自视觉方向已核实的综合表）。这三篇新增论文尚未入表，见 [PAPERS.md](PAPERS.md)。“与模型科学的关系”一节另用到 Olsson 等（Argument 1–2）、Nanda 等 arXiv:2301.05217、Chang 等 arXiv:2406.11813、Hase 等 arXiv:2301.04213、ShortGPT arXiv:2403.03853（摘要、§1、§5 局限）、LoRA §4.2、§7.2、§8，以及 ROME 式 (2)，均为 PDF 选段核对，未入综合表；“做不好的场景”另用到 Nakkiran 等 §2 对假说非正式性的说明。

**未核实 / 待验证**

- Choromanska 等的正式发表版本与作者单位；Safran 与 Shamir 的正式发表版本。正文因此未写这几项。
- Xiong 等 BERT 预训练的加速比例：转述的原句前后矛盾，未写入。
- 正文没有讨论训练中途的损失尖峰（loss spike）与大模型的训练不稳定，本轮没有选到对应的原文；入门的排查思路见[梯度与 SGD 讲义](../../../foundations/lessons/modules/optimization/gradient-sgd.md)第 9 节。
- Transformer 语言模型上的模式连通与鞍点测量：本轮没有检索，“不同模态的差异”一节因此写成开放问题。
