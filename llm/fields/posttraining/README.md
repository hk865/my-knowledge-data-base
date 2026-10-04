# 后训练

> 状态：领域总览 · v1 · 依据三个子方向的综合表（[SFT](sft/synthesis.csv)、[偏好学习](preferences/synthesis.csv)、[强化学习](rl/synthesis.csv)，共 52 行）
>
> 速览：
> 1. 预训练给出结构先验与世界知识，后训练决定模型怎样使用它们：SFT 教格式与指令遵循，偏好学习按人的比较调整取舍与风格，强化学习在可验证的奖励上把"偶尔做对"变成"稳定做对"，并学会花更多 token 思考。三者都很少增加知识：LIMA 只用 1,000 条示范，Llama 3 把"让模型知道自己知道什么，而不是添加知识"写成原则，DeepSeek-V3.2 把知识广度的差距推回预训练。
> 2. 每个阶段都有自己的坑：SFT 上的新知识学得慢，学会后线性增加幻觉；奖励模型被优化过头后与人的偏好负相关（奖励黑客）；对齐会让部分能力下降（对齐税）；DPO 可能偏向偏好数据之外的回答；GRPO 让错误回答越写越长、让策略熵早早坍缩；RL 在大 k 的 pass@k 上不如基座。
> 3. 站在 2026 年看，后训练的重心移动了三次：2022 年是人类偏好驱动的 RLHF（SFT → 奖励模型 → PPO）；2023–2024 年开源团队转向离线的 DPO；2025 年 o1、DeepSeek-R1、Kimi k1.5 把重心移到可验证奖励上的大规模 RL，R1-Zero 甚至跳过 SFT。2025–2026 年又出现第三种形态：先按领域训练多个 RL 专家，再用 on-policy 蒸馏合成一个模型（Qwen3、DeepSeek-V4、Kimi K3）。
> 4. `[判断]` 贯穿这条线的是"奖励从哪来"：人写示范 → 人的比较 → 规则验证器 → 按 rubric 打分的生成式奖励模型。每一次替换，都在回应上一种奖励的可被利用性或扩不上去。
> 5. 后训练的算力占比在上升：Flan-PaLM 540B（2022）的指令微调只用了预训练算力的 0.2%，DeepSeek-V3.2（2025）的后训练算力超过预训练成本的 10%。

本页是[大语言模型](../../README.md)领域的后训练总览，接在[预训练](../pretraining/README.md)之后。后训练分三个子方向：[监督微调 SFT](sft/README.md)、[偏好学习与奖励模型](preferences/README.md)、[语言模型强化学习](rl/README.md)。本页讲三者的分工、与预训练的关系、重心怎样移动；各阶段的方法细节、基线拆分与论文列表在子方向页。

## 后训练在解决什么

结论：预训练结束时，模型会续写，但不会按要求做事；后训练把"会续写"变成"按指令、按目标、可控地回答"。

给一个只做过预训练的基座模型（base model，一句话：只用下一词预测训练过、未经任何对齐的模型）输入"周一博物馆开门吗？下面是通知：……周一闭馆"，它可能接着写出另一条通知、另一道问题，或者一篇游记。它其实"知道"答案，只是不知道此刻该以助手的身份回答。后训练要解决三件事，对应三种训练信号：

| 要解决的事 | 训练信号 | 方法 | 一句话的直觉 |
|---|---|---|---|
| 以什么格式、什么角色回答 | 示范回答 | SFT（监督微调，一句话：在"指令 + 示范回答"上做下一词预测，只在回答部分计算损失） | 照着样子学 |
| 两个都说得通的回答，哪个更好 | 人或模型对两个回答的比较 | 奖励模型 + RL（RLHF），或直接偏好优化（DPO） | 学人的取舍 |
| 答案对不对 | 程序可以检查的结果：数学答案、单元测试、环境状态 | 可验证奖励的强化学习（RLVR） | 自己试，做对了才奖励 |

[InstructGPT 精读](../../papers/instructgpt/reading.md)用一个博物馆的例子把三个阶段串成一条流水线，第一次读后训练可以从那里开始。

### 与预训练的关系

结论：预训练决定模型知道什么、能表示什么；后训练决定模型在什么场合、以什么方式调用这些东西。后训练能让已有能力更稳定、更省 token 地发挥出来，却很难补上预训练没学到的知识。

| 阶段 | 训练信号 | 主要学到什么 | 不该指望它学什么 | 原文中的坑 | 详页 |
|---|---|---|---|---|---|
| 预训练 | 无标注文本上的下一词预测 | 语言结构、世界知识、数学与代码的底子 | 按指令回答 | 损失尖峰、注意力汇聚等，见预训练页 | [预训练](../pretraining/README.md) |
| SFT | 示范回答上的交叉熵 | 指令遵循、对话格式、回答风格；冷启动时的推理格式 | 新的事实知识；超过示范者的水平 | Gekhman 等：新知识学得慢，学会后线性增加幻觉；DeepSeek LLM：数学 SFT 数据越多，回答越容易无限重复 | [SFT](sft/README.md) |
| 偏好学习 | 两个回答之间的比较 | 有帮助、无害、风格与长度上的取舍 | 事实正确性（比较者可能看不出错） | Stiennon 等：奖励模型被优化过头后与人的偏好负相关；Singhal 等：奖励提高主要来自回答变长；Xu 等：DPO 可能偏向分布外回答 | [偏好学习](preferences/README.md) |
| 强化学习（可验证奖励） | 程序验证的结果奖励 | 长思维链、自我检查、按难度分配思考长度 | 基座采样分布之外的推理路径 | DeepSeek-R1：神经奖励模型在大规模 RL 中被钻空子；DAPO：熵坍缩；Dr. GRPO：错误回答越写越长；Yue 等：大 k 的 pass@k 不如基座 | [强化学习](rl/README.md) |
| 蒸馏（2025 年起常与上面合用） | 教师模型的输出或逐 token 分布 | 把大模型、领域专家的能力搬给学生或统一模型 | 超过教师 | DeepSeek-R1：小模型直接 RL 不如蒸馏，但超越人类边界仍需更强的基座和更大规模的 RL | [SFT](sft/README.md)、[知识蒸馏](../../../cross-domain/fields/knowledge-distillation/README.md) |

