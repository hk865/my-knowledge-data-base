# 架构与效率

> 状态：领域入门页（研究对象变体）· v2 · 依据 [synthesis.csv](synthesis.csv)（23 篇）
>
> 速览：
> 1. 本方向研究网络结构本身：token 之间怎样交换信息（注意力及其替代），每个 token 怎样被加工（FFN、MoE、查表记忆），几十上百层怎样串起来（归一化与残差），生成时缓存什么（KV 缓存）。它没有专属的 benchmark，好坏只能写成"某类工作负载下、花多少成本、得到多少质量"，所以本页先讲任务和测量，再讲方法谱系与历史。
> 2. 每一类改动都在用某种能力换效率，后来的工作把代价一项项测了出来：MQA 在 7B 稠密模型上让 MMLU 从 45.2 降到 37.9（DeepSeek-V2 附录），固定大小状态的模型找不回长上下文里的细节（电话簿查找中 Pythia-410M 胜过 Mamba-2.8B），Switch 的最大模型训练不稳，Pre-LN 让深层变得冗余。
> 3. 困惑度常常看不出这些代价：Mamba 在 Pile 上的困惑度低于同规模的 Pythia，复制和召回却更差；Kimi Linear 的 7:1 混合训练损失相近，分布外验证明显变差。比较架构要同时看召回类任务、分布外验证和每 token 的成本。
> 4. `[判断]` 2024 年以后的收敛方向：同一个模型里的注意力层不再相同（局部与全局、线性与全注意力、压缩与稀疏按比例交错，精确的全局层约占 1/8 到 1/4）；稀疏从 FFN 扩展到注意力和记忆；KV 缓存成为一等设计目标，DeepSeek 每 token 的全局 KV 缓存从 V1 到 V4.1-Flash 缩小约 437 倍。
> 5. `[判断]` 团队押注：DeepSeek 在 Transformer 内部逐代替换部件，做压缩与稀疏（DeepSeekMoE → MLA → 无辅助损失均衡与 MTP → NSA/DSA → mHC → Engram → V4 → V4.1-Flash，见"DeepSeek 架构线"一节），Kimi 改造序列与深度两个方向的信息流（KDA 线性注意力混合、Attention Residuals），Google 从 MQA、GQA、Switch 起步并在 Gemma 上坚持局部/全局交错，学界与 AI21 推动状态空间模型和混合架构。

本页是[大语言模型](../../README.md)领域的架构与效率方向。与相邻方向的分工：[预训练方向](../pretraining/README.md)讲"为了预训练目标改了哪些部件"（损失稳定、注意力不丢失、更长更大的网络、更多知识），本页讲部件本身怎样演化、各自用什么换什么；长上下文能力怎样获得与评测在[长上下文](../long-context/README.md)，推理系统与解码策略在[推理时计算](../inference/README.md)。

## 什么是 LLM 的架构

