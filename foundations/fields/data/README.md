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

## 与其他概念的关系

概念地图写的是四篇讲义共用的约定。本节写这些约定与其他分区的概念、与领域里正在使用的数据处理之间的关系。类型标注与[关系页](../../relations/README.md)相同：`[结构]` 数学上是同一结构或特例，推导在括号里的章节；`[经验]` 由实验发现，括号里给原文出处；`[历史]` 有作者自述或引用链。涉及具体模型的，写明版本与日期；数据集与评测的竞争留在领域页。

### 样本接口 (x, y, m, meta)

- `[结构]` 有效性掩码 m 在多机器人数据里有了新的用途：[π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md)（Physical Intelligence，2024-10）把所有机器人的状态与动作向量补零到数据集中最大的维度（18 维，能容纳两条 6 自由度机械臂、两个夹爪、移动底盘和升降躯干），相机少于三路时，把缺的图像位置用掩码遮掉（Black 等 2024，§V）。补零让形状一致，掩码说明哪些位置不该参与计算，与[样本接口](../../lessons/modules/data/01-data-contracts.md)第 2 节的 m、[回归与鲁棒损失](../../lessons/modules/objectives/01-regression-robustness.md)第 6 节的有效掩码是同一件事。
- `[经验]` meta 里的坐标约定缺失时，数据合在一起也对不上：[Open X-Embodiment](../../../robotics-embodied/papers/arxiv-2310.08864/README.md) 的 RT-X 实验没有对齐各数据集末端执行器的坐标系，作者写明同一个动作向量在不同机器人上会引起很不同的运动（OXE §IV-A）。后来各家 VLA 怎样统一动作空间，见[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)主线第 2 个节点。
- `[经验]` "数据集很大"有不同的含义（样本接口第 6 节），重复与改写把这一点量化了：[Kimi K2](../../../llm/papers/arxiv-2507.20534/README.md)（2025-07）把同一份 wiki 文本原样重复训练 10 遍，SimpleQA（简短事实问答）准确率 23.76%；改写 10 个版本、每个只训一遍，为 28.94%（K2 §2.2，Table 1）。训练的 token 数大致相同，独立的信息量不同（[预训练方向](../../../llm/fields/pretraining/README.md)"更多知识与更好泛化"一节）。

### 划分、同步与归一化

- `[结构]` 归一化参数只用训练集拟合（[数据管道](../../lessons/modules/data/02-data-pipeline.md)第 6 节），离散化的区间也一样：[OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 每一维动作的 256 个桶，区间取训练数据的第 1 到第 99 百分位，而不是最小值到最大值，少数离群动作就不会把桶撑宽（Kim 等 2024，§3.2）。这里的桶边界就是一组从训练集拟合出来的归一化参数。
- `[经验]` 测试必须真的是新的，在网页规模的语料上很难做到。[DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 在预训练与后训练数据中删掉与评测题或参考解有 10-gram 重合的文本，仅数学一项就删了约 600 万段；作者同时承认 n-gram 去重挡不住改写过的题，2024 年以前发布的 benchmark 可能仍有污染（R1 v2，2026-01，附录 D.1）。先分组再切窗（管道第 3 节）防的是同一来源跨过划分边界，污染是同一道题跨过了训练与评测的边界，检测与应对见[评估与监督可靠性](../../../cross-domain/fields/evaluation/README.md)"污染"一节。
- `[结构]` 时间戳对齐不只是预处理：视觉惯性里程计 [OpenVINS](../../../robotics-embodied/papers/openvins/README.md) 把相机与 IMU 之间的时间偏移当作状态的一部分在线估计（[状态估计与建图](../../../robotics-embodied/fields/localization-mapping/README.md)主线历史第 1 节）。管道第 4 节按时间戳插值，假设的是偏移已知；偏移未知时，它就成了要估计的量。
- `[结构]` 实时管道禁止把未来读数放进输入，与因果 mask 禁止读后面的位置是同一个约束（概念地图"只用过去的信息"）。机器人策略一次预测一段动作块时，块内的 k 步动作都只依据块开始时的观测，块内不再读新的输入，约束比逐步预测更紧（[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)"技术地基"的动作块一条）。

### 分类练习与它的放大版

- `[结构]` 文本实验里"embedding 查表 + 平均池化 + 线性分类头 + 交叉熵"（[分类实践](../../lessons/modules/data/03-classification-labs.md)第 8 节），把平均池化换成带因果 mask 的 Transformer、在每个位置都接一个覆盖整个词表的分类头，就是语言模型的下一词预测；分类实践第 10 节写了两者在目标上的区别。
- `[经验]` 数据本身成为研究对象：DataComp 固定训练代码、模型和算力，只允许改训练集，用来比较不同的数据过滤方法（[图文对齐](../../../multimodal/fields/alignment/README.md)主线第 6 个节点）。这与本分区"先固定划分和评价，再改一个变量"的实验习惯一致，只是被改的变量换成了数据。

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
- 跨机器人数据的接口问题（坐标、维度、相机数）与各家的处理：[视觉语言动作模型](../../../robotics-embodied/fields/vla/README.md)、[Open X-Embodiment 文献卡](../../../robotics-embodied/papers/arxiv-2310.08864/README.md)。
- 把数据当作研究对象（只改训练集的 benchmark、按元数据平衡）：[图文对齐](../../../multimodal/fields/alignment/README.md)。
- 重复与改写、合成数据能走多远：[预训练方向](../../../llm/fields/pretraining/README.md)"更多知识与更好泛化"一节。

## 批注

**易误读**

- 同一个任务可能需要不止一种掩码：补齐位置不进入句子平均，缺少目标的位置不进入损失，两者用途不同（样本接口第 2 节）。
- MSE 的单位是平方米，位移的欧氏误差单位是米，两者不能直接比较（IMU 位移第 8 节）。
- K2 的改写对照用的是 K2 的一个早期检查点（K2 §2.2），不是正式模型的成绩；作者正式训练时每份知识语料最多改写两次。
- DeepSeek-R1 的"约 600 万段"只是数学一项的去污染删除量（R1 附录 D.1）。
- π0 原文明确写了掩码的是缺失的相机图像槽位；补零的状态与动作维度在损失里怎样处理，§V 这一段没有说明。

**与其他论文的关联**

- [π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md) 的补零加掩码与 [Open X-Embodiment](../../../robotics-embodied/papers/arxiv-2310.08864/README.md) 的不对齐坐标，是跨机器人数据的两类接口问题：一类是形状，一类是含义。
- [OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)：用训练数据百分位定动作桶的手算，以及过滤全零首帧这类数据清洗。
- [DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 附录 D.1 与[评估与监督可靠性](../../../cross-domain/fields/evaluation/README.md)"污染"一节：模型方能做的 n-gram 去污染，以及它挡不住的改写题。

**未核实 / 待验证**

- OpenVINS 在线标定相机与 IMU 时间偏移、DataComp 的实验设计，取自对应方向页，本轮未重新打开原文。
