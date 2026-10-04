# 进阶连接

[回到基础模块](../../README.md) · [完整讲义目录](../../../docs/foundations/05-advanced-bridges.md) · [跨模块关系页](../../relations/README.md)

## 这一分区回答什么

基础训练是一台机器上的循环：读数据、算预测、给错误打分、改参数。有三种情况会改变这个循环。四条样本、一张卡一次只放得下两条，加一张卡各算两条之后，两张卡怎样合成同一次更新？机器人走完一段路才知道成没成功，没人告诉它每一步该把脚放在哪里，结果怎样变成梯度？一个学过电影影评的模型，换到餐厅评论时，怎样复用已经学到的东西？本分区的三篇导读分别回答这三个问题。

## 概念地图

| 模块 | 它解决的计算问题 | 先读 |
|---|---|---|
| [分布式训练](../../../docs/foundations/05a-distributed-training.md) | 多个设备合作完成同一次参数更新：数据并行先复制模型再合并梯度，张量并行把一层拆到多卡，流水线并行把层序列拆开并用微批次填满，状态分片与混合精度节省显存 | [梯度与 SGD](../../../docs/foundations/modules/optimization/gradient-sgd.md)第 6 节；[Adam 与 AdamW](../../../docs/foundations/modules/optimization/adam.md)第 2 节 |
| [强化学习](../../../docs/foundations/05b-reinforcement-learning.md) | 只知道行动后果、不知道每步正确答案时，把回报（一段未来奖励的累计）变成参数更新：价值与优势判断一个动作比平常好多少，策略梯度提高好动作的概率，PPO 限制每次更新的幅度，DPO 直接从偏好对训练 | [概率分类](../../../docs/foundations/modules/objectives/02-classification-probabilities.md)第 6、8 节 |
| [迁移与元学习](../../../docs/foundations/05c-transfer-meta-learning.md) | 复用已学到的东西：冻结、全量微调，或用 LoRA 只训练一个低秩增量；元学习把"适应之后的效果"写进训练目标；上下文学习靠提示里的示例适应，不改权重 | 梯度与 SGD；[Attention 与 Transformer](../../../docs/foundations/14-attention-transformer.md) |

三篇互不依赖，分别接在优化、目标和架构分区之后。它们与基础模块的关系如下，`[结构]` 表示数学上是同一结构或特例：

- **数据并行就是更大批量的 SGD**：两张卡样本数相同时，全局梯度 g = (g₁ + g₂)/2 与单卡用全部样本算出的平均梯度相同，两卡用它更新后参数仍然一致 `[结构]`（分布式训练第 3 节）。样本数不同时要按样本数加权（第 4 节）；梯度累积是在时间上做同一件事（第 5 节）。
- **状态分片拆的是优化器状态**：P 个参数用 4 字节浮点保存时，参数、梯度和 Adam 的两份状态合计约 16P 字节，状态分片把它们分到不同设备（分布式训练第 8 节）。
- **策略梯度是加权的 NLL**：代理损失 −A·log π_θ(a|s) 在优势 A = 1 时，就是对采样动作做分类的负对数似然；A 给每条样本加权，正优势提高该动作的概率，负优势降低它 `[结构]`（强化学习第 5 节）。由此，行为克隆（直接模仿示范动作）是所有权重都为 1 的特例。
- **KL 把新策略拴在参考模型附近**：后训练中的 KL 惩罚限制策略偏离参考策略的程度；DPO 从带 KL 正则的奖励优化目标推出直接训练策略的损失（强化学习第 8–9 节）。KL 的定义与方向性见概率分类第 8 节。
- **LoRA 是低秩的权重增量**：冻结 W₀，把更新写成 W = W₀ + sBA，A 的形状为 [r, d_in]，B 为 [d_out, r]，所有输出修正都由 B 的 r 个列方向组合而成，增量的秩至多为 r `[结构]`（迁移与元学习第 4–5 节）。秩与奇异方向的含义见 [Muon](../../../docs/foundations/modules/optimization/muon.md) 第 3 节。
- **元学习的内外两层**：MAML（学习一个共享的初始参数，使模型在每个任务上经过少量梯度更新后表现好）的内层是一次普通梯度下降 θ′ᵢ = θ − α∇L_support,i(θ)；外层对适配后的查询集损失求导，梯度要穿过这一步内层更新回到共同起点 θ（迁移与元学习第 7–8 节）。
- **上下文学习与微调改变的东西不同**：上下文学习改变的是本次计算中的上下文与内部表示，微调改变的是参数（迁移与元学习第 10 节）；前者发生在注意力按内容读取提示中示例的过程里。

## 与其他分区和关系页的连接

- [优化分区](../optimization/README.md)：三篇都建立在一次梯度更新之上；分布式训练改变的是谁来算这次更新，LoRA 改变的是哪些参数参与更新。
- [目标分区](../objectives/README.md)：策略梯度、KL 惩罚与 DPO 都用到概率分类第 6–8 节的 NLL 与 KL。
- [架构分区](../architectures/README.md)：LoRA 加在 Transformer 的线性层上；张量并行拆的也是这些矩阵乘法。
- [数据分区](../data/README.md)：元学习的支持集与查询集必须分开，与训练集、测试集分开出于同一个理由（迁移与元学习第 7 节）。
- [关系页索引](../../relations/README.md)：现有两条关系链都以架构分区为主。

## 阅读顺序

先读完优化分区的[梯度与 SGD](../../../docs/foundations/modules/optimization/gradient-sgd.md)和目标分区的[概率分类](../../../docs/foundations/modules/objectives/02-classification-probabilities.md)，三篇按需要任选：

1. [分布式训练](../../../docs/foundations/05a-distributed-training.md)：模型或数据放不下、算得太慢时。
2. [强化学习](../../../docs/foundations/05b-reinforcement-learning.md)：只有行动后果或偏好反馈时。
3. [迁移与元学习](../../../docs/foundations/05c-transfer-meta-learning.md)：要把已有模型用到新任务时。

## 往哪里去

- 大批量训练、混合精度、本征维度与 LoRA、灾难性遗忘这些训练层面的研究：[训练科学](../../../cross-domain/fields/training-science/README.md)；规模化的跨领域论证：[深度学习的规模化](../../../perspectives/scaling.md)。
- PPO、RLHF（先用人类偏好训练奖励模型，再用强化学习按奖励微调语言模型）与偏好优化在语言模型上的用法：[强化学习后训练](../../../llm/fields/posttraining/rl/README.md)、[偏好优化](../../../llm/fields/posttraining/preferences/README.md)、[PPO 文献卡](../../../llm/papers/ppo/README.md)。
- 机器人上的模仿学习与强化学习：[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)；用学到的世界模型做强化学习：[世界模型](../../../multimodal/fields/world-models/README.md)、[DreamerV3 文献卡](../../../multimodal/papers/dreamerv3/README.md)。
- LoRA 在机器人模型上的实际用法：[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)、[OpenVLA 文献卡](../../../robotics-embodied/papers/openvla/README.md)。

## 批注

**易误读**

- LoRA 的秩 r 限制的是这一处权重更新能用的独立方向数，不是说整个模型的知识只有 r 个维度（迁移与元学习第 4 节）。
- 代理损失 −A·log π 的一步例子只针对一个参数和一条样本；多步问题还要处理折扣、状态访问分布和采样权重（强化学习第 5 节）。