今天的大语言模型几乎都是 decoder-only 的 Transformer（只用因果注意力、按前文预测下一个 token 的结构，[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 13 节）。一个 token 先查嵌入表得到向量，再穿过几十到上百层，每层做两步：**序列混合**（注意力：这个 token 从前文的哪些位置读、读多少）和**通道混合**（FFN，前馈子层：只在这个 token 自己的向量上做两层变换，参数占大头）。两步之间用残差（把子层输出加回输入）和归一化（控制向量的尺度）串起来。生成时，每个历史 token 在每层算出的 K、V 被保存下来供后面的 token 读取，这就是 **KV 缓存**。注意力的 Q、K、V 怎样算见 [QKV 讲义](../../../foundations/lessons/15-qkv-deep-dive.md)第 4–5 节，FFN、残差与归一化见 Transformer 讲义第 10 节。

| 部件 | 它决定什么 | 本页对应的方法谱系 |
|---|---|---|
| 序列混合 | 谁能读到谁；计算怎样随长度增长 | 1 头与 KV；2 局部与稀疏；3 固定大小的状态 |
| KV 缓存 | 生成时每个历史 token 要存多少字节 | 7 KV 缓存的账 |
| 通道混合 | 每个 token 用多少参数，总共有多少参数 | 4 MoE；6 条件记忆 |
| 深度方向 | 信号与梯度怎样穿过几十上百层 | 5 归一化、残差与门控 |
| 层排布 | 不同类型的层按什么比例交错、放在第几层 | 2 与 3 中的交错与混合 |

这个方向没有自己的任务和 benchmark。架构的好坏只能写成"在某类工作负载下、花多少成本、得到多少质量"：成本有训练 FLOPs、每 token 推理 FLOPs、KV 缓存字节、显存带宽好几本账，质量又随评测协议变化。所以本页先讲任务和测量，再讲方法和历史。

## 从任务看

结论：不同工作负载的瓶颈在不同的部件上，没有在所有负载下都最好的架构。

先说两个词。**预填充**（prefill）：一次性处理整段输入，算出所有位置的 K、V；**解码**（decode）：之后逐个生成 token，每步都要读一遍全部 KV 缓存。前者主要花计算，后者主要花显存带宽（每步要搬的数据太多，算力在等数据）。

| 工作负载 | 瓶颈在哪 | 需要的架构性质 | 本库中的证据 |
|---|---|---|---|
| 预训练 | 每 token FLOPs、训练稳定性、跨设备通信 | 总参数与每 token 计算分开；训练不发散 | [Switch](../../papers/arxiv-2101.03961/README.md) 在相同计算下预训练最多快 7 倍；[DeepSeek-V2](../../papers/deepseek-v2/reading.md) 每训练 1T token 的成本比稠密的 67B 低 42.5%；Llama 3 为了稳定选稠密结构（[预训练方向](../pretraining/README.md)） |
| 短输入、大批量的对话服务 | 解码时每步读 KV 的显存带宽 | 每 token 的 KV 少 | [MQA](../../papers/arxiv-1911.02150/README.md)：解码器每 token 46 μs → 3.8 μs；[GQA](../../papers/arxiv-2305.13245/README.md)：T5-XXL 推理时间 1.51 → 0.28 |
| 长输出（长思考的推理） | 解码步数多，KV 随输出增长 | 每 token 的 KV 小，单步计算不随长度上涨 | [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)：1M 上下文下单 token FLOPs 为 V3.2 的 27%、KV 为 10%；[Kimi Linear](../../papers/arxiv-2510.26692/README.md)：1M 长度解码吞吐最多 6 倍 |
| 长输入且要找回其中的细节（文档问答、代码仓库） | 预填充随长度平方增长；要能精确召回 | 至少一部分层保留精确的全局读取 | [Based](../../papers/arxiv-2402.18668/README.md)：召回密集任务上注意力比 Mamba 高 32.2 个百分点；Kimi Linear 保留四分之一全注意力层 |
| 长程智能体（输入远多于输出，上下文反复续用） | 预填充计算；KV 在显存、主机内存、SSD 间的存储与搬运 | 预填充便宜；KV 小到可以持久化 | [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)：预填充每 token 只激活 8B 参数，全局 KV 约 890 字节/token |
| 知识密集的问答 | 参数容量 | 装更多事实而不增加每 token 计算 | [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) 16B 在 TriviaQA 等知识任务上强；[Engram](../../papers/arxiv-2601.07372/README.md) 推理时关掉查表，事实类基准只剩 29%–44% |

`[判断]` 拉扯集中在三对性质上。**召回与状态大小**：要从长上下文里精确找回任意一个 token，推理时保存的状态就得随长度增长（Based 的下界），省 KV 与能召回互相冲突。**容量与每 token 计算**：MoE 与查表记忆把两者分开，代价转移到通信、负载均衡和显存或主机内存。**训练容易与深层效率**：让梯度好传的结构（Pre-LN）同时让深层的贡献变小。

## 从测量看

结论：成本有好几本账，不能互相替代；质量指标换一个，架构之间的排名会翻转。

| 量 | 回答什么 | 容易混淆的地方 |
|---|---|---|
| 总参数 / 激活参数 | 模型能装多少；每个 token 实际算多少（MoE 中只有被选中的专家参与） | 两者可以差十几倍（DeepSeek-V2 为 236B / 21B），比较时要写清是哪一个 |
| 每 token FLOPs | 训练或推理一个 token 的计算量 | 长上下文时注意力部分随长度增长，短上下文时 FFN 占大头 |
| KV 缓存（每 token 字节） | 生成时每个历史 token 占多少显存 | 与精度有关（BF16、FP8、FP4）；局部窗口层与全局层要分开算 |
| 推理时状态大小 | 线性注意力、SSM 这类模型保存的固定大小状态 | 状态固定意味着能记住的上限固定（Based Theorem 3.1） |
| 预填充吞吐 / 解码吞吐 / 延迟 | 处理输入多快、生成多快、单个请求等多久 | 同一改动对两个阶段的收益可以完全不同（NSA §2 批评只加速一个阶段的方法） |
| 显存访问量 | 解码是否受带宽限制 | 理论 FLOPs 降了，访存没降，实际就不会快（NSA §2 对每头独立选 KV 的分析） |

排名翻转的五个例子：

1. **困惑度与召回**。在 Pile 上预训练的同规模模型中，Mamba 的困惑度低于 Pythia；但在电话簿查找（给一份"姓名：号码"列表再问某人的号码）上，列表足够长时最小的 Pythia-410M 也胜过最大的 Mamba-2.8B（[Repeat After Me](../../papers/arxiv-2402.01032/README.md) §5）。
2. **小模型与大模型**。MQA 原文在 1.9 亿参数的语言模型上，开发集困惑度只从 29.9 升到 30.2；DeepSeek-V2 附录 D.1 的 7B 稠密模型（1.33T token）上，MMLU 多头 45.2、GQA 41.2、MQA 37.9（两组实验的数据、规模、指标都不同，只能说明小规模的困惑度没有暴露代价）。
3. **训练损失与分布外验证**。Kimi Linear 的混合比消融中，7:1 的训练损失与 3:1 相近，在分布不同的验证集上明显变差（Table 1）。
4. **上游困惑度与下游微调**。Switch-C（1.6T 参数）与 Switch-XXL（395B 参数、每 token FLOPs 是前者的 10 倍）在 C4 上困惑度相近，微调后 SQuAD 却是 87.7 对 89.6（Switch §8）。
5. **训练长度内与长度外推**。Gated Attention 在原训练长度 32K 内与基线相差很小；用 YaRN 扩到 128K 后，RULER（合成的多任务长上下文评测）在 128K 上 31.65 对 58.82（[Gated Attention](../../papers/arxiv-2505.06708/README.md) Table 5）。

benchmark 的替换就是这个方向目标的迁移：WMT 机器翻译的 BLEU（Transformer、MQA）→ C4 困惑度与 SuperGLUE 微调（Switch）→ Long Range Arena 长序列分类（S4、LRU）→ Pile 困惑度加合成的选择性复制与 induction 任务（Mamba）→ 合成召回与复制（MQAR、电话簿，2024）→ 大海捞针、RULER、LongBench（NSA、Kimi Linear）→ 每 token KV 字节数、解码 FLOPs 随上下文长度的曲线与智能体任务（DeepSeek-V4、V4.1-Flash）。前一阶段的指标饱和或被证明看不出代价，下一阶段就换指标。

## 从内部看

结论：几项从模型内部观察到的现象，直接变成了架构设计的理由。通用的分析方法见[模型科学](../../../cross-domain/fields/model-science/README.md)，注意力与 FFN 的分工证据链见[关系页](../../../foundations/relations/attention-ffn-division.md)。

| 现象 | 证据 | 对架构的含义 |
|---|---|---|
| 注意力汇聚：大量注意力落在开头的 token 上 | Gated Attention 的基线平均 46.7% 的注意力落在第一个 token 上；[StreamingLLM](../../papers/arxiv-2309.17453/README.md) 逐出开头 token 后窗口注意力失效 | 两种做法：输出门控消除它（Qwen），softmax 里加可学习的 sink 项显式提供它（DeepSeek-V4） |
| pre-norm 模型的深层输入输出高度相似 | [ShortGPT](../../papers/arxiv-2403.03853/README.md) 删去 LLaMA 2-13B 的 25% 层，MMLU 55.0 → 52.2；[Hyper-Connections](../../papers/arxiv-2409.19606/README.md) 称为表示坍缩 | 深度方向的信息流需要重新设计（第 5 条谱系） |
| 事实主要存在 FFN，由注意力读出 | DeepSeekMoE 16B 知识任务强、选择题弱，作者归因于注意力参数只有约 0.5B；Engram 关掉查表后事实类大幅下降、阅读理解基本保留 | MoE 与查表记忆都稀疏化 FFN 一侧，注意力一侧的容量要单独保住 |
| 混合模型的少数注意力层里出现 induction head | [Jamba](../../papers/arxiv-2403.19887/README.md) 在 3 个注意力层中找到 12 个这类头，纯 Mamba 不按示例的格式回答 | 混合架构要保留精确注意力的一个理由 |
| 早期层在重建局部的静态模式 | Engram-27B 第 5 层的表示与 MoE 基线第 12 层最接近（CKA） | 层的位置成为设计变量：查表放在第 2 层最好，DeepSeek-V4 前 3 个 MoE 层用哈希路由 |

## 方法谱系

结论：七条线，每条都在某个部件上用一种能力换效率。下面每条先给对比表，再写做不好的场景，最后"站在现在看过去"：从后来的工作、竞争团队的选择反推当时没写明的代价。按部件拆分的基线与"后续工作在改哪个部件"见 [Baseline 页](BASELINES.md)。

### 1 头与 KV：MHA → MQA/GQA → MLA → 压缩加稀疏

结论：这条线的目标始终是解码时每个 token 要读的 KV 少一点，手段从"少存几个头"变成"存一个低维潜向量"，再变成"沿序列压缩后只读一部分"。

| 方法 | 每个历史 token 每层缓存什么 | 换来什么 | 代价 |
|---|---|---|---|
| MHA（多头注意力，[Transformer](../../papers/transformer/reading.md) 2017） | 每个头一组 K、V | 每个头独立决定读什么 | 缓存随头数增长；解码受显存带宽限制（MQA §2.4.1） |
| [MQA](../../papers/arxiv-1911.02150/README.md)（Google 2019） | 所有头共用一组 K、V | 缓存缩小为 1/h；解码器每 token 46 μs → 3.8 μs | 质量下降、训练不稳（见下） |
| [GQA](../../papers/arxiv-2305.13245/README.md)（Google 2023） | 每组查询头一组 K、V（常用 8 组） | 质量接近多头、速度接近 MQA；已有的多头模型用 5% 的原预训练算力就能改造 | 缓存仍随组数线性增长 |
| MLA（[DeepSeek-V2](../../papers/deepseek-v2/reading.md) 2024） | 一个 512 维潜向量加一个 64 维位置键 | 缓存相当于 2.25 组的 GQA，质量好于多头；V2 的 KV 缓存比 67B 少 93.3% | 计算仍随长度平方增长；推理时不显式构造 K，加不了 QK-Norm |
| 压缩加稀疏（DeepSeek-V4 的 CSA/HCA，V4.1-Flash 的 CSA2） | 沿序列每 4 个或 128 个 token 压成一个条目，再只读 top-k 个；后面的层复用前面层的全局 KV | 1M 上下文下 KV 约为 BF16、8 组 GQA 的 2%；V4.1-Flash 约 890 字节/token | 结构复杂（V4 自述）；稀疏选择可能出错（V4.1-Flash 自述） |

做不好的场景：[GQA](../../papers/arxiv-2305.13245/README.md) 附录 A 写明，从头训练的 T5-Large MQA 预训练中频繁出现损失尖峰，在长输入任务上微调时立刻发散；GQA 自己只在 encoder–decoder 模型上评估过。MLA 加不了 QK-Norm（计算注意力分数前对 Q、K 做归一化的稳定部件），[Kimi K2](../../papers/arxiv-2507.20534/README.md) 只好在优化器里另做 QK-Clip（详见[预训练方向](../pretraining/README.md)"损失稳定"一节）。

站在现在看过去：

- `[判断]` MQA 的质量损失被小模型上的 BLEU 与困惑度低估了。依据：MQA 原文只在 2 亿参数级的翻译与语言模型上报告"略差"；四年后 GQA 的引言与附录把"质量下降与训练不稳"作为出发点，DeepSeek-V2 附录 D.1 在 7B 上测出 MMLU 差 7.3 分，DeepSeekMoE 第 5 节也写到 DeepSeek 7B 的 MQA 版本在 MMLU 类任务上吃力。
- `[判断]` 同一个团队会因为自己的消融换路线：DeepSeek LLM 67B（2024 年 1 月）还用 GQA，四个月后的 V2 以"GQA、MQA 性能不及 MHA"为理由换成 MLA。Meta 的 Llama 3、阿里的 Qwen2.5 与 Qwen3 则一直用 GQA，稠密模型的默认配置停在这里。
- `[判断]` 省 KV 的结构会挡住别的部件：MLA 挡住 QK-Norm；GQA 让"每个头各选各的 KV"的推理期稀疏方法失效（同组头的选择取并集，访存省不下来，NSA §2）。新部件要和已有的 KV 结构一起设计，这正是 NSA 把块选择做成按 GQA 组共享的原因。
- `[判断]` 共享 KV 在压缩之后又回来了：DeepSeek-V4 的 CSA 与 HCA 在压缩后的 KV 上以 MQA 的方式计算（所有查询头共用压缩条目），说明当每个缓存条目本身已是信息密集的压缩表示时，"一组 KV 给所有头用"的代价变小了。

### 2 谁能读到谁：局部窗口、事后稀疏与训练时稀疏

结论：这条线减少每个查询要读的位置数。先是固定的局部窗口，再是推理时临时挑选，最后是从预训练开始就让模型学会挑选。

| 路线 | 代表 | 怎样省 | 做不好的地方 |
|---|---|---|---|
| 局部窗口与局部/全局交错 | Transformer §7 把"局部、受限的注意力"列为未来方向；Gemma 2（局部:全局 1:1，窗口 4096）→ Gemma 3（5:1，窗口 1024）→ Gemma 4（5:1，全局层的 key 兼作 value） | 只有全局层看全长；Gemma 3 的消融中局部:全局到 7:1 验证困惑度变化也很小 | 全局层仍按全长计算；窗口外的信息只能经全局层传递 |
| 局部窗口（2025–2026 的两种相反选择） | [gpt-oss](https://arxiv.org/abs/2508.10925)（OpenAI 2025-08）：带宽 128 token 的窗口层与稠密层交替，每个头带一个可学习的 softmax 分母偏置（作用同 sink）；[MiniMax-M2](../../papers/arxiv-2605.26494/README.md)（2026-05）：试过多种滑窗混合后全部改回全注意力 | gpt-oss 只有一半层看全长 | MiniMax-M2 报告滑窗混合在多跳推理、检索、上下文学习上变差，SFT 后 32K 以上更明显（§2.2.2） |
| 推理期事后稀疏与 KV 逐出 | H2O（按累计注意力逐出 KV）、Quest、[StreamingLLM](../../papers/arxiv-2309.17453/README.md) | 不改训练，推理时只保留或只读一部分 KV | 每查询约 2560 个 token 的同等预算下，LongBench 平均 H2O 0.303、全注意力 0.437（NSA Table 2）；StreamingLLM 作者写明不适合需要长程记忆的任务 |
| 训练时稀疏 | [NSA](../../papers/arxiv-2502.11089/README.md)（2025）→ DSA（[DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md)）→ CSA/HCA（DeepSeek-V4）→ CSA2（V4.1-Flash） | 压缩块、选块、滑窗三路合并，从预训练起端到端训练；64K 长度解码最多快 11.6 倍，LongBench 0.469 高于全注意力 | DSA 的索引器本身仍随长度平方增长（V3.2 §2）；NSA 为训练稳定把第一层的 MoE 换回普通 MLP；V4.1-Flash 自述选择误差可能在未测试的边界情形下损害能力 |
| 训练时稀疏被其他团队采用 | [GLM-5](../../papers/arxiv-2602.15763/README.md)（智谱 2026-02）在中段训练后从 MLA 转成 DSA：1000 步稠密预热 + 20B token 稀疏适应 | 长序列注意力计算省 1.5–2 倍；128K RULER 78.86，稠密 MLA 79.21 | RL 中非确定性的 top-k 会让训练几步内崩溃，要冻结索引器、改用确定性实现 |

做不好的场景：NSA §2 引用的研究显示，事后取 top 20% 的注意力只覆盖约 70% 的注意力分数，预训练中形成的检索头容易在推理时被剪掉；只稀疏化预填充（如 MInference）或只稀疏化解码（如 H2O）的方法，在另一阶段仍与全注意力一样贵。

站在现在看过去：`[判断]` 2023–2024 年的推理期稀疏把注意力模式当作训练好的既定事实，去猜哪些 KV 不重要；NSA 的分析说明模型在训练时根本没学过"只读一部分"，猜错的代价落在检索类任务上。DeepSeek 从 NSA 起三代都把稀疏放进训练，V4.1-Flash 进一步取消了稠密预热，稀疏注意力在 64K 长度上从头训练。长上下文能力本身怎样评测，见[长上下文方向](../long-context/README.md)。

### 3 固定大小的状态：线性注意力、状态空间模型与混合

结论：这条线把整段历史压进一个固定大小的状态，推理时每步的计算与显存都不随长度增长；代价是召回，所以 2024 年以后的生产模型都把它与一小部分精确注意力混合。

这些模型在数学上都是"用上一步的状态和本步输入算新状态"的递推，差别在状态转移怎样设计（[递推状态谱系](../../../foundations/relations/recurrent-state.md)）：线性注意力的转移是单位阵、只累加；S4 与 [LRU](../../papers/arxiv-2303.06349/README.md) 的转移固定、可并行扫描；[Mamba](../../papers/mamba/reading.md) 的转移随输入变化，既能按内容选择又能并行。机制入门见 [SSM、GNN 与 MoE 讲义](../../../foundations/lessons/18-ssm-gnn-moe.md)第 2 节。

| 节点 | 状态与读取 | 换来什么 | 做不好的地方 |
|---|---|---|---|
| [线性注意力](../../papers/arxiv-2006.16236/README.md)（Idiap/EPFL 2020） | 矩阵状态逐步累加 φ(k)vᵀ，用 φ(q) 读出 | 复杂度降到线性；CIFAR-10 逐像素生成吞吐为 softmax 的 4462 倍 | WSJ 语音识别音素错误率 8.08，softmax 为 5.12；没有做语言建模 |
| [Mamba](../../papers/mamba/reading.md)（CMU/Princeton 2023） | 选择性 SSM：步长与读写矩阵随输入变化 | 生成吞吐为同规模 Transformer 的 5 倍；3B 模型常识推理比 Pythia-3B 高 4 分 | 原文自述只验证到较小规模；复制与召回差（见下） |
| [Based](../../papers/arxiv-2402.18668/README.md)（Stanford 2024） | 泰勒近似的线性注意力 + 64–128 宽的滑动窗口 | 1.3B 上召回密集任务比 Mamba 高 10.36 个百分点；生成吞吐为 FlashAttention-2 的 24 倍 | 原文证明任何递推模型解联想召回都需要随长度线性增长的状态 |
| [Jamba](../../papers/arxiv-2403.19887/README.md)（AI21 2024） | 注意力:Mamba = 1:7，加 MoE | 256K 上下文 KV 缓存 4GB，Mixtral 为 32GB | 7B 级时 Mamba 层内部出现大激活值与损失尖峰，加 RMSNorm 才稳定 |
| [Kimi Linear](../../papers/arxiv-2510.26692/README.md)（2025）→ [Kimi K3](../../papers/arxiv-2607.24653/README.md)（2026） | KDA（带逐通道遗忘门的线性注意力）:MLA = 3:1，全局层不用位置编码；K3 最后一层固定为全局注意力 | 相同 1.4T token 配方下超过全 MLA 基线；KV 缓存最多少 75% | 7:1 时分布外验证明显变差；作者把长上下文检索列为纯线性结构的主要瓶颈 |
| [Qwen3.5](../../papers/qwen3.5/README.md)（2026-02）→ Qwen3.6（2026-04） | Gated DeltaNet:门控注意力 = 3:1（沿用 Qwen3-Next），稠密的 27B 与 MoE 都用 | 原生 262K，可扩展到约 1M | 只有模型卡，没有消融 |
| [Nemotron 3](../../papers/arxiv-2512.20856/README.md)（NVIDIA 2025-12） | Mamba-2 与 MoE 交错为主，只留少数注意力层，注意力层不用 RoPE | Nano 吞吐为 Qwen3-30B-A3B 的 3.3 倍（8K 入、16K 出）；1M RULER 54.19 | 白皮书未给出层比例；1M 上仍只有约一半 |

做不好的场景：[Repeat After Me](../../papers/arxiv-2402.01032/README.md) 证明固定状态的模型无法准确复制比状态比特数更长的串，学会复制长度 300 的串所需样本是 Transformer 的 100 倍以上；Jamba 中 1.3B 的纯 Mamba 在 IMDB 上常不按"Positive / Negative"作答，得分 48.8，纯注意力 84.1，混合 90.9；Based 测得召回密集任务上注意力比 Mamba 高 32.2 个百分点。

站在现在看过去：

- `[判断]` 2020 与 2023 年的两篇奠基论文都没有用召回类任务检验自己：线性注意力只测图像与语音，Mamba 的语言实验以困惑度与常识推理为主。2024 年 Based、Repeat After Me 用合成召回与复制任务、Jamba 用格式遵循，才把代价测出来，而 Mamba 在困惑度上本来是领先的。这是"困惑度看不出召回"在架构选择上付出的学费。
- `[判断]` 纯固定状态的结构没有成为前沿模型的主干，它以混合的形式存活：Jamba 保留 1/8 的注意力层，Kimi Linear 与 K3 保留 1/4，K3 再把最后一层固定为全局注意力。比例怎样定，各家都只给出自己条件下的消融，而 Kimi Linear 的 7:1 只在分布外验证上露出问题，训练损失看不出来。
- `[判断]` 在递推状态谱系里看，这条线的进步都落在"转移矩阵"上：从单位阵（只累加、不遗忘）到随输入变化的衰减（Mamba）、再到逐通道的遗忘门（KDA）。能否遗忘决定了固定大小的状态里装的是不是有用的东西，但遗忘解决不了状态容量的上限，这就是混合的理由。

### 4 FFN 与 MoE：从 Switch 到细粒度专家与无辅助损失均衡

结论：MoE（混合专家：把 FFN 拆成许多专家，每个 token 只送到少数几个）让总参数与每 token 计算分开；早期的问题是训练不稳和负载不均，此后几代分别从数值精度、专家粒度、均衡方式上修补，到万亿参数级又出现了新的不稳定。

| 节点 | 改了什么 | 换来什么 | 做不好的地方 |
|---|---|---|---|
| [Switch Transformer](../../papers/arxiv-2101.03961/README.md)（Google 2021） | 每个 token 只送 1 个专家；每个专家容量固定（超出的 token 被丢弃、直接走残差）；路由器局部用 float32；初始化缩小 10 倍；微调时专家内 dropout 加大 | 相同计算下预训练最多快 7 倍；首次用 bfloat16 训练大型稀疏模型 | 最大的 Switch-XXL 偶有不稳定，作者写明未解决；微调中小数据集易过拟合；ARC 上没有收益；把注意力的 Q、K、V 专家化在 bfloat16 下不稳定 |
| [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md)（2024） | 专家切细（更多更小的专家、每 token 激活更多个），并隔离出所有 token 共用的共享专家 | 2B 规模与专家参数和计算量都是其 1.5 倍的 GShard 相当 | 16B 在选择题上偏弱，作者归因于注意力参数只有约 0.5B |
| [无辅助损失均衡](../../papers/arxiv-2408.15664/README.md)（DeepSeek 2024）→ [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md) | 用按负载调整的路由偏置代替负载均衡辅助损失 | 1B 模型验证困惑度 9.56 → 9.50，全局负载偏离 0.72 → 0.04 | 验证只到 3B；V3 仍保留极小的序列级损失 |
| Kimi K2、K3；DeepSeek-V4 | K2 按稀疏度规模定律把专家增到 384；K3 用 896 个专家、在半宽潜空间里计算，按分位数设定偏置；V4 前 3 个 MoE 层按 token ID 哈希路由 | 固定激活参数时，专家越多损失越低（K2） | V4 训练中 MoE 层离群值引发损失尖峰，两种修补的原理不明；K3 的路由分支出现内部激活爆炸，近千个专家超出逐步调偏置的适用范围 |
| Qwen3.5、MiniMax-M2、Nemotron 3（2025-12 – 2026） | Qwen3.5 用 512 个专家、每 token 激活 10 个路由专家加 1 个共享专家；MiniMax-M2 用 256 个专家激活 8 个、sigmoid 门控加可学习的逐专家偏置；Nemotron 3 的 LatentMoE 把 token 投到更小的潜空间里路由与计算，路由参数与 all-to-all 通信约省 4 倍 | 极低激活比（MiniMax-M2 每 token 激活 4.3%）；LatentMoE 省下的预算用于更多专家 | 三家都未给出与本表前几代的同条件对照 |

各代的专家数、激活数与均衡方式的对照表在[预训练方向](../pretraining/README.md)"更深更大的网络"一节。

做不好的场景：Switch 原文给出三个早期 MoE 的坑。容量固定意味着负载不均时 token 被丢弃，加大容量又浪费计算和通信；稀疏模型参数多，在小数据集上微调更容易过拟合；1.6T 的 Switch-C 与 395B 的 Switch-XXL 困惑度相近，SQuAD 却低近 2 分，参数量、每 token 计算与微调质量的关系没弄清。

站在现在看过去：

- `[判断]` 早期 MoE 的不稳定被分三层处理：数值（Switch 的 float32 路由器）、结构（DeepSeekMoE 的细粒度与共享专家）、目标（无辅助损失均衡把均衡从损失函数里拿出来）。但规模到 1.6T–2.8T 时不稳定以新形式回来（V4 的离群值、K3 的激活爆炸），说明稀疏带来的数值问题只是被推后了。
- `[判断]` MoE 让 FFN 越来越大，注意力占的参数比例随之下降，代价落在依赖注意力的能力上：DeepSeekMoE 16B 的选择题短板、Kimi K2 为了 128K 推理成本把注意力头从 128 减到 64。为什么稀疏化的是 FFN 而不是注意力，见[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 7 节：Switch 附录 A 的专家化注意力在 bfloat16 下不稳定，是原因之一。

### 5 归一化、残差与门控：深度方向的信息流

结论：Pre-LN 解决了"训练要靠预热"的问题，却让深层的贡献被稀释；2024–2026 年三家用三种办法重新设计残差流，同时在每个会放大数值的地方补上归一化或门控。

| 节点 | 改了什么 | 换来什么 | 做不好的地方 |
|---|---|---|---|
| Post-LN（Transformer 2017） | 残差相加之后做层归一化 | 原始配方 | 必须先用小学习率预热：IWSLT14 德→英不预热时 BLEU 8.45，预热后约 34 |
| [Pre-LN](../../papers/arxiv-2002.04745/README.md)（Microsoft Research Asia 等 2020） | 归一化移到子层输入，残差通路保持恒等 | 可以去掉预热，收敛更快 | 深层输入输出高度相似（ShortGPT）；隐藏状态幅度随层数增长、每层贡献被稀释（Attention Residuals） |
| QK-Norm 与门控（Wortsman 等 2023、[Gated Attention](../../papers/arxiv-2505.06708/README.md) 2025） | 对 Q、K 归一化；在注意力输出后加逐头 sigmoid 门 | 压住注意力 logit 与大激活值；Gated Attention 可以用更大的学习率，首 token 注意力 46.7% → 4.8% | QK-Norm 与 MLA 不兼容；门控为什么改善长度外推，原文未从理论上解释 |
| [Hyper-Connections](../../papers/arxiv-2409.19606/README.md)（ByteDance 2024） | 残差流扩成 n 条，可学习的深度与宽度连接 | OLMoE 上收敛快 1.8 倍 | 混合矩阵无约束：27B 模型约第 12k 步损失突升，复合增益峰值约 3000（mHC 的测量） |
| [mHC](../../papers/arxiv-2512.24880/README.md)（DeepSeek 2025） | 混合矩阵约束为双随机矩阵 | 恢复恒等映射，额外开销 6.7%；DeepSeek-V4 采用 | 原文未单列局限 |
| [Attention Residuals](../../papers/arxiv-2603.15031/README.md)（Kimi 2026） | 用跨层注意力有选择地取回前面各层的输出 | 块级版本相当于基线多用 1.25 倍算力；Kimi K3 采用 | 全量版本的显存与通信随层数增长，因此要分块 |

做不好的场景：[ShortGPT](../../papers/arxiv-2403.03853/README.md) 把 pre-norm 模型深层"输入输出相似"作为删层的依据，删掉 25% 的层后选择题只小幅下降，但 7B 模型的生成类任务（XSum、C3）几乎降到零，冗余并不等于可以随便删。Jamba 在 Mamba 层内部、Kimi K3 在专家聚合之后都要额外加 RMSNorm 才能稳定。

站在现在看过去：

- `[判断]` Pre-LN 用"训练容易"换来了"深层效率低"，代价要到模型很深之后才显现：Pre-LN 的理论解释在 2020 年，ShortGPT 与 Hyper-Connections 指出深层冗余与表示坍缩在 2024 年，DeepSeek 与 Kimi 的两种解法在 2025–2026 年。两种解法怎样比较，见预训练方向"更深更大的网络"一节。
- `[判断]` 稳定性部件越来越跟着新模块走：每引入一个会放大数值的结构（MLA、Mamba 层、万亿级 MoE 的路由分支），就要在它旁边补一处归一化或截断。这使"架构"与"训练配方"难以分开比较。

### 6 条件记忆：把静态知识从计算里拿出来

结论：[Engram](../../papers/arxiv-2601.07372/README.md) 在 MoE 的条件计算之外加了第二条稀疏轴：按当前 token 与前几个 token 组成的 N-gram 做哈希，从大嵌入表里直接取出向量，经门控加回残差流。

- **换来什么**：总参数与每 token 计算都固定时，把约 20%–25% 的稀疏参数从专家挪给查表，验证损失最低（U 形曲线）；Engram-27B 相对同参数、同计算的 MoE-27B，BBH +5.0、HumanEval +3.0，长上下文扩展后多查询大海捞针 84.2 → 97.0。地址只取决于 token，推理前就知道，所以表可以放在主机内存里提前取：100B 参数的表放到主机内存，开销低于 3%。
- **进入生产**：[DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md) 接入 196B 参数的 Engram（两个模块，放在第 1 与第 14 层），并去掉了原设计中的短卷积，理由是收益抵不过推理系统里增加的复杂度。
- **做不好的场景**：U 形曲线的另一端说明记忆不能替代计算，几乎全给查表时依赖上下文的推理受损；放得早能更早卸下局部模式，放得晚门控更准、预取延迟更好藏，位置要折中；Engram-40B 没有在所有任务上超过 27B，作者归因于训练不足。表与分词器绑定、搬到别的模型上要重新训练读取器，这两点由后续的 [Tokenizer-Agnostic Engram Module](../../papers/arxiv-2607.29065/README.md) 与 [Frozen Memory Is Not Enough](../../papers/arxiv-2608.17050/README.md) 处理。
- **站在现在看过去**：`[判断]` "FFN 是键值记忆"在 2020 年是可解释性的观察，2026 年变成了可以单独扩容、单独放在主机内存里的模块；证据链见[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 8–9 节。

### 7 KV 缓存的账：五种压缩手段

结论：KV 缓存可以从五个方向压，各压一个维度，可以叠加；DeepSeek 五代模型几乎把五个方向都用上了。

| 手段 | 压缩的维度 | 代表与数字 | 做不好的地方 |
|---|---|---|---|
| 少存几个头 | 头数 | MQA、GQA；Llama 3 用 8 个 KV 头 | 头越少质量越受影响（DeepSeek-V2 附录 D.1） |
| 存低维表示 | 每个位置的宽度 | MLA：KV 为同规模多头模型的 14%（16B MoE）与 4%（250B MoE） | 加不了 QK-Norm |
| 少存位置 | 历史长度 | 局部窗口（Gemma）、固定状态与混合（Jamba 4GB 对 Mixtral 32GB，Kimi Linear 少 75%）、沿序列压缩（V4 的 CSA/HCA）、逐出（H2O、StreamingLLM） | 召回受限；事后逐出在长文任务上掉分 |
| 少存比特 | 数值精度 | [KIVI](../../papers/arxiv-2402.02750/README.md) 的 2 比特免训练量化；DeepSeek-V4 的 FP8、V4.1-Flash 的 FP4 KV（训练中做量化感知） | KIVI 在已用 MQA 的 Falcon-7B 上需要 4 比特 |
| 跨层共享 | 层数 | V4.1-Flash 的 CSA2 让后面的层复用前面层的全局 KV 与 top-k 选择 | 自述选择误差的鲁棒性边界未完全刻画 |

`[判断]` DeepSeek 把每 token 的 KV 字节数当作跨代的核心指标：V2 用 MLA 比 67B 少 93.3%，V4 在 1M 上下文下约为 BF16、8 组 GQA 的 2%，V4.1-Flash 的报告直接画出了从 V1 到 V4.1-Flash 每 token 全局 KV 的下降曲线（约 437 倍）。每一步换一个压缩维度，而前一步的手段保留下来。

## DeepSeek 架构线：一个团队怎样逐个部件改

结论：DeepSeek 在 2024–2026 年的这一串报告里，几乎每篇只换一两个部件，并保留上一代验证过的部件；把它们排成一列，就是上面七条谱系中五条的同一家实例。每一步"留下的问题"往往就是下一步的出发点。

| 顺序 | 论文 | 改的部件 | 改法 | 换来什么 | 留下的问题或自述局限 |
|---|---|---|---|---|---|
| 1 | [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md)（2024） | 通道混合（FFN） | 专家切细，加共享专家 | 2B 规模与 1.5 倍专家参数和计算的 GShard 相当 | 16B 选择题偏弱，作者归因于注意力参数少 |
| 2 | [DeepSeek-V2](../../papers/deepseek-v2/reading.md)（2024） | 注意力的 KV | MLA：缓存一个低维潜向量加一个位置键；FFN 沿用 DeepSeekMoE，配三项负载均衡损失 | KV 缓存比 67B 少 93.3%，最大生成吞吐 5.76 倍 | 负载均衡损失系数两难；MLA 加不了 QK-Norm |
| 3 | [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)（2024） | MoE 的均衡方式；训练目标 | [无辅助损失均衡](../../papers/arxiv-2408.15664/README.md)（按负载调路由偏置）；多 token 预测 MTP（每个位置额外预测再下一个 token，推理时可丢弃或用作投机解码的草稿） | 671B 总参数、37B 激活；MTP 的第二个 token 接受率 85%–90% | 推荐的部署单元较大，小团队负担重（§6） |
| 4 | [NSA](../../papers/arxiv-2502.11089/README.md)（2025） | 注意力的读取范围 | 压缩块、选块、滑窗三路，从预训练开始训练 | LongBench 平均高于全注意力；64K 解码最多快 11.6 倍 | 验证规模为 27B 总参数、270B token（实验设置一节；引言写 260B）；第一层要换回普通 MLP 才稳定 |
| 5 | [DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md)（2025） | 注意力的读取范围 | DSA：轻量索引器为每个查询选 2048 个 KV，建在 MLA 之上；从 V3.1-Terminus 继续训练，先稠密预热 1000 步、2.1B token，再稀疏训练 943.7B token | 长上下文推理成本下降 | 索引器本身仍随长度平方增长（§2）；自述世界知识广度落后 |
| 6 | [Hyper-Connections](../../papers/arxiv-2409.19606/README.md)（ByteDance，2024）→ [mHC](../../papers/arxiv-2512.24880/README.md)（2025） | 深度方向（残差流） | 残差流扩成多条；mHC 把混合矩阵约束为双随机矩阵 | 恢复恒等映射，扩展 4 倍时额外开销 6.7% | HC 在 27B 上约第 12k 步损失突升，复合增益峰值约 3000（mHC 的测量） |
| 7 | [Engram](../../papers/arxiv-2601.07372/README.md)（2026） | 通道混合旁新增记忆轴 | N-gram 哈希查表，经门控加回残差流 | 同参数、同计算下优于 MoE-27B；100B 的表放主机内存开销低于 3% | 分配比例呈 U 形；Engram-40B 训练不足 |
| 8 | [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)（2026） | 注意力（压缩加稀疏）、残差流、路由 | CSA/HCA 交错，加滑窗分支与可学习 sink；残差改为 mHC；前 3 个 MoE 层按 token ID 哈希路由；保留 MTP | 1M 上下文下单 token FLOPs 为 V3.2 的 27%、KV 为 10% | 训练中损失尖峰，Anticipatory Routing 与 SwiGLU 截断的原理不明；结构偏复杂（§6） |
| 9 | [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)（2026） | KV 缓存、层组织、记忆 | CSA2 跨层复用全局 KV 与 top-k；FP4 KV；因果编码器-解码器；接入 196B 的 Engram；骨干预训练去掉 MTP，改用单独训练的 DSpark 草稿器 | 全局 KV 约 890 字节/token，约为 DeepSeek-V1 的 1/437 | 选择误差与滑窗状态近似重建的鲁棒性边界未刻画（§6） |

`[判断]` 这条线有三个特点。第一，到 V4 为止部件几乎只增不减：DeepSeekMoE 从第 1 步留到第 9 步，MLA 从 V2 留到 V3.2（DSA 直接建在 MLA 上），mHC 与 Engram 各在下一代模型里落地，V4 自述"为降低风险保留了许多组件"。第二，几乎每一步都把一个外部或自家的研究原型放大进旗舰模型：无辅助损失均衡 → V3，NSA → V3.2 的 DSA → V4，Hyper-Connections → mHC → V4，Engram → V4.1-Flash。第三，代价随部件叠加而集中到稳定性与复杂度上：V4 的尖峰与"结构偏复杂"、V4.1-Flash 的鲁棒性边界，都是在这条线的末端才写出的局限。成批的删减直到 V4.1-Flash 才出现：骨干预训练去掉 V3 起使用的 MTP，注意力去掉 HCA、CSA 的重叠压缩与绝对位置偏置、单独的索引键压缩路径，训练去掉稠密预热（V4.1 §1–§2）；哈希路由与查询 RMSNorm 很可能也被去掉，依据是官方 config 与 FlashMLA README，原文没有逐项说明（未核实）。这说明 V4 为降低风险保留的组件里，有一部分在下一代被证明可以拿掉，见 [V4.1-Flash 精读](../../papers/arxiv-2609.19969/reading.md)。

## 主线历史

结论：2017–2022 年是在原始 Transformer 上逐个部件打补丁；2023–2024 年递推结构回归、稀疏专家规模化；2025–2026 年注意力、深度方向与记忆一起被重新设计，KV 缓存成为一等目标。每个节点先写上一节点留下的问题。

1. **Transformer（2017，Google）**。多头注意力、Post-LN、稠密 FFN，目标是 WMT 翻译的 BLEU（英→德 28.4）。**做不好**：原文把"高效处理长输入的局部注意力"列为未来方向；生成时每步要重读全部 KV；Post-LN 离不开学习率预热。
2. **给注意力和归一化打补丁（2019–2020）**。留下的问题：解码慢、长序列贵、训练要预热。改变：[MQA](../../papers/arxiv-1911.02150/README.md) 共享 KV，解码器每 token 快约 12 倍；[线性注意力](../../papers/arxiv-2006.16236/README.md)把复杂度降到线性并写成 RNN；[Pre-LN](../../papers/arxiv-2002.04745/README.md) 解释并去掉预热。**做不好**：MQA 质量下降、从头训练不稳（GQA 附录 A）；线性注意力在语音上明显差于 softmax（8.08 对 5.12），没有在语言建模上检验；Pre-LN 的深层冗余要到 2024 年才被指出。
3. **稀疏专家规模化（2021–2022）**。留下的问题：稠密模型增加参数就同比增加每 token 计算。改变：[Switch](../../papers/arxiv-2101.03961/README.md) 用 top-1 路由把 MoE 简化到可以用 bfloat16 训练到 1.6T 参数，评测是 C4 困惑度加 SuperGLUE 微调。**做不好**：最大模型不稳、丢 token、微调过拟合，参数多的模型下游不一定更好。
4. **递推结构回归，GQA 成为默认（2023）**。留下的问题：注意力的计算与 KV 随长度增长，线性注意力质量不够。改变：[LRU](../../papers/arxiv-2303.06349/README.md) 说明 SSM 的关键成分可以从 RNN 推出来；[Mamba](../../papers/mamba/reading.md) 的选择性 SSM 在 1B 级困惑度上追平 Transformer++（PaLM/LLaMA 式的现代配方）；[GQA](../../papers/arxiv-2305.13245/README.md) 折中 MQA 与多头，随后成为 Llama 3、Qwen2.5、Qwen3 的默认配置。目标从 LRA 移到 Pile 困惑度与合成的选择性复制任务。**做不好**：Mamba 只验证到 3B 级，复制与召回的缺陷要到 2024 年才被测出。
5. **混合架构与 DeepSeek 的稀疏栈（2024）**。留下的问题：固定状态的模型召回差；稠密注意力的 KV 太大；MoE 均衡两难。改变：[Based](../../papers/arxiv-2402.18668/README.md) 与 [Repeat After Me](../../papers/arxiv-2402.01032/README.md) 用合成召回与复制把缺口量化，[Jamba](../../papers/arxiv-2403.19887/README.md) 以 1:7 的注意力:Mamba 混合发布开放权重；DeepSeek 一年内连出 [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md)、[V2](../../papers/deepseek-v2/reading.md)（MLA）、[无辅助损失均衡](../../papers/arxiv-2408.15664/README.md)与 [V3](../../papers/arxiv-2412.19437/README.md)。**做不好**：Jamba 的 Mamba 层在 7B 级出现损失尖峰；DeepSeekMoE 的选择题短板；MLA 加不了 QK-Norm。
6. **训练时稀疏、规模化的线性混合、门控与超连接（2025）**。留下的问题：推理期稀疏猜不准；混合架构缺少大规模、同配方的对照；深层冗余。改变：[NSA](../../papers/arxiv-2502.11089/README.md) 与 DSA 把稀疏放进训练；[Kimi Linear](../../papers/arxiv-2510.26692/README.md) 在 1.4T token 上让 3:1 混合超过全注意力；[Gated Attention](../../papers/arxiv-2505.06708/README.md) 用门控消除注意力汇聚；[Hyper-Connections](../../papers/arxiv-2409.19606/README.md) 扩宽残差流，[mHC](../../papers/arxiv-2512.24880/README.md) 给它加约束。评测移到 RULER、LongBench。**做不好**：DSA 的索引器仍是平方复杂度；7:1 混合分布外变差；无约束的超连接在 27B 上不稳。
7. **深度与记忆成为新轴，KV 缓存成为一等目标（2026）**。留下的问题：百万上下文与长程智能体让 KV 存储和预填充成为部署成本的主体。改变：[Attention Residuals](../../papers/arxiv-2603.15031/README.md)、[Engram](../../papers/arxiv-2601.07372/README.md)、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)（CSA/HCA + mHC）、[Kimi K3](../../papers/arxiv-2607.24653/README.md)（KDA 混合 + AttnRes + LatentMoE）、[V4.1-Flash](../../papers/arxiv-2609.19969/README.md)（跨层 KV 复用 + FP4 + Engram）。报告开始按"每 token KV 字节"和"解码 FLOPs 随上下文长度的曲线"比较各代模型。**做不好**：V4 自述结构偏复杂、训练尖峰的修补原理不明；V4.1-Flash 自述鲁棒性边界未刻画清楚；Engram 的收益随分配比例呈 U 形。

## 趋势

以下都是跨论文的 `[判断]`，支撑论文与反例列在批注里。

1. **注意力层不再同质。** 一个模型里交错使用不同类型的层：局部与全局（Gemma 5:1）、线性与全注意力（Jamba 1:7、Kimi 3:1）、只滑窗与压缩稀疏（DeepSeek-V4 前两层只用滑窗）。精确的全局读取只留在少数层，比例落在 1/8 到 1/4。
2. **稀疏从 FFN 扩展到注意力和记忆。** 条件计算（MoE 选专家）→ 条件读取（稀疏注意力选 KV 块）→ 条件记忆（Engram 按 N-gram 查表）。三者都是"总量很大、每个 token 只用一小部分"。
3. **效率结构从事后改造移到训练之初。** 推理期逐出与稀疏（H2O、Quest）让位于训练时稀疏（NSA 到 V4.1-Flash），混合架构从头训练。反例是 GQA：从多头检查点升级训练只花 5% 的算力，事后改造在 KV 头数这个维度上是成功的。
4. **KV 缓存成为一等设计目标。** 从 MQA 的"解码受带宽限制"开始，到 V4.1-Flash 以 KV 压缩为题目，每 token 字节数成为跨代比较的主指标。
5. **深度方向被重新设计。** Pre-LN 的固定求和被可学习、受约束的混合（mHC）或跨层注意力（AttnRes）替代，层的位置（查表放第 2 层、前 3 层用哈希路由、最后一层用全局注意力）成为设计变量。

## 主要路线与团队偏好

结论：公开详细技术报告的团队，可以从多篇报告里读出押注与代价；同一团队在两篇以上论文中、在有替代方案时重复同一选择，才算偏好。

| 团队 | `[判断]` 押注 | 代表 | 代价与做不好的地方 |
|---|---|---|---|
| DeepSeek | 保留 Transformer 主体，在内部做压缩与稀疏，并把 KV 字节数当作跨代指标 | DeepSeekMoE、V2（MLA）、V3、NSA、V3.2（DSA）、mHC、Engram、V4（CSA/HCA）、V4.1-Flash | 部件越叠越多，V4 自述结构偏复杂；稳定技巧原理不明；V3 部署单元大 |
| Kimi（Moonshot AI） | 改造序列方向（KDA 线性注意力混合）与深度方向（跨层注意力）的信息流；注意力的全局层沿用 DeepSeek 的 MLA | K2、Kimi Linear、Attention Residuals、K3 | 线性部分召回受限，保留 1/4 全注意力；近千个专家时激活爆炸 |
| Google（含 Gemma 团队） | 在注意力上省 KV（MQA → GQA → Gemma 4 的 key 兼作 value）；稀疏专家；开放模型坚持局部/全局交错 | MQA、Switch、GQA、Gemma 2/3/4 | MQA 质量与稳定；Switch-XXL 不稳；Gemini 等闭源模型不公开结构细节 |
| Meta | 到 Llama 3 为止：稠密结构加 GQA，换取稳定与简单；Llama 4 起改为 MoE | Llama 3；[ScaleRL](../../papers/arxiv-2510.13786/README.md)（Llama-4 Scout） | 稠密模型每 token 计算随参数增长 |
| 阿里巴巴 Qwen | GQA 加 QK-Norm 的稠密/MoE 模型；研究注意力内部的门控 | Qwen2.5、Qwen3、Gated Attention | 门控的作用机制尚无理论解释 |
| 学界与 AI21（CMU、Princeton、Stanford、Harvard、AI21） | 用递推状态替代或部分替代注意力，并用合成任务测量代价 | LRU、Mamba、Based、Repeat After Me、Jamba | 规模多在 3B 以下；纯 SSM 召回与上下文学习弱 |
| ByteDance Seed | 改造残差连接 | Hyper-Connections | 无约束的混合在更大规模上不稳（mHC 的测量） |
| 智谱（GLM） | 不自研注意力，直接采用 DeepSeek 的 DSA，并在 9B 上比较了滑窗与线性注意力 | [GLM-5](../../papers/arxiv-2602.15763/README.md) | 128K 上比稠密低 0.35 分 |
| MiniMax | 从 Lightning Attention 混合（MiniMax-Text-01）退回全注意力，等基础设施与评测成熟 | [MiniMax-M2](../../papers/arxiv-2605.26494/README.md) | 长序列成本按平方增长 |
| NVIDIA | Mamba-2 为主的混合加 LatentMoE，全部公开 | [Nemotron 3](../../papers/arxiv-2512.20856/README.md) | 层比例与消融在白皮书中未量化 |
| 阿里巴巴 Qwen（2026 起） | 从 GQA 稠密/MoE 转为 Gated DeltaNet 3:1 混合 | [Qwen3.5](../../papers/qwen3.5/README.md) | 只有模型卡 |
| OpenAI（开放权重） | 窗口层与稠密层交替、GQA、可学习的 sink 偏置、MoE 权重 4 位（MXFP4）后训练量化 | [gpt-oss 模型卡](https://arxiv.org/abs/2508.10925) | 闭源主力模型的结构仍不公开 |

`[判断]` 收敛与分化：MoE 与"少量全局层 + 大量省 KV 的层"已是开源大模型的共同选择；KV 缓存压缩各家都做。分化在三处：长上下文用训练时稀疏（DeepSeek）还是线性混合（Kimi）；注意力汇聚是消除（Qwen）还是显式提供（DeepSeek-V4）；残差流用约束混合（DeepSeek）还是跨层注意力（Kimi）。

## 当前开放问题

- **精确注意力最少要留多少，留在哪几层？** Based 的下界说明不能为零；各家的比例（Jamba 1:7、Kimi 3:1、Gemma 局部:全局 5:1、K3 最后一层全局）都只在各自条件下消融过，没有同条件的跨家对照。入口：[Based](../../papers/arxiv-2402.18668/README.md)、[Jamba](../../papers/arxiv-2403.19887/README.md)、[Kimi Linear](../../papers/arxiv-2510.26692/README.md)。
- **稀疏选择出错时怎样发现、怎样兜底？** V4.1-Flash 写明选择误差可能在未测试的边界情形下损害能力，并计划专门压力测试长上下文的稀疏检索；DSA 的索引器仍是平方复杂度。入口：[NSA](../../papers/arxiv-2502.11089/README.md)、[DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)、[长上下文方向](../long-context/README.md)。
- **深层冗余解决了吗？** mHC 与 Attention Residuals 都报告了收益，但都没有用 ShortGPT 式的删层实验检验深层是否仍然冗余。入口：[mHC](../../papers/arxiv-2512.24880/README.md)、[Attention Residuals](../../papers/arxiv-2603.15031/README.md)、[ShortGPT](../../papers/arxiv-2403.03853/README.md)。
- **条件记忆的边界在哪里？** U 形曲线给出了一个规模下的最优比例，Engram-40B 训练不足；查表能否移植到别的模型、别的分词器。入口：[Engram](../../papers/arxiv-2601.07372/README.md)、[关系页](../../../foundations/relations/attention-ffn-division.md)第 9 节。
- **稀疏结构放大后的不稳定有没有统一原理？** Switch-XXL、Jamba 的 Mamba 层、DeepSeek-V4 的 MoE 离群值、K3 的路由分支都靠局部补丁稳住。入口：[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md)、[预训练方向](../pretraining/README.md)的同名开放问题。

## 阅读顺序

1. [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10、12.4、14 节 → [Transformer 精读](../../papers/transformer/reading.md)：先算清一层的计算和 KV 缓存的账，后面每条线都在改这本账的某一项。
2. [MQA](../../papers/arxiv-1911.02150/README.md) → [GQA](../../papers/arxiv-2305.13245/README.md) → [DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md)第 1–3 节：头与 KV 一线，V2 精读里有 MLA 的手算。
3. [递推状态谱系](../../../foundations/relations/recurrent-state.md) → [线性注意力](../../papers/arxiv-2006.16236/README.md) → [Mamba 精读](../../papers/mamba/reading.md) → [Repeat After Me](../../papers/arxiv-2402.01032/README.md) 与 [Based](../../papers/arxiv-2402.18668/README.md) → [Jamba](../../papers/arxiv-2403.19887/README.md) → [Kimi Linear](../../papers/arxiv-2510.26692/README.md)：先看固定状态怎样省，再看它做不好什么，最后看混合怎样补。
4. [Switch](../../papers/arxiv-2101.03961/README.md) → [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) → [无辅助损失均衡](../../papers/arxiv-2408.15664/README.md) → [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md) → [Engram](../../papers/arxiv-2601.07372/README.md)：通道混合一线，从条件计算到条件记忆。
5. [Pre-LN](../../papers/arxiv-2002.04745/README.md) → [Hyper-Connections](../../papers/arxiv-2409.19606/README.md) → [mHC](../../papers/arxiv-2512.24880/README.md) 与 [Attention Residuals](../../papers/arxiv-2603.15031/README.md)：深度方向，后两篇对照着读。
6. 按"DeepSeek 架构线"一节的表格顺序读：[DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) → [DeepSeek-V2](../../papers/deepseek-v2/reading.md) → [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md) → [NSA](../../papers/arxiv-2502.11089/README.md) → [DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md) → [mHC](../../papers/arxiv-2512.24880/README.md) → [Engram](../../papers/arxiv-2601.07372/README.md) → [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) → [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)：每篇只问"这一步换了哪个部件、保留了哪些"，读完就是一条团队内部的架构史，终点是训练时稀疏与 KV 压缩。

按部件拆分的基线见 [Baseline 页](BASELINES.md)，带检验题的路线见[路线图](ROADMAP.md)，本方向收录的论文见[论文目录](PAPERS.md)。

## 批注

**易误读**

- MQA 的"46 μs → 3.8 μs"是 TPUv2 上、批量 1024、源与目标各 128 token 的翻译模型解码器每 token 摊销时间（MQA Table 2）；GQA 的 1.51 与 0.28 是 T5-XXL 每个样本在每块 TPUv4 上的推理时间（GQA Table 1）。两组数不能互相换算。
- DeepSeek-V2 附录 D.1 的 MHA/GQA/MQA 对照是 7B 稠密模型、1.33T token，各模型通过调整层数把参数对齐到约 7B；附录 D.2 的 MLA 对 MHA 是 MoE 模型。正文"MQA 在 7B 上让 MMLU 降 7.3 分"指前者。
- "约 437 倍"是 V4.1-Flash Figure 1(b) 中每 token **全局** KV 缓存相对 DeepSeek-V1 的倍数；滑动窗口部分的 KV 另算（V4.1-Flash §1）。DeepSeek-V4 的"约 2%"以 BF16、8 组 GQA、每头 128 维为基线，1M 上下文（V4 §2）。
- NSA 表中 H2O、Quest 的分数是 NSA 作者在自己的 27B 模型上、按每查询约 2560 个 token 的统一预算复现的，不是这些方法原论文的结果。
- 线性注意力的"4462 倍"是 CIFAR-10 逐像素生成的图像/秒之比（Table 2），"4000 倍"是摘要中的概括；同样 7 天训练，线性模型跑的 epoch 约为 softmax 的 3 倍，bits/dim 的比较因此不是同步数对照。
- Engram 摘要写 MMLU +3.4，§4.2 正文写 +3.0，本页不引用这个数，只引用两处一致的 BBH +5.0、HumanEval +3.0。
- Jamba 的 1:3 与 1:7 对照是 1.3B 模型、250B token（Table 4）；IMDB 48.8 / 84.1 / 90.9 也是 1.3B（Table 6）。
- Based 的 32.2 个百分点是 Table 1 中注意力（Transformer++）与 Mamba 在召回密集任务上的平均差；10.36 是 Based 对 Mamba，1.3B、50B token。
- Mamba "3B 常识推理比 Pythia-3B 高 4 分"是原文 §1 的概括（零样本平均）；规模定律对照只到约 1.3B。

**判断的支撑论文**

- MQA 的代价被低估：MQA §4.2 与 Table 1–3、GQA §1 与附录 A、DeepSeek-V2 §2.1 与附录 D.1、DeepSeekMoE 第 5 节（Table 3 讨论）。反例与边界：MQA 原文在 beam-4 测试集上 BLEU 28.5 反而最高；PaLM 用了 MQA（GQA §1 的转述）。
- 同一团队按消融换路线：DeepSeek LLM §2.2 写明 67B 用 GQA；DeepSeek-V2 §1 与 §2.1 以 GQA、MQA 不及 MHA 为由提出 MLA。GQA 作为默认：Llama 3 §3.2、Qwen2.5 §2、Qwen3 §2。
- 省 KV 的结构挡住其他部件：Kimi K2（MLA 与 QK-Norm，见卡片）、NSA §2（Quest 式逐头选择与 GQA）、NSA §3 的按组共享选择。
- 共享 KV 在压缩后回来：DeepSeek-V4 §2 中 CSA、HCA 的 "Shared Key-Value MQA"。
- 推理期稀疏猜不准：NSA §2 与 Table 2、StreamingLLM 卡片的自述局限、V4.1-Flash §1（稀疏注意力 64K 从头训练）。
- 固定状态需要混合：Based §3 与 Theorem 3.1、Repeat After Me §4–5、Jamba §6.2、Kimi Linear §4 与 Table 1、Kimi K3 卡片（最后一层全局）。反例：Mamba 原文的规模定律中纯 Mamba 在 1.3B 以下追平 Transformer++；Jamba Table 5 中 7B、50B token 的纯 Mamba "相当有竞争力"。
- 早期 MoE 的修补层次与新不稳定：Switch §2.4 与 §8、DeepSeekMoE §1–3、无辅助损失均衡 §1–2、DeepSeek-V4 §4.2.3（见卡片）、Kimi K3 卡片。
- MoE 挤压注意力：DeepSeekMoE 第 5 节、Kimi K2（见预训练方向"更深更大的网络"一节）。
- Pre-LN 的代价：Pre-LN §3–4、ShortGPT §2 与附录 A、Hyper-Connections §1、Attention Residuals §1–2（见卡片）。
- 团队偏好按"两篇以上、存在替代方案时重复同一选择"判断：DeepSeek 在 V2、V3、V4、V4.1-Flash 中都保留 DeepSeekMoE，在 NSA、V3.2、V4、V4.1-Flash 中四次推进训练时稀疏；Kimi 在 K2、Kimi Linear、K3 中都用 MLA，在 Kimi Linear、K3 中都用 KDA 混合；Google 在 MQA、GQA 两篇中都以共享 KV 为解码提速，在 Gemma 2、3、4 中都用局部/全局交错；Qwen 在 Qwen2.5、Qwen3 中都用 GQA。Meta 与 ByteDance Seed 在本页只依据一篇报告，写的是该报告的选择，不构成偏好判断。

**与其他论文的关联**

- [预训练方向](../pretraining/README.md)：本页第 1、2 条谱系对应那里的"注意力不丢失""更长更大的注意力"，第 4、5 条对应"损失稳定""更深更大的网络"；那里有 MoE 各代配置表与 MuonClip、FP8 等训练侧细节。
- [递推状态谱系](../../../foundations/relations/recurrent-state.md)：第 3 条谱系的数学底座；该页已补入 Mamba-2（SSD）与 KDA（Kimi Linear）两个节点，以及 2026 年的混合结构（Kimi K3、Qwen3.5）。
- [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)：第 4、6 条谱系的解释链；第 7 节已收入 DeepSeekMoE 的选择题短板、DeepSeek-V2 附录 D 的对照与 Kimi K2 减半注意力头，作为"注意力容量被 MoE 挤压"的证据。
- [模型科学](../../../cross-domain/fields/model-science/README.md)：Jamba 在混合模型中找到 induction head，是该页"大模型上 induction head 只有相关性证据"之外的一条架构侧观察。
- [长上下文方向](../long-context/README.md)与[推理时计算方向](../inference/README.md)：前者讲稀疏与线性结构怎样被评测为长上下文能力，后者讲 KV 量化、投机解码等推理系统手段；DeepSeek-V4.1-Flash 的 DSpark 与 V3 的 MTP 属于后者。

**未核实 / 待验证**

- Gemma 2/3/4 的局部/全局配置取自预训练方向已核实的报告段落，本页只额外核对了 Gemma 3 §5.2 与 Gemma 4 摘要附近的 key 复用 value 一句；Gemini、GPT 系列等闭源模型的结构不写入正文。
- H2O、Quest、MInference、Wortsman 等未单独打开原文，本页只引用 NSA、预训练方向对它们的转述与测量。
- Gated DeltaNet 原文未打开；Mamba-2 已在[递推状态谱系](../../../foundations/relations/recurrent-state.md)按原文核对（A 为标量乘单位阵、SSD 比 Mamba 的 scan 快 2–8 倍、约 10% 注意力层最好）。KDA"在 Gated DeltaNet 基础上改为逐通道遗忘门"取自 Kimi Linear 原文 §1、§3。
- Based 的发表信息以 arXiv v2 页脚为准（ICML 2024 研讨会），是否另有会议正式版未核实。
- Kimi K2 与 K3 的注意力头数、专家配置取自卡片与预训练方向，本轮未重新打开原文。
- 2025-10 以后新增的表格行（GLM-5、Qwen3.5/3.6、Nemotron 3、MiniMax-M2、gpt-oss）依据各篇卡片中核对过的章节；Qwen3.5 只有模型卡，Nemotron 3 只读了总览白皮书，Super 与 Ultra 的单独报告（arXiv 2604.12374、2606.15007）未打开；Gemma 4 的 MoE 版本与 Llama 4 的原始发布材料未打开。

**与原结论的张力（2025-10 以后的材料）**

- 历史：2026-10-04 之前，主要路线表中 Meta 一行只写"稠密结构加 GQA"，依据是 Llama 3；巡检后正文已改正。ScaleRL（Meta 等，2025-10）的实验用的是"17B×16 专家的 Llama-4 Scout MoE"，说明 Llama 4 已是 MoE；这一行描述的是 2024 年的 Llama 3。Meta 2026-04 的 Muse Spark 博客只说重建了结构、优化与数据，没有给出结构。
- 主要路线表中阿里巴巴 Qwen 一行写"GQA 加 QK-Norm 的稠密/MoE 模型"，依据是 Qwen2.5 与 Qwen3；2026 年的 Qwen3.5 与 Qwen3.6 已改为 Gated DeltaNet 与门控注意力 3:1 的混合，与 Kimi 的线性混合同一方向。
- 收敛判断"少量全局层 + 大量省 KV 的层已是开源大模型的共同选择"有一个明确的反例：MiniMax-M2 全部层用全注意力，并写明试过的滑窗混合在多跳推理上变差。"分化：训练时稀疏（DeepSeek）还是线性混合（Kimi）"在 2026 年扩展到其他团队：GLM-5 选了前者，Qwen3.5 与 Nemotron 3 选了后者一侧。
