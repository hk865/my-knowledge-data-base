# 预训练的基线

> 状态：Baseline 页 · v2 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 基线是谁、为什么是它

结论：预训练有两个基线。[Llama 3](../../papers/arxiv-2407.21783/README.md) 定义了"稠密 Transformer + AdamW + 下一词预测 + 末段加长与退火"这套最简单的配方；[DeepSeek-V3](../../papers/arxiv-2412.19437/README.md) 定义了"MLA + 细粒度 MoE + 无辅助损失均衡 + 多 token 预测 + FP8"这套稀疏配方。2025–2026 年的开源报告大多从后者的结构出发，又把前者当作稠密的参照。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| [Llama 3](../../papers/arxiv-2407.21783/README.md)（2024，Meta） | 结构：126 层稠密 Transformer，405B 参数，GQA（分组查询注意力，几个查询头共享一组 K、V；这里 8 个 KV 头）。训练：15.6T token、3.8×10²⁵ FLOPs，AdamW 加余弦学习率，批量分两次加倍；8K 上下文训练主体，再用约 800B token 分六级加到 128K，最后 40M token 退火（学习率降到 0、上采样高质量数据）。评估：小模型规模定律定配比，两步法预测下游表现，退火实验评估新数据 | 作者写明为了训练稳定和流程可控，选稠密结构而不用 MoE（混合专家，每个 token 只激活少数几个专家 FFN），后训练也选较简单的 SFT（监督微调）、拒绝采样（从多个采样中挑出好的回答再训练）与 DPO（直接偏好优化）；配比、退火、"每一级加长是否适应"的判据都写成了可照做的规则。DeepSeek-V3 的基座对照表、OLMo 2 的摘要都把 Llama 3.1 列为对照 |
| [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)（2024，DeepSeek-AI） | 结构：671B 总参数、每 token 激活 37B；注意力用 MLA（多头潜在注意力，把每个 token 的 K、V 压成一个低维潜向量再缓存），FFN 用 DeepSeekMoE（1 个共享专家 + 256 个路由专家，每 token 激活 8 个，前 3 层保持稠密）。训练：14.8T token，下一词预测加 MTP（多 token 预测，在每个位置额外预测再下一个 token）与 FIM（让模型根据前缀和后缀补中间）；FP8 混合精度；学习率先恒定到 10T token、再余弦衰减 4.3T；全部训练 2.788M H800 GPU 小时，没有不可恢复的损失尖峰 | Kimi K2 写明结构仿 DeepSeek-V3，只把专家从 256 增到 384、注意力头从 128 减到 64；DeepSeek-V4 保留 DeepSeekMoE 与 MTP；Qwen3 的 MoE 也用细粒度专家切分。要比较"稀疏配方"时，能逐部件对照的就是它 |

