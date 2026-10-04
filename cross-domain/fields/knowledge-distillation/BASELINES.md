# 知识蒸馏的基线

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md) · [综合表](synthesis.csv)

## 基线是谁、为什么是它

结论：有两个基线。经典基线是 Hinton 等 2015 的"温度软目标 + 硬标签"，它定义了"教师传什么、怎样算损失"；LLM 时代的基线是"学生自己生成、教师逐 token 打分"的 on-policy 蒸馏（GKD 与 MiniLLM 提出，Qwen3 用于生产），它定义了"在谁写出的数据上传"。后来的工作都在替换这两个基线的部件。

- **[Distilling the Knowledge in a Neural Network](../../papers/arxiv-1503.02531/README.md)（Hinton、Vinyals、Dean，Google，2015）**。接口：教师与学生在同一批迁移数据上各自输出 logit，都除以温度 T 后做 softmax，学生的损失 = 与教师软分布的交叉熵 × T² + 与硬标签的交叉熵（较小权重）。它统一了前作：[Ba & Caruana](../../papers/arxiv-1312.6184/README.md)（2014）的 logit 回归是 T → ∞ 的极限（原文 §2.1）；[Model Compression](../../papers/url-cornell-compression.kdd06/README.md)（2006）用教师的硬标签训练学生，相当于 T → 0 的另一端（`[判断]`，原文 §2.1 只写了高温极限）。评估方式：学生对教师（或集成）保留多少提升，对同结构从头训练强多少。
- **on-policy 蒸馏**：[GKD](https://arxiv.org/abs/2306.13649)（Google DeepMind，ICLR 2024）与 [MiniLLM](https://arxiv.org/abs/2306.08543)（清华、Microsoft Research，ICLR 2024）同年提出，[Qwen3](../../../llm/papers/arxiv-2505.09388/README.md)（2025）在 6 个小模型上用作后训练主干。接口：给定提示，学生采样整段回答；教师在学生写出的每个前缀上给出下一个 token 的分布；学生最小化两者的散度（通常是反向 KL）。它针对的是离线蒸馏的暴露偏差：学生训练时只见过教师写好的前缀。评估方式：与同起点的 RL、离线蒸馏比较分数与 GPU 小时（Qwen3 Table 21）。

## 基线的结构拆分

把一次蒸馏拆成五个可替换的部件：

1. **教师**：一个模型、一个集成，还是多个领域专家；比学生大，还是同尺寸。
2. **传什么**：硬标签、整段输出（序列级）、逐 token 分布（logit 级）、中间层特征或关系。
3. **数据由谁写出**：伪数据、原训练集、教师生成（离线），还是学生自己生成（on-policy）。
4. **损失**：交叉熵 / 前向 KL、反向 KL、JSD、L2；逐 token 估计还是全词表；多个教师怎样加权或路由。
5. **放在训练的哪一段**：任务微调、预训练、后训练的最后一段，还是部署前单独一步。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 数据由谁写出 | 合成伪数据（MUNGE） | [Model Compression](../../papers/url-cornell-compression.kdd06/README.md)（2006） | 没有无标签数据也能压缩；伪数据造不对时失效（ADULT） |
| 传什么 | 回归教师 logit | [Ba & Caruana](../../papers/arxiv-1312.6184/README.md)（2014） | 浅网络接近深网络；迁移集不够时差距拉大 |
| 传什么 | 中间层提示 | [FitNets](../../papers/arxiv-1412.6550/README.md)（2015） | 学生可以比教师更深更窄、参数少 10 倍仍更准；提示层选深了会过度正则 |
| 传什么 + 放在哪一段 | 预训练阶段蒸馏，软目标 + 隐状态余弦 | [DistilBERT](../../../llm/papers/arxiv-1910.01108/README.md)（2019） | 一个通用小模型可再微调；RTE、CoLA 掉分多 |
| 传什么 + 放在哪一段 | 逐层对齐注意力与隐状态，预训练与微调两段都蒸，任务数据增强 | [TinyBERT](../../../llm/papers/arxiv-1909.10351/README.md)（2019） | 4 层学生快 9.4 倍；强依赖数据增强 |
| 传什么 | 只蒸最后一层的注意力分布与 value 关系；助教模型 | [MiniLM](../../../llm/papers/arxiv-2002.10957/README.md)（2020） | 学生层数、宽度自由；师生差距大时需要中间模型 |
| 数据由谁写出 + 损失 | 学生自己采样，反向 KL | [MiniLLM](https://arxiv.org/abs/2306.08543)（2023） | 暴露偏差更低、长回答更好；需要多种稳定技巧 |
| 数据由谁写出 + 损失 | 学生自己采样，散度可换 | [GKD](https://arxiv.org/abs/2306.13649)（2023） | 更接近监督训练、更稳；可与 RL 微调合用 |
| 放在哪一段 | logit 蒸馏作为小模型的预训练目标；按教师概率采 256 个 logit | [Gemma 2](../../../llm/papers/arxiv-2408.00118/README.md)、[Gemma 3](../../../llm/papers/arxiv-2503.19786/README.md)（2024–2025） | 2B 学生三项平均 60.3 → 67.7；需要一直运行教师；大小教师的优劣随训练长度反转 |
| 传什么 + 教师 | 序列级：学教师的长推理轨迹 | [DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md)（2025）、[CodePLAN](../../../llm/papers/arxiv-2403.13271/README.md)（2024） | 比小模型自己做 RL 更好更省；上限是教师，只做 SFT |
| 数据由谁写出 | 离线蒸馏打底，再 on-policy | [Qwen3](../../../llm/papers/arxiv-2505.09388/README.md)（2025）、[Thinking Machines](../../../llm/papers/thinking-machines-on-policy-distillation/README.md)（2025） | 约十分之一的 GPU 小时超过 RL，且提高 pass@64；只在数学、代码上对照 |
| 教师 + 放在哪一段 | 多个领域专家当教师，后训练最后一段合并 | [MiMo-V2-Flash](https://arxiv.org/abs/2601.02780)、[GLM-5](../../../llm/papers/arxiv-2602.15763/README.md)、[Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)（2026） | 避开多领域 RL 的跷跷板和顺序 RL 的遗忘；逐 token 估计的方差 |
| 损失 | 多教师全词表反向 KL，取代混合 RL | [DeepSeek-V4](../../../llm/papers/arxiv-2606.19348/README.md)（2026） | 梯度更稳；要卸载教师权重、缓存隐状态、按教师排序样本 |
| 教师 + 传什么 | 多个视觉基础模型的摘要向量与逐块特征 | [AM-RADIO](../../../multimodal/papers/arxiv-2312.06709/README.md)（2023）→ [C-RADIOv4](../../../multimodal/papers/arxiv-2601.17237/README.md)、[RADIO1D](../../../multimodal/papers/arxiv-2607.03624/README.md)（2026） | 一个编码器兼有 CLIP、DINO、SAM 的长处；学生会学到教师的伪影，要随机平移、按离散度平衡教师 |
| 教师 | 仿真里能看特权信息的策略，DAgger 采样 | [Lee 等 2020](../../../robotics-embodied/papers/arxiv-2010.11251/README.md)、[RMA](../../../robotics-embodied/papers/rma/reading.md) | 学生只用真机传感器；学生看不到的信息传不过去 |

## 批注

**易误读**

- "教师越大越好"不是稳定的规律：MiniLM 要靠助教模型，Gemma 3 的结论随训练长度反转，Busbridge 等（[arXiv 2502.08606](https://arxiv.org/abs/2502.08606)）把它写成蒸馏规模定律中的容量差距。
- 表中"约十分之一的 GPU 小时"来自 Qwen3 Table 21，只比较了从同一检查点出发的后续训练，没有计入训练教师的成本。

**与其他论文的关联**

- on-policy 蒸馏与机器人里的 DAgger 是同一个结构，见[入门页](README.md)"不同模态的差异"与[后训练总览](../../../llm/fields/posttraining/README.md)"与机器人强化学习的共性"。
- 多教师视觉蒸馏在[视觉表征方向的 Baseline 页](../../../multimodal/fields/visual-representation/BASELINES.md)"训练信号 = 多教师蒸馏"一行有更细的拆分。
- LLM 后训练中蒸馏与 SFT、RL 的分工见 [SFT 方向](../../../llm/fields/posttraining/sft/README.md)第 6 节。

**未核实 / 待验证**

- GKD 与 MiniLLM 本轮只读了摘要、引言与主要实验段，没有逐项核对各数据集上的分数。
