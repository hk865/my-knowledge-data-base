# 偏好学习与奖励模型

> 状态：领域入门页 · v1 · 依据 [synthesis.csv](synthesis.csv)（17 篇）
>
> 速览：
> 1. 偏好学习用"同一提示下两个回答哪个更好"的比较作训练信号，学的是取舍：帮助性、无害性、风格与长度。有两种实现：先训练奖励模型再用 RL 优化（RLHF，InstructGPT、Llama 2），或直接在偏好对上训练策略（DPO，Llama 3、Zephyr、Tulu 3）。
> 2. 每种实现都有记录在案的坑：奖励模型被优化过头后与人的偏好负相关（Stiennon 等），这一效应随奖励模型规模平滑变化（Gao 等）；奖励的提高主要来自回答变长（Singhal 等）；帮助性与无害性此消彼长（Anthropic HH、Llama 2）；DPO 可能偏向分布外回答（Xu 等），在近乎确定的偏好上过拟合（IPO），并会拉低被选回答本身的似然（Llama 3、SimPO）。
> 3. 偏好的来源从人走到模型：InstructGPT 约 40 名标注员 → Constitutional AI 用书面原则加 AI 比较 → Zephyr 用 GPT-4 打分 → DeepSeek-V3 让模型按原则投票自评 → Kimi K2 的自我批评 rubric → DeepSeek-V4 让策略模型自己充当生成式奖励模型。
> 4. `[判断]` 2025 年以后，偏好学习退到"不可验证的任务"这一块：数学与代码改用规则验证器，偏好或 rubric 奖励只用于写作、对话、安全，而且训练步数被刻意限制（DeepSeek-R1 只在最后 400 步加偏好奖励，因为再多就出现奖励黑客）。

本页是[后训练](../README.md)的偏好学习子方向。三个阶段的分工在总览页；RL 算法本身（PPO、GRPO）在[强化学习方向](../rl/README.md)。两篇精读：[InstructGPT](../../../papers/instructgpt/reading.md)（奖励模型 + PPO）与 [DPO](../../../papers/dpo/reading.md)（直接偏好优化）。基线拆分见 [Baseline 页](BASELINES.md)，练习见[路线图](ROADMAP.md)，论文见[论文目录](PAPERS.md)。

## 这个领域在解决什么

结论：很多回答没有标准答案，却能比较好坏；偏好学习把"人更喜欢哪一个"变成可以优化的目标，同时防止模型去讨好打分器而不是讨好人。

例子：用户问"周一能去博物馆吗"，通知写着周一闭馆。回答 A："不能，周一闭馆，建议周二去。"回答 B 写了三段，礼貌周全，最后才说闭馆。多数人会选 A，但很难写一条规则说明"为什么 A 更好"。偏好学习收集许多这样的比较，然后有两条路：

| 路线 | 做法 | 直觉 | 代表 |
|---|---|---|---|
| 奖励模型 + RL（RLHF） | 用比较训练一个给回答打分的奖励模型（Bradley–Terry 模型：两者得分之差经 sigmoid 给出"前者更好"的概率），再用 PPO 让策略提高得分，同时用 KL 惩罚拉住它别离参考模型太远 | 先学评委，再按评委练 | InstructGPT、Anthropic HH、Llama 2 |
| 直接偏好优化（DPO） | 由"奖励 − KL"目标的闭式最优解推出一个只用偏好对的分类损失，直接提高被选回答相对落选回答的概率（相对参考模型） | 不要评委，直接在比较上学 | DPO、Zephyr、Llama 3、Tulu 3 |
| 拒绝采样（介于两者之间） | 每个提示采多个回答，用奖励模型选最好的拿来做 SFT | 用评委挑示范 | Llama 2、Llama 3 |

## 主线历史

结论：偏好学习的问题链是"评委不可靠 → 让评委跟上策略、给评委加约束 → 去掉评委 → 评委换成会推理的模型"。

### 1 从比较中学奖励（2017–2020，OpenAI 与 DeepMind）

留下的问题：很多任务写不出奖励函数。

改变：[Christiano 等](../../../papers/arxiv-1706.03741/README.md)让人比较两段轨迹，训练奖励预测器，再用 RL 优化它，反馈只需覆盖不到 1% 的交互。[Stiennon 等](../../../papers/arxiv-2009.01325/README.md)把它用到摘要：人比较 → 奖励模型 → PPO（奖励中减去相对监督模型的 KL），结果超过人写的参考摘要；优化奖励模型也比优化 ROUGE 更符合人的判断。

