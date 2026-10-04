# 任务、损失与监督

[回到基础模块](../../README.md) · [完整讲义目录](../../lessons/03-tasks-losses.md) · [跨模块关系页](../../relations/README.md)

## 这一分区回答什么

同一张有猫的照片，可以问"有没有猫"、"猫在哪里"或"猫离相机几米"。三个问题要的答案不同，打分规则也不同：预测 3 米、实际 5 米，差了 2 米，这个差值要变成一个能汇总、能求导的分数，也就是损失。本分区回答三件事：怎样把预测和答案的差异变成损失，答案从哪里来（人工标注、数据本身或物理测量），以及训练误差相同时为什么还要约束参数。

## 概念地图

| 模块 | 它解决的计算问题 | 先读 |
|---|---|---|
| [回归与鲁棒损失](../../lessons/modules/objectives/01-regression-robustness.md) | 把带正负号的残差（预测减目标）变成可以汇总的分数；平方、绝对值和 Huber（小误差用平方、大误差改为线性增长）对大误差的惩罚不同；有效掩码决定哪些位置参与计分 | 无 |
| [概率分类](../../lessons/modules/objectives/02-classification-probabilities.md) | 把 logit（网络输出的原始分数）变成概率，用交叉熵或 BCE 衡量正确答案得到了多少概率；再把这些损失统一到负对数似然，并用 KL 比较两个分布 | 无 |
| [自监督与生成目标](../../lessons/modules/objectives/03-pretraining-objectives.md) | 没有人工答案时，从数据本身构造题目：自回归（预测下一个）、掩码（补全被遮住的）、对比（在候选中找配对）、去噪（去掉加进去的噪声） | 回归、概率分类 |
| [机器人与 IMU 目标](../../lessons/modules/objectives/04-robotics-imu.md) | 输出带物理意义时，先规定坐标、单位和旋转误差的算法，再算损失；判断传感器读数能否确定要预测的量 | 回归；概率分类第 7 节 |
| [参数正则化](../../lessons/modules/objectives/05-regularization.md) | 训练误差相同的解对输入扰动的敏感程度不同；用 L1、L2、权重衰减等约束参数，用 dropout、数据增强、早停限制拟合方式 | 回归；[Adam 与 AdamW](../../lessons/modules/optimization/adam.md)第 7 节 |

前两篇是地基，第三、四篇分别把它们用到"答案来自数据本身"和"答案带物理意义"两种情况上，第五篇讨论损失之外对参数的约束。五篇的损失大多可以统一到负对数似然（NLL：模型给真实答案的概率取负对数，ℓ = −ln p_θ(y|x)）上，`[结构]` 表示数学上是同一结构或特例：

- **NLL**（概率分类第 6 节）
  - 交叉熵是类别分布的 NLL，BCE 是伯努利分布（只有是与否两种结果）的 NLL `[结构]`（同上第 6 节）。
    - 下一词预测：每个位置做一次覆盖整个词表的分类，目标是错开一位的下一个词元 `[结构]`（自监督与生成目标第 2–3 节）。
    - 对比学习：在一批候选里找出配对，对相似度做 softmax（把一组分数变成非负、和为 1 的概率）后取正例的交叉熵 `[结构]`（同上第 7–9 节）。
  - MSE 是固定方差的高斯 NLL：概率分类第 7 节的高斯 NLL 为 ½[ln σ² + (y − μ)²/σ²]，取 σ² = 1 就剩 ½(y − μ)² `[结构]`。让网络同时输出 σ²，就得到会报告不确定性的回归，机器人与 IMU 目标第 8 节把它用在融合上。
    - 遮蔽图像重建：在被遮住的图像块上算像素的 MSE（回归与鲁棒损失第 9 节）。
    - 去噪：扩散模型回归加进去的噪声，同样是 MSE（自监督与生成目标第 10 节，[Diffusion](../../lessons/17-diffusion.md) 第 4 节）。
- **交叉熵与 KL**：CE(P, Q) = H(P) + KL(P‖Q)，目标分布 P 固定时，最小化交叉熵与最小化 KL 是同一件事 `[结构]`（概率分类第 8 节）。KL 还出现在 VAE 的变分下界（[VAE](../../lessons/16-vae.md) 第 4 节）、知识蒸馏的软标签，以及强化学习后训练中对偏离参考模型的惩罚（[强化学习](../../lessons/05b-reinforcement-learning.md)第 9 节）。
- **L2 惩罚与权重衰减**：对普通 SGD，损失里加 λ‖θ‖²/2 等价于每步把参数乘 (1 − ηλ)；换成 Adam 后不再等价，因此有 AdamW `[结构]`（参数正则化第 6–7 节）。

