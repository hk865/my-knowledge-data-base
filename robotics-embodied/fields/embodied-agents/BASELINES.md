# 具身 Agent 的基线

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md) · [讲义](../embodied-agents.md)

## 基线是谁、为什么是它

- **[SayCan](../../papers/saycan/reading.md)（2022）。** 它定义了"大模型做高层、技能做底层"的最小接口：输入是自然语言指令、已执行的步骤和当前观测；高层是冻结的 LLM，对技能库里每个技能的文字名称打"有用"分；中间层是每个技能的价值函数，打"现在做得到"分；两者相乘选下一个技能执行，循环到 LLM 选出"结束"。评估把规划成功与执行成功分开报告。
- **[ReAct](../../../cross-domain/papers/react/reading.md)（2022）。** 不限于机器人的对照：推理、行动、观察交替写进同一段上下文，是闭环 Agent 的最小形式，见[跨方向 Agent 页](../../../cross-domain/fields/agents/README.md)。

两者合起来给出后续工作的参照：SayCan 回答"选哪个技能"，ReAct 回答"执行后怎样把结果读回来"。

## 基线的结构拆分

| 部件 | SayCan 中的形态 |
|---|---|
| ① 高层规划器 | 冻结的 PaLM / FLAN，按少样本提示给技能名称打分 |
| ② 技能库与技能接口 | 551 个用行为克隆或 RL 训练的技能，接口是一个文字名称 |
| ③ 可行性与接地 | 每个技能的价值函数，估计当前状态下的成功概率 |
| ④ 反馈、验证与恢复 | 没有：开环执行，默认技能成功 |
| ⑤ 记忆与状态 | 只有已执行步骤的文字历史 |
| ⑥ 评估 | 101 条指令，规划成功与执行成功分开 |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| ⑥ 评估 | 长程家务基准，端到端基线 | [ALFRED](../../papers/arxiv-1912.01734/README.md) | 暴露端到端模型在长程任务上近乎为零（未见 0.4%）；仿真 |
| ④ 反馈 | 成功检测、场景描述、人类回答写回提示 | [Inner Monologue](../../papers/arxiv-2207.05608/README.md) | 扰动下 30.8% → 60.4%；检测器的错误会以事实身份进入提示 |
| ④ 反馈 | 推理—行动—观察交替 | [ReAct](../../../cross-domain/papers/react/reading.md) | 文本环境里的最小闭环；观察的可靠性由环境保证 |
| ① 高层 + ④ | 少样本 kNN 选示例，失败时带物体列表重规划 | [LLM-Planner](../../papers/arxiv-2212.04088/README.md) | 100 条示例接近全量数据的 HLSM；受低层检测限制 |
| ② 技能接口 | LLM 直接写调用感知与控制 API 的代码 | [Code as Policies](../../papers/arxiv-2209.07753/README.md) | 技能可组合、可表达空间推理；受限于 API 与原语 |
| ② 技能库 | 把验证过的代码存为技能，自动课程 | [Voyager](../../../llm/papers/arxiv-2305.16291/README.md) | 开放世界中持续积累；只在 Minecraft，无视觉 |
| ② + ③ | LLM+VLM 组合三维价值图，运动规划器零样本合成轨迹 | [VoxPoser](../../papers/arxiv-2307.05973/README.md) | 不需要预定义原语，88% 对 24%；接触丰富任务仍需动力学模型 |
| ② 技能 → 模型 | 动作当词元，技能收进一个 VLA | [RT-2](../../papers/arxiv-2307.15818/README.md) | 网络知识迁移到动作；长程任务仍需分层 |
| ① 高层（训练） | 同一模型先预测语义子任务，再出动作块 | [π0.5](../../papers/arxiv-2504.16054/README.md) | 新家庭中的长程任务；需要大量异构数据 |
| ① 高层（训练） | VLM 用合成对话数据训练，输出语言指令给 π0 | [Hi Robot](../../papers/arxiv-2502.19417/README.md) | 处理开放指令与中途纠正，比 GPT-4o 高层高约 40%；无记忆 |
| ⑥ 评估 | 高层与低层、六个能力子集分开测多模态大模型 | [EmbodiedBench](../../papers/arxiv-2502.09560/README.md) | 量化"高层够用、低层不够"；只在仿真 |
| ③ + ④ | 技能调用作为提案：前提检查、有限片段执行、验证 | [EmbodiedSkills](../../papers/embodiedskills/reading.md) | 去掉验证 86.2% → 48.2%；底层逐任务微调，记忆任务 12.5% |
| ② 技能库 | 保存实际执行过的代码与视觉触觉经验，选择后适配 | [RoboSkill](../../papers/roboskill/reading.md) | 首回合成功与用时改善；跨任务迁移有时变差 |
| ⑤ 记忆 | 四种记忆存储，在线编辑、离线整理 | [MEMORA](../../papers/memora/reading.md) | 记忆支持规划；全量 QA 不优于最强基线，真机只定性 |
| ⑤ 记忆 + ④ | 三维层级场景图记忆 + Agent 运行时 + 多类技能 | [HoloAgent-0](../../papers/holoagent-0/reading.md) | 物体导航 82.6%；长程任务只有定性演示 |
| ① + ③ + ④（2026 年补充） | 具身推理模型作编排器，以工具调用调 VLA；按 VLA 训练指令的摘要判断可行性，另有安全工具负责停机 | [Gemini Robotics 1.5](../../papers/arxiv-2510.03342/README.md)、[Gemini Robotics 2 安全评测](../../papers/gemini-robotics-2-safety/README.md) | ER 1.5 编排总失败率 22%（通用 Gemini 2.5 Flash 44.5%）；可行性判断 62.0% → 95.8% / 人员接近监测的漏报与误报不可兼得，多轮重规划常失败 |
| ⑤ 记忆（2026 年补充） | 高层策略自己改写一段文字摘要作长时记忆，配合视频短时记忆 | [MEM](../../papers/arxiv-2603.03596/README.md) | 约 15 分钟的真机任务 / 只在一个回合内 |
| ② 技能接口 | 用人类视频作为新任务说明，预测机器人视频再解码动作 | [Zero-WAM](../../papers/zero-wam/reading.md) | 未见任务 47.0%；属于[世界模型方向](../world-models/README.md)的动作生成底座 |