两个基线之前，2017–2023 年的报告逐个定下了今天配方里的部件，详见入门页[主线历史](README.md#主线历史)第 1 阶段。每个节点定下的部件如下：

| 节点 | 定下的部件 | 留给后来的问题 |
|---|---|---|
| Seq2seq、Bahdanau 注意力（2014） | 架构：encoder–decoder 读入整句再生成；注意力让解码时按需读取源句 | 仍是 RNN，逐位置串行；Bahdanau 自述罕见词处理不好 |
| [Transformer](../../papers/transformer/reading.md)（2017） | 架构：用注意力代替循环，整句并行训练 | 每个任务仍要单独的标注数据 |
| GPT、BERT（2018） | 训练目标：先在无标注文本上预训练，再逐任务微调；GPT 用下一词预测，BERT 用遮蔽语言模型 | 两种目标谁更好，取决于下游是微调还是直接生成 |
| GPT-2、[T5](../../papers/arxiv-1910.10683/README.md)（2019） | 训练目标与数据：GPT-2 检验不微调的 zero-shot；T5 在统一的文本到文本框架下比较，微调设定中 encoder–decoder 加去噪最好，并发布 C4 语料 | T5 自述去噪目标获取通用知识可能效率不高 |
| Scaling Laws、[GPT-3](../../papers/gpt3/reading.md)（2020） | 规模：损失随参数、数据、算力幂律下降；175B 模型只靠提示中的例子完成任务 | Scaling Laws 的配比后来被 Chinchilla 修正 |
| Wang 等、[PaLM](../../papers/arxiv-2204.02311/README.md)（2022） | 架构与目标：不微调的评测下，因果 decoder-only 加下一词目标最好 | PaLM 约 20 次损失尖峰，没有找到有原则的缓解办法 |
| [Chinchilla](../../../cross-domain/papers/arxiv-2203.15556/README.md)、LLaMA（2022–2023） | 数据与参数的配比：固定算力下参数与 token 等比例增长；LLaMA 把推理成本算进来，只用公开数据并发布权重 | 开源社区多训练固定尺寸模型，超参与配比的规模研究不足（DeepSeek LLM 第 1 节） |

## 基线的结构拆分

结论：一个预训练配方可以拆成七个部件，与入门页["问题与手段"](README.md#问题与手段)总表的七列一一对应；架构一列再细分为注意力、FFN 与知识容量、残差与归一化三处。两个基线在注意力、FFN、数值精度上分歧最大，在课程与中途评估上做法相近。

| 部件 | 含义 | Llama 3 | DeepSeek-V3 |
|---|---|---|---|
| 架构 · 注意力 | 每个位置怎样读上下文、生成时缓存什么 | GQA，8 个 KV 头；RoPE（旋转位置编码）基频 500,000 | MLA，缓存低维潜向量，潜向量后加 RMSNorm；KV 缓存比 DeepSeek 67B 少 93.3%（DeepSeek-V2 的测量） |
| 架构 · FFN 与知识容量 | 事实主要存放的地方，见入门页"结构先验与世界知识分别落在哪里" | 稠密 SwiGLU FFN，每 token 过全部参数 | 1 共享 + 256 路由专家、激活 8 个；前 3 层稠密；用偏置调节做无辅助损失的负载均衡，另加极小的序列级损失 |
| 架构 · 残差与归一化 | 层间怎样累加更新、怎样控制数值尺度 | 沿用标准结构，报告未单列改动 | 沿用标准结构，只在 MLA 潜向量后加归一化 |
| 优化器 | 用什么规则更新参数 | AdamW；峰值学习率 8×10⁻⁵，余弦衰减 | AdamW；学习率 2.2×10⁻⁴ 恒定到 10T token，再余弦衰减 4.3T |
| 损失与任务 | 在哪些位置算什么损失 | 下一词预测 | 下一词预测 + MTP（损失权重前 10T token 为 0.3、之后 0.1）+ 比例 0.1 的 FIM |
| 数据组成 | 用什么数据、什么配比 | 15.6T token；约 50% 通用知识、25% 数学与推理、17% 代码、8% 多语言 | 14.8T token；相对 V2 提高数学与编程比例，扩展英文、中文以外的多语言 |
| 课程与退火 | 长度、学习率、批量、数据怎样随训练推进而变 | 批量 4M → 8M → 16M token；8K 训练主体 → 六级加到 128K（约 800B token）→ 最后 40M token 退火 | 批量 3072 → 15360（前 469B token）；4K 训练主体 → 用 YaRN（一种调整 RoPE 频率的位置外推方法）扩到 32K → 128K，各 1000 步 |
| 中途评估 | 花掉大部分算力之前怎样看到结果 | 小模型规模定律选配比；两步法预测下游；每级加长看"短上下文恢复 + 大海捞针（在长文本中埋一句话让模型找回）"；退火评估新数据 | 每个新部件先在两个规模上消融（MTP、负载均衡、FP8 对 BF16） |
| 数值精度 | 矩阵乘法与存储用几位浮点数 | BF16 | FP8 混合精度：激活按 1×128、权重按 128×128 的小块缩放，定期用 FP32 累加；优化器状态用 BF16 |

部件之间有依赖：注意力的形式决定能用哪种稳定手段（MLA 不显式构造 Key 矩阵，加不了 QK-Norm）；FFN 换成 MoE 后，负载均衡与数值离群值成了新的稳定性来源；数值精度能降多低，取决于离群值出现在哪个部件。下表按部件分行，同一篇论文改了几个部件，就在几行出现。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 架构 · 注意力 | 对 Q、K 做归一化（QK-Norm），替代 QKV 偏置或 logit 软截断 | [Wortsman 等](../../papers/arxiv-2309.14322/README.md)（小模型证据）、[OLMo 2](../../papers/arxiv-2501.00656/README.md)、[Qwen3](../../papers/arxiv-2505.09388/README.md)、[Gemma 3](../../papers/arxiv-2503.19786/README.md)、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) | 压住注意力 logit 的增长；小模型上能在三个数量级的学习率范围内稳定训练。代价：MLA 加不了，Kimi K2 只能在优化器里另做 QK-Clip（每步更新后，按比例缩小最大 logit 超过阈值的头的 Q、K 权重；见"优化器"行） |
| 架构 · 注意力 | 注意力输出后加逐头 sigmoid 门，消除注意力汇聚（attention sink，多余的注意力权重倒在开头 token 上） | [Gated Attention](../../papers/arxiv-2505.06708/README.md)（Qwen） | 落在第一个 token 上的注意力从平均 46.7% 降到 4.8%；用 YaRN 扩到 128K 后，RULER（合成的多任务长上下文评测）在 128K 上从 31.65 提高到 58.82；基线调高学习率时不收敛，门控模型可以。代价：在原训练长度 32K 以内与基线相差很小 |
| 架构 · 注意力 | 显式提供 sink：预训练时在样本开头放可学习的 sink token，或在 softmax 分母里加可学习的 sink 项 | [StreamingLLM](../../papers/arxiv-2309.17453/README.md)（160M 模型上验证）、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) | 一个头的注意力总量可以小于 1，截断缓存后不再崩溃。代价：StreamingLLM 自述不扩展上下文窗口、不增强长程记忆；与门控路线没有同条件对照 |
| 架构 · 注意力 | 压缩每个 token 的 KV（MLA） | [DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md)、[DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)、[Kimi K2](../../papers/arxiv-2507.20534/README.md) | KV 缓存比 DeepSeek 67B 少 93.3%。代价：历史位置数不变，计算仍随长度平方增长；加不了 QK-Norm |
| 架构 · 注意力 | 局部滑动窗口层与全局层交错 | [Gemma 2](../../papers/arxiv-2408.00118/README.md)（1:1，窗口 4096）→ [Gemma 3](../../papers/arxiv-2503.19786/README.md)（5:1，窗口 1024）→ Gemma 4（5:1，全局层 key 兼作 value） | 只有全局层看全长；Gemma 3 中只用全局层的配置在 32K 时 KV 缓存额外占约 60% 显存，交错加小窗口降到 15% 以下，7:1 的验证困惑度变化也很小。代价：全局层仍按全长计算 |
| 架构 · 注意力 | 训练时就稀疏：每个查询只读选中的少量 KV 或压缩块。DSA（DeepSeek 稀疏注意力）用一个小索引器为每个查询挑出得分最高的 KV；CSA/HCA 先沿序列压缩 KV 再稀疏或稠密地读 | [NSA](../../papers/arxiv-2502.11089/README.md) → DSA（[DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md)）→ CSA/HCA（[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)）→ CSA2（[DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)） | NSA 在 27B 模型上 LongBench（长文本理解评测集）平均分比全注意力高 0.032，64K 解码快 11.6 倍；1M 上下文下 V4-Pro 单 token 推理 FLOPs 为 V3.2 的 27%；V4.1-Flash 全局 KV 约 890 字节/token。代价：DSA 的索引器仍是平方复杂度；V4.1-Flash 自述稀疏选择误差可能在未测试的边界情形下损害能力 |
| 架构 · 注意力 | 线性注意力与全注意力混合：大部分层用固定大小的递推状态 | [Kimi Linear](../../papers/arxiv-2510.26692/README.md)（3 层 KDA 接 1 层 MLA；KDA 即 Kimi Delta Attention，一种带逐通道遗忘门的线性注意力）→ [Kimi K3](../../papers/arxiv-2607.24653/README.md) | KV 缓存最多少 75%；全局层不用位置编码，扩上下文时不必调 RoPE。代价：纯线性结构检索弱，仍保留四分之一全注意力；7:1 混合时分布外验证明显变差 |
| 架构 · FFN 与知识容量 | 细粒度专家 + 共享专家（MoE），并不断增加专家数 | [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) → [DeepSeek-V2](../../papers/deepseek-v2/reading.md) → [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)；[Kimi K2](../../papers/arxiv-2507.20534/README.md)（384 个）、[Kimi K3](../../papers/arxiv-2607.24653/README.md)（896 个）；[Qwen3](../../papers/arxiv-2505.09388/README.md)（128 个、无共享专家）；前作 [Switch Transformer](../../papers/arxiv-2101.03961/README.md) | 总参数与每 token 计算分开；K2 的稀疏度规模定律显示固定激活参数时专家越多损失越低。代价：DeepSeekMoE 16B 选择题偏弱，作者归因于注意力参数太少；Llama 3 为了稳定不用 MoE；K3 的 896 专家路由分支出现内部激活爆炸 |
| 架构 · FFN 与知识容量 | 负载均衡从辅助损失改为按负载调整路由偏置 | [Auxiliary-Loss-Free Load Balancing](../../papers/arxiv-2408.15664/README.md) → [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)；Qwen3 用全局批次的均衡损失；Kimi K3 按分位数设偏置 | 1B 模型验证困惑度从 9.56 降到 9.50；按整批而非单个序列均衡，专家更能按领域分工。代价：辅助损失系数小了均衡不住，大了干扰语言建模，所以才换 |
| 架构 · FFN 与知识容量 | 把局部、静态的知识交给 N-gram 哈希查表记忆 | [Engram](../../papers/arxiv-2601.07372/README.md) → [DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)（196B 参数的查表模块） | 总参数固定时，把约 20%–25% 的稀疏参数从 MoE 挪给记忆表，验证损失最低；多查询大海捞针从 84.2 提高到 97.0。代价：关掉查表后知识类基准只剩 29%–44%，但这是训练与推理不一致的事后消融 |
| 架构 · 残差与归一化 | 约束残差流的混合矩阵（双随机矩阵），恢复恒等映射 | [mHC](../../papers/arxiv-2512.24880/README.md) → [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) | 修复 Hyper-Connections（把残差流加宽成多条并学习层间混合矩阵）在 27B 模型上约第 12k 步的损失突升（复合映射增益峰值达 3000）。代价：额外开销 6.7% |
| 架构 · 残差与归一化 | 用跨层注意力有选择地取回前面各层的输出，代替逐层求和 | [Attention Residuals](../../papers/arxiv-2603.15031/README.md) → [Kimi K3](../../papers/arxiv-2607.24653/README.md) | 解决预归一化残差的幅度随层数线性增长、每层贡献被稀释；块级版本相当于基线多用 1.25 倍算力。代价：与 mHC 的比较只有 Kimi 一方的测量 |
| 架构 · 残差与归一化 | 把归一化移到注意力与 FFN 的输出上（reordered norm） | [OLMo 2](../../papers/arxiv-2501.00656/README.md) | 与 QK-Norm 合用时，梯度范数的尖峰分数从 0.108 降到 0.069。代价：作者写明两项单独使用都没有好结果，必须一起用 |
| 优化器 | AdamW 换成 Muon：把梯度动量矩阵近似正交化后再更新，加权重衰减、按矩阵形状缩放 | [Moonlight](../../papers/arxiv-2502.16982/README.md) → [Kimi K2](../../papers/arxiv-2507.20534/README.md)（MuonClip）→ [Kimi K3](../../papers/arxiv-2607.24653/README.md)（按头分块正交化）；[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) 采用 | 计算最优设定下达到 AdamW 同样损失约需 52% 的 FLOPs；K2 在 15.5T token 上零尖峰。代价：原版 Muon 的最大注意力 logit 超过 1000，需要 QK-Clip；AdamW 预训练的模型用 Muon 微调（或反过来）效果欠佳 |
| 优化器 | 在 AdamW 框架内调稳：更长的 warm-up、与学习率解耦的权重衰减、按规模调 ε | [Wortsman 等](../../papers/arxiv-2309.14322/README.md) | 降低学习率敏感度；梯度 RMS 逼近 AdamW 的 ε 时可提前预警。代价：研究对象是缓慢发散，不是突发尖峰 |
| 损失与任务 | 加辅助损失压住输出 logit：z-loss 让 log Z 接近 0 | [PaLM](../../papers/arxiv-2204.02311/README.md)、[Wortsman 等](../../papers/arxiv-2309.14322/README.md)、[OLMo 2](../../papers/arxiv-2501.00656/README.md) | 防止输出 logit 偏离对数概率导致的发散。代价：PaLM 加了 z-loss 仍有约 20 次尖峰 |
| 损失与任务 | 附加目标"加在旁边、推理时可以去掉"：MTP、FIM | [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)；[DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md) 去掉 MTP | MTP 在两个规模的消融中多数 benchmark 提升，可用于投机解码（第二个 token 接受率 85%–90%）。代价：V4.1-Flash 在骨干预训练中去掉 MTP，改为预训练后单独训练草稿模块 |
| 损失与任务 | 以教师模型的分布代替真实下一词（知识蒸馏） | [Gemma 2](../../papers/arxiv-2408.00118/README.md)（2B、9B）、[Gemma 3](../../papers/arxiv-2503.19786/README.md)（每 token 采样 256 个 logit） | 小模型可以在超过计算最优 50 倍的 token 上继续变好。代价：需要先有一个大教师 |
| 损失与任务 | 合成"必须读远处才能答对"的任务 | [Qwen2.5-1M 精读](../../papers/qwen2.5-1m/reading.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md) | 让长度带来真正的长程能力。代价：K3 写明只有长度不够，还要上采样长文档 |
| 数据组成 | 用分类器与小模型规模定律定配比，按主题上下采样 | [Llama 3](../../papers/arxiv-2407.21783/README.md)、[Qwen2.5](../../papers/arxiv-2412.15115/README.md)（7T → 18T）、[Qwen3](../../papers/arxiv-2505.09388/README.md)（36T，从 PDF 抽取文本、合成数万亿 token）、[DeepSeek LLM](../../papers/arxiv-2401.02954/README.md)（数据质量越高，新增算力越应分给模型） | 同样算力学到更多知识。代价：DeepSeek LLM 提醒不同数据集上的规模定律差别显著；DeepSeek-V4 要过滤模板化网页以防模型坍缩 |
| 数据组成 | 改写知识语料，代替原样重复 | [Kimi K2](../../papers/arxiv-2507.20534/README.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md) | 同一份 wiki 文本原样重复 10 遍，SimpleQA（简短事实问答）为 23.76，改写 10 次各训一遍为 28.94。代价：K2 自述合成数据要继续扩展，难点是事实准确与幻觉 |
| 数据组成 | 删除会诱发尖峰的数据：含长串重复 n-gram 的文档 | [OLMo 2](../../papers/arxiv-2501.00656/README.md) | 平均而言减少梯度范数与损失尖峰。代价：关系不确定，同一序列在小模型上或换一种数据顺序后可能不出尖峰 |
| 数据组成 | 不用选择题数据 | [DeepSeek LLM](../../papers/arxiv-2401.02954/README.md) | 避免对 benchmark 过拟合：在微调中加 2000 万道中文选择题，MMLU（多学科选择题）从 49.4 升到 60.9，生成式问答 TriviaQA 保持 57.9 不变 |
| 课程与退火 | 预训练末段换成高质量数据并把学习率降到 0（退火、中段训练） | [Llama 3](../../papers/arxiv-2407.21783/README.md)、[OLMo 2](../../papers/arxiv-2501.00656/README.md)（中段训练占 5%–10% FLOPs，多次退火后取平均）、[Qwen3](../../papers/arxiv-2505.09388/README.md)（S2 约 5T 推理数据）、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)（中段训练加入智能体数据） | 注入新知识、修补数学等短板，为后训练准备材料。代价：Llama 3 用 GSM8k、MATH（两个数学题评测）的训练集退火，8B 分别提高 24.0% 和 6.4%，405B 几乎没有提升 |
| 课程与退火 | 分级加长上下文 | [Llama 3](../../papers/arxiv-2407.21783/README.md)（六级、约 800B token）、[DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)（YaRN 两级）、[Qwen3](../../papers/arxiv-2505.09388/README.md)（32K，基频 1M）、[Gemma 3](../../papers/arxiv-2503.19786/README.md)（32K 预训练，末段缩放到 128K）、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)（4K → 1M） | 把平方增长的注意力开销集中在末段。代价：DeepSeek-V3.2 自述即使有 128K，搜索类智能体流程仍常被长度截断 |
| 课程与退火 | 稀疏注意力先稠密预热、再转稀疏 | [DeepSeek-V3.2](../../papers/arxiv-2512.02556/README.md)（2.1B token 只训索引器）、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)（前 1T token 稠密） | 让索引器先对齐稠密注意力的分布。反例：[DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md) 在 64K 上从头训练稀疏注意力，不再预热 |
| 课程与退火 | 学习率与批量的调度 | [DeepSeek LLM](../../papers/arxiv-2401.02954/README.md)（三段阶梯）、[DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)（恒定后余弦）、[Kimi K2](../../papers/arxiv-2507.20534/README.md)（WSD：预热、长时间恒定、末段衰减）→ [Kimi K3](../../papers/arxiv-2607.24653/README.md)（改回余弦）；[Qwen3](../../papers/arxiv-2505.09388/README.md)（分阶段拟合超参规模定律） | 阶梯学习率的第一段可直接复用于继续训练。代价：K3 发现 WSD 与余弦的最优超参差别很大，各自调参后余弦的最终损失更低；结构一改，最优区域就要重调 |
| 中途评估 | 用小模型预测终点：最终损失、下游准确率 | [GPT-4](../../papers/arxiv-2303.08774/README.md)、[DeepSeek LLM](../../papers/arxiv-2401.02954/README.md)、[Llama 3](../../papers/arxiv-2407.21783/README.md)（两步法） | GPT-4 用算力最多为其万分之一的模型准确预测最终损失。代价：部分能力仍难预测（Inverse Scaling Prize 的 Hindsight Neglect 任务上，较小模型随规模变差，GPT-4 却扭转了这一趋势） |
| 中途评估 | 训练中盯先兆量 | [Kimi K2](../../papers/arxiv-2507.20534/README.md)（每个头的最大 logit）、[mHC](../../papers/arxiv-2512.24880/README.md)（复合映射的最大增益）、[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)（自动检测尖峰并短回滚）、[Wortsman 等](../../papers/arxiv-2309.14322/README.md)（梯度 RMS 的规模趋势） | 在尖峰或发散之前发现问题。代价：V4 的两种稳定技巧原理尚未理解 |
| 中途评估 | 便宜地评估一份新数据：在训练到一半的模型上短退火 | [Llama 3](../../papers/arxiv-2407.21783/README.md)（40B token、新数据占 30%）、[OLMo 2](../../papers/arxiv-2501.00656/README.md)（微退火） | 比为每份数据做规模定律实验便宜。代价：结论只对退火那一刻的模型成立 |
| 中途评估 | 用分布外验证集检查泛化 | [Kimi Linear](../../papers/arxiv-2510.26692/README.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md) | 能看出"训练损失相近、泛化变差"的配置，例如 7:1 的线性注意力混合 |
| 数值精度 | FP8 训练：小块缩放加定期 FP32 累加 | [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md) | 约 16B 与约 230B 两个规模上相对 BF16 的损失相对误差低于 0.25%。代价：激活梯度也按 128×128 块量化时，约 16B 的 MoE 在约 300B token 后发散 |
| 数值精度 | 更低精度的权重与 KV 缓存；局部回到高精度 | [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)（路由专家 FP4 量化感知训练，KV 缓存 FP8）、[DeepSeek-V4.1-Flash](../../papers/arxiv-2609.19969/README.md)（FP4 KV 缓存）、[Kimi K3](../../papers/arxiv-2607.24653/README.md)（注意力输出保留 FP32） | 显存与带宽下降。代价：K3 发现 flash attention 中有偏的舍入误差，只能在这一处回到 FP32 |
| 数值精度 | FP4（NVFP4）预训练：权重、激活、梯度 4 位，最后约 15% 的层与注意力、MTP 等投影保留 BF16 | [Nemotron 3](../../papers/arxiv-2512.20856/README.md)（Super、Ultra） | Nano 上与 BF16 的损失相对差不到 1%。代价：依赖 NVIDIA 新硬件；Super、Ultra 的完整对照在单独报告中 |
| 数据组成 | 按语言适配清洗、去重与质量重加权 | [FineWeb2](../../papers/arxiv-2506.20920/README.md)（2025） | 把多语言数据质量拆成可消融步骤；代价：每种语言需要可靠的早期评测，单语言消融不直接代表联合训练 |
| 损失与任务 | 有限语料多遍训练时，附加掩码输入的下一词损失 | [MIR / SoftQ](../../papers/arxiv-2606.06888/README.md)（2026） | 减轻记忆性拟合；代价：每批两次前向，需与强权重衰减基线比较 |
| 中途评估 | 把选对数据配方作为小实验的目标 | [DataDecide](../../papers/arxiv-2504.11393/README.md)（2025） | 比较简单排名与规模律预测的决策效率；代价：目标规模与 token/参数比限制外推范围 |

