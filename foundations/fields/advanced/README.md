# 进阶连接

[回到基础模块](../../README.md) · [完整讲义目录](../../lessons/05-advanced-bridges.md) · [跨模块关系页](../../relations/README.md)

## 这一分区回答什么

基础训练是一台机器上的循环：读数据、算预测、给错误打分、改参数。有三种情况会改变这个循环。四条样本、一张卡一次只放得下两条，加一张卡各算两条之后，两张卡怎样合成同一次更新？机器人走完一段路才知道成没成功，没人告诉它每一步该把脚放在哪里，结果怎样变成梯度？一个学过电影影评的模型，换到餐厅评论时，怎样复用已经学到的东西？本分区的三篇导读分别回答这三个问题。

## 概念地图

| 模块 | 它解决的计算问题 | 先读 |
|---|---|---|
| [分布式训练](../../lessons/05a-distributed-training.md) | 多个设备合作完成同一次参数更新：数据并行先复制模型再合并梯度，张量并行把一层拆到多卡，流水线并行把层序列拆开并用微批次填满，状态分片与混合精度节省显存 | [梯度与 SGD](../../lessons/modules/optimization/gradient-sgd.md)第 6 节；[Adam 与 AdamW](../../lessons/modules/optimization/adam.md)第 2 节 |
| [强化学习](../../lessons/05b-reinforcement-learning.md) | 只知道行动后果、不知道每步正确答案时，把回报（一段未来奖励的累计）变成参数更新：价值与优势判断一个动作比平常好多少，策略梯度提高好动作的概率，PPO 限制每次更新的幅度，DPO 直接从偏好对训练 | [概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)第 6、8 节 |
| [迁移与元学习](../../lessons/05c-transfer-meta-learning.md) | 复用已学到的东西：冻结、全量微调，或用 LoRA 只训练一个低秩增量；元学习把"适应之后的效果"写进训练目标；上下文学习靠提示里的示例适应，不改权重 | 梯度与 SGD；[Attention 与 Transformer](../../lessons/14-attention-transformer.md) |

三篇互不依赖，分别接在优化、目标和架构分区之后。它们与基础模块的关系如下，`[结构]` 表示数学上是同一结构或特例：

- **数据并行就是更大批量的 SGD**：两张卡样本数相同时，全局梯度 g = (g₁ + g₂)/2 与单卡用全部样本算出的平均梯度相同，两卡用它更新后参数仍然一致 `[结构]`（分布式训练第 3 节）。样本数不同时要按样本数加权（第 4 节）；梯度累积是在时间上做同一件事（第 5 节）。
- **状态分片拆的是优化器状态**：P 个参数用 4 字节浮点保存时，参数、梯度和 Adam 的两份状态合计约 16P 字节，状态分片把它们分到不同设备（分布式训练第 8 节）。
- **策略梯度是加权的 NLL**：代理损失 −A·log π_θ(a|s) 在优势 A = 1 时，就是对采样动作做分类的负对数似然；A 给每条样本加权，正优势提高该动作的概率，负优势降低它 `[结构]`（强化学习第 5 节）。由此，行为克隆（直接模仿示范动作）是所有权重都为 1 的特例。
- **KL 把新策略拴在参考模型附近**：后训练中的 KL 惩罚限制策略偏离参考策略的程度；DPO 从带 KL 正则的奖励优化目标推出直接训练策略的损失（强化学习第 8–9 节）。KL 的定义与方向性见概率分类第 8 节。
- **LoRA 是低秩的权重增量**：冻结 W₀，把更新写成 W = W₀ + sBA，A 的形状为 [r, d_in]，B 为 [d_out, r]，所有输出修正都由 B 的 r 个列方向组合而成，增量的秩至多为 r `[结构]`（迁移与元学习第 4–5 节）。秩与奇异方向的含义见 [Muon](../../lessons/modules/optimization/muon.md) 第 3 节。
- **元学习的内外两层**：MAML（学习一个共享的初始参数，使模型在每个任务上经过少量梯度更新后表现好）的内层是一次普通梯度下降 θ′ᵢ = θ − α∇L_support,i(θ)；外层对适配后的查询集损失求导，梯度要穿过这一步内层更新回到共同起点 θ（迁移与元学习第 7–8 节）。
- **上下文学习与微调改变的东西不同**：上下文学习改变的是本次计算中的上下文与内部表示，微调改变的是参数（迁移与元学习第 10 节）；前者发生在注意力按内容读取提示中示例的过程里。