### 通用模型与动作模型之间的可替换接口

这张表把“高层是否冻结”与“干预发生在哪里”分开；先选需要改的接口，再读具体模型。

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| ① + ② + ⑤ 编排与经验 | 现成 Agent 调用 VLA 原语、解析工具并使用执行经验 | [HarnessVLA](../../papers/arxiv-2607.08448/reading.md) | 复用通用模型与已有技能 / 工具覆盖、历史质量与调用预算影响结果 |
| ② + ③ 代码与物理接口 | 冻结 Agent 生成控制程序，或通过有类型参数调用固定规划模板 | [Agent as Policy](../../papers/arxiv-2609.12541/README.md)、[MCP + MTC](../../papers/arxiv-2608.29379/README.md) | 将模型推理接入物理计算 / 需准备接口、状态机或平台约定 |
| ② + ④ 测试反馈 | 在局部执行或仿真后修改程序；ENPIRE 还组织低层策略训练 | [Local Coding](../../papers/arxiv-2609.26499/README.md)、[SimEX](../../papers/arxiv-2609.38982/README.md)、[ENPIRE](../../papers/arxiv-2606.19980/README.md) | 不更新通用模型参数也能适配 / 试验次数、人工重置、仿真差距仍有成本 |
| ③ 初始环境 | VLM 决定移除对象，经 SAM3、三维定位、IK 整理后再交给 VLA | [StageCraft](../../papers/arxiv-2603.20659/README.md) | 减少干扰与遮挡 / 需成功上下文与移动对象的可行性，低层先经任务微调 |
| ② 动作生成 | VLM 生成可微奖励或粗方向，以数值工具引导动作生成 | [VLS](../../papers/arxiv-2602.03973/reading.md)、[FRS](../../papers/arxiv-2606.13675/README.md) | 更靠近连续动作的接口 / 受奖励、几何和动作先验限制 |
| ② + ③ 候选搜索 | 黑盒奖励下迭代变异，或仿真结果与语言计划对齐后筛选 | [VLA-Pilot](../../papers/arxiv-2511.14178/reading.md)、[SEAL](../../papers/arxiv-2510.16281/README.md) | 2025 年的两种前史；一个优化候选，一个验证候选 / 额外延迟与候选覆盖限制 |
| ③ 专用动作工具 | 学习代理、相对动作critic，或组合世界模型与冻结评分器 | [PPS](../../papers/arxiv-2609.09148/README.md)、[VLA-ATTC](../../papers/arxiv-2605.01194/README.md)、[ViTaL](../../papers/arxiv-2606.14981/README.md) | 可减少昂贵搜索或改善候选评价 / 有专门训练条件，完整 LLM Agent 效果需另测 |
| ① + ④ 训练型对照 | 修改 π0.5 高层并训练 Florence-2 critic，按事件重规划 | [Critic in the Loop](../../papers/arxiv-2603.05185/README.md) | 更密集的进度与异常监控 / 需任务与恢复示范，区别于冻结通用模型外挂 |

接口的前向流程与手算见[动作模型干预讲义](action-model-intervention.md)；领域问题链见[入门页](README.md)。

## 批注

**易误读**

- 表中数字的口径（扰动设置、条件子集、逐任务微调）见[入门页](README.md)批注与各篇精读。

**与其他论文的关联**

- 本方向收录的 LLM 侧参照：[GPT-3](../../../llm/papers/gpt3/README.md) 提供少样本提示的基础；[SWE-agent](../../../llm/papers/arxiv-2405.15793/README.md) 与 [Recursive Introspection](../../../llm/papers/arxiv-2407.18219/README.md) 是软件与文本任务里的接口设计和自我改进，可与部件②、④对照。
- 导航中的同构做法（VLM 给地标、前沿打分再交给导航模型）见[导航与规划的基线](../navigation-planning/BASELINES.md)。
- 本表各行的原文出处见 [synthesis.csv](synthesis.csv)。
