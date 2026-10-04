# 视频与时序表征路线图

> 状态：路线图 · v2

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md)

结论：五步。先弄清"外观"和"运动"是两种线索、benchmark 偏向哪一种；再看时间算子怎样从光流、3D 卷积走到注意力；然后看训练信号怎样摆脱动作标签；接着学会怀疑 benchmark；最后进入视频大模型的 token 预算与长视频评测。每一步配一个能动手检验的问题。

## 第 1 步：外观与运动是两种线索

读 [Two-Stream](../../papers/arxiv-1406.2199/README.md) → [I3D](../../papers/arxiv-1705.07750/README.md)，对照 [Something-Something](../../papers/arxiv-1706.04261/README.md) 第 4.4 节。

为什么在这里：后面每一篇的结论都要放在"这个数据集靠外观能解多少"之下读。双流把两种线索拆成两路，I3D 的表格第一次在大数据集上给出两路的强弱，Something-Something 写明了模型怎样靠外观"作弊"。

检验：用 I3D Table 2 中双流 I3D 的单路结果，写出三个数据集上 RGB 与光流的大小关系（UCF-101 84.5 对 90.6，HMDB-51 49.8 对 61.9，Kinetics 71.1 对 63.4）。说明为什么 Kinetics 与另两个数据集方向相反，作者给了什么解释，这个解释之外还可能有什么原因。

## 第 2 步：时间算子

读 [SlowFast](../../papers/arxiv-1812.03982/README.md) → [TimeSformer](../../papers/arxiv-2102.05095/README.md) → [ViViT](../../papers/arxiv-2103.15691/README.md)；注意力的成本见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 14 节。

为什么在这里：第 1 步留下的问题是"光流要预算、3D 卷积只看几帧"。SlowFast 让时间轴与空间不对称，TimeSformer、ViViT 把时间交给注意力并必须做分解。TimeSformer Table 1 只做空间注意力的那一行，是全方向最常被引用的对照。

检验：
- 224×224 的帧切 16×16 的块，每帧 N = 196 块，取 F = 8 帧。算联合时空注意力下每个块要比较的对象数（NF + 1 = 1569）和分开时空注意力下的数（N + F + 2 = 206）。再算 TimeSformer-L 的 96 帧共有多少 token（196 × 96 = 18,816）。
- SlowFast 的 Slow 路取 T = 4 帧、间隔 τ = 16，覆盖多少原始帧？Fast 路帧率高 α = 8 倍，取多少帧？说明为什么 Fast 路通道只有 1/8 却仍有用（Fast 单独 51.7%，加到 Slow 上 +3.0）。

## 第 3 步：训练信号离开动作标签

读 [VideoMAE](../../papers/arxiv-2203.12602/README.md) → [V-JEPA](../../papers/arxiv-2404.08471/README.md)，先复习图像一侧的 [MAE](../../papers/mae/README.md) 与[视觉表征方向](../visual-representation/README.md)的"从测量看"。

为什么在这里：第 2 步的 Transformer 离不开图像预训练，而 Kinetics 标签奖励外观。这两篇让视频自己出题，并分别给出了 Kinetics 偏外观的直接证据。V-JEPA 也是机器人一侧 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) 的前作。

检验：
- 16 帧 224×224 的视频按 2×16×16 切块，共 8 × 14 × 14 = 1568 个 token；遮蔽 90% 后编码器只处理约 157 个。用一个"手指几乎不动"的块说明：随机遮蔽时为什么能从相邻帧抄到答案，管道遮蔽怎样堵住这条路。
- 用 V-JEPA Table 6 算 DINOv2 减 V-JEPA（ViT-H/16）在 K400 与 SSv2 上的差（+1.4 与 −20.8 个百分点），并解释同一对模型为什么在两个数据集上排名相反。

## 第 4 步：学会怀疑 benchmark

读 [Revealing Single Frame Bias](../../papers/arxiv-2206.03428/README.md) → [EgoSchema](../../papers/arxiv-2308.09126/README.md)。

为什么在这里：任务换成视频-文本检索与问答之后，外观捷径换了形式继续存在。这两篇给出两种工具：只留动作、去掉物体的模板任务，以及时间证书长度。没有这一步，第 5 步的长视频分数无从判断。

检验：
- 为两道题估计时间证书长度：Kinetics 的"这个人在滑雪吗"（给定类别互斥规则），以及三分钟视频里的"他最后把钥匙放回抽屉了吗"。说明证书长度与视频长度为什么是两回事。
- EgoSchema 上 mPLUG-Owl 1 帧 27.0%、5 帧 31.1%、30 帧 20.0%。给出两个可能的原因，并说明各需要什么实验来区分。

## 第 5 步：视频大模型的 token 预算与长视频

读 [Video-LLaVA](../../papers/arxiv-2311.10122/README.md) → [LLaVA-Video](../../papers/arxiv-2410.02713/README.md)（附录 A.2 与 C）→ [Qwen2.5-VL 技术报告](../../papers/arxiv-2502.13923/README.md)第 2.1 节 → [Video-MME](../../papers/arxiv-2405.21075/README.md)；长上下文的一般成本见 [LLM 长上下文方向](../../../llm/fields/long-context/README.md)。

为什么在这里：前四步的模型都在网络内部建模时间；视频大模型把时间交给语言模型的上下文，于是问题变成"帧数、每帧 token、时间位置怎样分配"。Video-MME 按时长分档，正好检验这些分配在长视频上是否成立。

检验：
- 1 小时视频按每秒 1 帧取 3600 帧、每帧 729 个 token，共多少 token？在 Qwen2.5-VL 评测用的 24,576 个视频 token 上限内，列出三种分配（例如 768 帧 × 32、192 帧 × 128、96 帧 × 256），各自相当于每隔几秒看一帧；按 LLaVA-Video 附录 C 的结论，你会先试哪一种，它的结论在什么条件下测得。
- 用 Video-MME Table 5 说明：Gemini 1.5 Pro 长视频加字幕提高 10.1 个百分点，这对"长视频题测的是不是画面中的时间"意味着什么。

## 续篇：从"装得下"到"找得到并核对得上"

第三步后先读 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)，接 [V-JEPA 2.1](../../papers/arxiv-2603.14482/README.md)（必读）：画一张时空网格，标出原来只监督被遮块与现在也约束可见块的差别；为什么全局动作分类可能看不出局部特征退化？

第五步后读 [Qwen3-VL](../../papers/arxiv-2511.21631/README.md)（必读），再读 [InternVideo3](../../papers/arxiv-2606.12195/README.md)（选读）。练习：同样的第100帧，在1 fps与25 fps采样下分别对应几秒？设计一个需要回看两段视频才能回答的问题，分别用更多帧、文字时间戳、压缩缓存、调用检索工具四种方案，指出每种方案解决什么、仍可能漏掉什么。InternVideo3 的工具案例按定性证据读，不能替代定量 agent 成功率。

## 动手时先查什么

拿一个视频模型或一个视频 benchmark 的分数之前，先查六件事：
- 训练与推理各取多少帧、按什么规则取（均匀、按帧率、关键帧）；两者是否一致；
- 每帧多少 token、是否在时间上合并或池化；
- 测试用了多少视图（片段 × 裁剪）；
- 评测是微调、冻结探针还是零样本；冻结探针是线性层还是注意力探针；
- 问答题是否过滤了能盲答的题，开放式问答用哪个模型打分；
- 长视频分数是"只看画面"还是加了字幕或音频。
