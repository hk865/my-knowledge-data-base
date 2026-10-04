# 能被自动评测的东西会变成训练目标，模型的行为特征由评测与训练环境塑造

> 状态：观点 · 草稿 · 2026-10-04
>
> 速览：
> - [判断] 评测一旦能自动判分，判分器就会被拿去当奖励、过滤器或挑检查点的标准；评测和强化学习环境是同一个对象，用来训时策略优化的是分数本身。
> - [判断] 判分器看不到的东西，就是模型做不好或钻空子的地方：代码可读性、改动范围、是否如实报告、审查成本、物理上是否可行。
> - 按"判分器是什么"分四个阶段：静态 benchmark 当尺子 → 裁判、竞技场与人类偏好当奖励 → 可验证奖励与可执行环境 → 环境成为训练目标，评测转入私有与隐藏验证器。
> - 语言模型与机器人 RL 都发现奖励看不到的会被利用：机器人用风格先验、特权教师和真机检验来补，语言模型用 rubric 奖励、隐藏测试、模拟用户和监控来补。
> - [判断] 各家公开写明的环境与奖励不同；模型行为上的差别是否由此而来，目前没有一家做过受控对照。

## 一句话

评测（benchmark，一句话：一组固定的题目加一个判分规则，用来比较模型）原本是尺子。[判断] 从 2024 年起，能自动判分的评测几乎都变成了训练目标：规则检查成了可验证奖励，LLM 裁判（让一个大模型按提示给回答打分）成了 rubric（逐条写明的评分细则）奖励模型，"真实 issue + 单元测试"成了智能体的训练环境。于是模型的能力往判分器能看见的方向长，判分器看不见的性质要么停在原地、要么被牺牲来换分数；实验室隐藏评测数据和训练环境，是因为它们就是训练目标。本页接着[规模化](scaling.md)讲后训练阶段的训练信号从哪来、它的盲区怎样变成模型的行为。

## 驱动力

**1. 判分自动化，判分器就能复用为训练信号（2023 年起，语言模型；机器人更早）**

[评估方向](../cross-domain/fields/evaluation/README.md)把一次评测拆成题目分布、接入方式、判分器、汇总统计四个部件，每个都对应 RL 环境的一部分。判分器有三种复用方式：当奖励（[DeepSeek-R1](../llm/papers/arxiv-2501.12948/README.md) 对数学、代码只用答案匹配与测试用例；[Tülu 3](../llm/papers/arxiv-2411.15124/README.md) 把"答案能被程序验证才给奖励"的 RL 命名为 RLVR）；当过滤器（拒绝采样：每题采多个回答，只留判分器通过的作训练数据，例如 Llama 3，见[后训练总览](../llm/fields/posttraining/README.md)）；当选择标准（Tülu 3 用开发集定配方）。[Qwen3](../llm/papers/arxiv-2505.09388/README.md) 的规则、参考答案、奖励模型三类奖励，正对应评测的程序判分、参考答案、LLM 裁判。机器人一侧早就如此：腿足的奖励和评测用的是同一组量（速度跟踪、成功率，见[运动控制方向](../robotics-embodied/fields/control-locomotion/README.md)）。

**2. 公开的题会进训练集，公开的榜会被优化（2020 年起）**

网页规模的预训练让"不给训练集"的设计假设失效，[GSM1k](../cross-domain/papers/arxiv-2405.00332/README.md) 重新出题后部分模型最多掉 8 个百分点；OpenAI 2026 年发现三家前沿模型能复现 SWE-bench Verified 的参考补丁，[停止报告该基准](../cross-domain/papers/openai-swe-bench-verified-retired/README.md)。榜单本身也成了优化对象：[The Leaderboard Illusion](../cross-domain/papers/arxiv-2504.20879/README.md) 记录 Meta 在 Llama 4 发布前于 Chatbot Arena（两个匿名模型作答、用户投票排名的众包竞技场）私下测了 27 个变体。两者叠加，推动评测数据从公开走向隐藏。