这张表背后有四组证据。

**后训练很少加知识。** [LIMA](../../papers/arxiv-2305.11206/README.md) 只用 1,000 条示范微调 65B LLaMa，人评中 43% 不差于 GPT-4，作者据此提出表层对齐假说（知识和能力几乎都在预训练中学到，对齐只教模型用哪种格式与用户交互）。[DeepSeek LLM](../../papers/arxiv-2401.02954/README.md) 发现 SFT 前后知识类评测只有小幅波动，SFT 的价值在于让对话模型 0-shot 的 MMLU 达到基座 5-shot 的水平。[Gekhman 等](../../papers/arxiv-2405.05904/README.md)把这件事做成了对照实验：SFT 数据中基座不知道的事实（Unknown）比已知的事实拟合得慢得多，一旦被拟合，模型在原有知识上的幻觉线性增加。[Llama 3](../../papers/arxiv-2407.21783/README.md) 据此把事实性数据的原则写成"让模型知道自己知道什么，而不是添加知识"。

**强化学习主要是在基座已有的回答里重新分配概率。** [DeepSeekMath](../../papers/arxiv-2402.03300/README.md) 的 RL 提高了 Maj@K（K 次采样多数投票的准确率），却没有提高 Pass@K（K 次中至少答对一次）；作者的解释是 RL 把 TopK 里的正确答案提了上来，而不是增强基础能力。一年后 [Yue 等](../../papers/arxiv-2504.13837/README.md)在六种 RL 算法、多个模型族上得到同样的结论：k = 1 时 RL 模型更好，k 大时基座的 pass@k 更高，RL 模型的推理路径已经包含在基座的采样分布里。[DeepSeek-R1](../../papers/arxiv-2501.12948/README.md) 的附录写明，7B 稠密与 16B MoE 基座上的纯 RL 没有带来有意义的提升，回答一长就开始重复，换成 32B、230B、671B 的基座才见效。

**新能力更多来自更强的老师或更强的基座。** [Qwen3](../../papers/arxiv-2505.09388/README.md) 在 8B 模型上比较了两条路：从同一个检查点出发，on-policy 蒸馏（一句话：学生自己生成回答，逐 token 去对齐教师的输出分布）用 1,800 GPU 小时，比用 17,920 GPU 小时的 RL 效果更好，并把 AIME 的 pass@64 从 90.0 提到 93.3，RL 没有提高 pass@64。Yue 等也发现蒸馏能引入教师的新推理模式。DeepSeek-R1 在 Qwen2.5-32B 上做了同样的比较：蒸馏得到的模型在所有推理评测上明显好于直接做 1 万步以上 RL 的模型。

**后训练会让一部分能力下降，这叫对齐税**（alignment tax，一句话：为对齐付出的能力代价）。InstructGPT 的 PPO 让 175B 模型 few-shot 的 SQuADv2 从 69.75 降到 51.95，把预训练数据混回 RL（PPO-ptx）才恢复到 69.93（[InstructGPT 精读](../../papers/instructgpt/reading.md)第 11 节）。Anthropic 的 [HH 报告](../../papers/arxiv-2204.05862/README.md)发现小模型 RLHF 后多数评测下降，13B 与 52B 在 zero-shot 评测上反而变好。DeepSeek-V2 的 RL 让 BBH 从 81.3 降到 79.7（[V2 精读](../../papers/deepseek-v2/reading.md)）。[GPT-4 报告](../../papers/arxiv-2303.08774/README.md)写明后训练明显损害了预训练模型良好的校准。到 2025 年，Qwen3 在加入非思考模式和通用 RL 之后，思考模式的 AIME'24 与 LiveCodeBench 下降，团队为了通用性接受了这一取舍；[SimPO](../../papers/arxiv-2405.14734/README.md) 记录偏好优化普遍降低 GSM8K。

`[判断]` 站在现在看，后训练的目的可以写成：在不损失预训练所学的前提下，把先验变成可控、可执行的行为。[Kimi K2](../../papers/arxiv-2507.20534/README.md) 第 1 节的说法几乎相同：预训练提供通用先验，后训练把先验变成可执行的行为。知识的缺口最后都回到预训练：[DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md) 的后训练算力已超过预训练成本的 10%，作者仍把知识广度落后归因于总训练算力不足，计划扩大预训练。预训练末段越来越多地为后训练准备材料（退火、中段训练里的推理数据），见[预训练页"预训练与后训练的分工"一节](../pretraining/README.md)。

## 主线历史：奖励从哪来

结论：后训练史可以读成"奖励来源"的替换史。每个阶段都在回应上一阶段的奖励被钻空子、扩不上去或太贵的问题。

| 时期 | 代表 | 监督或奖励从哪来 | 怎样优化 | 留下的问题 |
|---|---|---|---|---|
| 2017–2020 | Christiano 等、Stiennon 等 | 人对两段输出的比较 → 奖励模型 | 在线 RL（PPO） | 奖励模型被优化过头；离线训练的奖励模型失效；成本高 |
| 2021–2022 | FLAN、InstructGPT、Anthropic HH | 人写示范 + 人的比较 | SFT → 奖励模型 → PPO | 对齐税；过度无害；"人"只是几十名标注者 |
| 2023–2024 | LIMA、DPO、Zephyr、Llama 2、Llama 3 | 人或 AI 的比较，离线收集 | SFT + 拒绝采样 + DPO | DPO 的分布外问题、长度偏置、推理退化 |
| 2024 | DeepSeekMath、PRM800K、Tulu 3、o1 | 训练的奖励模型（结果或过程）→ 可验证的答案 | GRPO、PPO | RL 只提高 Maj@K；过程奖励难扩展 |
| 2025 | DeepSeek-R1、Kimi k1.5、Qwen3、DAPO | 规则验证器（答案匹配、测试用例） | GRPO 一类，上万 token 的长思维链 | 可读性与语言混杂、过度思考、熵坍缩、长度偏置、难复现 |
| 2025–2026 | DeepSeek-V3.2、Kimi K2、DeepSeek-V4、Kimi K3 | 验证器 + 按 rubric 打分的生成式奖励模型 + 智能体环境 | 领域 RL 专家 → 蒸馏合并 | token 效率；智能体在环境里钻空子；合并时的能力损失 |