## 与其他概念的关系

概念地图写的是三篇导读与基础模块的对应。本节写它们之间、以及与领域里正在使用的机制之间的关系。类型标注与[关系页](../../relations/README.md)相同：`[结构]` 数学上是同一结构或特例，推导在括号里的章节；`[经验]` 由实验发现，括号里给原文出处；`[历史]` 有作者自述或引用链。涉及具体模型的，写明版本与日期；各家为什么这样选，留在领域页。

### 分布式训练

- `[结构]` 状态分片与矩阵级优化器相互牵制：Muon 的 Newton–Schulz 迭代要用完整的权重矩阵，状态分片却把参数切到不同设备上。[Moonlight](../../../llm/papers/arxiv-2502.16982/README.md)（2025-02）实现了 ZeRO-1 式的分布式 Muon（§2.3），[DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)（2026-04）为此设计了混合的 ZeRO 分桶策略（§3.4.1），[Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)（2026-07）让每个设备只用点对点通信取回自己负责的矩阵分片（§5.2.2）（Muon 见[优化分区](../optimization/README.md)）。
- `[结构]` 混合精度的难点在离群值：一个异常大的数会占满低精度格式的表示范围，其余数失去精度。[DeepSeek-V3](../../../llm/papers/arxiv-2412.19437/README.md) 的 FP8 训练给激活和权重分小块各自设缩放因子，就是在缩小"共用一个范围"的元素组（[分布式训练](../../lessons/05a-distributed-training.md)第 8 节；[预训练方向](../../../llm/fields/pretraining/README.md)"数值精度"一节）。
- `[结构]` 张量并行切开的是 Transformer 线性层的矩阵乘法（分布式训练第 6 节）。MoE 让另一种切法成为可能：FFN 只读本位置的向量，每个 token 可以被单独送到持有它所选专家的设备上计算，输出形状不变（[SSM、GNN 与 MoE](../../lessons/18-ssm-gnn-moe.md)第 4 节，[注意力与 FFN 的分工谱系](../../relations/attention-ffn-division.md)第 7 节）。

### 强化学习

- `[结构]` 策略梯度是加权的 NLL（概念地图），所以 on-policy 蒸馏可以直接借用强化学习的框架：把每个位置的 log(π_教师/π_学生) 当作优势，代入同一个代理损失。DeepSeek-V4 的报告写明这是常见做法，并指出它梯度方差大、常致训练不稳，自己改为在完整词表上计算反向 KL（V4 §5.1.2）。KL 的方向见[概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)第 8 节，前向与反向 KL 的区别见[目标分区](../objectives/README.md)"与其他概念的关系"。
- `[结构]` DAgger 与 on-policy 蒸馏是同一种安排：让学生自己走，在学生到达的状态（或生成的前缀）上向专家要标签，从而纠正行为克隆只在专家状态上训练的复合误差。机器人里，仿真中能看特权信息的 RL 教师经 DAgger 蒸馏成只用真机传感器的学生；语言模型里，学生采样、教师给每个 token 打分（[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)"模仿与强化的分工"，[监督微调](../../../llm/fields/posttraining/sft/README.md)主线第 6 个节点）。
- `[经验]` 价值模型的去留在两个领域走向不同：腿足 RL 在仿真里每步都有奖励，PPO 加价值函数是标准做法（[运动控制](../../../robotics-embodied/fields/control-locomotion/README.md)"技术地基"）；[DeepSeekMath](../../../llm/papers/arxiv-2402.03300/README.md) 的 GRPO 去掉价值模型，用同一题一组回答的奖励均值与标准差归一化得到优势，KL 直接加进损失（§4.1）；[DAPO](../../../llm/papers/arxiv-2503.14476/README.md) 在长思维链训练中去掉了 KL（§2.3）。同一套 GRPO 配方又被搬回 VLA：[SimpleVLA-RL](../../../robotics-embodied/papers/arxiv-2509.09674/README.md) 用 0/1 成功奖励训练动作模型（[强化学习后训练](../../../llm/fields/posttraining/rl/README.md)"与机器人强化学习的共性"）。
- `[结构]` 同一个优势 A 有两种用法：策略梯度把它乘在 log π 上，当作每条样本的权重；[π*0.6](../../../robotics-embodied/papers/arxiv-2511.14759/README.md) 把"A 是否超过按任务设定的阈值"二值化，以"Advantage: positive / negative"的文字放进输入，只用监督学习（离散 token 的似然与流匹配损失）训练，让同一个策略学会区分好坏动作（原文 §IV-B、§V-B；[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)"技术地基"的价值与优势一条；[强化学习](../../lessons/05b-reinforcement-learning.md)第 4 节）。

