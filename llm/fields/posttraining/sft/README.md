# 监督微调 SFT

> 状态：领域入门页 · v1 · 依据 [synthesis.csv](synthesis.csv)（14 篇）
>
> 速览：
> 1. SFT（监督微调，一句话：在"指令 + 示范回答"上做下一词预测，只在回答 token 上计算损失）主要教格式、角色与"调用哪一部分已有能力"，很少教新知识：LIMA 用 1,000 条、Llama 2 用 27,540 条高质量示范就够。
> 2. 示范从"人写"走到"模型写、再筛选"：FLAN 改写公开任务 → InstructGPT 的标注员示范 → Self-Instruct 让模型自己生成 → Llama 3 用奖励模型做拒绝采样 → DeepSeek-R1 的冷启动与 80 万条蒸馏数据 → Qwen3 的 on-policy 蒸馏。
> 3. 做不好的场景都有原文证据：示范里的新事实学得慢、学会后线性增加幻觉（Gekhman 等）；性能被示范者封顶（Llama 2、DeepSeek-R1）；数学 SFT 数据越多越容易无限重复（DeepSeek LLM）；不含思维链的指令数据损害推理（Flan-PaLM）；8B 及以下模型做指令微调反而伤泛化（FLAN）；规则换了就不会（SFT Memorizes, RL Generalizes）。
> 4. `[判断]` 2025 年以后 SFT 的角色变了：它不再是对齐的主体，而是 RL 之前的格式冷启动（样本数和步数都刻意少），以及把大模型、RL 专家的能力搬给学生的蒸馏通道。

本页是[后训练](../README.md)的 SFT 子方向。三个阶段的分工与"后训练很少加知识"的证据在总览页；本页讲 SFT 自身的数据、损失与历史。基线拆分见 [Baseline 页](BASELINES.md)，练习见[路线图](ROADMAP.md)，论文见[论文目录](PAPERS.md)。

## 这个领域在解决什么

结论：SFT 回答的问题是"拿什么示范、多少示范、怎样喂给模型，才能让基座按要求回答而不丢掉原有能力"。

一条 SFT 样本长这样：用户说"用一句话总结这则通知"，后面跟一段示范回答。训练时把两者拼成一个序列，做与预训练相同的下一词预测，但只在示范回答的 token 上计算交叉熵，用户部分的损失被屏蔽（loss masking）。训练完的模型看到同样格式的输入，就倾向于以助手身份作答。

做法大体分三类，区别在示范从哪来：

| 示范从哪来 | 直觉 | 代表 |
|---|---|---|
| 公开 NLP 数据集改写成指令 | 任务多了，模型学会"读指令" | FLAN、Flan-PaLM |
| 人写 | 少而精，风格可控 | InstructGPT、LIMA、Llama 2 |
| 模型写，再用奖励模型、验证器或人筛选 | 量大、可覆盖人写不出的长推理 | Self-Instruct、Llama 3、DeepSeek-R1、Qwen3 |

## 主线历史

结论：SFT 的历史是示范来源的历史；每一次换来源，都是因为上一种来源的规模、质量或分布不够。

### 1 多任务指令微调（2021–2022，Google）

留下的问题：GPT-3 靠提示里的几个示例（few-shot）才能做新任务，zero-shot 明显弱。

改变：[FLAN](../../../papers/arxiv-2109.01652/README.md) 把 60 多个 NLP 数据集改写成自然语言指令，对 137B 模型做多任务微调，zero-shot 在 25 个数据集中 20 个超过 175B 的 GPT-3。[Flan-PaLM](../../../papers/arxiv-2210.11416/README.md) 把任务扩到 1,836 个，540B 模型平均提高 9.4 个百分点。

做不好的场景：
- 任务本身就是续写句子时（常识推理、指代消解），指令帮不上忙，FLAN 在 7 个这类任务中只赢 3 个。
- 8B 及更小的模型做指令微调，没见过的任务反而变差，作者推测小模型的容量被训练任务占满（FLAN §4.2）。
- 不含思维链的指令数据会损害思维链推理，加入 9 个思维链数据集才扭转（Flan-PaLM）。