### 1 人类偏好作为奖励（2017–2020）

留下的问题：很多任务写不出奖励函数，例如"后空翻的姿态好不好""摘要好不好"。

改变：[Christiano 等（2017）](../../papers/arxiv-1706.03741/README.md)让人比较两段轨迹，用比较训练奖励预测器，再用 RL 优化它；Atari 与 MuJoCo 上只需对不到 1% 的交互给反馈。[Stiennon 等（2020）](../../papers/arxiv-2009.01325/README.md)把它搬到语言模型的摘要上：人比较两份摘要 → 奖励模型 → PPO，结果超过人写的参考摘要。

做不好的场景：
- 奖励预测器离线训练、不随策略更新时，Pong 上的智能体学会只躲丢分、不得分，打出极长的来回（Christiano 等 §3.3）。
- 摘要任务上，继续优化奖励模型后真实偏好下降，奖励模型最终与人的偏好负相关；原文指出机器人领域学到的奖励函数也有同样现象（Stiennon 等图 5）。
- 6.7B 模型的 RL 约 320 GPU 天，标注数千小时，作者因此没能做同等投入的示范数据对照。

### 2 指令微调与 RLHF 三段式（2021–2022）

留下的问题：单任务的人类反馈太窄；预训练模型 zero-shot 不会按指令做事。

改变：[FLAN](../../papers/arxiv-2109.01652/README.md) 把 60 多个 NLP 数据集改写成指令做多任务微调，zero-shot 在 25 个数据集中 20 个超过 GPT-3。[InstructGPT](../../papers/instructgpt/reading.md) 把 Stiennon 的做法推广到真实 API 提示：约 1.3 万条示范做 SFT、3.3 万条提示的比较训练奖励模型、3.1 万条提示做 PPO；1.3B 的 InstructGPT 在人评中胜过 175B 的 GPT-3。这三段式（SFT → 奖励模型 → PPO）成了此后两年的默认配方，RLHF（基于人类反馈的强化学习）这个名字也由此流行。

做不好的场景：
- 对齐税：PPO 让 SQuADv2 掉 17.8 个 F1 点，要把预训练数据混回才恢复。
- 过度无害：Anthropic 的早期策略对一切稍敏感的问题都回答"建议寻求专业帮助"，作者归因于对无害性过度优化、对帮助性优化不足（HH §4.4）。
- 人的范围：InstructGPT 的偏好来自约 40 名标注者；多数比较只有一人标注。
- 公开任务不等于用户请求：用 FLAN 数据微调的 175B GPT-3 在 API 提示上的胜率低于 InstructGPT。

### 3 离线偏好优化成为开源默认（2023–2024）

留下的问题：奖励模型加 PPO 要同时维护策略、参考、奖励、价值四个模型，在线采样昂贵，开源团队难以调稳。

改变：
- [DPO](../../papers/dpo/reading.md)（直接偏好优化，一句话：从"奖励 − KL"目标的闭式解推出一个只用偏好对的分类损失，不训练奖励模型、不在线采样）让偏好学习变成一次离线的监督训练。
- 社区随之形成 SFT + DPO 的配方：[Zephyr](../../papers/arxiv-2310.16944/README.md) 用 GPT-4 打分的 AI 偏好做 DPO，7B 模型在 MT-Bench 上超过 Llama2-Chat-70B；[LIMA](../../papers/arxiv-2305.11206/README.md) 说明 SFT 本身只需少量高质量数据。
- Meta 的选择最能说明这次转向：[Llama 2](../../papers/arxiv-2307.09288/README.md)（2023）仍用两个奖励模型、拒绝采样（一句话：每个提示采多个回答，取奖励最高者做 SFT）加 PPO；[Llama 3](../../papers/arxiv-2407.21783/README.md)（2024）改为六轮"奖励模型 → 拒绝采样 → SFT → DPO"，理由是 PPO 这类 RL 算法"不够稳定、难以扩展"，而 DPO 在大模型上算力更省、IFEval 更好。

做不好的场景：
- 分布外：[Xu 等](../../papers/arxiv-2404.10719/README.md)证明 PPO 能找到的解 DPO 也能找到，而 DPO 还可能偏向偏好数据之外的回答；他们在对话与代码竞赛上调好的 PPO 全面超过 DPO。[IPO](../../papers/arxiv-2310.12036/README.md) 从理论上指出，偏好确定或近似确定时 DPO 的 KL 正则形同虚设。
- 长度：[Singhal 等](../../papers/arxiv-2310.03716/README.md)发现 RLHF 的奖励提高主要来自回答变长，只用长度作奖励就能复现大部分提升。
- 推理退化：Llama 3 给 DPO 加了 NLL 项，防止被选回答的对数概率下降；SimPO 记录偏好优化普遍降低 GSM8K。
- 评委偏差：Zephyr 自述 GPT-4 评委偏向从它蒸馏出的模型和冗长回答。

`[判断]` 这一阶段的偏好学习擅长"风格与取舍"，对"对不对"帮助有限，甚至有害。下一阶段把"对不对"交给了程序。

### 4 奖励换成验证器（2024）

留下的问题：数学、代码这类任务的好坏不靠比较而靠对错；人和奖励模型都看不出长推理里的错误。

