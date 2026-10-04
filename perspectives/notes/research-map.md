# 研究兴趣与论文知识库

## 当前目录与公开状态（2026年10月3日）

公开仓库保存学术内容、目录与官方来源链接。私有Page地址、编号、版本及内部同步基线保留在私下，不进入公开导出；Page内容仍受原账户与协作者权限控制。

当前合并目录为199项资源（194篇论文、2篇官方技术报告、1个代码仓库、2篇官方博客），另有34项待核实线索，不计入已核验资源。按[全库分层导航](../../README.md)进入基础模块、LLM、多模态、机器人与跨方向内容；单篇文件夹分别保存原创讲解、来源、配图与证据，论文原文提供官方链接，本次不上传或镜像PDF。下文带日期的数量与状态是当时记录，不代表当前库的总量。

[完整论文目录](../../docs/paper-catalog.md) · [学术内容索引](../../index.json) · [同步约定](../../SYNC.md) · [今日短报](../../daily/2026-10-03.md)


以可检索的聊天为起点，提炼研究兴趣、未解决问题与实验约束，再据此筛选论文。分类随证据演变；模型训练与多模态、机器人与具身智能只是初始入口，不限定未来方向。

## 本轮新增问题与导读

[2026年10月3日短报](../../daily/2026-10-03.md) · [大小模型草拟与验证机制导读](../../llm/fields/inference/draft-verification-guide.md)。33篇既有单篇讲解保留；本轮新增文献卡与方向机制导读不冒充单篇全文精读。

## 阅读入口

- [模型训练与多模态](model-training-multimodal.md)

- [机器人与具身智能](robotics-embodied.md)

两页是当前有初始论文卡的入口。下方兴趣地图覆盖更广的主题；后续按真实问题与材料密度拆分，不将你的兴趣硬塞进两类。

## 研究画像与分类

2026年10月3日问题细化：大小模型协作需要区分精确目标分布验证、近似质量判断与关键token/片段接管；四足学习关注持续受阻、风险敏感策略与恢复控制，但尚未确认根因；Agent可靠性需把上下文保持、性质测试和执行轨迹验证分开。本次按官方身份与方法证据补文献，不据此宣称完成新实验或新增全文精读。

明确需求：先持续整理聊天并提炼兴趣，再提供个性化学术信息与云端知识库；模型训练涵盖大语言模型和多模态，机器人涵盖传统感知、导航与运动控制。每天一份合并短报，需要时再做专题总结。

初始画像来自此前对话的整理，具体优先级仍待你确认：模型训练包括架构与注意力、KV cache 与压缩、数据筛选与合成、课程学习、预训练与 SFT 与 RL 的关系；具身智能包括 VLA、VLN、世界模型、四足 RL 周期控制、非对称 PPO 与教师学生蒸馏、深度与 IMU、定位与 SLAM 与导航。

兴趣判断分三级：反复关注须有多次独立讨论支持；探索性问题保留为候选，不自动升级为长期方向；明确选定课题须有你的直接确认。现有主题是初始画像，仍需补齐聊天来源和时间线，未据此判定任何正式课题。

## 记录与证据规则

每篇论文记录标题、首次公开年份、原文链接、arXiv 或 DOI、问题、方法、证据边界、与你的关联和阅读状态。按不带版本号的 arXiv ID 去重；期刊 DOI 与预印本核实对应后合并，跨主题只交叉引用。

论文主张和实验结果标注来源；关联分析和可尝试的实验明确标为判断或建议。只保存原文链接与原创摘要，不复制受版权保护的全文。当前首批条目已核对官方 arXiv 摘要和元数据，尚未完成逐篇全文精读或独立复现；不把你的阅读状态推定为已读。

## 更新范围与待确认项

可整理当前工具能够检索到的历史聊天和新讨论，但不能保证覆盖完整聊天档案，也不能保证实时发现每条新消息。找不到来源时标注缺口，不补写成既定事实。

待确认：近期目标、机器人与传感器平台、算力与数据条件，以及理论理解、选题、复现的优先级。每日合并短报已启用，每天约 UTC 08:00（北京时间16:00），采用一小时灵活执行窗口；需要时再做专题总结。定时任务独立运行，未附加到本页的任务面板。

建立日期：2026年9月30日

## 聊天来源兴趣地图

以下依据可检索的历史聊天摘要形成，日期为 2026年；当前未取得可直接打开的原会话链接，因此是可修订的证据线索，不是完整档案。记录结构为主题与子问题、用户证据与日期、证据类型、状态、演变修订、下一问题及检索词。助手建议不等于用户已选方向。

### 项目中

**Agent 系统与协作工程**：9月27日你明确说已重构为图驱动多 Agent 平台，探索通信、编排与 Repo 管理；Architecture Graph 与 Task Graph 管理分工和上下文。演变：ContextCompiler 已不是核心，转向长上下文和粗粒度图搜索。证据类型：用户陈述的项目事实。下一问题：图结构如何改善可靠性和协作成本？检索词：multi agent orchestration、graph workflow、repository agents。