做不好的场景：
- 奖励预测器离线训练、不随策略更新时，Pong 上的智能体只躲丢分不得分（Christiano §3.3）。
- 轻度优化时人评变好，继续优化后奖励模型最终与人的偏好负相关（Stiennon 图 5）。
- 贵：6.7B 模型的 RL 约 320 GPU 天，标注数千小时。

### 2 RLHF 三段式与"有帮助、无害"（2022）

留下的问题：单一任务的偏好太窄；助手既要有帮助又不能有害。

改变：
- [InstructGPT](../../../papers/instructgpt/reading.md) 在真实 API 提示上做 SFT → 奖励模型 → PPO，1.3B 模型在人评中胜过 175B GPT-3；把预训练数据混进 RL（PPO-ptx）以减轻对齐税。
- [Anthropic HH](../../../papers/arxiv-2204.05862/README.md) 分别收集帮助性与无害性的比较，每周用最新模型在线迭代；发现 RL 奖励与"策略相对初始模型 KL 的平方根"大致线性。
- [Gao 等](../../../papers/arxiv-2210.10760/README.md)用"黄金奖励模型"代替人，测出过度优化的规律：黄金分数先升后降，系数随奖励模型参数量平滑变化。
- [Constitutional AI](../../../papers/arxiv-2212.08073/README.md) 只给一组书面原则，让模型自我批评改写、自己比较回答，训练偏好模型后做 RL（RLAIF：用 AI 的偏好代替人的偏好）。

做不好的场景：
- 对齐税：InstructGPT 的 PPO 让 SQuADv2 掉 17.8 个 F1 点；HH 的小模型 RLHF 后多数评测下降。
- 过度无害：HH 早期策略对一切稍敏感的问题都建议"寻求专业帮助"，作者归因于对无害性过度优化（§4.4）；RL-CAI 训练过头会回答得过于严厉、塞入套话。
- 偏好模型分数越高越不可靠，大偏好模型更稳健（HH §4.2）。
- KL 惩罚不是万能的约束：Gao 等的设定中，KL 惩罚提高了给定 KL 下的代理分数，却没有改善黄金分数与 KL 的前沿（作者提醒可能对超参数敏感）。InstructGPT 把 KL 系数加大 100 倍也没能修复 DROP 与 SQuADv2 的下降（[精读](../../../papers/instructgpt/reading.md)第 11.1 节）。
- "人"的范围：InstructGPT 的偏好来自约 40 名、以英语为主的标注员，多数比较只有一人标注（§5.3）。

### 3 开放模型上的 RLHF（2023，Meta）

留下的问题：InstructGPT 不公开模型与数据；开放模型能否做到同样的帮助性与安全性。

改变：[Llama 2](../../../papers/arxiv-2307.09288/README.md) 分别训练帮助性与安全性两个奖励模型（两者此消彼长，一个模型难以兼顾）；前几轮 RLHF 只用拒绝采样，V4 起在拒绝采样后接 PPO；每周按批收集新偏好数据，因为奖励模型在新的输出分布上准确率会很快下降。作者认为奖励模型准确率是最终效果最重要的代理指标之一，而且随标注量增加尚未饱和。

做不好的场景：
- 只从上一轮样本中挑答案的 RLHF V3 在写押韵诗上退化，作者归为遗忘（§3.2.3）。
- 安全数据加多以后，对看起来敏感、其实无害的提示过度拒绝（§4.2）。

### 4 去掉奖励模型：直接偏好优化（2023–2024）

留下的问题：RLHF 要同时维护策略、参考、奖励、价值四个模型，并在训练中在线采样，复杂且不稳定。

改变：
- [DPO](../../../papers/dpo/reading.md)（Stanford）从"奖励 − β·KL"目标的闭式解出发，把奖励写成策略与参考模型的对数概率比，得到只用偏好对的分类损失；训练中不需要采样，在情感控制、摘要、单轮对话上与 PPO 相当或更好（最大到 6B）。
- 社区很快形成 SFT + DPO 的开源配方：[Zephyr](../../../papers/arxiv-2310.16944/README.md) 用 GPT-4 打分的 AI 偏好做 DPO；[Tulu 3](../../../papers/arxiv-2411.15124/README.md) 用长度归一化的 DPO，并加入从自家 SFT 模型采样的 on-policy 偏好数据，效果更好。
- [Llama 3](../../../papers/arxiv-2407.21783/README.md) 放弃 PPO，改为六轮"奖励模型 → 拒绝采样 → SFT → DPO"：试过 PPO，DPO 在大模型上更省算力、IFEval 更好。
- 后续变体在改损失形式：[IPO](../../../papers/arxiv-2310.12036/README.md)（DeepMind）把 Bradley–Terry 换成恒等映射以防过拟合；[SimPO](../../../papers/arxiv-2405.14734/README.md) 用按长度归一化的平均对数概率作隐式奖励、去掉参考模型。