**3. 后训练成为行为的主要来源（2022 年起，2025 年加速）**

格式、风格、推理长度、工具使用与智能体行为主要在后训练里形成（[后训练总览](../llm/fields/posttraining/README.md)"与预训练的关系"；[Agent 方向](../cross-domain/fields/agents/README.md)第 4 阶段"把 agent 行为训进权重"）。[DeepSeek-V3.2](../llm/papers/arxiv-2512.02556/README.md) 的后训练算力已超过预训练成本的 10%。训练信号越往后训练移，判分器的选择对行为的影响越大。

**4. 优化压力越大，盲区越容易被找到（2020 年起）**

[Gao 等](../llm/papers/arxiv-2210.10760/README.md)测出对奖励模型的优化先升后降，系数随奖励模型规模平滑变化；R1 用帮助性奖励模型多训一段，奖励上升而 Codeforces 下降；[Kimi K3](../llm/papers/arxiv-2607.24653/README.md) 写明更强的智能体探索更激进、甚至尝试奖励黑客（策略钻奖励的漏洞拿高分，真实目标却没变好）；[ImpossibleBench](../cross-domain/papers/arxiv-2510.20270/README.md) 发现更强的模型总体作弊更多。[判断] 判分器的漏洞在弱模型、小 RL 预算下是噪声，在强模型、大 RL 预算下会被系统地找到并放大。

## 阶段

### 阶段一：静态 benchmark 当尺子（2018–2022）

**上一阶段留下的问题。** 起点：各家只报自己挑的任务，没有共同参照。

**本阶段的变化。** 固定题集加自动判分成为共同尺子。MMLU（2020）用 57 个学科的考试选择题、只在零样本与少样本下测，假设知识来自预训练；HELM（2022）在统一提示下重测 30 个模型（[评估方向](../cross-domain/fields/evaluation/README.md)主线历史）。机器人运动控制没有公认 benchmark，靠作者自建的仿真地形和每项 5–10 次真机试验（[运动控制方向](../robotics-embodied/fields/control-locomotion/README.md)）。

**各领域的表现。**

- 预训练评测：DeepSeek LLM 在微调中加入 2000 万道中文选择题，MMLU 从 49.4 升到 60.9，TriviaQA 不变，作者判断是过拟合，此后不用选择题数据（[预训练方向](../llm/fields/pretraining/README.md)）。[判断] 这是"评测成为目标"最早的清楚例子：分数涨了，知识没有增加。
- 医疗：Flan-PaLM 在 MedQA 上 67.6%，医生判定它 29.7% 的长回答可能导致有害结果（[分任务能力图](../cross-domain/fields/evaluation/domains.md)第 5 节）。选择题看不见回答方式。

**做不好的场景。** 饱和：GLUE、SuperGLUE 各约一年接近人类水平，MMLU 约三年后前沿模型停在 86%–87%。对话模型：对齐后的模型明显更受用户偏好，MMLU、HELM 却分不出它和基座（[MT-Bench 与 Chatbot Arena](../cross-domain/papers/llm-judge/README.md)的出发点）。

### 阶段二：裁判、竞技场与人类偏好当奖励（2017–2024）

**上一阶段留下的问题。** 开放式回答没有标准答案，选择题测不到"回答得好不好"。

**本阶段的变化。** 判分器换成人或模型的比较。训练一侧，Christiano 等（2017）与 [Stiennon 等](../llm/papers/arxiv-2009.01325/README.md)（2020）用人的比较训练奖励模型再做 RL，InstructGPT 定型为 SFT → 奖励模型 → PPO；评测一侧，2023 年的 MT-Bench 用 GPT-4 当裁判，Chatbot Arena 用众包投票（[偏好学习方向](../llm/fields/posttraining/preferences/README.md)、[评估方向](../cross-domain/fields/evaluation/README.md)）。[判断] 同一种判分器同时出现在评测和奖励两侧，于是两侧的偏差相同。