### 反复深入的兴趣

**模型学习机制**：8月29日围绕预训练与后训练、Scaling Law、SFT、RL、DPO、轨迹和结果奖励、数据闭环连续追问，并联系机器人 RL。证据类型：用户深入问题；不推断你正在训练大模型。下一问题：不同学习阶段改进能力的机制和数据需求是什么？

**推理时计算与能力激活**：9月4日多路径与多 Agent 搜索，9月10日 token efficiency、CoT 和 test time compute，9月23日廉价模型递归思考及环境上下文。下一问题：固定成本下，搜索、长上下文和多 Agent 如何公平比较？

**知识检索与上下文**：9月22日你强调 Jev 在语言块中判断最贴合 topic，不应与 RAG 对立；9月23日继续讨论历史运行、知识库和上下文。项目相关兴趣，可与 Agent 主题交叉。下一问题：哪些信息应检索、缓存或直接进入上下文？

**传统机器人系统**：1月7日 IMU 纯惯性里程计与 EKF，8月16日 SLAM、规划、传感融合、PID 与 LQR，8月22日四足 PPO、CPG、课程与 sim to real，9月29日 FAST LIVO2 的 ROS2 移植。证据类型：问题与工程经历；实验以仿真为主、真机较少。下一问题：感知误差和时延如何传递到导航与控制？

**VLA 与具身基础模型**：8月24日 physical prompting、GEN 1.5 与公开 recipe 边界，8月29日 Zero WAM、Agent 与 ICL，你提到与自己课题相关；9月11日已有 VLA 手册。部分课题关联已明确，具体选题仍待确认。下一问题：公开证据究竟支持哪些架构、数据与能力判断？

**世界模型与结构化表征**：9月4日 object centric、3D 几何和可执行场景，9月23日 latent 等变性、可干预性、动力学与复用。关注表征是否具有结构，而非只看 benchmark。下一问题：如何区分任务有用特征、预测表征、结构表征与因果物理表征？

### 探索性线索

**跨领域工程 Agent**：9月10日讨论编译器、机器人、安全、HPC 和软硬件边界的共通结构。暂为探索；助手提出的 Engineering Agent Harness 不记录成你已采纳的项目。

**认知与可信解释及 AI 社会影响**：8月25日集中讨论 CoT 忠实性、事后合理化、split brain、偏见、跨文化语料与 AI 中介。现有证据集中单日，不据此推断政治立场或长期主线。

**生物计算**：9月3日你主动提供 DOI，追踪脑组织闭环感觉运动学习。单一研究线索；助手扩展的 organoid、wetware 等不视为你的研究承诺。

### 明确选定课题与待核实

目前明确的是图驱动多 Agent 项目正在推进，以及部分具身讨论与你的课题相关。尚不足以给其他兴趣贴上已立项、论文选题或实施中的标签。新证据优先更新状态与否定修订，再决定是否新增专题页。

## 每日短报

### 2026年9月30日

首次整理：形成跨 Agent、模型学习、推理计算、上下文、传统机器人、具身模型、世界表征和探索性主题的兴趣地图；保留原有 VLA 手册，建立 6 篇基础论文卡。首批论文用于建立共同参考，不能视为覆盖全部兴趣或最新进展。

后续每份合并短报先记录新增聊天带来的兴趣或问题变化，再给少量相关论文与推荐理由；无显著变化时保持简短。每条区分原文证据、关联判断和待验证假设。

## GitHub 与导出