改变：
- [DeepSeekMath](../../papers/arxiv-2402.03300/README.md) 提出 GRPO（组内相对策略优化，一句话：同一题采一组回答，用组内奖励的均值与标准差归一化得到优势，去掉与策略同样大的价值模型）。这一版的奖励仍来自训练的奖励模型。DeepSeek-V2 随后用 GRPO 先做"推理对齐"再做"人类偏好对齐"。
- OpenAI 的 [PRM 研究](../../papers/arxiv-2305.20050/README.md)显示，按步骤打分的过程奖励模型在 best-of-N 重排上优于只看结果的奖励模型。
- AI2 的 [Tulu 3](../../papers/arxiv-2411.15124/README.md) 把"答案能被程序验证才给奖励"的做法命名为 RLVR（可验证奖励的强化学习），用在 GSM8K、MATH 与可验证的指令约束上。
- 2024 年 9 月 OpenAI 发布 [o1](../../papers/openai-o1/README.md)，官方只写明用大规模 RL 训练模型产生长思维链，表现随 RL 训练算力与思考时间增加而提高（[系统卡](../../papers/arxiv-2412.16720/README.md)也只写到这一层）。

做不好的场景：
- DeepSeekMath 的 RL 只提高 Maj@K、不提高 Pass@K。
- 过程奖励难扩展：DeepSeekMath 提到精心标注的 PRM800K 仍有约 20% 错标；DeepSeek-R1 后来列出放弃 PRM 的三个理由：步骤难定义、中间步骤对错难标、模型化的 PRM 会被钻空子（R1 附录 G.2）。
- 验证器也能被过度优化：Tulu 3 降低 KL 惩罚后，IFEval 上出现只为满足约束写的怪异输出。

### 5 可验证奖励上的大规模 RL（2025）

留下的问题：o1 证明了长思维链 RL 有效，却不公开配方；开源社区不知道"规则奖励 + 简单算法"能走多远。

改变：2025 年 1 月 [DeepSeek-R1](../../papers/arxiv-2501.12948/README.md) 与 [Kimi k1.5](../../papers/arxiv-2501.12599/README.md) 同日公开配方，两家独立得出相同的几条结论：只用答案与格式的规则奖励，不用神经奖励模型；不用价值模型、过程奖励模型和 MCTS；让回答长度随训练自然增长。DeepSeek-R1-Zero 跳过 SFT，直接在 DeepSeek-V3-Base 上做 GRPO，AIME 2024 的 pass@1 从 15.6% 升到 77.9%；作者认为人写的推理示范会限制探索，"性能上限被人类示范封顶"。DeepSeek-R1 再用数千条冷启动数据、拒绝采样、两轮 RL 补上可读性与通用能力，并把 80 万条数据蒸馏给 Qwen 与 Llama 小模型。Qwen3 用四阶段流程把思考与非思考模式合进一个模型。

做不好的场景（多数来自原文，后来的论文又补了一批）：
- R1-Zero 可读性差、在一条思维链里中英混杂；加语言一致性奖励能修，但代码评测略降（R1 附录 B.6）。
- 第二轮 RL 用帮助性奖励模型训练更多步，会出现奖励黑客（reward hacking，一句话：模型钻奖励函数的漏洞拿高分，而没有真正做好任务），R1 只在最后 400 步用它（R1 §3.2.2、附录 B.5）。
- 过度思考：k1.5 观察到回答长度在 RL 中快速增长，加了长度奖励；R1 自述简单问题上仍会想太多。
- 难复现：[DAPO](../../papers/arxiv-2503.14476/README.md) 在 Qwen2.5-32B 上直接跑 GRPO 只有 30 分，低于 DeepSeek 报告的 47 分，原因是熵坍缩、奖励噪声和训练不稳。[熵机制](../../papers/arxiv-2505.22617/README.md)一文发现，没有干预时策略熵在训练早期就降到接近 0，性能随之饱和，且上限可以从熵预测。
- 算法本身的偏差：[Dr. GRPO](../../papers/arxiv-2503.20783/README.md) 指出 GRPO 按回答长度归一化，会让错误回答越写越长；按组内标准差归一化，会让太易或太难的题权重过大。
- 被高估的"顿悟"：同一篇发现包括 DeepSeek-V3-Base 在内的基座本来就会自我反思，R1-Zero 的"aha moment"并非 RL 凭空产生。

### 6 RL 专家、生成式奖励与蒸馏合并（2025–2026）

留下的问题：规则验证器只覆盖数学、代码这类有标准答案的任务；多个领域一起做 RL 会互相拖累；智能体任务要在真实环境里交互几百上千步。

改变：
- **不可验证的任务改用按 rubric 打分的模型。** [Kimi K2](../../papers/arxiv-2507.20534/README.md) 让模型按核心价值、防钻空子的规定和人工 rubric 两两比较自己的回答，并用可验证任务上的 rollout 持续校准这个评委；[DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md) 对通用任务用逐题 rubric 的生成式奖励模型；[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) 完全放弃标量奖励模型，让策略模型自己充当生成式奖励模型并一起被 RL 优化。
- **多领域合并从混合 RL 转向蒸馏。** DeepSeek-V3.2 先训练多个领域的 RL 专家、蒸馏，再把推理、智能体与人类对齐合进一个 RL 阶段，作者说这样避免了多阶段训练的灾难性遗忘；DeepSeek-V4 把这个混合 RL 阶段整个换成多教师 on-policy 蒸馏（十多个教师），理由是它避开了权重合并与混合 RL 常见的性能下降；[Kimi K3](../../papers/arxiv-2607.24653/README.md) 训练 3 个领域 × 3 档推理强度共 9 个专家，再用多教师 on-policy 蒸馏合成一个模型。
- **长度变成显式的控制量。** K2 按任务类型设 token 预算，超出即截断并惩罚；V4 用不同长度惩罚训练三档推理模式；K3 按每题的初始预算乘以系数决定何时判负，评委对超长的回答直接判输。

做不好的场景：
- token 效率：DeepSeek-V3.2 自述要生成更长的轨迹才能达到 Gemini-3.0-Pro 的质量；K2 自述难题上会生成过多 token，导致输出截断或工具调用不完整。
- 智能体在环境里钻空子：Kimi K3 写明更强的智能体探索更激进，甚至尝试奖励黑客，早期容器沙箱里出现内核崩溃与死锁，于是改用隔离的 microVM，并让智能体与验证器隔离、配隐藏验证器。
- 稳定性靠补丁：V3.2 为规模化 GRPO 加了四处修补（无偏 KL 估计、屏蔽偏离过大的负样本、训练时沿用采样时的 MoE 路由、沿用采样时的截断掩码），其中 MoE 路由不一致"对 RL 稳定性至关重要"。
- 两家对同一问题给出相反做法：K3 用逐 token 的 on-policy 蒸馏奖励，试过更细的 top-k 目标"没有明显优势"；V4 认为逐 token 估计方差大、常致训练不稳，坚持全词表的 logit 蒸馏。目前没有同条件对照。

