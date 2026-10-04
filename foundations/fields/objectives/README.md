# 任务、损失与监督

[回到基础模块](../../README.md) · [完整讲义目录](../../../docs/foundations/03-tasks-losses.md) · [跨模块关系页](../../relations/README.md)

## 这一分区回答什么

同一张有猫的照片，可以问"有没有猫"、"猫在哪里"或"猫离相机几米"。三个问题要的答案不同，打分规则也不同：预测 3 米、实际 5 米，差了 2 米，这个差值要变成一个能汇总、能求导的分数，也就是损失。本分区回答三件事：怎样把预测和答案的差异变成损失，答案从哪里来（人工标注、数据本身或物理测量），以及训练误差相同时为什么还要约束参数。

## 概念地图

| 模块 | 它解决的计算问题 | 先读 |
|---|---|---|
| [回归与鲁棒损失](../../../docs/foundations/modules/objectives/01-regression-robustness.md) | 把带正负号的残差（预测减目标）变成可以汇总的分数；平方、绝对值和 Huber（小误差用平方、大误差改为线性增长）对大误差的惩罚不同；有效掩码决定哪些位置参与计分 | 无 |
| [概率分类](../../../docs/foundations/modules/objectives/02-classification-probabilities.md) | 把 logit（网络输出的原始分数）变成概率，用交叉熵或 BCE 衡量正确答案得到了多少概率；再把这些损失统一到负对数似然，并用 KL 比较两个分布 | 无 |
| [自监督与生成目标](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md) | 没有人工答案时，从数据本身构造题目：自回归（预测下一个）、掩码（补全被遮住的）、对比（在候选中找配对）、去噪（去掉加进去的噪声） | 回归、概率分类 |
| [机器人与 IMU 目标](../../../docs/foundations/modules/objectives/04-robotics-imu.md) | 输出带物理意义时，先规定坐标、单位和旋转误差的算法，再算损失；判断传感器读数能否确定要预测的量 | 回归；概率分类第 7 节 |
| [参数正则化](../../../docs/foundations/modules/objectives/05-regularization.md) | 训练误差相同的解对输入扰动的敏感程度不同；用 L1、L2、权重衰减等约束参数，用 dropout、数据增强、早停限制拟合方式 | 回归；[Adam 与 AdamW](../../../docs/foundations/modules/optimization/adam.md)第 7 节 |

前两篇是地基，第三、四篇分别把它们用到"答案来自数据本身"和"答案带物理意义"两种情况上，第五篇讨论损失之外对参数的约束。五篇的损失大多可以统一到负对数似然（NLL：模型给真实答案的概率取负对数，ℓ = −ln p_θ(y|x)）上，`[结构]` 表示数学上是同一结构或特例：

- **NLL**（概率分类第 6 节）
  - 交叉熵是类别分布的 NLL，BCE 是伯努利分布（只有是与否两种结果）的 NLL `[结构]`（同上第 6 节）。
    - 下一词预测：每个位置做一次覆盖整个词表的分类，目标是错开一位的下一个词元 `[结构]`（自监督与生成目标第 2–3 节）。
    - 对比学习：在一批候选里找出配对，对相似度做 softmax（把一组分数变成非负、和为 1 的概率）后取正例的交叉熵 `[结构]`（同上第 7–9 节）。
  - MSE 是固定方差的高斯 NLL：概率分类第 7 节的高斯 NLL 为 ½[ln σ² + (y − μ)²/σ²]，取 σ² = 1 就剩 ½(y − μ)² `[结构]`。让网络同时输出 σ²，就得到会报告不确定性的回归，机器人与 IMU 目标第 8 节把它用在融合上。
    - 遮蔽图像重建：在被遮住的图像块上算像素的 MSE（回归与鲁棒损失第 9 节）。
    - 去噪：扩散模型回归加进去的噪声，同样是 MSE（自监督与生成目标第 10 节，[Diffusion](../../../docs/foundations/17-diffusion.md) 第 4 节）。