本页面仍为私有；你已确认将面向你的完整学术知识库发布到公开仓库 [my knowledge data base](https://github.com/hk865/my-knowledge-data-base)。首次发布已核验：[提交 ba96193](https://github.com/hk865/my-knowledge-data-base/commit/ba96193055e928fb60962f5b0e1742a984a50e91)。公开仓库中的内容可被任何人访问。

每日合并更新任务也会同步 GitHub，保留你的手动修改；遇到无法安全合并的冲突时通知你，不覆盖冲突内容。知识库更新按每日同步流程处理；每次发布状态以实际核验的 GitHub 提交为准。

已提供的 ZIP 包含 Markdown 与 JSON、CSV 索引，是2026年9月30日的独立快照，不会随云端页面或 GitHub 自动更新。

## 聊天论文提取与细分类

2026年9月30日更新：已从可检索历史聊天恢复并核验 96 条独立资源链接，包括 95 篇论文和 1 个代码仓库。其中 1 条为用户提供的 Zero WAM，95 条由聊天中的助手提供；助手曾经推荐不等于你已经认可、读过或选定课题。

合并去重后共有 117 条资源：包含上述聊天来源、16 条已有手册参考及6条初始推荐；来源集合存在重叠，不能直接相加。另有18条候选因名称、链接或身份不足而暂不入已核验清单。本次核验题名、标识与原始链接，不等于全文精读、复现或结果复核。聊天来源是检索摘要，没有可打开的原会话链接。

分类按研究问题细分：大语言模型包含预训练、后训练的 SFT、偏好学习与 RL，以及架构效率和推理时计算；多模态包含视觉表征、图文对齐、VLM、视觉生成与世界模型；机器人包含感知融合、定位建图、导航规划、运动控制与具身策略。Agent、解释和生物计算保留为跨方向主题。

ViT 属于架构标签，CLIP 是图文对齐方法与模型家族，WM 是世界模型方向；对比学习、掩码重建、自蒸馏、监督、偏好和 RL 是可交叉的监督标签。分类不互斥，跨主题展示不重复计入独立资源数。空栏目明确标为覆盖缺口，不以通用论文填充。

完整模型及多模态链接见 [模型训练与多模态](model-training-multimodal.md)，机器人链接见 [机器人与具身智能](robotics-embodied.md)。

### 跨方向方法与探索

#### Agent 与上下文系统

- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://arxiv.org/abs/2407.18219) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：iterative fine-tuning, online imitation, environment feedback

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://mlanthology.org/iclr/2023/yao2023iclr-react/) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://mlanthology.org/tmlr/2024/wang2024tmlr-voyager/) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23

#### 机制与可信解释

- [OLMo: Accelerating the Science of Language Models](https://arxiv.org/abs/2402.00838) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised language modeling

- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](https://arxiv.org/abs/2403.03853) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [In-context Learning and Induction Heads](https://arxiv.org/abs/2209.11895) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913) · 2020 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：targeted factual editing

- [Naturalness of Attention: Revisiting Attention in Code Language Models](https://arxiv.org/abs/2311.13508) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [Probing Pretrained Models of Source Code](https://arxiv.org/abs/2202.08975) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](https://arxiv.org/abs/2312.05092) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](https://arxiv.org/abs/2510.01171) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](https://arxiv.org/abs/2508.10014) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

- [On scalable oversight with weak LLMs judging strong LLMs](https://arxiv.org/abs/2407.04622) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](https://aclanthology.org/2024.findings-emnlp.882/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://aclanthology.org/2025.emnlp-main.504/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Reasoning Does Not Necessarily Improve Role-Playing Ability](https://aclanthology.org/2025.findings-acl.537/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

#### 生物计算探索

已恢复用户于2026-09-03 16:11:26 UTC亲自提供的 [DOI 10.21203/rs.3.rs-9638576/v1](https://doi.org/10.21203/rs.3.rs-9638576/v1)。官方入口访问失败，身份与题名待核实，单列候选；尚无已核验条目。来源为检索摘要，没有原会话链接。

#### 评估与监督可靠性

- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](https://arxiv.org/abs/2312.05092) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](https://arxiv.org/abs/2508.10014) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

- [On scalable oversight with weak LLMs judging strong LLMs](https://arxiv.org/abs/2407.04622) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](https://aclanthology.org/2024.findings-emnlp.882/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://aclanthology.org/2025.emnlp-main.504/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Reasoning Does Not Necessarily Improve Role-Playing Ability](https://aclanthology.org/2025.findings-acl.537/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

## 2026年9月30日研究短报（补充）

1. **长上下文训练与长程推理分开看。** 你在02:29和02:47 UTC追问线性/稀疏注意力、因果掩码，以及128K任务与32K/64K RL轨迹的关系。优先回读历史聊天已出现的 [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383)：作者在摘要中说明结合长上下文预训练、多阶段SFT与推理优化；这是训练和部署路线的案例，不能直接证明超长RL轨迹的信用分配已解决。

2. **SFT问题细化为数据、目标与评估口径。** 03:10–03:11 UTC的问题是SFT损失为何较大、示范数据为何不更早纳入训练。已有基础条目 [InstructGPT](https://arxiv.org/abs/2203.02155) 可用来对照示范监督与偏好排序后RL的流程；作者报告的是其提示分布上的偏好结果，不能由此推出SFT数据不能混入预训练，或不同目标的loss数值可以直接比较。下一步阅读问题：比较是否固定数据、token掩码、归一化和训练预算？此问题拆分是整理建议，不是你已选定的实验。

3. **回收了一条你亲自提供的历史DOI。** 9月3日16:11:26 UTC的 [10.21203/rs.3.rs-9638576/v1](https://doi.org/10.21203/rs.3.rs-9638576/v1) 已加入待核实；官方入口本轮访问失败，不用旧助手题名替代核验。

本轮未新增已核验论文：117项资源、96项已核验聊天来源保持不变；待核实由17项增至18项。06:14–08:13 UTC的有限检索未恢复新增学术链接，并补查凌晨问题及上述历史DOI；不代表全部聊天已覆盖。四篇凌晨技术报告已在库中，不重复计入。今天围绕已有材料补充问题与阅读线索，没有另推新论文。两篇阅读线索只核对官方摘要与元数据，未全文精读或复现。

[细分类目录](../../docs/topics.md) · [全部论文与来源](../../docs/paper-catalog.md)

