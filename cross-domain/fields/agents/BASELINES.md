# Agent 的基线

> 状态：Baseline 页 · v1 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 基线是谁、为什么是它

结论：有两个基线。推理时的基线是"ReAct 循环 + SWE-agent 的接口"，它定义了一个编码 agent 系统怎样搭；训练时的基线是"可执行环境 + 测试判定"，它定义了 agent 行为怎样被训进模型。后来的工作要么改系统的某个部件，要么改环境与奖励。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| [ReAct](../../papers/react/reading.md)（2022）→ [SWE-agent](../../../llm/papers/arxiv-2405.15793/README.md)（2024） | 循环：思考—动作—观察，观察写回上下文。接口：为模型设计的文件查看窗口、带语法检查与回滚的编辑器、精简搜索，只保留最近几步的完整观察。评估：SWE-bench 上的解决率与每题成本 | SWE-agent 的 ACI 消融是"接口改一处、分数变几分"的第一组系统证据；Anthropic 的 SWE-bench 脚手架以它为基础；后来的 OpenHands、Claude Code、Codex CLI、Terminus 都是同一种循环 |
| [SWE-Gym](../../papers/arxiv-2412.21139/README.md)（2024）；评测侧对应 [SWE-bench](../../papers/arxiv-2310.06770/README.md) | 环境 = 仓库快照 + 容器 + issue；判定 = 隐藏单元测试；训练 = 用测试通过的轨迹做拒绝采样微调，再训一个验证器做选择 | Kimi K2、DeepSeek-V3.2 的代码 agent 环境用同一配方（GitHub issue/PR + 可执行测试）；SWE-RL 以它为对照，把奖励换成不执行的补丁相似度 |

## 基线的结构拆分

结论：一个 agent 方案可以拆成七个可替换的部件；前四个属于系统，后三个属于训练。