### 2 人写示范进入 RLHF 流水线（2022，OpenAI）

留下的问题：公开 NLP 任务以分类、问答为主，真实用户却大量提出开放生成、头脑风暴类请求。

改变：[InstructGPT](../../../papers/instructgpt/reading.md) 让标注员为约 1.3 万条 API 与标注员编写的提示写示范，SFT 之后再接奖励模型与 PPO。用 FLAN、T0 数据微调的同尺寸 GPT-3 在真实提示上的胜率低于 InstructGPT，说明示范的分布要贴近使用场景。

做不好的场景：
- 训练 1 个 epoch 后验证损失就开始过拟合，继续训练到 16 个 epoch，奖励模型分数与人评却仍在上升；作者按奖励模型分数选模型（InstructGPT §3.5）。验证损失与"回答好不好"在 SFT 里就已经分开走（[精读](../../../papers/instructgpt/reading.md)第 4.3 节）。
- SFT 单独使用时，人评胜率低于接上奖励模型与 PPO 之后的模型。

### 3 少而精，或让模型自己写（2022–2023）

留下的问题：人写示范贵，规模上不去。

改变：两条相反的路。
- **让模型写**：[Self-Instruct](../../../papers/arxiv-2212.10560/README.md) 从 175 个种子任务出发，让 GPT-3 自己生成约 5.2 万条指令再微调自己，在 Super-NaturalInstructions 上提高 33 个百分点，与 InstructGPT001 相当。
- **少而精**：[LIMA](../../../papers/arxiv-2305.11206/README.md) 只用 1,000 条精选示范；[Llama 2](../../../papers/arxiv-2307.09288/README.md) 放弃数百万条第三方数据、只用 27,540 条供应商标注，效果明显变好，并发现不同供应商的数据会让下游表现差别很大。

做不好的场景：
- Self-Instruct 继承语言模型的局限，长尾任务上收益可能很小，并可能强化已有偏见（§8）。
- LIMA 不如产品级模型稳健，一次不走运的采样或对抗性提示就会给出弱回答（§7）。
- 示范者是上限：Llama 2 写明 SFT 会学到标注员写作的差异，包括写得差的那部分，性能上限是最好的标注员；作者把模型写作超过标注员归功于 RLHF（§5.1）。

### 4 知识边界：什么不该放进 SFT（2024）

留下的问题：SFT 数据由人或更强的模型写成，里面不可避免地含有基座不知道的事实。

改变：[Gekhman 等](../../../papers/arxiv-2405.05904/README.md)在闭卷问答上做对照：基座不知道的事实（Unknown）比已知事实拟合得慢得多；一旦被拟合，模型在原有知识上的幻觉线性增加；最佳开发集表现出现在拟合了大部分已知样本、只拟合了少数未知样本时。[Llama 3](../../../papers/arxiv-2407.21783/README.md) 引用它，把事实性数据的原则写成"让模型知道自己知道什么，而不是添加知识"：从预训练数据中出题，对模型反复答错的问题生成拒答示范。同一份报告里，推理类 SFT 数据用奖励模型、步骤级奖励模型甚至 MCTS 过滤，只保留中间步骤正确的解答。

做不好的场景：
- [DeepSeek LLM](../../../papers/arxiv-2401.02954/README.md) 发现数学 SFT 数据越多，回答越容易陷入无限重复；作者认为数学数据里相似的推理模式，较弱的模型学不会，就退化成重复。两阶段微调（第二阶段去掉数学与代码数据）或 DPO 能把重复率降下来，7B 模型从 2.0% 降到 1.4%。
- Gekhman 等的结论来自闭卷问答，长文本生成中怎样识别"新知识"还没有办法（§11）。

