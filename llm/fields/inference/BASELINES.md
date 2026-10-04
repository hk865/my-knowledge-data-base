# 推理时计算的基线

> 状态：Baseline 页 · v2 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md) · [草稿—验证导读](draft-verification-guide.md)

## 基线是谁、为什么是它

结论：本方向有两个基线。
- **"答得更对"一线**：思维链加自洽投票。
- **"算得更快"一线**：标准投机解码。

后来的工作要么在这两套流程上换部件，要么像推理模型那样，把其中一个部件训进模型里。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| [思维链](../../papers/arxiv-2201.11903/README.md) + [自洽投票](../../papers/arxiv-2203.11171/README.md)（2022，Google） | **接口**：问题进、推理链加答案出，不改参数。<br>**预算**：采样 N 条推理链。<br>**选择**：对最终答案多数投票。<br>**评估**：GSM8K、MATH 这类有唯一答案的题，报准确率 | 不需要训练和验证器，任何模型都能直接用。<br>后来的 best-of-N、PRM 搜索、Large Language Monkeys 都拿"多数投票"作对照。<br>推理模型报告的 cons@64，就是自洽投票 |
| [投机解码](../../papers/arxiv-2211.17192/README.md) / [投机采样](../../papers/arxiv-2302.01318/README.md)（2022–2023，Google 与 DeepMind） | **接口**：目标模型 + 一个更小的草稿模型。<br>**草稿**：连写 K 个 token。<br>**验证**：目标模型一次前向并行算 K+1 个分布，按 min(1, 目标/草稿) 逐个接受，拒绝处从残差分布补一个。<br>**评估**：同一硬件、批量为 1 时相对普通自回归的加速倍数，并证明输出分布不变 | 后来的 EAGLE 系列、MTP、DFlash 只换草稿器，沿用这套验证规则，加速倍数都以它为分母。<br>BiLD、Judge Decoding、Faster Cascades 改动验证规则，都要说明自己离开了"分布不变"的保证。<br>机制与手算见[导读](draft-verification-guide.md) |

两个基线之上还有一个"预算分配"的参照：[Snell 等](../../papers/test-time-compute/reading.md)（2024）把 best-of-N、PRM 引导的 beam 搜索、顺序修订放在同一预算轴上比较，后来的工作常用它的"按难度分配"来解释自己的收益。

## 基线的结构拆分

结论：一次"推理时计算"可以拆成六个可替换的部件。前四个决定答得对不对，后两个决定算得快不快。

| 部件 | 含义 | 思维链 + 自洽 | 投机解码 |
|---|---|---|---|
| 生成器 | 产生候选的模型，以及它有没有被训练成会长思考、会修订 | 现成的预训练或指令模型，只靠提示 | 目标模型不变，另配一个草稿模型 |
| 预算分配 | 算力花在并行（多采样）、顺序（修订、长思考）还是搜索上，每题花多少 | 并行采样 N 条，每题一样多 | 不改变输出，只改变每个 token 的串行步数 |
| 选择与验证 | 怎样从多个候选里挑答案：投票、奖励模型、单元测试、过程打分 | 多数投票 | 按概率比值接受或拒绝草稿 token |
| 停止与长度 | 什么时候停止思考或停止采样 | 模型自己写到结束符 | 草稿长度 K 固定或动态调整 |
| 解码执行 | 每个 token 怎样算得更快 | 普通自回归 | 草稿 + 并行验证 |
| 显存与批处理 | KV 缓存怎样存放、压缩、共享，一张卡同时服务多少请求 | 不涉及 | 不涉及（加速主要在小批量下成立） |