### 迁移、LoRA 与上下文学习

- `[经验]` LoRA 在机器人模型上的代价很小：[OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 在新机器人上微调时，秩 32 的 LoRA 只训练约 1.4% 的参数，成功率 68.2%，全参数微调 69.7%；显存从 163.3 GB 降到 59.7 GB（Kim 等 2024，§5.3 Table 1；Franka 桌面任务上各 33 次试验，标准误约 ±7 个百分点，两者的差距在误差之内）。
- `[历史]` LoRA 原文以本征维度的测量为依据，假设微调时的权重变化是低秩的（[训练科学](../../../cross-domain/fields/training-science/README.md)主线第 6 个节点）；本征维度是"训练实际用到多少自由度"的测量，LoRA 把它变成了一种参数化（[迁移与元学习](../../lessons/05c-transfer-meta-learning.md)第 4–6 节）。
- `[经验]` 上下文学习有一个可以定位的机制：两层注意力头组合成的 induction head，完成"[A][B] … [A] → [B]"的续写；在作者分析的小模型中，它的形成与上下文学习能力的跃升发生在同一训练窗口（[注意力与 FFN 的分工谱系](../../relations/attention-ffn-division.md)第 2 节）。这就是迁移与元学习第 10 节"改变的是本次计算中的表示，不是参数"的一个具体例子。
- `[经验]` 预训练与后训练的分阶段本身就是一次迁移，后一阶段改动权重，可能冲掉前一阶段的能力。InstructGPT 把预训练数据的梯度混进 PPO 更新（PPO-ptx），收回了公开基准上的大部分回退；on-policy 蒸馏用原模型当教师，可以找回中段训练后下降的指令遵循。RLHF 的 KL 惩罚，作者写明是为了缓解对奖励模型的过度优化，但它同样把策略拴在 SFT 模型附近（[训练科学](../../../cross-domain/fields/training-science/README.md)主线第 7 个节点，[监督微调](../../../llm/fields/posttraining/sft/README.md)主线第 6 个节点）。

## 与其他分区和关系页的连接

- [优化分区](../optimization/README.md)：三篇都建立在一次梯度更新之上；分布式训练改变的是谁来算这次更新，LoRA 改变的是哪些参数参与更新。
- [目标分区](../objectives/README.md)：策略梯度、KL 惩罚与 DPO 都用到概率分类第 6–8 节的 NLL 与 KL。
- [架构分区](../architectures/README.md)：LoRA 加在 Transformer 的线性层上；张量并行拆的也是这些矩阵乘法。
- [数据分区](../data/README.md)：元学习的支持集与查询集必须分开，与训练集、测试集分开出于同一个理由（迁移与元学习第 7 节）。
- [关系页索引](../../relations/README.md)：现有两条关系链都以架构分区为主。

## 阅读顺序

先读完优化分区的[梯度与 SGD](../../lessons/modules/optimization/gradient-sgd.md)和目标分区的[概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)，三篇按需要任选：

1. [分布式训练](../../lessons/05a-distributed-training.md)：模型或数据放不下、算得太慢时。
2. [强化学习](../../lessons/05b-reinforcement-learning.md)：只有行动后果或偏好反馈时。
3. [迁移与元学习](../../lessons/05c-transfer-meta-learning.md)：要把已有模型用到新任务时。

## 往哪里去

- 大批量训练、混合精度、本征维度与 LoRA、灾难性遗忘这些训练层面的研究：[训练科学](../../../cross-domain/fields/training-science/README.md)；规模化的跨领域论证：[深度学习的规模化](../../../perspectives/scaling.md)。
- PPO、RLHF（先用人类偏好训练奖励模型，再用强化学习按奖励微调语言模型）与偏好优化在语言模型上的用法：[强化学习后训练](../../../llm/fields/posttraining/rl/README.md)、[偏好优化](../../../llm/fields/posttraining/preferences/README.md)、[PPO 文献卡](../../../llm/papers/ppo/README.md)。
- 机器人上的模仿学习与强化学习：[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)；用学到的世界模型做强化学习：[世界模型](../../../multimodal/fields/world-models/README.md)、[DreamerV3 文献卡](../../../multimodal/papers/dreamerv3/README.md)。
- LoRA 在机器人模型上的实际用法：[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)、[OpenVLA 文献卡](../../../robotics-embodied/papers/openvla/README.md)。
- on-policy 蒸馏、用 RL 训练领域专家再合并：[监督微调](../../../llm/fields/posttraining/sft/README.md)、[强化学习后训练](../../../llm/fields/posttraining/rl/README.md)。
- 腿足 RL、特权教师与学生蒸馏：[运动控制](../../../robotics-embodied/fields/control-locomotion/README.md)。
- Muon 与状态分片、FP8/FP4 训练：[预训练方向](../../../llm/fields/pretraining/README.md)"优化器"与"数值精度"两节。

## 批注

**易误读**

- LoRA 的秩 r 限制的是这一处权重更新能用的独立方向数，不是说整个模型的知识只有 r 个维度（迁移与元学习第 4 节）。
- 代理损失 −A·log π 的一步例子只针对一个参数和一条样本；多步问题还要处理折扣、状态访问分布和采样权重（强化学习第 5 节）。
- OpenVLA 的 LoRA 对照只在 Franka 桌面任务的一组微调上做（§5.3），68.2% 与 69.7% 的差距小于各自约 7 个百分点的标准误。
- DAgger 与 on-policy 蒸馏的对应是结构上的：两者都在学生的状态分布上取专家标签；DAgger 原文的复合误差界针对逐步决策的模仿，不能直接当成语言模型上的定理。
- DeepSeek-V4 说逐 token 估计"梯度方差大、常致训练不稳"，是作者的自述，该节没有给出对照实验（V4 §5.1.2）。
- π*0.6 的"好动作"阈值按任务设定：预训练时取使约 30% 的示范数据为 positive 的阈值，微调时一般使每轮约 40% 的评测回合为 positive（原文附录）；它不是"优势大于 0"。

**与其他论文的关联**

- [SimpleVLA-RL](../../../robotics-embodied/papers/arxiv-2509.09674/README.md) 与 [DAPO](../../../llm/papers/arxiv-2503.14476/README.md)：GRPO 在语言模型上的修补被原样搬到 VLA。
- [π*0.6](../../../robotics-embodied/papers/arxiv-2511.14759/README.md) 与本分区的策略梯度：同一个优势，一个乘在损失上，一个作为条件放进输入。
- [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md) 与 [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)：状态分片与 Muon 冲突的两种工程解法。

**未核实 / 待验证**

- DeepSeek-V3 FP8 训练的分块缩放、SimpleVLA-RL 的配方、PPO 在腿足 RL 中的默认地位，取自对应方向页，本轮未重新打开原文。