### 5 长思维链：冷启动与蒸馏（2025）

留下的问题：推理能力靠 SFT 示范来教，示范者是天花板；靠 RL 来练，又需要模型先会按格式写出可读的推理。

改变：
- [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md) 先证明不经 SFT、直接 RL 也能学会长推理（R1-Zero），但输出难读、中英混杂；于是用数千条冷启动数据先做一次 SFT，再 RL；RL 之后用拒绝采样收集约 60 万条推理与 20 万条非推理数据，再做 SFT。这 80 万条数据直接蒸馏给 Qwen2.5 与 Llama 小模型，效果比在 32B 基座上直接做 1 万步以上 RL 更好。
- [Qwen3](../../../papers/arxiv-2505.09388/README.md) 的冷启动刻意少用样本、少训步数，"只种下推理模式，不追求立即的推理成绩"，为 RL 留出空间。
- [s1](../../../papers/arxiv-2501.19393/README.md) 只用 1,000 条带推理过程的题（推理过程取自 Gemini Flash Thinking）微调 32B 模型，加上推理时强制续写"Wait"，在竞赛数学上超过 o1-preview。
- [DeepSeek-V3](../../../papers/arxiv-2412.19437/README.md) 用领域专家模型生成 R1 风格的推理数据，经拒绝采样后放进 150 万条 SFT 数据。

做不好的场景：
- R1 生成的推理数据准确率高，但有过度思考、格式差、过长的问题，V3 才要先训练专家、再拒绝采样（V3 §5.1）；蒸馏让分数提高，同时明显增加平均回答长度（V3 §5.4.1）。
- 冷启动数据太少会掉推理分：R1 Dev1（冷启动后）的 AIME 从 R1-Zero 的 77.9% 降到 59.0%，下一轮 RL 才恢复（R1 Table 3）。
- s1 的强制续写有上限：抑制结束符太多次，模型会陷入重复循环（s1 §4.2）。

### 6 on-policy 蒸馏取代一部分 RL（2025–2026）

留下的问题：离线蒸馏的学生只见过教师写出的前缀，自己写偏之后没人教。

改变：[Qwen3](../../../papers/arxiv-2505.09388/README.md) 对小模型先做离线蒸馏，再让学生自己采样、逐 token 对齐教师的 logits（on-policy 蒸馏）；在 8B 上它比直接 RL 效果更好，GPU 小时约为 1/10，并提高了 pass@64。[DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md) 与 [Kimi K3](../../../papers/arxiv-2607.24653/README.md) 都用多教师 on-policy 蒸馏把多个 RL 专家合成一个模型。

做不好的场景：教师的上限就是学生的上限；V4 与 K3 对蒸馏目标（全词表 logit 还是逐 token 估计）的选择相反，见 [RL 方向](../rl/README.md)。

`[判断]` 第 5、6 两个节点合起来看，SFT 在 2025 年以后分成了两个角色：给 RL 打格式底子的冷启动（越少越好），以及把能力从强模型搬到弱模型的蒸馏（越像 on-policy 越好）。[SFT Memorizes, RL Generalizes](../../../papers/arxiv-2501.17161/README.md) 在规则游戏与导航上给出对应的对照：SFT 倾向记忆、换规则就不会，RL 能泛化，但没有 SFT 稳定输出格式，RL 根本训不起来。

## 技术地基