部件之间有依赖：
- **预算分配要靠选择与验证兑现**：采得再多，挑不出来也没用（Large Language Monkeys）。
- **长思考把停止与长度变成一等问题**：推理模型之后，思考多长要专门控制。
- **显存与批处理决定解码执行的收益**：批量越大，投机解码能借用的闲置算力越少。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 生成器 | **基线本身**：提示中写出推理步骤 | [CoT](../../papers/arxiv-2201.11903/README.md) | **改进**：PaLM 540B 的 GSM8K 从 17.9% 到 56.9%。<br>**代价**：约 100B 参数以上才有收益；推理路径不保证正确 |
| 生成器 | 提示层面的推理结构：每个任务先让模型挑选、改写、组织推理模块 | [Self-Discover](../../papers/arxiv-2402.03620/README.md) | **改进**：比 CoT 最多高 32%；比自洽高 20% 以上，推理计算少 10–40 倍。<br>**代价**：仍是外挂提示，依赖强模型 |
| 生成器 | 训练修订能力：把多轮自我改进写成马尔可夫决策过程来微调 | [Recursive Introspection](../../papers/arxiv-2407.18219/README.md)；[Snell 等](../../papers/test-time-compute/reading.md)的修订模型 | **改进**：同等推理计算下，数学准确率随轮数提高。<br>**代价**：Snell 等的修订模型约 38% 的情况把对的答案改错，必须从历史候选里挑 |
| 生成器 | 用强化学习训练长思维链（结果奖励，不用过程奖励与搜索） | [OpenAI o1](../../papers/openai-o1/README.md)、[DeepSeek-R1](../../papers/arxiv-2501.12948/README.md)、[Kimi k1.5](../../papers/arxiv-2501.12599/README.md) | **改进**：R1-Zero 的 AIME 2024 从 15.6% 到 77.9%；R1 与 o1-1217 相当。<br>**代价**：可读性差、语言混杂（R1-Zero）；few-shot 变差；简单题过度思考；RL 算力巨大 |
| 生成器 | 蒸馏：用大模型的推理轨迹监督小模型 | [DeepSeek-R1](../../papers/arxiv-2501.12948/README.md)（附录 F.1）、[CodePLAN](../../papers/arxiv-2403.13271/README.md)、[s1](../../papers/arxiv-2501.19393/README.md) | **改进**：Qwen2.5-32B 上，蒸馏的 AIME 为 72.6%，直接 RL 只有 47.0%；s1 只用 1000 道题。<br>**代价**：上限受教师限制，R1 认为突破边界仍要更强基座与更大 RL |
| 预算分配 | 并行：大量重复采样，用覆盖率衡量 | [Large Language Monkeys](../../papers/arxiv-2407.21787/README.md) | **改进**：SWE-bench Lite 单次 15.9%，250 次采样 56%。<br>**代价**：没有自动验证器时，选择方法约 100 次后进入平台 |
| 预算分配 | 按题目难度在并行、顺序、搜索之间分配 | [Snell 等](../../papers/test-time-compute/reading.md) | **改进**：约 1/4 的生成次数追平 best-of-N；易题与中等题上可胜过 14 倍大的模型。<br>**代价**：难度估计要 2048 次采样，没计入成本；难题上收益小 |
| 预算分配 | 多棵推理树并行搜索，共识决策 | [Forest-of-Thought](../../papers/arxiv-2412.09078/README.md) | **改进**：能修正单棵树走错的路径。<br>**代价**：计算量随树的数量增加 |
| 选择与验证 | **基线本身**：答案多数投票 | [自洽](../../papers/arxiv-2203.11171/README.md) | **改进**：PaLM 540B 在 GSM8K 上从 56.5% 到 74.4%，无需训练。<br>**代价**：5–10 条后很快饱和；选不出"少数但正确"的答案 |
| 选择与验证 | 过程奖励模型（PRM）给每一步打分，引导 beam 搜索 | [Snell 等](../../papers/test-time-compute/reading.md) | **改进**：中等难度题上搜索比 best-of-N 更省。<br>**代价**：简单题上搜索会钻 PRM 的空子；R1 在大规模 RL 中放弃 PRM，原因是奖励作弊（附录 G.2） |
| 选择与验证 | 用规则或测试做验证（单元测试、证明检查、答案比对） | [Large Language Monkeys](../../papers/arxiv-2407.21787/README.md)、[DeepSeek-R1](../../papers/arxiv-2501.12948/README.md)（规则奖励） | **改进**：覆盖率能直接变成准确率。<br>**代价**：测试本身不可靠（SWE-bench Lite 有 11.3% 的题测试不稳定）；写作等任务没有这样的验证器 |
| 选择与验证 | 增加候选多样性：让模型说出一组回答及其概率 | [Verbalized Sampling](../../papers/arxiv-2510.01171/README.md) | **改进**：创意写作的多样性高 1.6–2.1 倍，不需要训练。<br>**代价**：针对对齐后的模式坍缩，不直接提高推理准确率 |
| 停止与长度 | 预算强制：追加"Wait"延长思考，或强制结束 | [s1](../../papers/arxiv-2501.19393/README.md) | **改进**：AIME 2024 从 50.0% 到 56.7%，长度可控。<br>**代价**：约 6 次后变平，再多会陷入重复，受上下文窗口限制 |
| 停止与长度 | 训练时加长度奖励；把长思考模型转成短回答（long2short） | [Kimi k1.5](../../papers/arxiv-2501.12599/README.md) | **改进**：短回答版 AIME 2024 为 60.8%，平均 3,272 token。<br>**代价**：长度惩罚要预热，否则影响前期训练 |
| 停止与长度 | 偏好优化压缩冗余思考：以"第一个正确解加一次反思"为正例 | [Overthinking](../../papers/url-https-proceedings.mlr.press-v267-chen25bx.html/README.md) | **改进**：QwQ 在 MATH500 上 token 从 2,408 降到 1,331，准确率 93.0% 到 92.8%。<br>**代价**：AIME 上从 46.7% 降到 43.3% |
| 停止与长度 | 取最短的正确回答做自我改进（TOPS） | [Thinking-Optimal](../../papers/arxiv-2502.18080/README.md) | **改进**：GSM8K 上用 412 个 token 达到 QwQ 用 761 个 token 的准确率。<br>**代价**：只研究数学与 SFT；AIME 略低于 QwQ |
| 预算分配 | 并行派出子智能体，编排器用并行与完成率奖励训练（PARL） | [Kimi K2.5](../../papers/arxiv-2602.02276/README.md) | **改进**：WideSearch 上执行时间快 3–4.5 倍，BrowseComp 60.6% → 78.4%。<br>**代价**：省的是墙钟时间，总 token 未必更少；子智能体冻结、不联合训练 |
| 选择与验证 | 训练出的证明验证器 + 元验证器；生成—验证—修改循环 | [DeepSeekMath-V2](../../papers/arxiv-2511.22570/README.md) | **改进**：没有最终答案的证明也能挑选与修正，IMO 2025 解出 5/6、Putnam 2024 118/120。<br>**代价**：每题数千次生成与验证；验证器会编造问题，需元验证 |
| 停止与长度 | 训练低、中、高等推理强度档位，按提示或预算切换 | [gpt-oss 模型卡](https://arxiv.org/abs/2508.10925)、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)、[Nemotron 3](../../papers/arxiv-2512.20856/README.md) | **改进**：用户按任务选成本，准确率随长度近似对数线性（gpt-oss 图 3）。<br>**代价**：每档都要单独训练或调长度惩罚 |
| 停止与长度 | 预算受限与放开长度两阶段交替训练（Toggle） | [Kimi K2.5](../../papers/arxiv-2602.02276/README.md) | **改进**：K2 Thinking 输出 token 少 25%–30%，性能几乎不降。<br>**代价**：多几个阈值与切换周期要调 |
| 生成器（多轮） | 跨轮保留思考：以前各轮的思考与工具调用都留在上下文 | [MiniMax-M2](../../papers/arxiv-2605.26494/README.md)、[Qwen3.5 卡片中的 Qwen3.6](../../papers/qwen3.5/README.md) | **改进**：剥掉以前的思考在智能体评测上一致变差（M2 §7.1）。<br>**代价**：上下文更快变长；与 gpt-oss"删掉以前推理"的格式相反 |
| 解码执行 | **基线本身**：独立小模型写草稿，精确验证 | [投机解码](../../papers/arxiv-2211.17192/README.md)、[投机采样](../../papers/arxiv-2302.01318/README.md) | **改进**：T5-XXL 上 2–3 倍，Chinchilla 70B 上 2–2.5 倍，分布不变。<br>**代价**：要额外的并行算力；草稿长度增大后加速趋平 |
| 解码执行 | 草稿器读目标模型多层特征，训练时模拟推理时的多步草稿 | [EAGLE-3](../../papers/arxiv-2503.01840/README.md) | **改进**：单请求 3.0–6.5 倍，SGLang 批量 64 时吞吐仍高 38%。<br>**代价**：要访问内部特征并专门训练；vLLM 大批量下几乎无收益 |
| 解码执行 | 草稿模块在预训练时就长在目标模型里（MTP） | [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)（见[预训练方向](../pretraining/README.md)⑥） | **改进**：第二个 token 接受率 85%–90%，生成速度 1.8 倍。<br>**代价**：只多预测一个 token |
| 解码执行 | MTP 推广：多层共享参数的 MTP、预训练只训 1 层再复制成 3 层 | [GLM-5](../../papers/arxiv-2602.15763/README.md)、[MiniMax-M2](../../papers/arxiv-2605.26494/README.md)、[Nemotron 3](../../papers/arxiv-2512.20856/README.md) | **改进**：GLM-5 的 4 步投机平均接受长度 2.76（V3.2 为 2.55）。<br>**代价**：对比只在各家私有测试集上 |
| 解码执行 | 块扩散模型一次并行写完整块草稿 | [DFlash](../../papers/arxiv-2602.06036/README.md)、[DFlash 2](../../papers/dflash-2/README.md) | **改进**：草稿长度不再受串行步数限制。<br>**代价**：要读目标模型隐状态并专门训练；加速随模型、任务、温度变化 |
| 解码执行 | 预测可能的验证结果，在独立设备上提前写下一轮草稿 | [SSD](../../papers/arxiv-2603.03251/README.md) | **改进**：命中时隐藏草稿等待，取出的候选仍按通常规则验证。<br>**代价**：额外设备、缓存与未命中回退成本 |
| 解码执行 | 用条件接受概率和引擎吞吐曲线动态选择验证长度 | [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md) §2.4.3（DSpark） | **改进**：让预期推进长度适应服务负载。<br>**代价**：专用草稿器训练和引擎成本测量 |
| 草稿训练 | 按贪心一致或随机采样分布重叠优化连续接受窗口 | [Acceptance-Aware Draft Model Training](../../papers/arxiv-2609.24150/README.md) | **改进**：训练目标对齐部署时的接受方式。<br>**代价**：固定前缀上的代理目标；接受长度提升仍需换算为端到端耗时 |
| 解码执行 | 放宽验证：按置信度回退、训练判别头接受"足够好"的 token、精确采样一个混合分布 | [BiLD](../../papers/arxiv-2302.07863/README.md)、[Judge Decoding](../../papers/arxiv-2501.19309/README.md)、[Faster Cascades](../../papers/arxiv-2405.19261/README.md) | **改进**：比精确验证更快，Judge Decoding 相对优化过的实现为 3.9 倍。<br>**代价**：不再保证与目标模型同分布，必须另测质量（[导读](draft-verification-guide.md)第 6 节） |
| 解码执行 | 小模型主写，遇难点发信号请大模型接管一段 | [RelayLLM](../../papers/arxiv-2601.05167/README.md) | **改进**：大模型只在部分位置调用。<br>**代价**：没有分布保证，收益要按任务实测 |
| 显存与批处理 | KV 缓存分页存放、按需分配、可共享 | [vLLM](../../papers/arxiv-2309.06180/README.md) | **改进**：KV 有效占比从 20%–38% 到 96%，吞吐 2–4 倍。<br>**代价**：attention kernel 慢 20%–26% |
| 显存与批处理 | 减少 KV 头数（GQA）或压缩成潜向量（MLA） | [GQA](../../papers/arxiv-2305.13245/README.md)、[DeepSeek-V2](../../papers/deepseek-v2/reading.md) | **改进**：GQA-8 的推理时间接近 MQA、质量接近多头。<br>**代价**：要改结构并继续训练（GQA 用原预训练算力的 5%） |
| 显存与批处理 | KV 缓存量化到 2 比特（Key 按通道、Value 按 token） | [KIVI](../../papers/arxiv-2402.02750/README.md) | **改进**：批量放大 4 倍，吞吐 2.35–3.47 倍，不需要微调。<br>**代价**：已用 MQA 的模型需要 4 比特 |
| 显存与批处理 | 长输入的稀疏 prefill 与分块执行 | [Qwen2.5-1M](../../papers/qwen2.5-1m/reading.md) | **改进**：1M 输入的首 token 延迟降低 3.2–6.7 倍。<br>**代价**：稀疏配置要在 1M 长度上重新校准，否则 400K 以上检索掉到 60% 以下（详见[长上下文方向](../long-context/README.md)） |
| 显存与批处理 | 换序列算子：选择性状态空间模型，状态大小固定 | [Mamba](../../papers/mamba/reading.md) | **改进**：生成时不需要随长度增长的 KV 缓存。<br>**代价**：精确检索弱于注意力，主流模型以混合结构使用（见[递推状态谱系](../../../foundations/relations/recurrent-state.md)） |

几个不在表中的边界：
- **思维链是否忠实于模型真实的计算**：[Making Reasoning Matter](../../papers/url-https-aclanthology.org-2024.findings-emnlp.882/README.md)、[Measuring CoT Faithfulness by Unlearning](../../papers/url-https-aclanthology.org-2025.emnlp-main.504/README.md)。
- **推理在角色扮演这类开放任务上可能反而有害**：[Reasoning Does Not Necessarily Improve Role-Playing](../../papers/url-https-aclanthology.org-2025.findings-acl.537/README.md)。
- **把推理时计算扩展到多步工具调用的智能体**：[ReAct](../../../cross-domain/papers/react/README.md)、[SWE-agent](../../papers/arxiv-2405.15793/README.md)、[Voyager](../../papers/arxiv-2305.16291/README.md)，见[智能体方向](../../../cross-domain/fields/agents/README.md)。

## 批注

**易误读**
- 表中各"倍数"的对照实现不同，不能跨行比较：
  - Leviathan 对 T5X；
  - Chen 对 Chinchilla 的自回归采样；
  - EAGLE-3 对普通 HuggingFace 解码与 SGLang；
  - Judge Decoding 相对 HuggingFace 为 9.7 倍、相对 GPT-fast 为 3.9 倍。
- 推理模型一行的数字来自各自报告，对照模型的评测设置不完全相同。R1 与 o1-1217 的对比由 DeepSeek 统一重测。

**与其他论文的关联**
- 生成器一格的 RL 算法细节（GRPO、在线镜像下降、长度奖励的位置）在[强化学习方向](../posttraining/rl/README.md)。
- 显存与批处理一格和[长上下文方向](../long-context/README.md)的"推理成本"环节是同一组手段，那里侧重长输入的 prefill。

**未核实 / 待验证**
- BiLD、Judge Decoding、Faster Cascades、RelayLLM、DFlash、DFlash 2 的结论沿用 2026-10-03 文献卡的核验，本轮未重新打开原文。
