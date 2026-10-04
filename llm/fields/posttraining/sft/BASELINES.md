# SFT 的基线

> 状态：Baseline 页 · v1 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md) · [后训练总览](../README.md)

## 基线是谁、为什么是它

结论：SFT 有两个基线。InstructGPT 的 SFT 阶段定义了"人写示范 + 只在回答上算损失 + 作为 RLHF 第一步"的做法；DeepSeek-R1 的蒸馏定义了"强模型写长思维链、拒绝采样筛选、直接微调学生"的做法。2025 年以后的工作多以后者为起点。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| [InstructGPT](../../../papers/instructgpt/reading.md) 的 SFT 阶段（2022，OpenAI） | 接口：真实 API 提示 + 标注员写的示范，约 1.3 万条提示，只在回答 token 上算交叉熵。训练：16 个 epoch，按奖励模型分数而不是验证损失选模型。评估：同一提示下与其他模型回答的成对人评 | 它是 RLHF 三段式的第一段；Llama 2、LIMA、Tulu 3 都沿用"指令 + 示范 → 交叉熵"的接口，只换数据来源与规模 |
| [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md) 的蒸馏（2025，DeepSeek） | 接口：R1 生成的推理与非推理回答，经拒绝采样约 80 万条，直接微调 Qwen2.5 与 Llama 基座 2–3 个 epoch，不做 RL。评估：AIME、MATH-500、GPQA Diamond、LiveCodeBench、Codeforces | 同一个 32B 基座上，蒸馏明显好于直接做 1 万步以上 RL（附录 F.1）；s1、Qwen3、DeepSeek-V3 都在这个接口上改数据量、改筛选、改成 on-policy |

更早的参照是 [FLAN](../../../papers/arxiv-2109.01652/README.md)（2021）：示范来自公开 NLP 数据集的指令改写，目标是 zero-shot 泛化，而不是对话。InstructGPT 用 FLAN 数据微调同尺寸 GPT-3 作对照，结果在真实提示上输给自己的 SFT + RLHF。

## 基线的结构拆分

结论：一个 SFT 方案可以拆成五个可替换的部件；两个基线在"示范从哪来"和"在流水线中的位置"上差别最大。