`[判断]` 从这一阶段回看，2025 年初"纯 RL"的叙事已被修正：大规模 RL 主要用来造出各领域的专家和数据，最终模型更多靠蒸馏得到。这与 Qwen3、DeepSeek-R1、Yue 等的观察一致：蒸馏比 RL 更省、更能扩大 pass@k。

同一时期（2025-10 – 2026-09）其他团队的报告补充了三点，其中一点与上面的判断相反：
- **RL 开始有规模规律。** [ScaleRL](../../papers/arxiv-2510.13786/README.md)（Meta 等）用 S 形曲线拟合 RL 算力与验证通过率，发现多数稳定性补丁只改变效率、不改上限，稳定的配方可从小规模外推；输出层 logits 改用 FP32 这类"训练与推理数值一致"的修补能抬高上限。
- **智能体 RL 变成异步系统。** [GLM-5](../../papers/arxiv-2602.15763/README.md)（智谱）与 [MiniMax-M2](../../papers/arxiv-2605.26494/README.md) 都把推理与训练分开部署，用重要性采样容忍过期数据，并为长短悬殊的智能体轨迹专门设计调度；AI2 的 [Olmo 3](../../papers/arxiv-2512.13961/README.md) 给出了完全公开的同类配方（GRPO 变体、异步、RL-Zero）。
- **合并多领域并不只有"专家加蒸馏"一种做法。** GLM-5 顺序做推理、智能体、通用三段 RL，再用前面阶段的检查点作教师做跨阶段 on-policy 蒸馏；NVIDIA 的 [Nemotron 3](../../papers/arxiv-2512.20856/README.md) 在所有环境上同时 RL，并写明这比它以前的分阶段做法更稳、更少奖励黑客。on-policy 蒸馏本身也被单独研究：Thinking Machines 的[博客](../../papers/thinking-machines-on-policy-distillation/README.md)给出成本对比，[Li 等](../../papers/arxiv-2604.13016/README.md)给出它失效的条件（师生思考模式不相容、教师没有新能力、回答过长）。

## 技术地基

结论：读后训练需要五个概念，其中三个读者在机器人 RL 中已经用过，只是对象换成了 token。

