# 知识蒸馏：阅读与问题路线

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md)

五步，每步配一道检验题。答不出检验题，回到对应的论文再读。先读[概率分类讲义](../../../foundations/lessons/modules/objectives/02-classification-probabilities.md)第 8 节（软目标、交叉熵与 KL 的关系），本路线默认读者会算这三者。

## 第一步：软目标里有什么信息

读 [Hinton 等 2015](../../papers/arxiv-1503.02531/README.md) §2–3 与 §6，再翻 [Model Compression](../../papers/url-cornell-compression.kdd06/README.md) 与 [Ba & Caruana](../../papers/arxiv-1312.6184/README.md) 的方法一节。

**检验题**：教师对一张"2"的图片输出 logit (5, 2, 1)（类别 2、3、7）。分别算 T = 1 和 T = 5 时的软目标，说明"3 比 7 更像 2"这条信息在哪个温度下更容易被学生学到。再解释为什么软目标的梯度要乘 T²，以及 Hinton 等只用 3% 数据时软目标训练能到 57.0%、硬标签只有 44.5%（Table 5）说明了什么。

## 第二步：只传输出够不够

读 [FitNets](../../papers/arxiv-1412.6550/README.md) §2.2 与 §4.1，[MiniLM](../../../llm/papers/arxiv-2002.10957/README.md) §3，对照 [DistilBERT](../../../llm/papers/arxiv-1910.01108/README.md) 与 [TinyBERT](../../../llm/papers/arxiv-1909.10351/README.md) 的损失设计。

**检验题**：TinyBERT 逐层对齐需要一张"学生第 m 层对教师第 n 层"的映射表，MiniLM 只蒸最后一层。各写出一个学生层数、宽度都与教师不同的例子，说明两种做法各要额外引入什么（回归矩阵、映射规则、关系矩阵）。再用 TinyBERT Table 2 解释：为什么去掉数据增强时 CoLA 掉得最多。

## 第三步：生成模型的暴露偏差

读 [GKD](https://arxiv.org/abs/2306.13649) §1、§3 与 [MiniLLM](https://arxiv.org/abs/2306.08543) §2，再读 [Thinking Machines 博客](../../../llm/papers/thinking-machines-on-policy-distillation/README.md)。

**检验题**：教师对下一个 token 的分布是 (0.6, 0.4, 0)，学生只能放在一个 token 上。分别算学生选第一个、第二个 token 时的前向 KL 与反向 KL，说明为什么 MiniLLM 认为反向 KL 更适合生成。再画出离线蒸馏与 on-policy 蒸馏各自的数据流，标出"谁写前缀、谁给标签"。

## 第四步：蒸馏与 RL 的直接对照

读 [DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 附录 F、[Qwen3](../../../llm/papers/arxiv-2505.09388/README.md) §4.5 与 Table 21、[Gemma 3](../../../llm/papers/arxiv-2503.19786/README.md) §5.4。

**检验题**：Qwen3 Table 21 里 on-policy 蒸馏用 1,800 GPU 小时、RL 用 17,920 GPU 小时。写出这个比较没有计入的成本（提示：教师从哪里来），再结合 [Busbridge 等](https://arxiv.org/abs/2502.08606)的结论，说明在什么情况下直接训练学生比蒸馏更划算。最后解释 Gemma 3 的"训练短时小教师更好、训练长时大教师更好"。

## 第五步：多个专家合成一个模型

读 [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md) §5.1.2 与 §5.2.2、[Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md) §4.1.3、[Li 等](../../../llm/papers/arxiv-2604.13016/README.md)第 6 节；视觉一侧读 [C-RADIOv4](../../../multimodal/papers/arxiv-2601.17237/README.md) §2。

**检验题**：写出 V4 的全词表反向 KL 与 K3 的逐 token 截断奖励各自需要教师提供什么（整个分布，还是只要采样到的那个 token 的概率），各自的显存与方差代价是什么。再把 on-policy 蒸馏与三个机器人例子对齐成一张表：[R2R](../../../robotics-embodied/papers/r2r/reading.md) 的 student-forcing、[RMA](../../../robotics-embodied/papers/rma/reading.md) 第二阶段、[Lee 等 2020](../../../robotics-embodied/papers/arxiv-2010.11251/README.md) 的 DAgger。列出"谁执行、谁打标签、标签是什么、学生缺什么信息"四列，说明哪一列决定了蒸馏修不了的失败（例如 R2R 在没见过的建筑上只从 19.6% 提到 21.8%）。

## 往哪里去

- 蒸馏在 LLM 后训练流水线中的位置：[后训练总览](../../../llm/fields/posttraining/README.md)、[SFT 方向](../../../llm/fields/posttraining/sft/README.md)第 5–6 节。
- 蒸馏作为预训练目标：[预训练方向](../../../llm/fields/pretraining/README.md)。
- 多教师视觉蒸馏：[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。
- 特权教师与 DAgger：[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)。
- 早期文献的来源记录：[history.md](history.md)。