## 与其他概念的关系

概念地图写的是五篇讲义之间的统一关系。本节写本分区的损失与其他分区的概念、与领域里正在使用的训练目标之间的关系。类型标注与[关系页](../../relations/README.md)相同：`[结构]` 数学上是同一结构或特例，推导在括号里的章节；`[经验]` 由实验发现，括号里给原文出处；`[历史]` 有作者自述或引用链。涉及具体模型的，写明版本与日期；各家为什么这样选，留在领域页。

### 交叉熵与下一词预测

- `[经验]` 规模定律拟合的对象，就是留出集上每个 token 的交叉熵：它随参数量、数据量、算力按幂律下降（Kaplan 等 2020、Hoffmann 等 2022，见[训练科学](../../../cross-domain/fields/training-science/README.md)主线第 5 个节点）。交叉熵平滑下降，不等于下游能力同步提升，这一点要另外验证（同上"用什么衡量进展"）。
- `[结构]` 离散化之后，动作预测也是分类。OpenVLA 把每一维连续动作按训练数据的第 1 到第 99 百分位均分成 256 个桶，每个桶当作词表里的一个 token，用下一词预测的交叉熵训练（Kim 等 2024，§3.2；[OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)）。图像的自回归生成也一样：先用分词器把图压成离散编号，再按下一词预测训练（[视觉生成](../../../multimodal/fields/generation/README.md)"自回归"一段）。
- `[结构]` 掩码语言模型与下一词预测用同一个计分函数，只是条件不同：前者看两侧、补中间，后者只看左侧（[自监督与生成目标](../../lessons/modules/objectives/03-pretraining-objectives.md)第 5 节）。两者在语言模型上的路线分化与收敛，见[预训练方向](../../../llm/fields/pretraining/README.md)和 [Attention 与 Transformer](../../lessons/14-attention-transformer.md)第 13.5 节。

### 对比目标：softmax 与 sigmoid

- `[结构]` CLIP 对一批 N 对图文的 N×N 相似度矩阵逐行、逐列做 softmax 交叉熵；SigLIP 把每一格当作一个独立的"配不配"二分类，逐格算 BCE。这正是[概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)第 4–5 节"单标签用一组 softmax、多标签用逐个 sigmoid"的区别，搬到了"一批里谁和谁配对"上（[图文对齐](../../../multimodal/fields/alignment/README.md)"对比损失"与"sigmoid 损失"两段）。
- `[经验]` 这个结构差别有可测的后果：在冻结图像塔、只训练文本塔的设定下，批小于 16k 时 sigmoid 损失明显好于 softmax；批一路加到 100 万，两种损失都在 32k 左右饱和（[SigLIP](../../../multimodal/papers/arxiv-2303.15343/README.md)，Zhai 等 2023，§4.1）。逐格计分不必拼出整张矩阵，所以也更省内存。

### 平方误差：回归、去噪与流匹配

- `[结构]` 扩散模型回归加进去的噪声，流匹配回归把噪声推向数据的速度，两者的损失都是平方误差（[Diffusion](../../lessons/17-diffusion.md)第 4、6.1 节）。[π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md)（Physical Intelligence，2024-10）的动作专家用的就是条件流匹配损失 ‖v_θ − u‖²，一次生成一段动作块（Black 等 2024，§IV）；图像与视频生成的主流也是潜空间里的扩散或流匹配（[视觉生成](../../../multimodal/fields/generation/README.md)）。
- `[结构]` 同样是平方误差，直接回归动作与回归去噪目标的含义不同。直接回归等于固定方差的单峰高斯 NLL（[概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)第 7 节），最优解是条件均值；示范里同一个场景可以向左绕也可以向右绕时，均值是一条哪边都不走的路线。去噪与流匹配回归的是每个噪声强度下的局部量，多步积分后得到的是整个分布中的一个样本（[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)"多峰动作与扩散"，[Diffusion Policy 精读](../../../robotics-embodied/papers/diffusion-policy/reading.md)）。
- `[结构]` 遮蔽图像重建（[MAE](../../../multimodal/papers/mae/README.md)）在被遮住的图块上算像素 MSE（[回归与鲁棒损失](../../lessons/modules/objectives/01-regression-robustness.md)第 9 节）。`[经验]` 它与对比目标学到的特征，在线性评测与全量微调两种协议下排名会翻转（[视觉表征](../../../multimodal/fields/visual-representation/README.md)"从测量看"一节）。

### KL：把一个分布拴在另一个附近