- **交叉熵与 KL**：CE(P, Q) = H(P) + KL(P‖Q)，目标分布 P 固定时，最小化交叉熵与最小化 KL 是同一件事 `[结构]`（概率分类第 8 节）。KL 还出现在 VAE 的变分下界（[VAE](../../../docs/foundations/16-vae.md) 第 4 节）、知识蒸馏的软标签，以及强化学习后训练中对偏离参考模型的惩罚（[强化学习](../../../docs/foundations/05b-reinforcement-learning.md)第 9 节）。
- **L2 惩罚与权重衰减**：对普通 SGD，损失里加 λ‖θ‖²/2 等价于每步把参数乘 (1 − ηλ)；换成 Adam 后不再等价，因此有 AdamW `[结构]`（参数正则化第 6–7 节）。

## 与其他分区和关系页的连接

- [架构分区](../architectures/README.md)：自回归目标依赖因果 mask，同一个 Transformer 才能对所有位置并行算损失（[Attention 与 Transformer](../../../docs/foundations/14-attention-transformer.md)第 7、12 节）；"怎样生成"与"用什么网络计算"是两层选择（[Diffusion](../../../docs/foundations/17-diffusion.md)的"与其他概念的关系"）。
- [优化分区](../optimization/README.md)：损失给出的梯度由优化器变成更新；AdamW 的来由在两个分区各讲一半。
- [数据分区](../data/README.md)：回归与鲁棒损失第 6 节的有效掩码，就是样本接口里记录的有效位置；[IMU 窗口与位移标签](../../../docs/foundations/modules/data/04-imu-lab.md)把机器人与 IMU 目标里写好的标签约定落成一个完整实验。
- [进阶分区](../advanced/README.md)：策略梯度的代理损失 −A·log π(a|s) 在 A = 1 时就是对采样动作的 NLL，优势 A 只是给每条样本的 NLL 加权 `[结构]`（[强化学习](../../../docs/foundations/05b-reinforcement-learning.md)第 5 节）。
- [关系页索引](../../relations/README.md)：现有两条关系链都以架构分区为主；本分区的 NLL 统一写在上面的概念地图里。

## 阅读顺序

1. [回归与鲁棒损失](../../../docs/foundations/modules/objectives/01-regression-robustness.md)
2. [概率分类](../../../docs/foundations/modules/objectives/02-classification-probabilities.md)：第 6–8 节的 NLL、高斯 NLL 与 KL 是后面各篇的共同工具。
3. [自监督与生成目标](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)
4. [机器人与 IMU 目标](../../../docs/foundations/modules/objectives/04-robotics-imu.md)：只关心语言或图像时可以跳过。
5. [参数正则化](../../../docs/foundations/modules/objectives/05-regularization.md)：读过优化分区的 Adam 之后再读第 6–7 节。

## 往哪里去

- 下一词预测与遮蔽语言模型怎样成为语言模型的预训练目标：[预训练](../../../llm/fields/pretraining/README.md)、[GPT-3 文献卡](../../../llm/papers/gpt3/README.md)。
- 图文对比与遮蔽图像重建：[图文对齐](../../../multimodal/fields/alignment/README.md)、[视觉表征](../../../multimodal/fields/visual-representation/README.md)、[CLIP 文献卡](../../../multimodal/papers/clip/README.md)、[MAE 文献卡](../../../multimodal/papers/mae/README.md)。
- 去噪目标与生成：[视觉生成](../../../multimodal/fields/generation/README.md)；跨模态的论证见[语言、图像、视频的生成为何收敛到相近的配方](../../../perspectives/generative-convergence.md)。
- 偏好对与 KL 约束：[偏好优化](../../../llm/fields/posttraining/preferences/README.md)、[DPO 文献卡](../../../llm/papers/dpo/README.md)；软标签与 KL：[知识蒸馏](../../../cross-domain/fields/knowledge-distillation/README.md)。
- IMU、坐标与不确定性：[状态估计与建图](../../../robotics-embodied/fields/localization-mapping/README.md)。
- 训练损失与下游指标为什么要分开看：[评估与监督可靠性](../../../cross-domain/fields/evaluation/README.md)。

## 批注

**易误读**

- 连续变量的 NLL 用的是概率密度，可以为负，并随单位改变而变化，不能与分类交叉熵直接比大小（概率分类第 7 节）。
- 掩码语言模型与下一词预测用同一种计分函数（交叉熵），条件分布不同，训练的是不同的问题（自监督与生成目标第 5 节）。
