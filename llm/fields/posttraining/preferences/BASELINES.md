# 偏好学习的基线

> 状态：Baseline 页 · v1 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md) · [后训练总览](../README.md)

## 基线是谁、为什么是它

结论：偏好学习有两个基线，优化的是同一个"奖励 − β·KL"目标。InstructGPT 用显式奖励模型加在线 PPO 求解，DPO 用闭式解把奖励模型和在线采样都消掉。后来的工作要么改偏好从哪来，要么改两条路线中的某一步。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| [InstructGPT](../../../papers/instructgpt/reading.md) 的 RLHF（2022，OpenAI） | 接口：同一提示下 K 个回答的人工排序 → 两两比较 → Bradley–Terry 奖励模型（6B，标量头）；策略用 PPO 最大化"奖励 − β·KL(策略‖SFT)"，PPO-ptx 再混入预训练梯度。评估：API 提示上的成对人评、TruthfulQA、毒性、公开 NLP 任务（对齐税） | 三段式 RLHF 的标准形态；Anthropic HH、Llama 2、Tulu 3 的 PPO 对照都按这个接口实现 |
| [DPO](../../../papers/dpo/reading.md)（2023，Stanford） | 接口：偏好对 (x, y_w, y_l) + 冻结的参考模型；损失是 −log σ(β·[被选回答与落选回答相对参考模型的对数概率比之差])；训练中不采样、不训练奖励模型。评估：IMDb 情感控制（奖励—KL 前沿）、TL;DR 摘要与 Anthropic HH 单轮对话的 GPT-4 胜率 | 它把偏好学习变成一次监督训练，开源社区和 Llama 3 都采用；IPO、SimPO、长度归一化 DPO 都在改它的损失 |

两者之前的参照是 [Christiano 等](../../../papers/arxiv-1706.03741/README.md)与 [Stiennon 等](../../../papers/arxiv-2009.01325/README.md)：偏好 → 奖励模型 → RL 的做法在 Atari、MuJoCo 与摘要上先跑通，InstructGPT 把它推广到通用指令。

## 基线的结构拆分

结论：一个偏好学习方案可以拆成五个可替换的部件；两个基线在"奖励形式"和"优化方式"上不同，其余部件可以共用。