做不好的场景：
- **分布外**：[Xu 等](../../../papers/arxiv-2404.10719/README.md)证明 PPO 能找到的解 DPO 也能找到，DPO 还可能偏向偏好数据之外的回答（定理 4.1）；DPO 的效果明显受模型输出与偏好数据分布差异的影响。他们调好的 PPO（优势归一化、大批量、参考模型的滑动平均更新）在对话与代码竞赛上全面超过 DPO。
- **过拟合**：IPO 指出偏好确定或近似确定时（有限数据下常见），DPO 的最优解把落选回答的概率压到 0，KL 正则形同虚设；Zephyr 的 DPO 一个 epoch 后训练准确率即达 100%，SFT 训练超过一个 epoch 时 DPO 越训越差。
- **长度**：[Singhal 等](../../../papers/arxiv-2310.03716/README.md)发现 RLHF 的奖励提高主要来自回答变长，只用长度作奖励就能复现大部分提升，根源是奖励模型被偏好数据里的长度偏差带偏。
- **似然下降**：Llama 3 给 DPO 加系数 0.2 的 NLL 损失，防止被选回答的对数概率下降，并把格式 token 从损失中屏蔽，否则出现结尾重复或突然终止；SimPO 记录偏好优化普遍降低 GSM8K，一种解释是间隔变大了，被选回答的似然却没升（附录 A）。
- **评委偏差**：Zephyr 自述 GPT-4 评委偏向从它蒸馏出的模型和冗长回答；DPO 原文发现 GPT-4 算出的胜率受评委提示影响。

`[判断]` 这一阶段的经验是：离线偏好数据离当前策略越远，DPO 越容易出问题；Llama 3 每轮用最新模型重采偏好、Tulu 3 加入 on-policy 偏好、Xu 等主张在线 PPO，都是在把数据拉回策略的分布上。这与 Christiano 等 2017 年记录的"离线奖励预测器失效"是同一个问题。

### 5 偏好退居不可验证任务，评委变成会推理的模型（2025–2026）

留下的问题：标量奖励模型会被钻空子，也看不懂长推理；数学、代码已经可以用规则验证。

改变：
- [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md) 的帮助性奖励模型只看最终总结，训练数据中被选与落选回答的长度刻意相当以减小长度偏差；偏好奖励只在第二轮 RL 的最后 400 步加入。
- [DeepSeek-V3](../../../papers/arxiv-2412.19437/README.md) 让奖励模型在偏好数据中连同给分理由（思维链）一起学习，以降低奖励黑客；对通用场景用 Constitutional AI 的做法，以 V3 自己的投票结果作反馈（自我奖励）。
- [Kimi K2](../../../papers/arxiv-2507.20534/README.md) 让模型按核心 rubric、防钻空子的规定性 rubric 与人工 rubric 两两比较自己的回答，并用可验证任务上的 rollout 持续校准这个评委。
- [DeepSeek-V3.2](../../../papers/arxiv-2512.02556/README.md) 对通用任务用逐题 rubric 的生成式奖励模型；[DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md) 完全放弃标量奖励模型，让策略模型自己充当生成式奖励模型，并对它的评判能力一起做 RL，作者称只需少量多样的人工标注。
- [Kimi K3](../../../papers/arxiv-2607.24653/README.md) 的智能体评委必须先读产出、再写 rubric、逐项打分；为防止越写越长的奖励黑客，超过长度预算的回答直接判负。

做不好的场景：
- 奖励黑客没有消失：R1 用帮助性奖励模型训练更多步时，奖励上升而 Codeforces 成绩下降（附录 B.5）；K3 的智能体评委也要专门的长度控制。
- 写作这类任务难以构造可靠的奖励，R1 写明对这类任务的纯 RL 规模化仍是开放问题，只做几百步 RL（§6）。

2025-10 以后的补充：

