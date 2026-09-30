# 长上下文 LLM 技术路线图：以 Qwen2.5-1M 为第一篇完整精读

> 定位：这是一张解释机制与依赖的导航图，不是按年份排列的排行榜，也不是覆盖全部新工作的综述。锚点采用 [Qwen2.5-1M 技术报告 v1（2025-01-26）](https://arxiv.org/html/2501.15383v1)。外围论文用于解释它的来源、互补方案与边界。下文「原文」表示论文直接陈述；「分析」表示跨论文归纳，不冒充作者的因果结论。

## 1. 先分清五个问题

1. **位置能否表示？** 超出训练长度后，位置/相对距离分布发生什么变化？RoPE、PI、YaRN、DCA 处理这一轴。
2. **信息如何流动、计算如何执行？** dense attention、稀疏/滑窗、linear attention、SSM 是不同机制；FlashAttention 是精确 attention 的高效执行方法。
3. **模型有没有学会用远处的信息？** 训练长度、数据混合、远距离监督、长指令 SFT 影响这一轴。
4. **服务时是否装得下、跑得动？** KV 头数、KV 精度、prefill 稀疏度、分块调度分别节省不同资源。
5. **“有效长上下文”如何证明？** 简单检索、多目标/多跳/聚合、真实长文任务与短任务回归需分开观察。

这五轴是本图的分析框架。Qwen 报告的架构、训练、推理和评测章节分别覆盖其中多个问题；不存在单一“扩窗算法”包办全部环节。

## 2. 五条技术线与代表节点

### A. 位置表示与长度外推

- **RoPE → PI → YaRN：有明确机制关联。** RoPE 通过旋转把位置注入 Q/K；PI 把位置索引压回已有范围；YaRN 则区分频段处理插值，并引入 attention temperature。它们针对位置分布，不自动消除 attention 的计算成本。[RoPE](https://arxiv.org/abs/2104.09864) · [PI](https://arxiv.org/abs/2306.15595) · [YaRN，采用 2023 年 v2](https://arxiv.org/html/2309.00071v2)
- **DCA 是另一种位置处理路线。** 它区分块内、跨块和相邻块的相对位置，保留跨块信息通路；不是把长文切开独立回答，也不是仅保留最近窗口。[DCA](https://arxiv.org/abs/2402.17463)
- **在 Qwen 中的落点：** 推理时 DCA 与 YaRN 的 attention scaling 联用。这里不能简写成“使用完整 YaRN 插值训练”；报告的训练阶段另有 RoPE base 调整。[Qwen §3、§5.1](https://arxiv.org/html/2501.15383v1#S5.SS1)

### B. Attention 机制与高效执行：三类不能混为一谈

- **保留 dense softmax attention，优化执行：FlashAttention。** 分块和 IO-aware 实现避免显式落地整个 attention 矩阵；“精确”指不靠删 attention 边来近似。它减少 IO/中间显存，不把 dense attention 的二次算术量变成线性。[FlashAttention](https://arxiv.org/abs/2205.14135)
- **改变可见连接：滑窗/结构化稀疏。** Longformer 的局部窗口加全局 token 是代表。固定窗口与固定数量全局 token 时可线性扩展，但信息通路与 dense attention 已不同。它是较早的机制代表，不应画成 Qwen 的直接架构祖先。[Longformer](https://arxiv.org/pdf/2004.05150)
- **改变序列算子：linear attention 与 SSM。** Linear Attention 利用核特征分解和结合律形成递归计算；Mamba 使用输入依赖的 selective SSM。这两者都可避免显式全量两两 attention，但不是同一算法，也不是给现有 Qwen 换个推理 kernel 就能获得的等价结果。[Linear Attention](https://arxiv.org/pdf/2006.16236) · [Mamba](https://arxiv.org/pdf/2312.00752)

**分析：** 选择全局信息通路、选择位置表示、选择执行 kernel 是可区分的决定。可能组合不代表已经兼容，更不代表质量可无损保持。

### C. 长训练数据、课程与长监督

- **持续预训练的代表：Effective Long-Context Scaling。** 研究 RoPE base、长序列持续预训练、数据混合与长度课程；Qwen 明确引用它的 ABF。它提供“怎样从已有 checkpoint 延伸”的入口。[原文](https://arxiv.org/pdf/2309.16039)
- **数据选择的对照：Data Engineering for 128K。** 强调领域平衡与长样本上采样；只把某些领域的长文比例加大可能不够。不要把“更多长 token”直接等同于“更多有用的远距离依赖”。[原文](https://arxiv.org/html/2402.10171v1)
- **长指令对齐的代表：LongAlign。** 长 instruction 数据、变长样本 packing/sorted batching、loss weighting 与 LongBench-Chat 构成独立后训练问题；它讨论的是长输入指令遵循，不是长 rollout 的 RL 信用分配。[原文](https://aclanthology.org/2024.findings-emnlp.74.pdf)
- **在 Qwen 中的落点：** 逐级扩长与自然/合成长依赖数据后，做两阶段 SFT：先短指令，再短长混合。其意义是把“能接收长文本”与“能按要求利用长文本”分开处理。[Qwen §3–4](https://arxiv.org/html/2501.15383v1#S3)

**分析：** 课程、位置参数、数据配比与总训练预算相互耦合。报告中的阶段结果不能独立证明“只改长度”贡献多少；做训练研究时应控制其余变量，另测不同距离、证据密度、干扰强度。

### D. 推理资源：算力、临时激活、KV cache 是三笔账

- **MInference：减少 prefill 的 attention 计算。** 根据注意力头模式与输入动态选择稀疏连接；它是推理近似，应与精确 dense 基线比较质量和耗时。[原文](https://arxiv.org/html/2407.02490v1)
- **GQA：减少 KV 头数。** 多个 query heads 共享较少的 KV heads；这是架构与 checkpoint 层面的设计，不等于量化。[原文](https://arxiv.org/abs/2305.13245)
- **KIVI：减少缓存元素的存储精度。** key 按 channel、value 按 token 量化，并保留高精度残余窗口；减少 KV 字节数不等于增加模型学过的上下文长度。[原文](https://arxiv.org/html/2402.02750v1)
- **在 Qwen 中的落点：** GQA 已在架构中；prefill 使用 MInference 衍生稀疏方案、chunked prefill 与稀疏配置校准。不能把 KIVI 画成报告采用的方法。[Qwen §2、§5.2](https://arxiv.org/html/2501.15383v1#S5.SS2)

**三个 chunk，三个含义：** DCA 的 chunk 管位置映射；chunked prefill 的 chunk 管执行与临时激活；sliding window 管可见信息范围。名字相似，不应合成一个节点。

### E. 评测：先定位能力，再判断应用价值

- **NIAH/passkey → RULER：诊断难度扩展。** RULER 增加多针、多跳追踪与聚合；单针成绩接近满分仍可能在更长、更复杂任务上下降。它是可控合成诊断，不代表全部真实任务。[RULER](https://arxiv.org/html/2404.06654v1)
- **LongBench / LongBench-Chat：补充任务生态。** 前者覆盖中英文多类长文理解任务；后者随 LongAlign 提供长指令生成评测。任务分布、长度与指标不同，不能只比较一个总分。[LongBench](https://arxiv.org/html/2308.14508v2) · [LongAlign / LongBench-Chat](https://aclanthology.org/2024.findings-emnlp.74.pdf)
- **分析建议：** 同时记录长度 × 证据位置 × 任务类型；另测短任务回归、prefill 延迟、decode 吞吐、峰值显存。只有在指定工作负载、精度和硬件下，“更快且够准”才是可复现结论。

## 3. 如何读图中的边

- **实线「直接采用/改造」：** 原文明示采用或基于该方法，例如 Qwen ← DCA、YaRN attention scaling、MInference、ABF、GQA。
- **实线「机制依赖」：** PI/YaRN 以 RoPE 机制为对象；不是泛指后来论文更好。
- **虚线「互补/对照」：** KV 量化对稀疏计算、Longformer/linear/SSM 对 dense 路线。表示分析上的对照或组合空间，不表示某论文已经实现组合。
- **点线「评测」：** benchmark 指向被测系统，不是训练配方的继承关系。

配套 JSON 逐条保存来源和 evidence_level。没有来源证明的“取代”“彻底解决”“无损兼容”不画。

## 4. 回到模型训练问题：这篇报告能回答什么？

**能提供案例：** 如何安排长上下文持续预训练与长指令 SFT；为何需要显式长依赖样本；训练扩长、位置外推、推理稀疏化如何共同构成部署方案。它也提醒你拆开训练窗口、服务上下文上限与输出长度。

**不能据此宣称：** “百万 token 的 RL 已解决”。报告的偏好优化只使用至多 8K 的短样本，并给出长任务迁移结果；它未给出长 trajectory 的 reward 设计、token/action-level credit assignment、advantage estimator 或长时程探索的系统研究。[Qwen §4](https://arxiv.org/html/2501.15383v1#S4)

**分析：** 长输入说明决策能看到多少上下文；长输出说明生成序列有多长；长时程 RL 说明多少连续决策共享远期回报。三者可能相关，但任何一个变长都不自动解决另外两个。

### 把近期问题放到正确的研究轴上

- **“长上下文来自预训练，还是 SFT/RL？”** 先拆解能力：位置适配/长依赖学习、指令遵循、偏好优化。此报告给出组合案例，不能从组合后分数推导每阶段的普遍必要性；更不能把短偏好训练的迁移解释为长 rollout 学习
- **“为什么 SFT loss 大？”** 此报告没有给出足够的损失定义与训练曲线来回答。分析时先对齐 tokenizer、样本难度、仅回答 token 还是全序列计损、归一化方式与 label masking；不能只按阶段名称比较 loss，也不能由 loss 大直接推出能力差
- **“SFT 数据为什么不提前放进预训练？”** 这是目标、数据配比与训练时序的实验问题。此报告展示阶段安排，未做“同数据全部前置”的受控对照；需要分别测试前置、后置、重复使用，并控制 token 预算和 loss mask
- **“更便宜的 KV 命中/容量怎么做？”** 先明确命中指跨请求 prefix-cache 命中，还是模型取回远处内容。前者是服务复用；后者是能力评测。容量又可分 KV heads、每元素位数与保留 token 数，分别对应 GQA、量化、选择/压缩；它们不能用一个指标替代
- **“滑窗、linear、压缩 attention、Transformer 外创新？”** 本图给出代表分支，但不把所有压缩方法视为同类：丢弃 token、压缩 KV 表示、压缩历史状态改变的对象不同。Mamba 是外部架构参照；报告本身沿用 Transformer，不能用它否定其他架构
- **“数据筛选/生产/过滤/组合放在哪阶段？”** 建议把每项标为自然数据选择、合成任务生产、质量验证、长度/领域混合，再标注预训练或 SFT。报告描述部分生产与组合，但没有公开足够过滤细节来复现完整流水线；缺失信息应保留为缺失

上述实验与指标拆分是分析建议，不是声称这些论文已经完成全部验证。

## 5. 最小后续阅读路线

第一篇完整精读维持 Qwen2.5-1M。之后按问题选择，不要求把全部外围论文顺序读完：

1. **不清楚“256K 如何服务 1M”**：DCA → YaRN §2–3；RoPE 与 PI 只补相应公式
2. **想研究训练为什么有效**：Effective Long-Context Scaling → Data Engineering → LongAlign；优先看数据配方、对照设置与短任务回归
3. **想做性能优化**：FlashAttention → MInference；遇到 KV 显存问题再读 GQA/KIVI
4. **想改模型骨架**：Longformer、Linear Attention、Mamba 作为独立分支；先写明愿意牺牲/保留哪些信息访问能力
5. **想判断“真能用多长”**：RULER → LongBench；再按实际任务自建分层评测

每读完一个节点，补四行：它改变什么；它保持什么；直接证据是什么；还需要哪个实验才能支持自己的推断。

## 精读与可编辑关系数据

[Qwen2.5-1M 全文精读](../deep-readings/qwen2.5-1m.md) · [机制图](../../assets/qwen2.5-1m-mechanism.svg) · [节点与关系 JSON](long-context-graph.json)
