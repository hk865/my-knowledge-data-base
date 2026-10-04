# 数据与实验流程

[回到基础模块](../../README.md) · [完整讲义目录](../../lessons/04-data-and-datasets.md) · [跨模块关系页](../../relations/README.md)

## 这一分区回答什么

手机放在口袋里记录一段运动，希望模型判断你在走路还是跑步。动手之前要先说清：模型每次看多长的一段，要回答什么，答案来自哪里，测试时用的是不是训练中从没出现过的人。本分区把"一条样本"讲清楚，再讲多条样本怎样划分、对齐和处理，最后用图像与文本分类、IMU 位移两个练习把一条样本从读入走到评价。

## 概念地图

| 模块 | 它解决的计算问题 | 先读 |
|---|---|---|
| [样本接口与数据集选择](../../lessons/modules/data/01-data-contracts.md) | 把一道题写成四部分 (x, y, m, meta)：输入、目标、有效性掩码（哪些位置参与计算的 0/1 表）、来源信息；据此判断一个数据集能否支撑要做的任务 | 无 |
| [划分、同步与最小数据管道](../../lessons/modules/data/02-data-pipeline.md) | 把原始记录变成样本时保持输入、目标、来源的正确对应：先按来源分组再切窗口，按时间戳而不是行号对齐，坐标和单位统一，归一化参数只用训练集拟合 | 样本接口 |
| [图像与文本分类实践](../../lessons/modules/data/03-classification-labs.md) | 把一条样本走完训练闭环：编码器把输入变成特征，分类头给出类别分数，交叉熵计分，再用正确率、F1（精确率与召回率的调和平均）和错误样本检查结果 | 样本接口、管道；[CNN](../../lessons/11-cnn.md) 第 1–4 节；[概率分类](../../lessons/modules/objectives/02-classification-probabilities.md) |
| [IMU 窗口与位移标签](../../lessons/modules/data/04-imu-lab.md) | 把一段短时 IMU（惯性测量单元，测三轴加速度和三轴角速度）读数对应到一个位移标签：算准时间边界，指定坐标系，训练损失与米制误差分开报告 | 管道；[回归与鲁棒损失](../../lessons/modules/objectives/01-regression-robustness.md)、[机器人与 IMU 目标](../../lessons/modules/objectives/04-robotics-imu.md) |

依赖是一条主干加两个分支：样本接口 → 管道 → 图像与文本分类、IMU 位移两个练习，两个练习互不依赖。贯穿四篇的是同一个问题：模型在使用时到底能看到什么。下面几处机制在其他分区里以不同名字出现，`[结构]` 表示数学上是同一结构：

- **掩码**：一个 0/1 向量决定哪些位置参与求和或平均 `[结构]`。它在样本接口里是有效位置 m（样本接口第 2 节），在损失里是参与计分的位置（[回归与鲁棒损失](../../lessons/modules/objectives/01-regression-robustness.md)第 6 节），在文本实验里是 masked mean pooling 的 h = Σ(m_t e_t)/Σm_t（分类实践第 8 节），在 Transformer 里是 padding mask（[Attention 与 Transformer](../../lessons/14-attention-transformer.md)第 7.3 节）。
- **只用过去的信息**：实时管道在数据一侧禁止把未来读数放进输入（管道第 8 节）；因果 mask 在模型内部禁止读取后面的位置（Attention 与 Transformer 第 7.2 节）。两者施加的是同一个约束：t 时刻的输出只依赖 t 及之前的输入 `[结构]`。
- **测试必须真的是新的**：先分组再切窗（管道第 3 节）、归一化只用训练集拟合（管道第 6 节）、均值基线只用训练集标签（IMU 位移第 8 节），都是让测试集的信息不流进训练和模型选择。

## 与其他分区和关系页的连接

- [目标分区](../objectives/README.md)：机器人与 IMU 目标写下标签约定，IMU 位移练习把它落成一个实验；分类实践用的是概率分类里的交叉熵。
- [架构分区](../architectures/README.md)：图像实验用小型 CNN，文本实验用 embedding（每个词元 ID 对应一行可学习向量的查表）加平均池化；padding mask 与因果 mask 见上。
- [进阶分区](../advanced/README.md)：数据并行时各卡样本数不同，全局梯度要按样本数加权，属于"哪些样本、以什么权重参与一次更新"的同一类约定（[分布式训练](../../lessons/05a-distributed-training.md)第 4 节）。
- [关系页索引](../../relations/README.md)：现有两条关系链都以架构分区为主；本分区的掩码与因果约束写在上面的概念地图里。

## 阅读顺序

1. [样本接口与数据集选择](../../lessons/modules/data/01-data-contracts.md)
2. [划分、同步与最小数据管道](../../lessons/modules/data/02-data-pipeline.md)
3. [图像与文本分类实践](../../lessons/modules/data/03-classification-labs.md)，或 [IMU 窗口与位移标签](../../lessons/modules/data/04-imu-lab.md)，按自己的方向选一个先做。
4. 选数据集时查目录：[十五个代表数据集的选型说明](../../lessons/catalog/dataset-selection.md)，以及[机器可读 JSON](../../lessons/catalog/datasets.json) 与[可筛选 CSV](../../lessons/catalog/datasets.csv)。

## 往哪里去

- 数据泄漏、评测协议与指标口径：[评估与监督可靠性](../../../cross-domain/fields/evaluation/README.md)。
- IMU、时间同步与坐标系在机器人上的用法：[状态估计与建图](../../../robotics-embodied/fields/localization-mapping/README.md)、[感知与传感器](../../../robotics-embodied/fields/perception/README.md)。
- 大规模网络语料与人工标注数据怎样进入语言模型训练：[预训练](../../../llm/fields/pretraining/README.md)、[GPT-3 文献卡](../../../llm/papers/gpt3/README.md)、[InstructGPT 文献卡](../../../llm/papers/instructgpt/README.md)。
- 数据量与模型规模的配比：[训练科学](../../../cross-domain/fields/training-science/README.md)。

## 批注

**易误读**

- 同一个任务可能需要不止一种掩码：补齐位置不进入句子平均，缺少目标的位置不进入损失，两者用途不同（样本接口第 2 节）。
- MSE 的单位是平方米，位移的欧氏误差单位是米，两者不能直接比较（IMU 位移第 8 节）。