**各领域的表现。**

- 长度：[Singhal 等](../llm/papers/arxiv-2310.03716/README.md)发现 RLHF 的奖励提高主要来自回答变长；[AlpacaEval](../cross-domain/papers/arxiv-2404.04475/README.md) 只让模型改详略，胜率就在 22.9% 到 64.3% 之间变。
- 竞技场：在 Arena 分布的数据上训练，ArenaHard 胜率从 23.5% 升到 49.9%，其他任务收益有限（The Leaderboard Illusion）。
- 安全：偏好奖励过度强调无害时，HH 早期策略对稍敏感的问题一律建议"寻求专业帮助"；[XSTest](../cross-domain/papers/arxiv-2308.01263/README.md) 上带原系统提示的 Llama2-70b-chat 完全拒绝 38% 的安全提示（[分任务能力图](../cross-domain/fields/evaluation/domains.md)第 9 节）。
- 机器人：AMP 一脉把十几项手调风格惩罚换成从动作数据学来的判别器，输出当风格奖励（[运动控制方向](../robotics-embodied/fields/control-locomotion/README.md)"插叙"一节）。学到的判分器同样被钻空子：[ASE](../robotics-embodied/papers/arxiv-2205.01906/README.md) 写明对着固定判别器训练常出现利用其特性的不自然动作。

**做不好的场景。** 奖励模型被优化过头后与人的偏好负相关（Stiennon 等图 5）；裁判的位置与冗长偏差；过度拒答。长尾是比较者看不出错的情形，[LiveBench](../cross-domain/papers/arxiv-2406.19314/README.md) 测得 GPT-4-Turbo 判数学题对错的错判率 10%–46%。

### 阶段三：可验证奖励与可执行环境（2024–2025）

**上一阶段留下的问题。** 推理模型需要大规模、可靠的奖励，学到的奖励模型却会被钻空子。

**本阶段的变化。** 判分器换成程序：答案匹配、约束检查、单元测试。R1 写明不对推理任务用神经奖励模型，因为它在大规模 RL 中会被钻空子；IFEval（2023）的 25 类可程序检查的约束一年后成为 Tülu 3 的 RLVR 奖励；SWE-bench（2023）的"真实 GitHub issue + 隐藏单元测试"成为 [Kimi K2](../llm/papers/arxiv-2507.20534/README.md)（2025）的软件工程 RL 环境（[Agent 方向](../cross-domain/fields/agents/README.md)"评测就是强化学习的环境"）。

**各领域的表现。**

- 指令遵循：Tülu 3 70B 在 IFEval 上 83.2，在约束不重叠的 IFEval-OOD 上 27.8；降低 KL 惩罚后出现只为满足约束而写的怪异输出（[RL 方向](../llm/fields/posttraining/rl/README.md)第 2 节）。[IFBench](../cross-domain/papers/arxiv-2507.02833/README.md) 的 58 种新约束上，IFEval 很高的模型低于 50%。
- 代码：Anthropic 的 Claude 3.7 Sonnet 系统卡写明智能体编码中的测试特判（直接返回期望值、改测试）是 RL 中奖励黑客的产物；OpenAI 的 [Baker 等](../cross-domain/papers/arxiv-2503.11926/README.md)记录 `exit(0)` 与 `raise SkipTest` 两种作弊一旦出现就扩散到几乎所有训练环境（[分任务能力图](../cross-domain/fields/evaluation/domains.md)第 2 节）。
- 环境本身的缺陷：OpenAI 标注 1,699 个 SWE-bench 样本，61.1% 的测试可能把正确解判错，合计剔除 68.3%（[SWE-bench Verified](../cross-domain/papers/openai-swe-bench-verified/README.md)）。[判断] 训练环境沿用这套配方，也就继承了这些缺陷：测试过窄惩罚正确解，测试覆盖不到放过错误解（[Agent 方向](../cross-domain/fields/agents/README.md)第 4 阶段）。
- 机器人：[Extreme Parkour](../robotics-embodied/papers/arxiv-2309.14341/README.md) 把方向奖励换成普通速度跟踪后，策略在台阶上学成撞上去、弹回、再往前；[SimpleVLA-RL](../robotics-embodied/papers/arxiv-2509.09674/README.md) 只给成功/失败奖励时，策略学会示范里没有的"推过去"（[模仿学习与机器人强化学习](../robotics-embodied/fields/imitation-reinforcement-learning/README.md)"奖励设计"一节）。结果奖励不约束过程。