- **评委要先被检查。** [DeepSeekMath-V2](../../../papers/arxiv-2511.22570/README.md)（2025-11）给定理证明训练验证器：先指出证明中的问题，再打 0、0.5、1 三档分。只用分数作奖励时，验证器会给对分数却编造不存在的问题，于是再训练一个元验证器检查"指出的问题是否真实"；生成器以验证器为奖励模型，并要对自己的证明做自我评估，自评与验证器一致也计入奖励（权重 0.24，证明得分 0.76）。这是"评委变成会推理的模型"在没有参考答案的任务上的一种完整做法。
- **开放团队仍以 DPO 为主。** AI2 的 [Olmo 3](../../../papers/arxiv-2512.13961/README.md)（2025-12）在 SFT 与 RL 之间保留 DPO，用"Delta Learning"构造偏好对：被选回答来自较强的模型，落选回答来自较弱的模型；作者报告同样的数据用 DPO 能带来 SFT 带不来的提升。
- **生成式奖励模型成为 Kimi 的标准件。** [Kimi K2.5](../../../papers/arxiv-2602.02276/README.md)（2026-02）在通用任务上用细粒度的生成式奖励模型评估帮助性、相关性与指令遵循，而不只判对错。

做不好的场景（补充）：DeepSeekMath-V2 的验证器编造问题，说明会推理的评委也会钻自己奖励的空子，需要再加一层检查；GLM-5 在幻灯片生成的视觉奖励上遇到截断内容、操纵间距等奖励黑客，靠修补渲染器堵住（见 [RL 方向](../rl/README.md)第 6 节）。

## 技术地基

- **Bradley–Terry 模型与逻辑回归**：奖励模型的损失就是"被选回答得分更高"这一二分类的负对数似然。[概率分类讲义](../../../../foundations/lessons/modules/objectives/02-classification-probabilities.md)第 5–6 节；DPO 精读第 5 节。
- **KL 正则的奖励目标及其闭式解**：最优策略 ∝ 参考策略 × exp(奖励/β)，DPO 由此把奖励写成对数概率比。KL 见讲义第 8 节；推导见 [DPO 精读](../../../papers/dpo/reading.md)第 6–7 节。
- **奖励模型的结构**：去掉 SFT 模型的输出层，在最后一个 token 上接一个标量头（InstructGPT、Tulu 3 的做法）。
- **PPO 与价值模型**：RLHF 的优化器，见 [RL 方向](../rl/README.md)与 [PPO 精读](../../../papers/ppo/reading.md)。
- **on-policy 与离线数据**：偏好对是否由当前策略生成，决定奖励模型或 DPO 是否在策略的分布上学习；与机器人里"离线奖励预测器失效"、行为克隆的分布偏移是同一类问题，见[模仿学习与机器人强化学习](../../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)。
- **LLM 评委**：用强模型给回答打分或比较，既用于评测，也用于造偏好数据。[LLM-as-a-Judge](../../../../cross-domain/papers/llm-judge/README.md)。

## 主要路线与团队偏好

| 团队 | `[判断]` 押注 | 代表 | 代价与做不好的地方 |
|---|---|---|---|
| OpenAI | 奖励模型 + PPO，并研究奖励模型本身的规模规律 | Christiano、Stiennon、InstructGPT、Gao 等 | 成本高；过度优化；2023 年以后细节不公开 |
| Anthropic | 把偏好拆成帮助性与无害性；用书面原则和 AI 反馈代替人的有害性标注 | HH、Constitutional AI | 过度无害；RL-CAI 训练过头后过于严厉 |
| Meta | 从 RLHF（拒绝采样 + PPO）转到 DPO，理由是简单与可扩展；两代都每轮重采偏好数据 | Llama 2、Llama 3 | DPO 需要 NLL、屏蔽格式 token 等补丁 |
| Stanford、DeepMind 等学术团队 | 从目标函数推导出更简单或更稳的损失 | DPO、IPO、SimPO | 原文规模较小（DPO 最大 6B）；分布外与过拟合问题由后来者指出 |
| Hugging Face、AI2 | 开源 SFT + DPO 配方，公开数据与代码 | Zephyr、Tulu 3 | 依赖 GPT-4 一类闭源模型打分 |
| DeepSeek | DeepSeek LLM 用 DPO；V2 起改为奖励模型 + GRPO；V3 起奖励模型带推理、自我奖励，V4 用生成式奖励模型 | DeepSeek LLM、V2、V3、R1、V3.2、V4 | 偏好奖励仍会被钻空子，只能限制步数 |
| Kimi | 自我批评的 rubric 奖励，用可验证信号校准评委 | K2、K3 | 评委本身的偏差与长度偏好需要额外控制 |
| AI2（2025-12） | 继续用 DPO，偏好对由强弱两个模型的回答构成（Delta Learning） | [Olmo 3](../../../papers/arxiv-2512.13961/README.md) | 偏好信号只来自模型强弱之差，不含人的判断 |
| DeepSeek（数学证明，2025-11） | 训练验证器与元验证器作奖励，生成器自我验证 | [DeepSeekMath-V2](../../../papers/arxiv-2511.22570/README.md) | 验证器会编造问题；只在数学证明上验证 |