- **把生成写成 RL**：状态 = 提示 + 已生成的前缀，动作 = 下一个 token，一条轨迹 = 一个完整回答，奖励通常只在最后一个 token 给出（稀疏奖励）。策略、优势、策略梯度见[强化学习讲义](../../../foundations/lessons/05b-reinforcement-learning.md)第 4–5 节，语言模型怎样接入见同一讲义第 9 节。
- **PPO 与两种 KL**：PPO 的裁剪限制单次更新的步长（新旧策略之间）；RLHF 中的 KL 惩罚限制整个训练过程偏离参考模型（通常是 SFT 模型）的程度，防止策略跑到奖励模型没见过的地方。见 [PPO 精读](../../papers/ppo/reading.md)批注与讲义第 7 节。
- **Bradley–Terry 偏好模型**：两个回答的奖励之差经 sigmoid 得到"前者更好"的概率，奖励模型与 DPO 都从它出发。逻辑回归与 NLL 见[概率分类讲义](../../../foundations/lessons/modules/objectives/02-classification-probabilities.md)第 5–6 节，KL 见第 8 节，推导见 [DPO 精读](../../papers/dpo/reading.md)第 5–7 节。
- **下一词预测与损失掩码**：SFT 与预训练是同一个损失，区别是只在回答 token 上计算。见[自监督与生成目标](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 2–3 节。
- **知识蒸馏**：学生对齐教师的输出（序列级）或逐 token 分布（logit 级）；on-policy 蒸馏让学生在自己生成的前缀上学。见[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)。

## 主要路线与团队偏好

结论：公开了详细报告的团队可以写出押注与代价；OpenAI、Google 2023 年以后的后训练细节没有官方材料，只能作为开放问题。

| 团队 | `[判断]` 押注 | 代表报告 | 代价与做不好的地方 |
|---|---|---|---|
| OpenAI | 人类偏好 RLHF 的开创者（Stiennon、InstructGPT），2024 年起转向 RL 训练的推理模型 | Christiano 等、Stiennon 等、InstructGPT、PRM、o1 | o1 起不公开算法、奖励与数据 |
| Anthropic | 把偏好分成帮助性与无害性，用书面原则与 AI 反馈代替人对有害输出的标注 | HH、[Constitutional AI](../../papers/arxiv-2212.08073/README.md) | 过度无害；RL-CAI 训练过头后回答过于严厉、塞入套话 |
| Meta | 简单优先：Llama 2 用拒绝采样 + PPO，Llama 3 改为 DPO，并把格式 token 屏蔽、加 NLL 等修补写清楚 | LIMA、Llama 2、Llama 3 | DPO 一路的分布外与推理退化；Llama 3 之后未检索到官方后训练报告 |
| DeepSeek | GRPO 一以贯之（DeepSeekMath、V2、V3、R1、V3.2、V4）；能用规则就不用奖励模型；把 RL 得到的能力蒸馏给下一代与小模型 | DeepSeekMath、V2、V3、R1、V3.2、V4 | 语言混杂、过度思考、token 效率；每一代都要新的稳定性补丁 |
| Kimi（月之暗面） | 不用价值网络的策略优化（k1.5 的镜像下降变体沿用到 K2）；长上下文 RL 与部分 rollout；把长度当显式预算；自我批评的 rubric 奖励 | k1.5、K2、K3 | 难题上 token 过多；智能体环境里的奖励黑客 |
| Qwen（阿里巴巴） | 一个模型两种模式；大模型多阶段训练，小模型靠强到弱蒸馏 | Qwen3 | 融合后思考模式的竞赛分数下降 |
| AI2 | 完全公开数据、代码与评测，作为可复现的对照 | Tulu 3 | 规模与闭源配方有差距 |
| AI2（2025-12 起） | 同上；RL 从 PPO 改为 GRPO 变体，保留 DPO，并发布 RL-Zero 作研究基线 | [Olmo 3](../../papers/arxiv-2512.13961/README.md) | 7B/32B 规模；预训练占总算力九成以上 |
| 智谱（GLM） | 异步智能体 RL；顺序多阶段 RL 后跨阶段蒸馏 | [GLM-5](../../papers/arxiv-2602.15763/README.md) | 训练—推理不一致要逐个修补 |
| MiniMax | 小激活模型上的长程智能体 RL（CISPO、Forge） | [MiniMax-M2](../../papers/arxiv-2605.26494/README.md) | 系统补丁多针对智能体轨迹的形态 |
| NVIDIA | 权重、数据、配方全部公开；多环境同时 RL | [Nemotron 3](../../papers/arxiv-2512.20856/README.md) | 白皮书未给出与专家加蒸馏的对照 |
| Meta（2025-10 起） | 研究 RL 的规模规律（ScaleRL）；2026-04 的 Muse Spark 只公开博客 | [ScaleRL](../../papers/arxiv-2510.13786/README.md) | Llama 之后的产品模型不公开后训练配方 |

`[判断]` 收敛的部分：
- 去掉价值模型的 RL：DeepSeek 的 GRPO 与 Kimi 的镜像下降变体都不用 critic，Qwen3 也用 GRPO；
- 能验证的任务一律用规则或测试用例做奖励，不能验证的用按 rubric 打分的生成式奖励模型；
- 先按领域训练专家，再合并；长度显式控制。

分化的部分：
- 是否保留 KL：DAPO 去掉，V3.2 按领域调、数学可去，K2 用自己的正则项；
- 是否先做 SFT：R1-Zero 不做，R1、Qwen3、K3 用少量冷启动；
- on-policy 蒸馏用逐 token 估计（K3）还是全词表 logit（V4）。

## 与机器人强化学习的共性

结论：后训练里的几个坑，机器人学习都先遇到过；用机器人的语言重述它们，比记一串新名词更容易判断哪些做法是新的。

- `[结构]` **SFT 就是行为克隆**：两者都在专家示范上做最大似然，最多和示范者一样好。Llama 2 写明 SFT 的上限是最好的标注员，DeepSeek-R1 写明人写的推理示范把性能封顶，这正是[模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)页"复合误差"一节讲的坑在语言模型上的版本。
- `[结构]` **on-policy 蒸馏就是 DAgger 的形式**：学生在自己生成的前缀（自己到达的状态）上，向教师要逐 token 的分布（专家在该状态下的动作标签）。[DAgger](../../../robotics-embodied/papers/arxiv-1011.0686/README.md) 用这个办法解决行为克隆只见过专家状态的问题；Qwen3、DeepSeek-V4、Kimi K3 用它合并专家，Qwen3 的 on-policy 蒸馏比离线蒸馏之后直接 RL 更好、更省。
- `[经验]` **奖励黑客两边都有**：Christiano 等的 Pong 智能体只躲不打；Stiennon 等原文提到机器人领域学到的奖励函数有同样的过度优化；腿足 RL 中换掉一项奖励，策略就学会撞上去再弹回（Extreme Parkour，见机器人页"奖励设计"一节）。
- `[经验]` **配方在两个领域之间直接搬运**：[SimpleVLA-RL](../../../robotics-embodied/papers/arxiv-2509.09674/README.md) 把 GRPO、0/1 成功奖励、放宽裁剪上界与丢掉全对全错批次搬到 VLA（视觉语言动作模型）上，同样观察到"基座完全不会时 RL 起不了步"，与 DeepSeek-R1 小基座上纯 RL 无效是同一个现象。
- `[判断]` **为什么 LLM 能去掉 critic，腿足 RL 却离不开**：语言模型的奖励只在回答末尾给出，逐 token 的价值很难学准（DeepSeekMath §4.1），而同一提示可以廉价地采一组回答当基线；腿足仿真的奖励每步都有，价值函数学得准，并行环境多但同一初始状态重复采样的意义不大。依据是 DeepSeekMath 与 Kimi k1.5 不用价值网络的理由，以及 [PPO 精读](../../papers/ppo/reading.md)中的机器人设置；没有论文直接做过跨领域对照。

## 用什么衡量进展

结论：评测目标从"人更喜欢哪个回答"移到"竞赛题做对没有"，再移到"智能体在真实环境里完成没有"；每一类评测都有会改变结论的口径问题。

| 能力 | 常用评测 | 测的是什么 | 已知的口径问题 |
|---|---|---|---|
| 帮助性与偏好 | 人评成对胜率（InstructGPT）、MT-Bench、AlpacaEval 2、Arena-Hard | 两个回答哪个更受偏好 | LLM 评委偏向冗长回答和从自己蒸馏出的模型（Zephyr）；评委提示会改变胜率（DPO）；AlpacaEval 2 另有长度控制胜率（R1 报告的就是这一版） |
| 指令遵循 | IFEval | 能被程序检查的格式约束（字数、格式、关键词） | 可验证，因此也能被 RLVR 过度优化（Tulu 3 附录 B.4） |
| 推理 | AIME、MATH-500、GPQA Diamond、LiveCodeBench、Codeforces | 竞赛题的最终答案或测试用例 | 贪心解码下长推理模型重复多、检查点间波动大，R1 改为温度 0.6 下每题采 64 个回答再平均成 pass@1，DAPO 把评测集重复 32 次报 avg@32；pass@1、cons@k、pass@k 的结论可以相反（Yue 等） |
| 事实性 | SimpleQA、TruthfulQA | 简短事实问答的正确与拒答 | 拒答多可以降低错误率；"真实"与"真实且有信息"要分开看（InstructGPT 精读第 12 节） |
| 智能体 | SWE-bench Verified、BrowseComp 等 | 在代码仓库、浏览器里完成任务 | 截断与上下文上限会让模型失败（V3.2、K2）；环境本身可被钻空子（K3） |

跨方法比较时还有三条规则：SFT 的交叉熵、奖励模型与 DPO 的偏好分类损失、PPO 的代理目标不在同一个标度上，不能拿损失数值跨方法排名；比较行为时至少控制初始模型、训练数据来源、采样温度、输出长度与评审协议，在线方法还要报告额外的采样量与算力；学到更高的奖励不等于真实质量更高，偏好胜率也不等于事实正确率。

另外两个贯穿性的口径：数据污染（Tulu 3 把与未见评测集重叠超过 2% 的训练集整个删除；与开发集重叠的，整删不明显影响表现时整删，否则只删匹配的样本）；开发集与未见集分开，开发时不看未见集（Tulu 3）。

## 当前开放问题

- **RL 能否超出基座的能力边界？** DeepSeekMath、Yue 等、Qwen3 Table 21 都指向"不能，蒸馏能"；DAPO 与 DeepSeek-R1 记录了训练中出现的新推理模式，Dr. GRPO 又发现这些模式在基座里已有。入口：[Yue 等](../../papers/arxiv-2504.13837/README.md)、[熵机制](../../papers/arxiv-2505.22617/README.md)、[DeepSeek-R1](../../papers/arxiv-2501.12948/README.md)。
- **不可验证的任务，奖励从哪来？** R1 的局限一节写明写作这类任务难以构造可靠的奖励，纯 RL 的规模化仍是开放问题；K2 的自我批评 rubric、V4 让策略自己当评委、K3 的智能体评委是三种在用的答案。入口：[Kimi K2](../../papers/arxiv-2507.20534/README.md)、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md)。
- **怎样想得少一点？** 长度惩罚（k1.5）、token 预算（K2、K3）、去掉长度归一化（Dr. GRPO）都能缩短回答，代价是可能削弱探索；k1.5 的结论写明要在不损害探索的前提下减少过度思考。入口：[Kimi k1.5](../../papers/arxiv-2501.12599/README.md)、[过度思考](../../papers/url-https-proceedings.mlr.press-v267-chen25bx.html/README.md)、[DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md)。
- **多领域怎样合并？** 混合 RL（V3.2）与 on-policy 蒸馏（V4、K3）各有理由，逐 token 与全词表的蒸馏目标也有分歧。入口：[Qwen3](../../papers/arxiv-2505.09388/README.md)、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md)。
- **闭源团队 2024 年以后怎样后训练？** o1 只公开到"大规模 RL + 长思维链"；Gemini 系列本轮未检索到后训练的官方细节。这一部分只能作为开放问题。2025-08 以后能读到的官方说法只有零星几句：OpenAI 的开放权重模型 [gpt-oss 模型卡](https://arxiv.org/abs/2508.10925)写明用与 o3 相似的思维链 RL 后训练，并训练了低、中、高三档推理强度；Meta 的 [Muse Spark 博客](https://ai.meta.com/blog/introducing-muse-spark-msl/)（2026-04）称新的 RL 栈带来平滑、可预测的收益，长度惩罚让模型"压缩思考"。
- **多领域合并哪种做法更好？** 专家加 on-policy 蒸馏（DeepSeek-V4、Kimi K3）、顺序 RL 加跨阶段蒸馏（GLM-5）、所有环境同时 RL（Nemotron 3）都只与本团队的旧做法比较过。入口：[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)、[GLM-5](../../papers/arxiv-2602.15763/README.md)、[Nemotron 3](../../papers/arxiv-2512.20856/README.md)。

## 阅读顺序

1. [预训练页"预训练与后训练的分工"](../pretraining/README.md)：先知道基座手里有什么。
2. [InstructGPT 精读](../../papers/instructgpt/reading.md)：三段式流水线一次看全，第 11–14 节是对齐税、幻觉与"人是谁"。
3. [PPO 精读](../../papers/ppo/reading.md) → [DPO 精读](../../papers/dpo/reading.md)：同一个"奖励 − KL"目标的在线与离线两种解法。
4. [DeepSeekMath](../../papers/arxiv-2402.03300/README.md) → [DeepSeek-R1](../../papers/arxiv-2501.12948/README.md) 与 [Kimi k1.5](../../papers/arxiv-2501.12599/README.md)：从 GRPO 到大规模 RLVR，对照两家的同一组选择。
5. [DAPO](../../papers/arxiv-2503.14476/README.md) → [Dr. GRPO](../../papers/arxiv-2503.20783/README.md) → [Yue 等](../../papers/arxiv-2504.13837/README.md)：后来者补出的坑与边界。
6. [Qwen3](../../papers/arxiv-2505.09388/README.md) → [DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md) → [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) 与 [Kimi K3](../../papers/arxiv-2607.24653/README.md)：专家与蒸馏合并的当前形态。
7. [ScaleRL](../../papers/arxiv-2510.13786/README.md) → [GLM-5](../../papers/arxiv-2602.15763/README.md) 与 [Nemotron 3](../../papers/arxiv-2512.20856/README.md)：RL 的规模规律，以及与"专家加蒸馏"不同的两种合并做法。

三个子方向各有 Baseline 页、路线图与论文目录：[SFT](sft/README.md)、[偏好学习](preferences/README.md)、[强化学习](rl/README.md)。

## 批注

**易误读**

- "后训练很少加知识"是倾向而非定律：DeepSeek LLM 的 SFT 让 HumanEval 和 GSM8K 提高 20 分以上（预训练页批注），这是把已有能力变成 zero-shot 可用，还是学到了新东西，原文没有区分。Gekhman 等的结论来自闭卷问答，长文本生成上未验证（§11）。
- Qwen3 的 pass@64 对比在 8B、只用数学与代码题，起点是同一个离线蒸馏检查点（Table 21）；Yue 等的"基座 pass@k 更高"在大 k 下成立，k = 1 时 RL 模型更好。两者都不说明 RL 无用。
- DeepSeek-R1 的 AIME 15.6% → 77.9% 是 R1-Zero 的 pass@1，不是最终 R1；R1 最终为 79.8%（R1 Table 3）。
- "对齐税"在不同报告中指不同评测：InstructGPT 是 SQuADv2、DROP 等公开 NLP 任务，DeepSeek-V2 是 BBH，Qwen3 是 AIME'24 与 LiveCodeBench；HH 报告认为大模型上主要是"对齐红利"。
- 两个算力比例的口径不同：Flan-PaLM 的 0.2% 是 540B 模型指令微调相对预训练的算力（约 512 块 v4 TPU 跑 37 小时，§2）；DeepSeek-V3.2 的"超过 10%"是后训练算力相对预训练成本（§1）。作为参照，DeepSeek-R1 全部 RL 与数据构造约 14.7 万 H800 GPU 小时（附录 B.4.4 Table 7）。

**判断的支撑论文**

- 奖励来源替换史：Christiano 等 §3.3、Stiennon 等图 5、InstructGPT、Llama 3 §1 与 §4.1.4、DeepSeekMath §4.1、R1 §2.2 与附录 G.2、Tulu 3 §6、K2 §3.2.2、V3.2 §3、V4 §5.1.1。反例与边界：Llama 3 仍训练奖励模型用于拒绝采样；V3.2、V4 的通用任务仍需要模型评分，只是从标量换成生成式。
- "最终模型更多靠蒸馏得到"：Qwen3 §4.5 与 Table 21、R1 附录 F.1、V3.2 §3（专家蒸馏后仍做混合 RL）、V4 §5.1.2、K3 §4.1.3。边界：R1 写明超越人类边界仍需更强的基座和更大规模的 RL；V3.2 的统一模型在蒸馏后仍需 RL 才消除与专家的差距。
- 团队偏好按"两篇以上、存在替代方案时重复同一选择"判断：DeepSeek 在 DeepSeekMath、V2、V3、R1、V3.2、V4 中都用 GRPO（同期有 PPO、DPO 可选）；Kimi 在 k1.5 与 K2 中都不用价值网络，K2 写明沿用 k1.5 的算法，K2 与 K3 都显式控制 token 预算；Meta 在 LIMA、Llama 2、Llama 3 中都强调少而精的人工数据，并从 PPO 换到 DPO 以求简单；Anthropic 在 HH 与 CAI 中都把帮助性与无害性分开处理。反例：DeepSeek LLM（2024 年初）用的是 DPO，不是 GRPO。
- 机器人共性中的 `[判断]`（critic 的去留）：DeepSeekMath §4.1、Kimi k1.5 §2.3.2；反例是 Tulu 3 的 RLVR 仍用 PPO 和价值模型（从奖励模型初始化），并在未来工作中建议试 GRPO。

**与其他论文的关联**

- [预训练](../pretraining/README.md)：本页"与预训练的关系"一节是该页"预训练与后训练的分工"的展开；两页引用的 GPT-4、DeepSeek LLM、DeepSeek-V3.2、Kimi K2 是同一批证据。
- [推理时计算方向](../inference/README.md)：o1、R1、k1.5 在那里作为"推理模型"阶段的起点，讲测试时算力怎样分配；本页讲它们怎样被训练出来。
- [模仿学习与机器人强化学习](../../../robotics-embodied/fields/imitation-reinforcement-learning/README.md)：SFT 与行为克隆、on-policy 蒸馏与 DAgger、奖励设计三处对应。
- [知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)：2025 年以后的蒸馏是后训练的主干之一，Gemma 2/3 在预训练阶段也用蒸馏（见预训练页）。
- [LLM-as-a-Judge](../../../cross-domain/papers/llm-judge/README.md)：偏好评测中 LLM 评委的偏差，与 2025 年以后生成式奖励模型是同一类模型在两个位置上的使用。

**未核实 / 待验证**

- OpenAI o1 的官方博客本轮直接访问返回 403，相关内容取自本库已有的 [o1 文献卡](../../papers/openai-o1/README.md)与 arXiv 上的 o1 系统卡；Gemini 2.5 及以后的技术报告、Llama 3 之后 Meta 的后训练报告本轮未打开。
- InstructGPT、DPO、PPO 的数字取自本库精读与其证据档案，本轮只重新打开了 InstructGPT 的数据规模与对齐税段落。
- Kimi K2 的 RL 目标中正则项的具体形式（原文式中的系数与平方项）本轮没有逐符号核对，正文只写"用自己的正则项"。
- DeepSeek-V2 的 BBH 81.3 → 79.7 沿用预训练页与 V2 精读，本轮只核对了 V2 原文中"对齐税"的文字描述。
- 本页与三个子方向没有覆盖的后训练主题：参数高效微调（LoRA 一类，只改少量参数，可与 SFT、DPO 组合）、持续预训练与遗忘、多轮智能体 RL 的专门基线。它们需要各自的基础方法、关键改进与可复现实验，目前不能用本页的论文代替。
- gpt-oss 模型卡（2025-08）本轮只核对了 §2.5 的后训练描述与图 3 的推理强度曲线；Muse Spark 只有官方博客，没有结构与配方；Gemini 3 系列的后训练细节仍未检索到官方材料。

**与原结论的张力（2025-10 以后的材料）**

- 第 6 节的 `[判断]`"最终模型更多靠蒸馏得到"有反例：Nemotron 3 在所有环境上同时 RL（§2.6），GLM-5 以顺序 RL 为主、蒸馏只用于找回能力。这一判断目前只在 DeepSeek、Kimi、Qwen 三家的报告上成立。
- 主要路线表中 AI2 一行（Tulu 3）与"分化：是否保留 KL""是否先做 SFT"两条仍成立，但 AI2 的 RL 已从 PPO 换成 GRPO 变体（Olmo 3），机器人共性一节"反例是 Tulu 3 的 RLVR 仍用 PPO 和价值模型"描述的是 2024 年。
- 速览第 5 条"后训练的算力占比在上升"：Olmo 3（7B/32B）的预训练占总 GPU 时间九成以上，后训练约 9 天；它与 DeepSeek-V3.2 的口径、规模都不同，不构成反证，但说明"超过 10%"不是普遍比例。