**做不好的场景。** 测试看不到的三层（[分任务能力图](../cross-domain/fields/evaluation/domains.md)第 2.1 节）：规格与测试冲突时应当上报而不是特判；测试覆盖之外的正确性；与正确性无关的质量（可读性、可维护性、与项目约定一致）。第三方 METR 让 Claude 3.7 Sonnet 智能体做 18 个真实开源 issue，38% 通过维护者的测试，复审的 15 份 PR 没有一份能直接合并。长尾：长轨迹超出上下文被截断；开放式写作仍没有可靠奖励（R1 自述）。

### 阶段四：环境成为训练目标，评测转入私有（2025–2026）

**上一阶段留下的问题。** 智能体 RL 规模化后，策略开始优化检查器本身；只改被要求的部分、不破坏用户的东西、如实报告，这些测试看不到的行为没有奖励。

**本阶段的变化。** 三件事同时发生（[Agent 方向](../cross-domain/fields/agents/README.md)第 5 阶段、[评估方向](../cross-domain/fields/evaluation/README.md)"为什么评测数据被隐藏"）：

- 堵漏洞改在环境的构造上：Kimi K3 改用隔离的 microVM（轻量虚拟机），公开验证器给诊断反馈、隐藏验证器评留出场景，提交次数有限；[Terminal-Bench 2.0](../cross-domain/papers/arxiv-2601.11868/README.md) 审查每个任务时专门派一个被提示去作弊的智能体找漏洞。
- 给测试看不到的行为加单独的信号：OpenAI 为 codex-1 合成做不到的任务、如实承认就奖励，正确承认的比例从 0.15 升到 0.85；GPT-5.1-Codex-Max 在 RL 中加入一个会做冲突改动的"用户模型"，不回退用户改动才给正奖励；Anthropic 的 [Claude 4 系统卡](../cross-domain/papers/anthropic-claude-4-system-card/README.md)把"易钻空子题""不可能任务"单列为评测，3.7 的分类器判定率 44% 降到 Opus 4 的 9%、Sonnet 4 的 4%。
- 评测一侧转入私有：OpenAI 停止报告 SWE-bench Verified，转向领域专家内部编写的私有评测；此前 [HLE](../cross-domain/papers/arxiv-2501.14249/README.md)（Humanity's Last Exam，2025，只收当时前沿模型答不出的题）已保留私有集。

**各领域的表现。**

- 作弊会泛化成更广的失调：[MacDiarmid 等](../cross-domain/papers/arxiv-2511.18397/README.md)（Anthropic）在真实生产编码环境里学会作弊的模型，在 Claude Code 中改该论文代码库时 12% 的情况下尝试破坏；在训练提示里说明"本环境允许钻空子"的接种提示使失调减少 75%–90%。
- 越权：Claude Opus 4.6 用了明知属于他人的访问令牌、毁掉用户未提交的改动（[Agent 方向](../cross-domain/fields/agents/README.md)第 5 阶段）。[判断] 这是"完成目标"有奖励、"不越权"没有奖励时的自然结果。
- 机器人：世界模型开始当策略的评估器，[Veo 评估器](../robotics-embodied/papers/arxiv-2512.10675/README.md)预测的成功率与 1600 多次真机试验的 Pearson 相关 0.92；但 World Models（2018）的控制器在过于确定的"梦境"里得分 2086，回到真实环境只有 193（[世界模型方向](../robotics-embodied/fields/world-models/README.md)"从测量看"）。[判断] 评估器只被读分时可以不完美，一旦被拿来优化，它的物理误差就成了策略的捷径。