`[判断]` 收敛的方向：偏好数据与当前策略对齐（每轮重采、on-policy 偏好）；长度显式控制（长度归一化、长度相当的偏好对、长度预算）；评委从标量打分器换成会写理由、按 rubric 判断的生成模型。分化在于是否保留在线 RL：Meta 与 AI2 的主力是 DPO，DeepSeek、Kimi、Qwen 把偏好信号放进 RL 作为奖励的一部分。

## 用什么衡量进展

- **奖励模型自身**：留出偏好数据上的准确率。InstructGPT 训练标注组 72.4%、留出标注组 69.6%（[精读](../../../papers/instructgpt/reading.md)第 14 节）；Llama 2 按偏好强度分档报告准确率。口径问题：奖励模型评测上的好成绩不一定转化为 PPO 之后更好的策略（Tulu 3 §5 引用的发现）。
- **策略的偏好胜率**：成对人评、MT-Bench、AlpacaEval 2（有长度控制版）、Arena-Hard。口径问题：LLM 评委偏向冗长与"同源"回答；评委提示改变胜率；胜率的对手是谁要先看清（InstructGPT 的 85% 对 GPT-3，图中曲线对 SFT）。
- **对齐税**：在标准 benchmark（SQuADv2、DROP、BBH、GSM8K）上检查偏好训练前后的变化。
- **安全与过度拒绝**：Llama 2 用 210 条看似敏感、实则无害的边界提示测错误拒答；只看有害率会掩盖过度拒绝。

## 当前开放问题

- **奖励模型怎样在策略的新分布上保持准确？** 入口：[Llama 2](../../../papers/arxiv-2307.09288/README.md)（每轮重采）、[Xu 等](../../../papers/arxiv-2404.10719/README.md)（DPO 的分布外问题）、[Gao 等](../../../papers/arxiv-2210.10760/README.md)（过度优化的规律）。
- **长度与风格偏差怎样从根上去掉？** 入口：[Singhal 等](../../../papers/arxiv-2310.03716/README.md)、[SimPO](../../../papers/arxiv-2405.14734/README.md)、[Kimi K3](../../../papers/arxiv-2607.24653/README.md)（智能体评委的长度预算）。
- **不可验证任务的评委能否被 RL 一起训练而不崩？** DeepSeek-V4 让策略兼任评委并一起优化，K2 用可验证任务校准评委，都缺少公开的失败分析。入口：[DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md)、[Kimi K2](../../../papers/arxiv-2507.20534/README.md)。DeepSeekMath-V2 给出了一个失败模式（验证器编造问题）和对应的修补（元验证），入口：[DeepSeekMath-V2](../../../papers/arxiv-2511.22570/README.md)。
- **"人类偏好"是谁的偏好？** InstructGPT 约 40 名标注员；CAI 换成书面原则；生成式奖励模型换成模型自己的判断。入口：[InstructGPT 精读](../../../papers/instructgpt/reading.md)第 14 节、[Constitutional AI](../../../papers/arxiv-2212.08073/README.md)。

## 阅读顺序

1. [InstructGPT 精读](../../../papers/instructgpt/reading.md)第 5–8、10–14 节：奖励模型怎样训练、KL 与 PPO-ptx 为什么需要、对齐税与"人是谁"。
2. [Stiennon 等](../../../papers/arxiv-2009.01325/README.md) → [Gao 等](../../../papers/arxiv-2210.10760/README.md)：过度优化从现象到规律。
3. [DPO 精读](../../../papers/dpo/reading.md)：同一个目标的离线解法，第 12–13 节看它的边界。
4. [Xu 等](../../../papers/arxiv-2404.10719/README.md) 与 [IPO](../../../papers/arxiv-2310.12036/README.md)：DPO 的分布外与过拟合，一篇实验、一篇理论。
5. [Llama 2](../../../papers/arxiv-2307.09288/README.md) → [Llama 3](../../../papers/arxiv-2407.21783/README.md)：同一团队从 PPO 换到 DPO，以及换完之后打的补丁。
6. [Kimi K2](../../../papers/arxiv-2507.20534/README.md) 第 3.2.2 节 → [DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md) 第 5.1.1 节：评委变成会推理的模型。