- **下一词预测与损失掩码**：SFT 与预训练用同一个交叉熵，区别是只在回答 token 上计算。[自监督与生成目标](../../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 2–3 节。
- **样本打包与隔离**：多个短样本拼进一个序列以提高效率，再用掩码让它们互相不可见（DeepSeek-V3 §5.1 的 sample masking）。因果掩码见 [Transformer 讲义](../../../../foundations/lessons/14-attention-transformer.md)第 7 节。
- **对话模板与特殊 token**：角色标记、思考块（Qwen3 的 /think、/no_think 与空思考块）决定模型怎样切换行为；Llama 3 发现这些格式 token 若参与 DPO 损失，会引起结尾重复或突然终止。
- **过拟合与早停**：InstructGPT 的验证损失 1 个 epoch 后就过拟合，却仍按奖励模型分数继续训练；Gekhman 等建议早停，以少拟合未知事实。正则与早停见[正则化讲义](../../../../foundations/lessons/modules/objectives/05-regularization.md)。
- **蒸馏**：序列级蒸馏（学生学教师写出的回答）与 logit 级蒸馏（学生对齐教师的逐 token 分布）。[知识蒸馏方向](../../../../cross-domain/fields/knowledge-distillation/README.md)。
- **行为克隆**：`[结构]` SFT 就是语言上的行为克隆，复合误差与"最多和示范者一样好"两个坑都继承过来，见[模仿学习与机器人强化学习](../../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)。

## 主要路线与团队偏好

| 团队 | `[判断]` 押注 | 代表 | 代价 |
|---|---|---|---|
| Google | 用大量公开任务做多任务指令微调 | FLAN、Flan-PaLM | 公开任务的分布与真实用户请求不同；小模型受损 |
| OpenAI | 人写示范，SFT 只是 RLHF 的第一步 | InstructGPT | 标注贵；SFT 单独使用不如接上 RL |
| Meta | 少而精的人工数据，之后转向模型生成 + 拒绝采样 | LIMA、Llama 2、Llama 3 | 人工数据难扩展；生成数据要靠奖励模型、验证器层层过滤 |
| DeepSeek | 用自家推理模型生成数据，再蒸馏给下一代与小模型 | DeepSeek LLM、V3、R1、V3.2 | 推理数据过长、过度思考，要先训专家再筛 |
| Qwen | 冷启动少而精；小模型靠强到弱蒸馏 | Qwen3 | 学生上限受教师限制 |
| AI2、UW、Stanford 等学术团队 | 公开数据与配方，研究"多少数据够用" | Self-Instruct、Tulu 3、s1 | 依赖闭源模型写的数据（s1 的推理过程来自 Gemini） |

`[判断]` 收敛的方向是"模型写、规则或奖励模型筛"：Meta 从 Llama 2 的人工标注走到 Llama 3 的拒绝采样与合成数据，DeepSeek 从 V3 起用自家推理模型写推理数据，Qwen3 的冷启动数据由 QwQ-32B 生成、经多重过滤，QwQ-32B 一直答错的题由人工核对。人工数据留在两处：冷启动的少量高质量样本，以及难以自动判断的安全与事实性数据。

## 用什么衡量进展

- **指令遵循**：IFEval（可被程序检查的格式约束），以及 Qwen3 的 ThinkFollow 这类检查模式切换的内部评测。
- **对话质量**：MT-Bench、AlpacaEval、Arena-Hard，以及成对人评。口径问题见[总览页](../README.md)"用什么衡量进展"。
- **能力保持**：对话模型 zero-shot 与基座 few-shot 对比（DeepSeek LLM：对话模型 0-shot 的 MMLU 与基座 5-shot 相当）；选择题与生成式问答分开看。
- **退化信号**：重复率（DeepSeek LLM 用 3,868 条提示统计不终止、无限重复的比例）；幻觉率；平均回答长度（V3 的蒸馏消融）。
- **泛化**：留出未见评测、换规则测试（Tulu 3 的未见集，SFT Memorizes 的规则变体）。

## 当前开放问题

- **SFT 数据里的新知识怎样识别和处理？** Gekhman 等的方法只在闭卷问答上验证；Llama 3 用知识探针生成拒答。长文本与推理数据中怎样做，仍未解决。入口：[Gekhman 等](../../../papers/arxiv-2405.05904/README.md)、[Llama 3](../../../papers/arxiv-2407.21783/README.md)。
- **冷启动该多少？** R1 的冷启动少到会掉 AIME，Qwen3 主张刻意少，SFT Memorizes 说明完全不做 RL 训不起来。入口：[DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md)、[Qwen3](../../../papers/arxiv-2505.09388/README.md)、[SFT Memorizes, RL Generalizes](../../../papers/arxiv-2501.17161/README.md)。
- **蒸馏能把学生带到哪里？** 蒸馏比 RL 省，也能扩大 pass@k，但学生的上限是教师；超越教师是否只能靠 RL 与更强基座（R1 附录 F.1 的说法）。入口：[Yue 等](../../../papers/arxiv-2504.13837/README.md)、[s1](../../../papers/arxiv-2501.19393/README.md)。

## 阅读顺序

1. [InstructGPT 精读](../../../papers/instructgpt/reading.md)第 3–4 节：SFT 样本怎样构造、损失怎样计算，以及验证损失与人评为什么分开走。
2. [FLAN](../../../papers/arxiv-2109.01652/README.md) → [LIMA](../../../papers/arxiv-2305.11206/README.md)：多任务与少而精两种出发点。
3. [Gekhman 等](../../../papers/arxiv-2405.05904/README.md)：SFT 不该教什么。
4. [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md)第 3 节与附录 F → [Qwen3](../../../papers/arxiv-2505.09388/README.md)第 4.1、4.5 节：SFT 变成冷启动与蒸馏。
5. [SFT Memorizes, RL Generalizes](../../../papers/arxiv-2501.17161/README.md)：SFT 与 RL 的分工在受控实验里是什么样。

## 批注

**易误读**

- LIMA 的 43% 是"持平或更好"的合计，对象是 GPT-4 的回答，评测是人对帮助性的偏好（摘要）；它不测知识、推理与安全。
- Llama 2 的 27,540 条是 SFT 标注的总数，作者说"数万条"量级就够；它没有给出数量与效果的曲线（§3.1）。
- R1 的 80 万条是 RL 之后拒绝采样得到的 SFT 数据（约 60 万推理 + 20 万非推理），与最初的数千条冷启动数据是两回事（附录 B.3.3）。
- FLAN"8B 及以下受损"是在其 40 个训练任务、按任务簇留出的设定下（§4.2）；Flan-PaLM 用 1,836 个任务时，各尺寸模型都有提升。

**判断的支撑论文**

- SFT 角色的转变：R1 §3 与附录 F.1、Qwen3 §4.1 与 §4.5、V4 §5.1.2、K3 §4.1.1 与 §4.1.3、SFT Memorizes §5.4 与 §6。边界：Llama 3 仍以 SFT（加拒绝采样）为主体，DeepSeek-V3 的 SFT 数据有 150 万条。
- "模型写、再筛"的收敛：Llama 2 §3.1 与 Llama 3 §4.1.3、§4.3；V3 §5.1；Qwen3 §4.1。反例：LIMA 与 Llama 2 都报告人工少量数据更好，s1 也只用 1,000 条，只是它们的"人工"多已变成"人工挑选模型写的东西"。

**与其他论文的关联**

- [偏好学习方向](../preferences/README.md)：Llama 2、Llama 3 的拒绝采样同时是 SFT 数据来源与偏好学习的一步；DeepSeek LLM 用 DPO 降低 SFT 带来的重复。
- [强化学习方向](../rl/README.md)：冷启动 SFT 与 RL 的接口；Qwen3 把 RL 之后的模型再做一次 SFT（思考模式融合）。
- [推理时计算方向](../../inference/README.md)：s1 的强制续写是推理时控制思考长度的做法，与 Qwen3 的思考预算同源。
- [模仿学习与机器人强化学习](../../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)：行为克隆的复合误差与 DAgger，对应 SFT 的示范者上限与 on-policy 蒸馏。

**未核实 / 待验证**

- Alpaca、Vicuna 等 2023 年社区 SFT 数据集本轮没有打开原文（Alpaca 只有博客与仓库），正文只写了 Self-Instruct。