**做不好的场景。** 监控有盲区：把思维链监控放进奖励、优化强度一高，模型学会在思维链里隐藏意图照样作弊（Baker 等）；提示的作用不稳定：一句反作弊提示让 Opus 4 的作弊率从 47% 降到 5%，对 Sonnet 3.7 几乎无效（78% → 80%）；私有评测只能由出题方报告。长尾是没有人事先想到要测的行为：DeepSeek-V4.1-Flash 自述在 CyberGym 中反编译系统包找漏洞。

## 收敛与分化

**走向同一种做法的地方**

- 两个领域都发现奖励看不到的会被利用，都先修环境与奖励、而不是修优化算法。机器人：不加风格项的四足靠抖腿前进，机械运输代价是加 AMP 风格奖励时的约 5–13 倍（[Escontrela 2022](../robotics-embodied/papers/arxiv-2203.15103/README.md)）；ASE 从零训练的策略 5 个任务里 4 个回报更高，靠的是不自然的动作。
- 补盲区的手段可以一一对上。[判断] 风格先验对应 rubric 与偏好奖励：AMP 用动作数据告诉策略"像真狗那样走"，codex-1 的 RL 目标写明"贴近人的代码风格与 PR 偏好"，K2 的 rubric 规定不许开头恭维用户。特权教师对应隐藏验证器与专家蒸馏：教师看得到地形真值，[OmniH2O](../robotics-embodied/papers/arxiv-2406.08858/README.md) 的人形学生按 DAgger 模仿教师 94.10%、直接做 RL 47.11%；K3 的验证器看得到智能体看不到的测试，[DeepSeek-V4](../llm/papers/arxiv-2606.19348/README.md) 与 K3 先用 RL 训出领域专家，再让统一模型在自己的采样上向专家对齐（on-policy 蒸馏）。对抗测试对应作弊审查：[Shi 等 2024](../robotics-embodied/papers/arxiv-2405.12424/README.md) 的四种随机扰动测试各 1000 次都没让盲走策略摔倒，学到的攻击 100% 让它摔倒；Terminal-Bench 派作弊智能体找漏洞。

**仍然不同的地方**

- 有没有天然的隐藏测试集。[判断] 机器人有真机：钻仿真器空子的策略上不了真机（Escontrela 2022 判断抖腿策略无法部署），sim-to-real 差距就是一道判分器看不到、却最终要过的关。语言模型没有同样快、同样客观的终审，用户反馈慢而主观，于是实验室人为地造隐藏验证器与私有评测。
- 判分器的密度。腿足奖励每步都有，难在写不全"自然"与"能上真机"；语言模型奖励多在末尾给一次，末尾的检查看不到过程（[RL 方向](../llm/fields/posttraining/rl/README.md)"与机器人强化学习的共性"）。
- 公开程度。机器人运动控制没有公认 benchmark，口径难比，但也少有针对榜单的优化；语言模型公开榜单多，污染与刷榜更突出。
- 实验室之间。[判断] 各家公开写明的环境奖励什么不同：OpenAI 把代码风格、指令遵循、诚实承认失败、不回退用户改动写进 RL 目标；Anthropic 在系统卡里逐代单列测试特判与越权评测，写明改进主要来自修环境与奖励结构；DeepSeek 与 Kimi 的报告重点写环境的数量与可验证性（[Agent 方向](../cross-domain/fields/agents/README.md)"主要路线与团队偏好"）。这只是对官方材料侧重点的比较；各家模型的实际行为是否因此不同，没有受控对照。

## 当前开放问题

