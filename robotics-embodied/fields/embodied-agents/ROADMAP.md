# 具身 Agent：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

五步。每一步都先读材料，再做一个能检验理解的小练习。

1. **先走一遍完整闭环。** 读[讲义](../embodied-agents.md)第一至八节。放在第一步，因为本方向的论文各改闭环中的一环，先知道观测、记忆、计划、技能调用、验证各自是什么，才能读出每篇的增量。练习：把讲义里"拿杯子"的流程画成框图，标出哪些箭头传的是"计划"、哪些传的是"证据"。
2. **读基线并列出它留下的问题。** 读 [SayCan 精读](../../papers/saycan/reading.md)。放在这里，因为后面每一篇都在回答它第 7 节的四个问题之一。练习：用精读里的教学算例，假设每个技能成功率 0.9、长程任务 8 步，算整体成功率，再对照 SayCan 长程族 47% 的执行成功率，讨论两者为什么不能直接比较。
3. **闭环的两种写法。** 读 [ReAct 精读](../../../cross-domain/papers/react/reading.md)与 [Inner Monologue](../../papers/arxiv-2207.05608/README.md)。放在这里，因为闭环是 SayCan 之后第一个被补上的部件，也是你在四足控制里最熟悉的概念（反馈）在语言层的对应。练习：写出成功检测器误报一次后，Inner Monologue 的下一步提示会是什么样，系统要怎样才能发现。
4. **技能库的两种扩展方式。** 读 [VoxPoser](../../papers/arxiv-2307.05973/README.md)（生成结构、交给运动规划器）与 [Hi Robot](../../papers/arxiv-2502.19417/README.md)（训练高层、交给 VLA）。放在这里，因为它们代表 2023–2025 年对"技能库是瓶颈"的两种回答，对照读能看出代价各落在哪里。练习：对同一句"把海绵放进盒子"，分别写出 VoxPoser 与 Hi Robot 中高层传给底层的内容。
5. **2026 年的中间层。** 读 [EmbodiedSkills 精读](../../papers/embodiedskills/reading.md) → [RoboSkill 精读](../../papers/roboskill/reading.md) → [MEMORA 精读](../../papers/memora/reading.md)。放在最后，因为这三篇的价值在实验口径的细节里（逐任务微调、首回合与最终成功、条件子集与全量），需要前四步的背景才能读出它们证明了什么、没证明什么。练习：为三篇各写一句"这个数字不能被读成什么"。

读完后可以接着看[跨方向 Agent 页](../../../cross-domain/fields/agents/README.md)（文本与软件 Agent 中的同类问题）和[世界模型方向](../world-models/README.md)（Zero-WAM 用视频说明任务）。
