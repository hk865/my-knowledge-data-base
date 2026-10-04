# 预训练路线图

> 状态：路线图 · v2

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md)

结论：六步，按"先弄清预训练替后训练准备什么 → 读透两个基线 → 按入门页的问题逐个看后续工作改了哪个部件 → 看两条路线当前的汇合点"排列。每一步都有一个能动手检验的问题；带"示例数值"的算例只用原文给出的数字和公开的近似公式。

## 第 1 步：预训练替后训练准备什么

读入门页["预训练与后训练的分工"](README.md#预训练与后训练的分工)与[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)，再看 [Llama 3](../../papers/arxiv-2407.21783/README.md) 与 [GPT-4](../../papers/arxiv-2303.08774/README.md) 两张文献卡。

为什么在这里：入门页的六个问题都从"为后训练准备合理的结构先验和尽量广的世界知识"这个目的派生出来；不先定位，后面的稳定性、长上下文、MoE 都会读成互不相干的技巧。分工谱系给出"注意力决定从哪里读、FFN 存放事实"的证据，第 5 步讲知识容量时要用到。

检验：DeepSeek LLM 的对话模型 0-shot 的 MMLU（多学科选择题）与基座 5-shot（提示里给 5 个例题）相当，GPT-4 的考试成绩主要来自预训练、校准却被后训练损害。用这两个结果各说一句"后训练改变了什么、没有改变什么"；再说出 DeepSeek-V3.2 为什么在后训练算力超过预训练成本 10% 之后，仍计划扩大预训练算力。

## 第 2 步：读透两个基线

读 [Baseline 页](BASELINES.md)的前两节，对照 [Llama 3](../../papers/arxiv-2407.21783/README.md) 与 [DeepSeek LLM](../../papers/arxiv-2401.02954/README.md) → [DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md) → [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)。

为什么在这里：Llama 3 是写得最清楚的稠密配方，DeepSeek-V3 是后来者逐部件对照的稀疏配方；V2 精读里有 MLA 与 MoE 的手算，DeepSeek LLM 交代了 V3 之前的规模定律与学习率调度。后面每一步都在改这两个基线的某个部件。

检验（示例数值）：用 Kaplan 等 Scaling Laws 第 2.1 节的近似"训练 FLOPs ≈ 6 × 每 token 参与计算的（非嵌入）参数 × token 数"（忽略注意力随长度增长的那部分计算；规模定律的背景见[训练科学](../../../cross-domain/fields/training-science/README.md)），Llama 3 405B 为 6 × 405×10⁹ × 15.6×10¹² ≈ 3.8×10²⁵，与原文报告的数一致；DeepSeek-V3 按激活参数算为 6 × 37×10⁹ × 14.8×10¹² ≈ 3.3×10²⁴，约少一个数量级，总参数却是 Llama 3 405B 的约 1.7 倍。说出这个差距来自 Baseline 页结构拆分表的哪一行，以及它换来的代价出现在哪几行。

## 第 3 步：损失稳定与优化器

读 [PaLM](../../papers/arxiv-2204.02311/README.md) → [Wortsman 等](../../papers/arxiv-2309.14322/README.md) → [OLMo 2](../../papers/arxiv-2501.00656/README.md)；再读 [Muon 讲义](../../../foundations/lessons/modules/optimization/muon.md) → [Moonlight](../../papers/arxiv-2502.16982/README.md) → [Kimi K2](../../papers/arxiv-2507.20534/README.md)。

为什么在这里：入门页问题①的主线是"在数值被放大的地方加约束"，这条线从 PaLM 只能回滚跳批次开始，经 Wortsman 等在小模型上复现，到 QK-Norm 与 z-loss 成为常用部件；Muon 又带来新的放大（注意力 logit 超过 1000），K2 只能在优化器里约束，因为 MLA 加不了 QK-Norm。

检验：列出 z-loss、QK-Norm、QK-Clip、Muon 的权重衰减四种手段，分别写出它约束的是哪个量（输出 softmax 的 log Z、注意力 logit、某个头的 Q 与 K 权重、权重的 RMS），以及在训练的哪一步起作用（损失项、前向计算、每步更新之后、更新规则）。再解释 OLMo 2 为什么说重复 n-gram 与尖峰的关系"不是确定的"。

## 第 4 步：注意力不丢失与长上下文

读 [StreamingLLM](../../papers/arxiv-2309.17453/README.md) → [Lost in the Middle](../../papers/arxiv-2307.03172/README.md) → [Gated Attention](../../papers/arxiv-2505.06708/README.md) → [Qwen2.5-1M 精读](../../papers/qwen2.5-1m/reading.md)；再读 [Gemma 3](../../papers/arxiv-2503.19786/README.md) 与 [NSA](../../papers/arxiv-2502.11089/README.md) → [DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md)。

为什么在这里：入门页问题②③是同一个注意力的两面。前四篇说明 softmax 的注意力汇聚在截断缓存、信息在中间、长度外推时怎样失败，以及长上下文为什么要合成"必须读远处"的任务；后三篇是降低长上下文开销的两条路线（局部/全局交错、训练时稀疏），它们决定了第 6 步两家的分歧。

检验（示例数值）：设每层每个 token 的 KV 大小相同。Gemma 3 每 6 层有 5 层局部（窗口 1024）、1 层全局；128K（131,072 token）上下文时，KV 缓存是全部用全局层的 (1×131,072 + 5×1,024) ÷ (6×131,072) ≈ 17%。再算 DeepSeek-V4.1-Flash 每 token 约 890 字节的全局 KV，在 1M 上下文时约 0.9 GB。说出这两种省法各自没有省掉什么（Baseline 页"注意力"各行的代价列）。

## 第 5 步：更深更大的网络与更多知识

读 [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) → [无辅助损失均衡](../../papers/arxiv-2408.15664/README.md)；对照着读 [mHC](../../papers/arxiv-2512.24880/README.md) 与 [Attention Residuals](../../papers/arxiv-2603.15031/README.md)；最后读 [Engram](../../papers/arxiv-2601.07372/README.md) 与 [Gemma 2](../../papers/arxiv-2408.00118/README.md)。

为什么在这里：入门页问题④⑤回答"知识装在哪里、装多少"。MoE 把装知识的 FFN 做大而不增加每 token 计算；网络变深后残差流成为新瓶颈，DeepSeek 与 Kimi 给出两种改法；Engram 把一部分知识从 FFN 拆进查表记忆；Gemma 2 在数据不够时用蒸馏让小模型继续学。

检验：入门页把"能装多少知识"归到三个杠杆：预训练算力、承载知识的参数、高质量知识 token。给每个杠杆各找一篇本步的论文和一个原文数字；再说出 Kimi K2 的改写实验（原样重复 10 遍时 SimpleQA 简短事实问答为 23.76，改写 10 次各训一遍为 28.94）在动哪个杠杆。

## 第 6 步：两条路线的汇合点

读 [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) → [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)，对照 [Kimi Linear](../../papers/arxiv-2510.26692/README.md) → [Kimi K3](../../papers/arxiv-2607.24653/README.md)；补读 [Qwen3](../../papers/arxiv-2505.09388/README.md) 看第三家的做法。

为什么在这里：入门页的团队偏好写的是"DeepSeek 押注稀疏与压缩，Kimi 押注 token 效率"，到 2026 年 DeepSeek-V4 采用了 Kimi 规模化的 Muon。读完前五步，这几份报告的每一处改动都能在 Baseline 表里找到对应的行。

检验：把 DeepSeek-V4 与 Kimi K3 分别在 [Baseline 表](BASELINES.md)里标出改了哪些格，找出两家做法相同的格（例如都用 Muon、都把长上下文放在末段）与不同的格（稀疏对线性混合、mHC 对 Attention Residuals、显式 sink 对门控），并为每个不同之处写出各自自述的代价。

## 数据支线：把“质量好”变成可比较的实验

接在第 5 步后读 [DataDecide](../../papers/arxiv-2504.11393/README.md) → [FineWeb2](../../papers/arxiv-2506.20920/README.md) → [MIR / SoftQ](../../papers/arxiv-2606.06888/README.md)。三篇依次处理选配方、跨语言处理、有限数据重复利用，与前面的架构路线互补。

检验：为同一份语料写出三组对照：保持训练预算相同、只换筛选；保持语言与模型相同、只换处理步骤；保持独立 token 相同、比较原样重复与辅助损失。最后一组另报 FLOPs，才能看清节省的是数据还是计算。先用 DataDecide 的思路检查评测在小规模上有没有信号，再决定要不要放大实验。

## 读报告时先查什么

读一份新的预训练报告，先核对四个口径再看结论：token 数按采样次数还是去重后计；参数是总参数还是每 token 激活参数；长上下文结果是在哪个长度、是否经过位置外推；benchmark 是按困惑度打分还是按生成结果打分、是否在同一框架下重测了对照模型。入门页["用什么衡量进展"](README.md#用什么衡量进展)一节列出了这四个口径造成相反结论的例子。