| 部件 | 含义 | InstructGPT RLHF | DPO |
|---|---|---|---|
| 偏好来源 | 谁做比较 | 约 40 名标注员，对 4–9 个回答排序 | 原文用现成的人类偏好数据集（TL;DR、Anthropic HH）与 IMDb 上的合成奖励 |
| 数据与策略的关系 | 偏好对是否由当前策略生成 | 比较的回答由 SFT 与早期模型生成；PPO 在线采样 | 离线：偏好对在训练前就固定 |
| 奖励形式 | 怎样表示"好" | 显式标量奖励模型 | 隐式奖励 = β·log(策略/参考) |
| 优化方式 | 怎样把奖励变成策略更新 | 在线 PPO（含价值模型） | 偏好对上的分类损失 |
| 正则 | 怎样防止跑偏 | 奖励中的 KL 惩罚 + 预训练梯度（ptx） | 参考模型隐含在损失里，β 控制强度 |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 偏好来源 | 帮助性与无害性分开收集 | [Anthropic HH](../../../papers/arxiv-2204.05862/README.md)、[Llama 2](../../../papers/arxiv-2307.09288/README.md) | 两种目标都能顾到 / 两者此消彼长，需两个奖励模型或调配比；过度无害、错误拒答 |
| 偏好来源 | 书面原则 + AI 比较（RLAIF） | [Constitutional AI](../../../papers/arxiv-2212.08073/README.md) | 不需要人对有害输出打标 / 训练过头后过于严厉、塞入套话 |
| 偏好来源 | 强模型打分的 AI 偏好 | [Zephyr](../../../papers/arxiv-2310.16944/README.md) | 无人工标注，几小时训完 / 依赖 GPT-4；评委偏差 |
| 偏好来源 | 模型按 rubric 自我批评，评委由可验证信号校准 | [Kimi K2](../../../papers/arxiv-2507.20534/README.md) | 扩展到写作等主观任务 / 评委本身的偏差需持续校准 |
| 数据与策略的关系 | 每轮用最新模型重采偏好 | [Llama 2](../../../papers/arxiv-2307.09288/README.md)、[Llama 3](../../../papers/arxiv-2407.21783/README.md) | 奖励模型与 DPO 留在策略分布上 / 每轮都要新标注 |
| 数据与策略的关系 | 加入从自家 SFT 模型采样的 on-policy 偏好 | [Tulu 3](../../../papers/arxiv-2411.15124/README.md) | DPO 效果更好 / 需要额外采样与打分 |
| 奖励形式 | 奖励模型连同给分理由一起学 | [DeepSeek-V3](../../../papers/arxiv-2412.19437/README.md) | 降低奖励黑客 / 推理开销 |
| 奖励形式 | 逐题 rubric 的生成式奖励模型；策略自己兼任评委 | [DeepSeek-V3.2](../../../papers/arxiv-2512.02556/README.md)、[DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md) | 去掉标量奖励模型，少量人工标注 / 评委与策略一起变化，公开的失败分析少 |
| 偏好来源 | 被选回答来自强模型、落选回答来自弱模型（Delta Learning） | [Olmo 3](../../../papers/arxiv-2512.13961/README.md) | 同样数据上 DPO 带来 SFT 带不来的提升 / 偏好只反映模型强弱之差 |
| 奖励形式 | 先指出问题再打分的验证器 + 检查"问题是否真实"的元验证器；生成器自评一致也计奖励 | [DeepSeekMath-V2](../../../papers/arxiv-2511.22570/README.md) | 没有参考答案的证明也能给奖励 / 验证器会编造问题，需再加一层 |
| 优化方式 | 拒绝采样（best-of-K 后 SFT），可接 PPO | [Llama 2](../../../papers/arxiv-2307.09288/README.md) | 稳定、易实现 / 只从上一轮样本里挑会遗忘 |
| 优化方式 | 用 DPO 替代 PPO | [Llama 3](../../../papers/arxiv-2407.21783/README.md)、[Zephyr](../../../papers/arxiv-2310.16944/README.md)、[Tulu 3](../../../papers/arxiv-2411.15124/README.md) | 算力省、易调 / 分布外、过拟合、似然下降 |
| 优化方式 | 调好的 PPO（优势归一化、大批量、参考模型滑动更新） | [Xu 等](../../../papers/arxiv-2404.10719/README.md) | 对话与代码竞赛上超过 DPO / 实现与调参更难 |
| 损失形式 | 恒等映射代替 Bradley–Terry（IPO） | [IPO](../../../papers/arxiv-2310.12036/README.md) | 防止在确定性偏好上过拟合 / 原文以理论与小实验为主 |
| 损失形式 | 长度归一化、无参考模型、目标间隔（SimPO）；长度归一化 DPO | [SimPO](../../../papers/arxiv-2405.14734/README.md)、[Tulu 3](../../../papers/arxiv-2411.15124/README.md) | 抑制变长，省显存 / 间隔需手调；GSM8K 下降 |
| 正则 | DPO 加 NLL、屏蔽格式 token | [Llama 3](../../../papers/arxiv-2407.21783/README.md) | 防止被选回答似然下降、结尾重复 / 多两个超参 |
| 正则 | 长度相当的偏好对；偏好奖励只用于最后几百步 | [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md) | 减少长度偏差与奖励黑客 / 偏好信号用得少 |
| 评测与分析 | 过度优化的规模规律 | [Gao 等](../../../papers/arxiv-2210.10760/README.md) | 能预测"优化多少开始变坏" / 合成设定 |
| 评测与分析 | 长度与奖励的相关性 | [Singhal 等](../../../papers/arxiv-2310.03716/README.md) | 揭示改进主要来自变长 / — |

## 批注

**易误读**

- InstructGPT 的奖励模型只有 6B，策略是 175B；作者发现 175B 奖励模型训练可能不稳定、计算也更贵，才选了 6B（§3.5，精读第 5 节）。"奖励模型越大越好"的结论来自 HH 与 Gao 等，不是 InstructGPT。
- DPO 的"不需要奖励模型"指训练流程中没有独立的奖励模型；奖励以隐式形式存在，数据覆盖与 Bradley–Terry 假设的问题都还在（[DPO 精读](../../../papers/dpo/reading.md)第 12 节）。
- "离线"与"on-policy"是两个维度：Llama 3 的 DPO 是离线损失，但每轮的偏好数据来自上一轮最好的模型，因此大体在策略分布上。

**与其他论文的关联**

- [RL Baseline 页](../rl/BASELINES.md)：InstructGPT 的 PPO 部分在那里按 RL 部件拆分；GRPO 把"同一题多个回答的相对得分"当优势，原文认为这与奖励模型"在同一问题的回答之间比较"的训练方式相契合（DeepSeekMath §4.1）。
- [SFT Baseline 页](../sft/BASELINES.md)：拒绝采样在两张表中都出现。
- [DPO 精读](../../../papers/dpo/reading.md)与 [PPO 精读](../../../papers/ppo/reading.md)批注：两者优化同一个"奖励 − β·KL"目标，但只共享目标，不共享训练过程。

**未核实 / 待验证**

- 本页各格的数字均取自对应论文卡片与原文；Llama 2 两个奖励模型的分项准确率未引用。