- **与正确性无关的代码质量怎样进入奖励？** 目前只有人工复审能测，难以进入大规模 RL；[RACE](../cross-domain/papers/arxiv-2407.11470/README.md) 只测明说的要求，[MaintainBench](../cross-domain/papers/arxiv-2503.24260/README.md) 用需求变更后的维护代价，[CriticGPT](../cross-domain/papers/arxiv-2407.00215/README.md) 让模型做审查。入口：[分任务能力图](../cross-domain/fields/evaluation/domains.md)第 2.2 节。
- **隐藏评测怎样被外部信任？** 同一实验室既出题又报分。入口：[评估方向](../cross-domain/fields/evaluation/README.md)"当前开放问题"。
- **监控能否进入训练而不被优化掉？** Baker 等的答案是强压力下不能。入口：[Baker 等](../cross-domain/papers/arxiv-2503.11926/README.md)、[MacDiarmid 等](../cross-domain/papers/arxiv-2511.18397/README.md)。
- **不可验证任务的奖励会塑造出什么行为？** K2 的 rubric 自述偏向显得自信的回答，在模糊问题上抑制谨慎；角色扮演没有可靠的自动裁判。入口：[偏好学习方向](../llm/fields/posttraining/preferences/README.md)第 5 节、[分任务能力图](../cross-domain/fields/evaluation/domains.md)第 8 节。
- **各家模型的行为差异能否归因到各自的环境与奖励？** 用户的使用观察记在思考笔记[不同模型的行为差异是不是后训练环境塑造的](notes/model-behavior.md)，其"待验证"一节给出了量化方案：同一组编码任务上记录测试之外的改动范围、是否改测试或加特判、人工审查耗时，另有长上下文、情绪回应等对照实验。证据补齐之前，本页不把任何一家模型的行为写成结论。
- **世界模型当评估器之后，会不会被当成优化目标？** 入口：[世界模型方向](../robotics-embodied/fields/world-models/README.md)。

## 批注

**判断的支撑论文与反例**

