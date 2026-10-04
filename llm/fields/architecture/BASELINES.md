# 架构与效率的基线

> 状态：Baseline 页 · v2 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 基线是谁、为什么是它

结论：本方向有两个基线。稠密的"Transformer++"定义了 2023 年以后几乎所有对照实验里的参照结构；DeepSeek-V3 式的稀疏结构（MLA + DeepSeekMoE + 无辅助损失均衡）定义了 2025–2026 年大多数架构论文的实验骨架。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| 稠密 Transformer++：[Transformer](../../papers/transformer/reading.md)（2017）的 decoder-only 形式，加上 PaLM、LLaMA 式的改进 | 结构：每层一个因果多头注意力（后来普遍改成 [GQA](../../papers/arxiv-2305.13245/README.md)）加一个稠密 FFN，Pre-LN 式的归一化（多用 RMSNorm），RoPE 位置编码，SwiGLU 激活，不带线性层偏置（[Mamba](../../papers/mamba/reading.md) 原文 §4.2 对 Transformer++ 的定义）。生成时每层每个 KV 头缓存一组 K、V。评估：同数据、同 token 数下的困惑度与下游任务 | Mamba、[Based](../../papers/arxiv-2402.18668/README.md)、[Jamba](../../papers/arxiv-2403.19887/README.md) 都以它为主要对照；Llama 3 在 Llama 2 的基础上只改了 GQA（8 个 KV 头）等少数几处，Qwen2.5、Qwen3 同样以 GQA 稠密结构为主干 |
| 稀疏的 DeepSeek-V3 式结构：[DeepSeek-V2](../../papers/deepseek-v2/reading.md)（2024）定型，[DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)（2024）补上无辅助损失均衡与 MTP | 结构：注意力用 MLA（每个历史 token 只缓存一个低维潜向量加一个位置键），FFN 用 [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md)（细粒度路由专家 + 共享专家），负载均衡用按负载调整的路由偏置。评估：同一内部评测框架下与上一代及其他开源模型对照，同时报告 KV 缓存、训练成本与生成吞吐 | [NSA](../../papers/arxiv-2502.11089/README.md) 的骨干是 GQA + DeepSeekMoE；[mHC](../../papers/arxiv-2512.24880/README.md) 在 V3 式 MoE 上实验；[Engram](../../papers/arxiv-2601.07372/README.md) 以 DeepSeekMoE 的 MoE-27B 为对照；[Kimi K2](../../papers/arxiv-2507.20534/README.md) 的结构仿 V3；[Kimi Linear](../../papers/arxiv-2510.26692/README.md) 以全 MLA 模型为基线 |

两个基线之前还有一个"原点"：2017 年的 Transformer 是 encoder–decoder 结构，用 Post-LN、正弦位置编码、ReLU FFN，MQA、Pre-LN、线性注意力、Switch 这几篇早期工作都以它（或 T5）为对照。

## 基线的结构拆分

结论：一个 LLM 可以拆成七个可替换的部件；两个基线的差别集中在"KV 缓存"和"通道混合"两格，其余基本相同。

| 部件 | 含义 | 稠密基线（Transformer++） | 稀疏基线（DeepSeek-V3 式） |
|---|---|---|---|
| 序列混合 | token 之间怎样交换信息、读多远 | 每层全长的 softmax 因果注意力 | 同左（V3.2 起改为稀疏，见下表） |
| KV 缓存 | 生成时每个历史 token 每层存什么 | 每个 KV 头一组 K、V（GQA 时为组数） | 一个 512 维潜向量 + 一个 64 维位置键（V2 配置） |
| 位置编码 | 位置信息从哪里进入 | RoPE | RoPE，单独走一条解耦的位置分支 |
| 通道混合 | 每个 token 自己的变换；参数大头 | 稠密 SwiGLU FFN | DeepSeekMoE：V3 为 1 个共享 + 256 个路由专家、每 token 激活 8 个；前 3 层稠密 |
| 深度方向 | 层与层怎样串起来 | Pre-LN（RMSNorm）+ 恒等残差 | 同左 |
| 层排布 | 不同类型的层的比例与位置 | 每层相同 | 前 3 层稠密 FFN，其余 MoE |
| 稳定性部件 | 压住会被放大的数值 | QK-Norm（Qwen3、Gemma 3 等）或无 | MLA 加不了 QK-Norm；Kimi K2 改在优化器里做 QK-Clip |