几篇精读的位置：[DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md)占"注意力 = MLA"与"FFN = 细粒度与共享专家"两格；[Qwen2.5-1M 精读](../../papers/qwen2.5-1m/reading.md)占"损失与任务 = 合成必须读远处的任务"与"课程 = 分级加长"两格；[GPT-3 精读](../../papers/gpt3/reading.md)与 [Transformer 精读](../../papers/transformer/reading.md)属于基线之前的节点；[Mamba 精读](../../papers/mamba/reading.md)是"线性注意力混合"一路的前作，在[架构与效率方向](../architecture/README.md)展开。

## 批注

**易误读**

- Llama 3 的 3.8×10²⁵ FLOPs 与 DeepSeek-V3 的 2.788M H800 GPU 小时是两种口径，前者是训练计算量，后者是预训练 2664K、上下文扩展 119K、后训练 5K 的 GPU 小时之和（V3 第 1 节），两者不能直接相除比较效率。
- DeepSeek-V3 的原文措辞是没有"不可恢复的"损失尖峰、没有回滚；Llama 3 的原文是只有少数尖峰、无需干预（3.4.1 节），都不等于损失曲线完全平滑。
- NSA 的 +0.032 是 27B 模型、270B token 设定下 LongBench 的平均分之差（NSA 第 4.3 节），对照是同设定训练的全注意力模型。
- Gemma 3 图 4 的图例与图注对局部与全局的比例写法不一致（"3:1"与"1:3"），本页只写"局部层更多"，不引具体比例。
- "稠密预热后转稀疏"不是通用做法：V4.1-Flash 写明不再有稠密预热（第 1 节）。
- Muon 的"约 52% FLOPs"来自计算最优设定下 Llama 架构稠密模型的规模定律拟合（Moonlight 第 3.2 节）。
- Wortsman 等在脚注 1 中写明研究的是缓慢发散，不是突发的损失尖峰；把它列在"损失稳定"一行，依据是它复现的两类不稳定与 QK-Norm、z-loss 的有效性。

**与其他论文的关联**

- 注意力一行的细节在[架构与效率方向](../architecture/README.md)与[长上下文方向](../long-context/README.md)展开；FFN 一行的"注意力读、FFN 存"依据见[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)。
- 蒸馏一行与[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)相通：Gemma 2 把蒸馏用作预训练目标，而不只是压缩手段。
- 中途评估一行的规模定律与配比争论见[训练科学](../../../cross-domain/fields/training-science/README.md)；Chinchilla 与 Kaplan 的分歧，DeepSeek LLM 用数据质量解释。
- 退火与中段训练接到后训练：[SFT 方向](../posttraining/sft/README.md)从这里拿到的基座已经见过高质量推理数据。

**未核实 / 待验证**

- Kimi K2 的负载均衡方式在本轮查阅的章节中没有写明；Gemma 4、Gemini 1.5 只核实了 [synthesis.csv](synthesis.csv) 记录的部分，Gemma 4 的局限一节未打开。
- Kimi 系列（Kimi Linear、Attention Residuals、K3）各行的数字沿用入门页与对应文献卡的核实结果，本页没有重新打开原文。
- Llama 3 的归一化与残差细节报告未单列，表中"沿用标准结构"是按"只做小改动"的原文推断。