- `[结构]` 用教师生成的文本做监督微调，最小化的是 E_{y~教师}[−log π_θ(y)] = H(教师) + KL(教师‖学生)，即前向 KL；on-policy 蒸馏让学生自己采样、在学生的轨迹上最小化 KL(学生‖教师)，即反向 KL（KL 的方向性见[概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)第 8 节）。两者的差别不只在 KL 的方向，还在训练数据来自谁：学生在自己会走到的前缀上被纠正，这与机器人里 DAgger 在策略自己到达的状态上向专家要标签是同一种安排（[监督微调](../../../llm/fields/posttraining/sft/README.md)"on-policy 蒸馏"，[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)）。
- `[经验]` [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)（2026-04）用十多个领域教师做 on-policy 蒸馏，目标是各教师反向 KL 的加权和；作者写明，常见做法把它简化成每个位置的 log 比值、当作强化学习的优势，梯度方差大、常致训练不稳，所以改为在完整词表上计算 KL（V4 §5.1.2）。
- `[经验]` 强化学习后训练里的 KL 是否保留已经分化：[InstructGPT](../../../llm/papers/instructgpt/reading.md) 把相对 SFT 模型的逐 token KL 从奖励里扣掉；[DeepSeekMath](../../../llm/papers/arxiv-2402.03300/README.md) 的 GRPO 把 KL 直接加进损失（§4.1）；[DAPO](../../../llm/papers/arxiv-2503.14476/README.md) 认为训练长思维链时模型本来就会远离初始模型，去掉了 KL（§2.3）（[强化学习后训练](../../../llm/fields/posttraining/rl/README.md)"技术地基"）。KL 在 VAE 的变分下界里起的是另一种作用：把编码器的后验拉向先验（[VAE](../../lessons/16-vae.md) 第 4 节）。

### 物理量的目标与正则

- `[经验]` 坐标与单位不统一，跨机器人数据就对不上：[Open X-Embodiment](../../../robotics-embodied/papers/arxiv-2310.08864/README.md) 的 RT-X 实验没有对齐各数据集末端执行器的坐标系，动作值可以是绝对或相对的位置或速度，作者写明同一个动作向量在不同机器人上会引起很不同的运动（OXE §IV-A）。这正是[机器人与 IMU 目标](../../lessons/modules/objectives/04-robotics-imu.md)第 5、7 节要求先写清坐标与单位的原因；后来的 VLA 怎样处理，见[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)主线第 2 个节点。
- `[结构]` 域随机化在仿真参数上做的事，与数据增强在输入上做的事相同：两者最小化的都是对一族扰动取期望的损失 E_ξ[L(θ; ξ)]，ξ 一个是摩擦、质量这类仿真参数，一个是裁剪、颜色这类输入变换，结果都是让解对这些扰动不敏感（[参数正则化](../../lessons/modules/objectives/05-regularization.md)第 9 节；[运动控制](../../../robotics-embodied/fields/control-locomotion/README.md)"sim-to-real 的差距从哪里来"）。
- `[经验]` 权重衰减在新优化器上仍然必要：Muon 不加衰减时权重 RMS 在长训练中持续增长（Moonlight §2.2，见[优化分区](../optimization/README.md)"与其他概念的关系"）。

## 与其他分区和关系页的连接

- [架构分区](../architectures/README.md)：自回归目标依赖因果 mask，同一个 Transformer 才能对所有位置并行算损失（[Attention 与 Transformer](../../lessons/14-attention-transformer.md)第 7、12 节）；"怎样生成"与"用什么网络计算"是两层选择（[Diffusion](../../lessons/17-diffusion.md)的"与其他概念的关系"）。
- [优化分区](../optimization/README.md)：损失给出的梯度由优化器变成更新；AdamW 的来由在两个分区各讲一半。
- [数据分区](../data/README.md)：回归与鲁棒损失第 6 节的有效掩码，就是样本接口里记录的有效位置；[IMU 窗口与位移标签](../../lessons/modules/data/04-imu-lab.md)把机器人与 IMU 目标里写好的标签约定落成一个完整实验。
- [进阶分区](../advanced/README.md)：策略梯度的代理损失 −A·log π(a|s) 在 A = 1 时就是对采样动作的 NLL，优势 A 只是给每条样本的 NLL 加权 `[结构]`（[强化学习](../../lessons/05b-reinforcement-learning.md)第 5 节）。
- [关系页索引](../../relations/README.md)：现有两条关系链都以架构分区为主；本分区的 NLL 统一写在上面的概念地图里。

## 阅读顺序

