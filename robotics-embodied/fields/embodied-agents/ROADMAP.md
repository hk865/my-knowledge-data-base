# 具身 Agent：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

五步。每一步都先读材料，再做一个能检验理解的小练习。

1. **先走一遍完整闭环。** 读[讲义](../embodied-agents.md)第一至八节。放在第一步，因为本方向的论文各改闭环中的一环，先知道观测、记忆、计划、技能调用、验证各自是什么，才能读出每篇的增量。练习：把讲义里"拿杯子"的流程画成框图，标出哪些箭头传的是"计划"、哪些传的是"证据"。
2. **读基线并列出它留下的问题。** 读 [SayCan 精读](../../papers/saycan/reading.md)。放在这里，因为后面每一篇都在回答它第 7 节的四个问题之一。练习：用精读里的教学算例，假设每个技能成功率 0.9、长程任务 8 步，算整体成功率，再对照 SayCan 长程族 47% 的执行成功率，讨论两者为什么不能直接比较。
3. **闭环的两种写法。** 读 [ReAct 精读](../../../cross-domain/papers/react/reading.md)与 [Inner Monologue](../../papers/arxiv-2207.05608/README.md)。放在这里，因为闭环是 SayCan 之后第一个被补上的部件，也是你在四足控制里最熟悉的概念（反馈）在语言层的对应。练习：写出成功检测器误报一次后，Inner Monologue 的下一步提示会是什么样，系统要怎样才能发现。
4. **技能库的两种扩展方式。** 读 [VoxPoser](../../papers/arxiv-2307.05973/README.md)（生成结构、交给运动规划器）与 [Hi Robot](../../papers/arxiv-2502.19417/README.md)（训练高层、交给 VLA）。放在这里，因为它们代表 2023–2025 年对"技能库是瓶颈"的两种回答，对照读能看出代价各落在哪里。练习：对同一句"把海绵放进盒子"，分别写出 VoxPoser 与 Hi Robot 中高层传给底层的内容。
5. **2026 年的中间层。** 读 [EmbodiedSkills 精读](../../papers/embodiedskills/reading.md) → [RoboSkill 精读](../../papers/roboskill/reading.md) → [MEMORA 精读](../../papers/memora/reading.md)。放在最后，因为这三篇的价值在实验口径的细节里（逐任务微调、首回合与最终成功、条件子集与全量），需要前四步的背景才能读出它们证明了什么、没证明什么。练习：为三篇各写一句"这个数字不能被读成什么"。

读完后可以接着看[跨方向 Agent 页](../../../cross-domain/fields/agents/README.md)（文本与软件 Agent 中的同类问题）和[世界模型方向](../world-models/README.md)（Zero-WAM 用视频说明任务）。

## 通用模型参与机器人任务的专题路线

这条路线从现成模型怎样调用机器人能力出发，与上面的闭环入门衔接。

1. **先分接口。** 读[动作模型干预讲义](action-model-intervention.md)，为同一个拿杯任务写出语言子任务、关键点约束、奖励程序和动作候选各是什么。练习：说明哪个量被修改、谁负责执行、哪里可以检查失败。
2. **从生成过程看动作引导。** 读[VLS 精读](../../papers/arxiv-2602.03973/reading.md)和[FRS](../../papers/arxiv-2606.13675/README.md)。练习：把 VLM 推理、奖励计算、动作优化与实际控制分别画出来；标出哪些参数保持不变。
3. **回到完整 Agent。** 读[HarnessVLA 精读](../../papers/arxiv-2607.08448/reading.md)，再对照[Agent as Policy](../../papers/arxiv-2609.12541/README.md)。练习：列出一个任务需要的工具合同，包括输入坐标、返回证据、失败条件与耗时。
4. **执行经验怎样改变下一次尝试。** 对读[Local Coding](../../papers/arxiv-2609.26499/README.md)、[SimEX](../../papers/arxiv-2609.38982/README.md)与[ENPIRE](../../papers/arxiv-2606.19980/README.md)。练习：分别计算一次成功允许花多少候选、仿真与真机试验，区分开发期和评估期。
5. **补上物理验证与训练边界。** 读[MCP + MTC](../../papers/arxiv-2608.29379/README.md)，再从[PPS](../../papers/arxiv-2609.09148/README.md)、[VLA-ATTC](../../papers/arxiv-2605.01194/README.md)、[ViTaL](../../papers/arxiv-2606.14981/README.md)中选一个工具组件。练习：写明通用模型、动作底座、critic、世界模型各自是否训练，工具接入是否已经由论文实证。

[VLA-Pilot 精读](../../papers/arxiv-2511.14178/reading.md)与[SEAL](../../papers/arxiv-2510.16281/README.md)用于追溯 2025 年的黑盒搜索和候选验证；[StageCraft](../../papers/arxiv-2603.20659/README.md)用于辨认环境干预；[Critic in the Loop](../../papers/arxiv-2603.05185/README.md)用于对照训练过的调度与监控系统。