| 部件 | 含义 | InstructGPT SFT | DeepSeek-R1 蒸馏 |
|---|---|---|---|
| 示范来源 | 谁写回答 | 约 40 名标注员 | DeepSeek-R1 与 DeepSeek-V3 |
| 数据规模与配比 | 多少条、哪些任务、是否含推理过程 | 约 1.3 万条提示，以生成、问答、头脑风暴为主 | 约 60 万推理 + 20 万非推理 |
| 筛选 | 怎样去掉坏样本、不该教的样本 | 标注员筛选与培训 | 拒绝采样：只保留答案正确的回答，去掉语言混杂、过长段落与代码块 |
| 损失与格式 | 在哪些 token 上算什么损失、用什么对话模板 | 回答 token 上的交叉熵 | 同左，加 `<think>` 推理块的格式 |
| 在流水线中的位置 | SFT 之前与之后接什么 | RLHF 的第一步，之后接奖励模型与 PPO | 学生只做 SFT；在 R1 自身的流水线中，SFT 既是冷启动又是两轮 RL 之间的一步 |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 示范来源 | 公开 NLP 数据集改写成指令 | [FLAN](../../../papers/arxiv-2109.01652/README.md)、[Flan-PaLM](../../../papers/arxiv-2210.11416/README.md) | zero-shot 泛化，Flan-PaLM 540B 平均 +9.4 个百分点 / 续写类任务无益；8B 及以下受损；分布不像真实用户请求 |
| 示范来源 | 模型自己生成指令与回答 | [Self-Instruct](../../../papers/arxiv-2212.10560/README.md)、[Zephyr](../../../papers/arxiv-2310.16944/README.md) 的蒸馏 SFT | 规模与多样性，GPT-3 在 SuperNI 上 +33 / 继承语言模型的偏见与长尾短板 |
| 示范来源 | 推理模型写长思维链 | [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md)、[DeepSeek-V3](../../../papers/arxiv-2412.19437/README.md)、[s1](../../../papers/arxiv-2501.19393/README.md) | 推理能力能直接搬给学生 / 过度思考、格式差、回答变长（V3 §5.1、§5.4.1）；s1 的推理过程来自闭源的 Gemini |
| 数据规模 | 少而精 | [LIMA](../../../papers/arxiv-2305.11206/README.md)、[Llama 2](../../../papers/arxiv-2307.09288/README.md)、s1 | 1,000 条、27,540 条即可 / 精选费人力；LIMA 不够稳健；上限是示范者 |
| 数据配比 | 加入思维链数据 | [Flan-PaLM](../../../papers/arxiv-2210.11416/README.md) | 9 个思维链数据集就能保住推理 / — |
| 筛选 | 奖励模型拒绝采样；结果与步骤奖励模型、MCTS 过滤推理数据 | [Llama 3](../../../papers/arxiv-2407.21783/README.md) | 合成数据的质量 / 流程长，依赖奖励模型 |
| 筛选 | 去掉基座不知道的事实，对答不对的问题写拒答 | [Gekhman 等](../../../papers/arxiv-2405.05904/README.md)、[Llama 3](../../../papers/arxiv-2407.21783/README.md) | 减少幻觉 / 只在闭卷问答上验证过 |
| 筛选 | 规则去掉重复、猜测、思考与总结不一致、语言混杂 | [Qwen3](../../../papers/arxiv-2505.09388/README.md) | 冷启动数据可读 / 要多一层模型判断与人工核对 |
| 训练过程 | 两阶段微调、去掉数学代码数据或接 DPO，以降低重复 | [DeepSeek LLM](../../../papers/arxiv-2401.02954/README.md) | 7B 重复率 2.0% → 1.4% / 数学代码能力的取舍 |
| 位置 | RL 之前的冷启动，刻意少样本、少步数 | [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md)、[Qwen3](../../../papers/arxiv-2505.09388/README.md)、[Kimi K3](../../../papers/arxiv-2607.24653/README.md) | 可读、给 RL 一个稳定的格式 / 太少会掉分：R1 Dev1 的 AIME 从 77.9% 降到 59.0% |
| 位置 | RL 之后再 SFT，融合两种模式 | [Qwen3](../../../papers/arxiv-2505.09388/README.md) | 一个模型兼具思考与非思考 / 思考模式的竞赛分数下降 |
| 损失 | on-policy 的 logit 级蒸馏 | [Qwen3](../../../papers/arxiv-2505.09388/README.md)、[DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md)、[Kimi K3](../../../papers/arxiv-2607.24653/README.md) | 8B 上约 1/10 的 GPU 小时超过 RL，pass@64 提高 / 学生上限是教师；需要同时在线运行多个教师 |
| 评测 | 开发集与未见集分离；严格去污染 | [Tulu 3](../../../papers/arxiv-2411.15124/README.md) | 防止对开发集过拟合 / 评测成本 |
| 对照 | SFT 与 RL 在同一初始化下比泛化 | [SFT Memorizes, RL Generalizes](../../../papers/arxiv-2501.17161/README.md) | 说明 SFT 记忆、RL 泛化，SFT 是 RL 的前提 / 只在规则游戏与导航上 |

## 批注

**易误读**

- InstructGPT 选 SFT 模型用的是奖励模型分数，验证损失在 1 个 epoch 后就已过拟合（§3.5）；"SFT 训多久"不能按预训练的习惯看验证损失决定。
- R1 蒸馏的学生只做 SFT、不做 RL，作者写明这是为了展示蒸馏本身的效果，把 RL 留给社区（附录 F）；"蒸馏好于 RL"的比较对象是同一 Qwen2.5-32B 上从头做的 RL，不是"蒸馏 + RL"。
- Qwen3 的 on-policy 蒸馏用的是教师的 logits，比"学生学教师写出的文本"多了逐 token 的分布信息（§4.5）；它与 R1 那种序列级蒸馏不是同一种损失。

**与其他论文的关联**

- [偏好学习 Baseline 页](../preferences/BASELINES.md)：拒绝采样（Llama 2、Llama 3）同时是 SFT 数据来源和偏好学习的一步，两张表都有它。
- [RL Baseline 页](../rl/BASELINES.md)：冷启动 SFT 是 RL 流水线的第一格；DeepSeek-V4、Kimi K3 用 on-policy 蒸馏代替了混合 RL。
- [模仿学习与机器人强化学习](../../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)：`[结构]` SFT 是行为克隆，on-policy 蒸馏是 DAgger 的形式。

**未核实 / 待验证**

- InstructGPT 的 SFT 数据中各任务类别的比例本轮未重新核对，表中"以生成、问答、头脑风暴为主"取自[精读](../../../papers/instructgpt/reading.md)对 API 提示分布的描述。