1. [回归与鲁棒损失](../../lessons/modules/objectives/01-regression-robustness.md)
2. [概率分类](../../lessons/modules/objectives/02-classification-probabilities.md)：第 6–8 节的 NLL、高斯 NLL 与 KL 是后面各篇的共同工具。
3. [自监督与生成目标](../../lessons/modules/objectives/03-pretraining-objectives.md)
4. [机器人与 IMU 目标](../../lessons/modules/objectives/04-robotics-imu.md)：只关心语言或图像时可以跳过。
5. [参数正则化](../../lessons/modules/objectives/05-regularization.md)：读过优化分区的 Adam 之后再读第 6–7 节。

## 往哪里去

- 下一词预测与遮蔽语言模型怎样成为语言模型的预训练目标：[预训练](../../../llm/fields/pretraining/README.md)、[GPT-3 文献卡](../../../llm/papers/gpt3/README.md)。
- 图文对比与遮蔽图像重建：[图文对齐](../../../multimodal/fields/alignment/README.md)、[视觉表征](../../../multimodal/fields/visual-representation/README.md)、[CLIP 文献卡](../../../multimodal/papers/clip/README.md)、[MAE 文献卡](../../../multimodal/papers/mae/README.md)。
- 去噪目标与生成：[视觉生成](../../../multimodal/fields/generation/README.md)；跨模态的论证见[语言、图像、视频的生成为何收敛到相近的配方](../../../perspectives/generative-convergence.md)。
- 偏好对与 KL 约束：[偏好优化](../../../llm/fields/posttraining/preferences/README.md)、[DPO 文献卡](../../../llm/papers/dpo/README.md)；软标签与 KL：[知识蒸馏](../../../cross-domain/fields/knowledge-distillation/README.md)。
- IMU、坐标与不确定性：[状态估计与建图](../../../robotics-embodied/fields/localization-mapping/README.md)。
- 训练损失与下游指标为什么要分开看：[评估与监督可靠性](../../../cross-domain/fields/evaluation/README.md)。
- 动作的两种损失（离散 token 的交叉熵与流匹配的平方误差）怎样在机器人模型里竞争：[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)、[OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)、[π0 文献卡](../../../robotics-embodied/papers/arxiv-2410.24164/README.md)。
- on-policy 蒸馏与反向 KL：[监督微调](../../../llm/fields/posttraining/sft/README.md)主线第 6 个节点；KL 在强化学习后训练里的去留：[强化学习后训练](../../../llm/fields/posttraining/rl/README.md)。

## 批注

**易误读**

- 连续变量的 NLL 用的是概率密度，可以为负，并随单位改变而变化，不能与分类交叉熵直接比大小（概率分类第 7 节）。
- 掩码语言模型与下一词预测用同一种计分函数（交叉熵），条件分布不同，训练的是不同的问题（自监督与生成目标第 5 节）。
- SigLIP 的"批小于 16k 时 sigmoid 明显更好"与"32k 左右饱和"都出自 SigLiT（图像塔冻结、只训练文本塔）的批量扫描（§4.1）；从头训练两座塔的 SigLIP 也在合适的批量处饱和，sigmoid 的峰值出现得更早、略高，批量过大对两种损失都有害（Figure 2）。
- "监督微调等于前向 KL"是对整条序列成立的：E_{y~教师}[−log π_θ(y)] 展开成逐 token 时，每个位置的条件都来自教师写出的前缀，学生自己会走到的前缀没有被训练到，这正是 on-policy 蒸馏要补的。
- Open X-Embodiment 不对齐坐标系，是 RT-X 实验在数据格式整合时的选择（§IV-A），不是各个数据集本身的错误。

**与其他论文的关联**

- [OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 与 [π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md)：同一个"预测下一段动作"的任务，前者用 256 桶的交叉熵，后者用流匹配的平方误差；FAST 用 DCT 压缩动作 token，是离散路线的修补（[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)主线第 5 个节点）。
- [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md) 的全词表反向 KL 与 [Thinking Machines 的 on-policy 蒸馏博客](../../../llm/papers/thinking-machines-on-policy-distillation/README.md)的逐 token 写法，是同一个目标的两种估计。
- [SigLIP](../../../multimodal/papers/arxiv-2303.15343/README.md) 与 [CLIP](../../../multimodal/papers/clip/README.md)：概率分类讲义第 4–5 节的 sigmoid 与 softmax 之分，在图文对齐里的实例。

**未核实 / 待验证**

- Kaplan 等 2020、Hoffmann 等 2022 的规模定律结论取自[训练科学](../../../cross-domain/fields/training-science/README.md)页，本轮未重新打开原文。
- DAPO 与 DeepSeekMath 只核对了 KL 相关的段落（DAPO §2.3、DeepSeekMath §4.1）；InstructGPT 的逐 token KL 取自 InstructGPT 精读。