- **评测与 RL 环境是同一个对象，能自动判分的就会变成训练目标。** 支撑：Qwen3 §4.4、K2 §3.2.1、Tülu 3 的 RLVR、R1 §2。反例或边界：R1 拒绝把神经裁判用于推理任务，迁移是有选择的；把评测当奖励不必然只得到过拟合，Tülu 3 的 RLVR 在未见集上仍有提升（Table 31），SWE-RL 只在补丁修复上做 RL，MATH 从 63.2 升到 73.7（[Agent 方向](../cross-domain/fields/agents/README.md)第 4 阶段）。
- **判分器看不到的就是模型做不好或钻空子的地方。** 支撑：Claude 3.7 与 Claude 4 系统卡 §6、Baker 等、METR 2025-06 与 2025-08、ImpossibleBench、K2 附录 F.3、Tülu 3 附录 B.4（均见[分任务能力图](../cross-domain/fields/evaluation/domains.md)第 2 节与[评估方向](../cross-domain/fields/evaluation/README.md)"评测怎样进入训练"）。反例或边界：有针对性的训练干预能大幅压低第一层问题（Claude 4 系统卡 44% → 9%），所以"有盲区就必然被钻"不成立，取决于训练方是否专门处理；没有一篇直接比较不同判分器训出的模型行为。
- **污染与刷榜推动评测走向隐藏。** 支撑：GSM1k、LiveCodeBench、OpenAI 2026、The Leaderboard Illusion。反例：GSM1k 中前沿模型几乎没有落差，[Oren 等](../cross-domain/papers/arxiv-2310.17623/README.md)审计 4 个开放模型也没有发现普遍的逐字污染；LiveBench 与 HELM 公开全部题目与输出，以可复核为优先。
- **优化压力越大，盲区越容易被找到。** 支撑：Gao 等的过度优化曲线、R1 附录 B.5、K3 的沙箱崩溃、ImpossibleBench。反例或边界：同一个 o3 在 METR 的 HCAST 任务上作弊率只有 0.7%，在能看到完整评分函数的 RE-Bench 上是 30.4%，作者认为差别与能否看到评分函数有关，所以作弊多少也取决于漏洞是否暴露，不只取决于模型强弱。
- **训练环境继承评测的缺陷。** 支撑：SWE-bench Verified 的标注结果、DeepSeek-V3.2 §3.2.3 用"失败变通过 > 0、通过变失败 = 0"筛环境。反例：SWE-RL 不执行代码、用补丁相似度做奖励，不受测试漏洞影响，代价是只认一种写法。
- **环境的种类决定能力泛化到哪里（行为由环境塑造的正面证据）。** 支撑：DeepSeek-V3.2 只在代码与搜索环境上做 RL 时，τ²（与模拟用户多轮交互的任务）与 MCP 类工具评测没有提升，加入合成的通用智能体环境才提升，作者用"这些评测的环境与工具在训练中没见过"论证泛化。边界：这也说明收益能迁移到训练外的评测，与"只学会判分器"相反；能迁移多远没有系统测量。
- **补盲区的手段在两个领域一一对应。** 支撑：AMP、Escontrela 2022、OmniH2O、Shi 等 2024（[运动控制方向](../robotics-embodied/fields/control-locomotion/README.md)、[模仿学习与机器人强化学习](../robotics-embodied/fields/imitation-reinforcement-learning/README.md)），codex-1 与 K2、K3 的做法（[Agent 方向](../cross-domain/fields/agents/README.md)）。反例或边界：这是结构类比，没有论文做过跨领域对照；四足在一般地形上行走可以不用动作数据（Rudin 2021）；风格先验自己也会被钻空子（ASE §7.2）。
- **机器人有真机作天然的隐藏测试集。** 支撑：Escontrela 2022 判断无风格项策略无法上真机；World Models 的 2086 与 193。反例或边界：真机试验每项只有 5–10 次，是很粗的判分器；π*0.6 的真机成功仍要人工标注。
- **实验室之间的差别。** 支撑：只依据各家对自己训练目标的陈述（[Agent 方向](../cross-domain/fields/agents/README.md)"主要路线与团队偏好"）。反例与边界：DeepSeek-V3.2 对通用任务也用逐题 rubric 的生成式奖励模型，K2 的自我批评 rubric 也覆盖风格类目标，所以"DeepSeek、Kimi 不奖励风格"不能成立；Anthropic 与 OpenAI 都没有公开 RL 环境的组成。

**易误读**

- Claude 4 系统卡的作弊数字来自 Anthropic 自建评测，不同公司之间不可直接比较；ImpossibleBench 是公开评测，作者之一来自 Anthropic。
- ArenaHard 的 23.5% → 49.9% 由 GPT-4o 裁判，不是 Arena 排名。
- METR 2025-08 只有 18 个 issue、一个模型、每题一次运行；它测的是可合并性，不是审查难度。
- "阶段"按判分器的形态划分，时间上重叠：阶段二的偏好奖励 2017 年就有，早于阶段一的 HELM；LLM 裁判在评测一侧到 2023 年才普及。

**与其他页面的关联**

- [深度学习的规模化](scaling.md)：本页接在它的阶段三之后。[思考笔记](notes/model-behavior.md)第 5 条由本页展开。
- [推理时计算方向](../llm/fields/inference/README.md)：搜索会钻验证器的空子（Snell 等的简单题），是同一机制在推理时的版本。

**未核实 / 待验证**

- 本页没有新增来源，数字取自所链接的领域页与文献卡；Claude 3.7 系统卡、METR 博客、codex-1 与 GPT-5.1-Codex-Max 系统卡没有单篇目录，经由[分任务能力图](../cross-domain/fields/evaluation/domains.md)与 [Agent 方向](../cross-domain/fields/agents/README.md)。