部件之间有依赖：KV 缓存的形式决定能加哪些稳定性部件（MLA 与 QK-Norm），也决定稀疏读取怎样做才省访存（GQA 下要按组共享选择）；序列混合换成固定状态后，位置编码可以去掉（Jamba、Kimi Linear 的全局层）。下表按部件分行，同一篇论文改了几个部件，就在几行出现；标"DeepSeek 架构线"的行是[入门页](README.md)同名一节的九步。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| KV 缓存 | 所有头共用一组 K、V（MQA） | [MQA](../../papers/arxiv-1911.02150/README.md) | 解码器每 token 46 μs → 3.8 μs；代价：从头训练不稳（GQA 附录 A），7B 上 MMLU 45.2 → 37.9（DeepSeek-V2 附录 D.1） |
| KV 缓存 | 分组共享 K、V，并从多头检查点升级训练（GQA） | [GQA](../../papers/arxiv-2305.13245/README.md) | T5-XXL 上质量 47.1 对多头 47.2、推理时间 0.28 对 1.51，升级只花 5% 预训练算力；代价：只在 encoder–decoder 上验证 |
| KV 缓存 | 低秩联合压缩成潜向量（MLA）；DeepSeek 架构线第 2 步 | [DeepSeek-V2](../../papers/deepseek-v2/reading.md) | KV 比 67B 少 93.3%，MoE 中质量好于 MHA；代价：加不了 QK-Norm |
| KV 缓存 | 沿序列压缩后再稀疏读取（CSA/HCA），加可学习 sink；DeepSeek 架构线第 8 步 | [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) | 1M 上下文下单 token FLOPs 为 V3.2 的 27%、KV 为 10%；代价：结构偏复杂 |
| KV 缓存 | 跨层复用全局 KV 与 top-k（CSA2），FP4 存储；DeepSeek 架构线第 9 步 | [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md) | 全局 KV 约 890 字节/token，为 V4-Flash 的约 1/4；代价：选择误差的鲁棒性边界未刻画 |
| KV 缓存 | 2 比特免训练量化（Key 按通道、Value 按 token） | [KIVI](../../papers/arxiv-2402.02750/README.md) | Llama-2-7B 峰值显存降 2.6 倍；代价：已用 MQA 的模型需要 4 比特 |
| 序列混合 | 推理时保留开头 token 加滑动窗口 | [StreamingLLM](../../papers/arxiv-2309.17453/README.md) | 不微调稳定处理 400 万 token；代价：不扩展可用上下文，不适合需要长程记忆的任务 |
| 序列混合 | 训练时就稀疏：压缩块 + 选块 + 滑窗；DeepSeek 架构线第 4 步 | [NSA](../../papers/arxiv-2502.11089/README.md) | LongBench 0.469 对全注意力 0.437，64K 解码最多快 11.6 倍；代价：第一层要换回 MLP 才稳定 |
| 序列混合 | 轻量索引器选 top-k KV（DSA），建在 MLA 上；DeepSeek 架构线第 5 步 | [DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md) | 每查询只读 2048 个 KV；代价：索引器仍随长度平方增长，需要稠密预热 |
| 序列混合 | 线性注意力：核特征映射，因果版即 RNN | [线性注意力](../../papers/arxiv-2006.16236/README.md) | 复杂度降到线性，CIFAR-10 生成吞吐 4462 倍；代价：WSJ 音素错误率 8.08 对 softmax 5.12 |
| 序列混合 | 线性递推、固定转移 | [LRU](../../papers/arxiv-2303.06349/README.md) | 从 RNN 一侧追平 S4（LRA 上）；代价：转移不随内容变化 |
| 序列混合 | 选择性 SSM，无注意力 | [Mamba](../../papers/mamba/reading.md) | 生成吞吐 5 倍；代价：复制与召回差（[Repeat After Me](../../papers/arxiv-2402.01032/README.md)：电话簿查找中 Pythia-410M 胜过 Mamba-2.8B） |
| 序列混合 | 泰勒线性注意力 + 小滑动窗口 | [Based](../../papers/arxiv-2402.18668/README.md) | 召回密集任务比 Mamba 高 10.36 个百分点；代价：固定状态的召回有下界，仍落后于全注意力 |
| 层排布 | 注意力:Mamba = 1:7，加 MoE | [Jamba](../../papers/arxiv-2403.19887/README.md) | 256K KV 缓存 4GB 对 Mixtral 32GB；代价：Mamba 层在 7B 级需要内部 RMSNorm |
| 层排布 | KDA 线性注意力:MLA = 3:1，全局层不用位置编码；最后一层固定为全局 | [Kimi Linear](../../papers/arxiv-2510.26692/README.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md) | KV 最多少 75%，1M 解码吞吐最多 6 倍；代价：7:1 时分布外验证变差 |
| 层排布 | 前 3 个 MoE 层按 token ID 哈希路由；V4-Flash 前两层只用滑窗 | [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) | 早期层做静态、局部的处理；代价：未见单独消融 |
| 通道混合 | top-1 路由的稀疏 MoE，路由器 float32 | [Switch Transformer](../../papers/arxiv-2101.03961/README.md) | 相同计算下预训练最多快 7 倍；代价：最大模型不稳、丢 token、微调过拟合 |
| 通道混合 | 细粒度专家 + 共享专家；DeepSeek 架构线第 1 步 | [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) | 2B 与 1.5 倍规模的 GShard 相当；代价：16B 选择题偏弱 |
| 通道混合 | 无辅助损失的偏置均衡；多 token 预测（MTP）；DeepSeek 架构线第 3 步 | [无辅助损失均衡](../../papers/arxiv-2408.15664/README.md)、[DeepSeek-V3](../../papers/arxiv-2412.19437/README.md) | 1B 验证困惑度 9.56 → 9.50、全局负载偏离 0.72 → 0.04；MTP 推理时可丢弃或用作投机解码草稿；代价：V3 推荐部署单元大 |
| 通道混合 | 在 MoE 旁加 N-gram 哈希查表（条件记忆）；DeepSeek 架构线第 7 步 | [Engram](../../papers/arxiv-2601.07372/README.md)；后续 [Tokenizer-Agnostic Engram](../../papers/arxiv-2607.29065/README.md)、[Frozen Memory Is Not Enough](../../papers/arxiv-2608.17050/README.md) | 同参数、同计算下 BBH +5.0，多查询大海捞针 84.2 → 97.0；代价：分配比例呈 U 形，表与分词器绑定 |
| 深度方向 | 归一化移到子层输入（Pre-LN） | [Pre-LN](../../papers/arxiv-2002.04745/README.md) | 去掉学习率预热；代价：深层冗余（[ShortGPT](../../papers/arxiv-2403.03853/README.md)） |
| 深度方向 | 残差流扩成多条、可学习连接；DeepSeek 架构线第 6 步的前作 | [Hyper-Connections](../../papers/arxiv-2409.19606/README.md) | OLMoE 上收敛快 1.8 倍；代价：混合矩阵无约束，27B 上不稳 |
| 深度方向 | 混合矩阵约束为双随机矩阵；DeepSeek 架构线第 6 步 | [mHC](../../papers/arxiv-2512.24880/README.md) | 27B 上 BBH 51.0 对 HC 48.9、基线 43.8，额外开销 6.7% |
| 深度方向 | 跨层注意力取回前面各层的输出 | [Attention Residuals](../../papers/arxiv-2603.15031/README.md) | 块级版本相当于 1.25 倍算力；代价：全量版本显存与通信随层数增长 |
| 稳定性部件 | 注意力输出后的逐头 sigmoid 门 | [Gated Attention](../../papers/arxiv-2505.06708/README.md) | 首 token 注意力 46.7% → 4.8%，128K 外推 RULER 31.65 → 58.82；代价：机制缺少理论解释 |
| 稳定性部件 | 优化器里按头截断 Q、K 权重（QK-Clip），替代 MLA 用不了的 QK-Norm | [Kimi K2](../../papers/arxiv-2507.20534/README.md) | 15.5T token 上没有损失尖峰；代价：属于事后截断，前 7 万步内 12.7% 的头触发过 |

[DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md)位于"KV 缓存 = MLA"与"通道混合 = 细粒度专家"两格；[Mamba 精读](../../papers/mamba/reading.md)位于"序列混合 = 选择性 SSM"一格，它的召回缺陷由同一部件下的 Based、Repeat After Me 测出，由"层排布"一行的混合架构弥补。

## 批注

**易误读**

- Transformer++ 不是一篇论文，是 Mamba 原文对"PaLM、LLaMA 式现代配方"的称呼；各篇对照实验中的具体配置（是否用 GQA、QK-Norm）不完全相同。
- mHC 的 BBH 三个数是 27B 模型上基线 / HC / mHC 的对照（mHC Table 4）；Engram 的 BBH +5.0 是对同参数、同计算的 MoE-27B。
- KIVI、StreamingLLM 是推理期方法，不改训练；把它们放在 KV 缓存与序列混合两行，是为了与训练时就改结构的方法对照。

**与其他论文的关联**

- [预训练方向的 Baseline 页](../pretraining/BASELINES.md)与[入门页](../pretraining/README.md)从"预训练要解决的问题"出发使用同一批部件；本页从部件出发。
- [递推状态谱系](../../../foundations/relations/recurrent-state.md)解释"序列混合"各行在数学上只差状态转移；[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)解释"通道混合"各行为什么都落在 FFN 一侧。

**未核实 / 待验证**

- Gemma 系列的局部/全局交错未列入上表（本库没有 Gemma 的单篇目录），数字见入门页与预训练方向。
- DeepSeek-V4 前 3 层哈希路由、前两层只用滑窗的单独消融，本轮查阅的段落中未见。