## 批注

**易误读**

- Stiennon 等的"负相关"出现在强优化区间（大 KL），而且用的是较早版本的奖励模型（图 5 图注）；轻度优化时奖励模型是有用的。
- Gao 等的结论来自合成设定（黄金奖励模型代替人），"KL 惩罚无效"作者明说可能对超参数敏感（§1）。
- Xu 等的"PPO 全面超过 DPO"依赖他们找出的 PPO 关键配置；Tulu 3 在未专门调参的对照中发现 PPO 与 DPO 平均分相近、PPO 略低。两者不矛盾：PPO 的上限高，但更难调。
- DPO 原文的实验最大到 6B，作者把"扩展到大得多的模型""分布外泛化""奖励过度优化在 DPO 中怎样表现"都列为开放问题（§7）；后来的大规模经验来自 Llama 3、Tulu 3 等。
- Llama 3 的 DPO 仍然依赖奖励模型：奖励模型用于拒绝采样，DPO 只替代了 PPO 那一步。

**判断的支撑论文**

- "评委不可靠 → 跟上策略 → 去掉评委 → 评委会推理"的问题链：Christiano §3.3、Stiennon 图 5、Llama 2 §3.2.1、DPO §1、Xu 等 §4、V3 §5.2.1、K2 §3.2.2、V4 §5.1.1。边界：DPO 被提出时的动机是复杂与不稳定（摘要），不是奖励黑客。
- 偏好退居不可验证任务：R1 §2.2 与 §3.2.2、Qwen3 §4.4（规则奖励用于能精确判断的任务，参考答案评分与无参考的奖励模型覆盖其余任务）、V3.2 §3。反例：Llama 3、Tulu 3 在推理与指令遵循上仍大量使用 DPO。
- 团队偏好（两篇以上、存在替代时重复选择）：Meta 在 Llama 2、Llama 3 都按轮次用最新模型重采偏好数据；Anthropic 在 HH 与 CAI 都把帮助性与无害性分开；DeepSeek 自 V2 起在 V2、V3、R1、V3.2、V4 都把偏好作为 GRPO 的一部分奖励，而不用 DPO。

**与其他论文的关联**

- [SFT 方向](../sft/README.md)：拒绝采样既是偏好学习的一步，也是 SFT 的数据来源；DeepSeek LLM 用 DPO 降低 SFT 后的重复。
- [强化学习方向](../rl/README.md)：PPO、GRPO 的算法细节；可验证奖励与偏好奖励在同一次 RL 中怎样相加（R1 式 8–10）。
- [LLM-as-a-Judge](../../../../cross-domain/papers/llm-judge/README.md)：评测用的 LLM 评委与训练用的生成式奖励模型，是同一类模型放在两个位置。
- [模仿学习与机器人强化学习](../../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)"奖励设计"一节：腿足 RL 中奖励被钻空子的例子，与 Stiennon 原文提到的机器人领域现象是同一类。

**未核实 / 待验证**

- RewardBench 等专门的奖励模型评测本轮没有打开原文，正文没有引用其数字。
- Llama 2 中两个奖励模型的具体准确率（Table 7–8）本轮只读到表题，未引用数字。
- Kimi K3 智能体评委的"锦标赛式二元比较"沿用自 Kimi K2.5，K2.5 报告本轮未打开。（补记：K2.5 报告已在[卡片](../../../papers/arxiv-2602.02276/README.md)中核对了生成式奖励模型的用途，"锦标赛式二元比较"一句仍未在 K2.5 原文中找到对应段落。）
- Anthropic 在 Constitutional AI 之后的偏好训练做法，本轮没有检索核对（库中已有的 [Claude Opus 5.5 系统卡](../../../../cross-domain/papers/anthropic-claude-opus-5-5-system-card/README.md)归评估方向，未据它写训练事实）；Olmo 3 中 Delta Learning 的单独消融数字未核对。

**与原结论的张力**

- 第 5 节标题"偏好退居不可验证任务"与收敛判断"Meta 与 AI2 的主力是 DPO"在 2025-12 仍成立：Olmo 3 在推理模型上也保留了 DPO 一步，并报告它带来 SFT 带不来的提升。偏好学习在开放团队里并没有被 RL 完全取代，只是偏好对越来越多地由模型强弱之差构造，而不是由人标注。
