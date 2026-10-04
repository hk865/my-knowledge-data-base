# 架构与效率路线图

> 状态：路线图 · v2

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md)

结论：六步，按"先算清一层的账 → 头与 KV → 固定大小的状态及其代价 → 通道混合与记忆 → 深度方向 → 沿 DeepSeek 架构线看部件怎样叠起来"排列。前五步各读一条谱系，第六步把它们放回一个团队的九代报告里。每一步都有一个能动手检验的问题。

## 第 1 步：算清一层 Transformer 的账

读 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10、12.4、14 节与 [QKV 讲义](../../../foundations/lessons/15-qkv-deep-dive.md)第 4–5 节，再读 [Transformer 精读](../../papers/transformer/reading.md)。

为什么在这里：本方向的每篇论文都在改这本账的某一项：序列混合的计算、KV 缓存、FFN 参数、残差与归一化。不先算清楚，就分不出一篇论文省的是 FLOPs、显存还是带宽。

检验：对一个 32 层、32 个头、每头 128 维的模型，算出多头注意力下每个历史 token 的 KV 缓存元素数（2 × 32 × 128 × 32 = 262,144），再算 8 组 GQA 和 MQA 下各是多少；说出解码时为什么是显存带宽而不是算力先成为瓶颈（[MQA](../../papers/arxiv-1911.02150/README.md) §2.4.1）。

## 第 2 步：头与 KV 一线

读 [MQA](../../papers/arxiv-1911.02150/README.md) → [GQA](../../papers/arxiv-2305.13245/README.md) → [DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md)第 1–3 节。

为什么在这里：这是[入门页](README.md)谱系第 1 条，也是 KV 缓存第一次被当作设计目标；三篇合起来能看到"小规模测不出代价"的典型：MQA 原文只损失 0.3 的困惑度，五年后 DeepSeek-V2 的 7B 消融里 MMLU 差 7.3 分。

检验：照 V2 精读第 1 节的手算，说出 MLA 每层每 token 缓存 576 个数为什么等于 2.25 组 GQA；再说出 MLA 为什么加不了 QK-Norm、Kimi K2 怎样绕开（入门页谱系第 1 条）。

## 第 3 步：固定大小的状态及其代价

读[递推状态谱系](../../../foundations/relations/recurrent-state.md) → [线性注意力](../../papers/arxiv-2006.16236/README.md) → [Mamba 精读](../../papers/mamba/reading.md) → [Repeat After Me](../../papers/arxiv-2402.01032/README.md) 与 [Based](../../papers/arxiv-2402.18668/README.md) → [Jamba](../../papers/arxiv-2403.19887/README.md) → [Kimi Linear](../../papers/arxiv-2510.26692/README.md)。

为什么在这里：有了第 2 步"每个位置存多少"的概念，才能理解"干脆不按位置存、把整段历史压进一个状态"的收益与代价；先读两篇奠基论文，再读三篇测出代价的论文，最后读两种混合方案，顺序就是"站在现在看过去"的顺序。

检验：用 Based 的 MQAR 任务（先给 64 个键值对再按键提问）说明为什么固定状态的召回有上限；解释 Kimi Linear 的 7:1 混合为什么训练损失看不出问题、分布外验证才看得出（入门页"从测量看"第 3 例）。

## 第 4 步：通道混合与条件记忆

读 [Switch Transformer](../../papers/arxiv-2101.03961/README.md) → [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) → [无辅助损失均衡](../../papers/arxiv-2408.15664/README.md) → [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 7–9 节 → [Engram](../../papers/arxiv-2601.07372/README.md)。

为什么在这里：MoE 与 Engram 都只动 FFN 一侧，它们的理由要靠前三步建立的"注意力读、FFN 存"来理解；Switch 列出的早期 MoE 的坑（丢 token、不稳、微调过拟合），是后面每一篇的出发点。

检验：说出 Switch 的容量因子为什么在"丢 token"与"浪费计算"之间两难，无辅助损失均衡的偏置为什么不进入梯度；再用 Engram 的 U 形曲线说明为什么不能把全部稀疏参数都给查表。

## 第 5 步：深度方向

读 [Pre-LN](../../papers/arxiv-2002.04745/README.md) → [ShortGPT](../../papers/arxiv-2403.03853/README.md) → [Hyper-Connections](../../papers/arxiv-2409.19606/README.md) → [mHC](../../papers/arxiv-2512.24880/README.md) 与 [Attention Residuals](../../papers/arxiv-2603.15031/README.md)（对照着读），旁读 [Gated Attention](../../papers/arxiv-2505.06708/README.md)。

为什么在这里：这是代价显现得最晚的一条线（2020 年的选择，2024 年才被指出冗余），放在最后读，正好检验前几步练出的"从后续工作反推代价"的习惯。

检验：用一句话说出 Post-LN 与 Pre-LN 各自的问题（预热依赖；深层冗余）；说出 Hyper-Connections 为什么在 27B 上不稳，mHC 的双随机约束为什么能让任意多层的复合映射不放大信号。

## 第 6 步：沿 DeepSeek 架构线看部件怎样叠起来

按[入门页](README.md)"DeepSeek 架构线"一节的顺序读：[DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) → [DeepSeek-V2](../../papers/deepseek-v2/reading.md) → [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md) → [NSA](../../papers/arxiv-2502.11089/README.md) → [DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md) → [mHC](../../papers/arxiv-2512.24880/README.md) → [Engram](../../papers/arxiv-2601.07372/README.md) → [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) → [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)。

为什么在这里：前五步各讲一个部件，这一步看同一个团队怎样把它们逐代叠进旗舰模型：每代换一两个部件、保留其余，研究原型（NSA、mHC、Engram）一两代后进入正式模型。读完能把 [Baseline 页](BASELINES.md)里标"DeepSeek 架构线"的九行按时间串起来，也能看到部件叠加后代价集中到稳定性与复杂度上。

检验：为九篇各写一行"改了哪个部件、保留了哪些、自述的局限是什么"，与入门页的表对照；再回答两个问题：V4.1-Flash 为什么去掉 V3 起使用的 MTP（改用预训练后单独训练的 DSpark）；每 token 全局 KV 从 V2 到 V4.1-Flash 各代分别压缩了哪个维度（头、宽度、位置、比特、层，见入门页谱系第 7 条）。

## 读论文时先查什么

比较两篇架构论文之前，先对齐五件事：总参数与激活参数各是多少；训练 token 数与数据是否相同；评测是困惑度、召回类任务还是下游微调；长度是在训练范围内还是外推；效率数字是预填充还是解码、什么硬件和批量。入门页"从测量看"一节的五个翻转例子，都出在其中一项没对齐上。