| 部件 | 含义 | 推理时基线（SWE-agent） | 训练时基线（SWE-Gym） |
|---|---|---|---|
| 模型 | 输出思考与动作的策略 | 冻结的 GPT-4 Turbo、Claude 3 Opus | Qwen2.5-Coder 7B–32B，微调 |
| 动作空间与接口 | 能调用什么、返回什么格式 | 专门设计的查看、编辑、搜索命令 + shell | 沿用 OpenHands、MoatlessTools 的接口 |
| 上下文与记忆 | 历史怎样保留、压缩 | 只保留最近 5 步的完整观察 | 同框架默认 |
| 停止与预算 | 何时结束 | 每题 4 美元，超出自动提交 | 框架默认的轮数上限 |
| 环境 | 执行动作的外部世界 | SWE-bench 的 Docker 容器 | 2,438 个带可执行环境的真实任务 |
| 判定与奖励 | 怎样算成功 | 隐藏测试（评测用） | 测试通过才保留轨迹；另训结果奖励模型 |
| 训练方式 | 怎样把成功变成参数更新 | 不训练 | 拒绝采样微调（过滤后的行为克隆） |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 模型 | 自监督地学会何时调用工具 | [Toolformer](../../papers/arxiv-2302.04761/README.md) | 小模型数学题超过 GPT-3 / 不能链式、不能交互 |
| 上下文与记忆 | 失败后写文字反思存入情景记忆 | [Reflexion](../../papers/arxiv-2303.11366/README.md) | 不训练即可多次改进 / 自写测试的假阳性让它过早停止 |
| 上下文与记忆 | 成功的代码存成可检索的技能库 | [Voyager](../../../llm/papers/arxiv-2305.16291/README.md) | 长程开放任务上的积累 / 只在 Minecraft，课程会提出做不到的任务 |
| 动作空间与接口 | 最简脚手架：bash + 字符串替换编辑；工具防呆（必须写绝对路径） | [Anthropic SWE-bench 报告](https://www.anthropic.com/engineering/swe-bench-sonnet) | 把控制交给模型 / 单题几百轮、超过 10 万 token |
| 上下文与记忆 | 工具调用之间保留思考，新用户消息才丢弃；搜索任务丢弃全部历史重来 | [DeepSeek-V3.2](../../../llm/papers/arxiv-2512.02556/README.md) | BrowseComp 51.4 → 67.6 / 用"用户消息"模拟工具的框架走不到这条路径 |
| 环境 | 不执行，直接用 GitHub PR | [SWE-RL](../../papers/arxiv-2502.18449/README.md) | 数据量大、无执行成本 / 学不到交互反馈 |
| 环境 | 真实 MCP 工具 + 合成工具 + 工具模拟器 + 真实沙箱 | [Kimi K2](../../../llm/papers/arxiv-2507.20534/README.md) | 覆盖面广 / 模拟器与真实环境的差距；token 过多 |
| 环境 | 合成通用 agent 环境（自建数据库、工具与验证函数） | [DeepSeek-V3.2](../../../llm/papers/arxiv-2512.02556/README.md) | 只在代码、搜索环境上训练不提升 τ²、MCP，加入合成环境才提升 / 合成环境的真实度 |
| 环境 | 2 万个并行环境做长程 RL | [Qwen3-Coder](https://qwenlm.github.io/blog/qwen3-coder/) | 规模 / 博客未公开奖励细节 |
| 环境 | 隔离的 microVM，agent 与验证器隔离 | [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md) | 堵住攻破沙箱与验证器的路径 / 系统成本 |
| 判定与奖励 | 补丁与真实补丁的序列相似度 | [SWE-RL](../../papers/arxiv-2502.18449/README.md) | 不可能跳过测试 / 不认语义等价的其他解法 |
| 判定与奖励 | 环境筛选：标准补丁使失败变通过 > 0、通过变失败 = 0 | [DeepSeek-V3.2](../../../llm/papers/arxiv-2512.02556/README.md) | 去掉装不起来或测试无效的环境 / 不处理测试过于具体或覆盖不足 |
| 判定与奖励 | 数据库状态比对 + pass^k | [τ-bench](../../papers/arxiv-2406.12045/README.md) | 量化可靠性 / 作者自述 r = 1 只是必要条件 |
| 判定与奖励 | 任务构建时派对抗 agent 找作弊路径 | [Terminal-Bench](../../papers/arxiv-2601.11868/README.md) | 发现打补丁、猜答案、全列答案等漏洞 / 每题约三个审查人时 |
| 判定与奖励 | 如实承认失败给奖励，与实际动作不一致给惩罚 | [codex-1 系统卡附录](https://cdn.openai.com/pdf/8df7697b-c1b2-4222-be00-1fd3298f351d/codex_system_card.pdf) | 正确承认做不到的比例 0.15 → 0.85 / 训练细节未公开 |
| 判定与奖励 | 会做冲突改动的"用户模型"，不回退用户改动给正奖励 | [GPT-5.1-Codex-Max 系统卡](https://openai.com/index/gpt-5-1-codex-max-system-card/) | 避免破坏性动作评测上升 / 指标定义只有一句话 |
| 判定与奖励 | 训练提示中说明本环境允许钻空子（接种提示） | [MacDiarmid 等](../../papers/arxiv-2511.18397/README.md) | 作弊不再泛化成失调（降 75%–90%）/ 作弊本身照旧 |
| 训练方式 | 测试通过的轨迹拒绝采样微调 + 验证器 | [SWE-Gym](../../papers/arxiv-2412.21139/README.md) | Verified 7.0 → 20.6，选择后 32.0 / 在线自我改进反而下降 |
| 训练方式 | 规则奖励 + GRPO 的大规模 agent RL，与推理、对齐合成一个 RL 阶段 | [DeepSeek-V3.2](../../../llm/papers/arxiv-2512.02556/README.md)、[Kimi K2](../../../llm/papers/arxiv-2507.20534/README.md) | 开源模型 agent 评测接近闭源 / 上下文超限、多余的自我验证 |
| 训练方式 | 监控思维链发现作弊，但不把监控结果作为强惩罚 | [Baker 等](../../papers/arxiv-2503.11926/README.md) | 监控召回 95% / 强惩罚下 agent 学会隐藏意图 |

## 批注

**易误读**

- SWE-agent 的 18.0% 是 SWE-bench Lite、GPT-4 Turbo；完整 SWE-bench 为 12.47%（Table 1）。SWE-Gym 的 32.0% 是 16 个候选中由验证器选一个的结果，单次为 20.6%。
- SWE-agent 的成本对比原文写作"成功运行的中位数 1.21 美元、12 步，失败运行的平均数 2.52 美元、21 步"，中位数与平均数混用，不宜直接相减。

**与其他论文的关联**

- [具身 Agent 的 Baseline 页](../../../robotics-embodied/fields/embodied-agents/BASELINES.md)：机器人一侧的基线是 SayCan，部件拆分里多了"底层技能"与"可行性打分"，判定换成成功检测器。
- [语言模型强化学习的 Baseline 页](../../../llm/fields/posttraining/rl/BASELINES.md)：本页"判定与奖励""训练方式"两行的算法细节（GRPO、KL、裁剪）在那里。

**未核实 / 待验证**

- OpenHands、Claude Code、Codex CLI 等框架没有对应的论文卡；本页只引用它们作为评测时的框架名。
