# 预训练

> 状态：领域入门页 · v2 · 依据 [synthesis.csv](synthesis.csv)（42 篇）
>
> 速览：
> 1. 预训练用下一词预测在数万亿到数十万亿 token 上学到语言结构与世界知识；后训练（SFT、偏好学习、强化学习）把这些先验变成按指令、按目标行动的行为。GPT-4 报告称考试能力主要来自预训练，DeepSeek-V3.2 把自己知识广度的差距归因于预训练算力不足。
> 2. `[经验]` 事实主要写在 FFN（前馈子层）里，由注意力读出；注意力决定从上下文的哪里读。MoE 与查表记忆正在把这条训练中出现的分工做成模块边界，层的位置也成了设计变量。
> 3. 2023 年以后的技术报告集中处理六个问题：损失稳定、注意力不丢失、更长的上下文、更深更大的网络、更多知识与更好泛化、训练方式保持简单。手段分七类，对应关系见"问题与手段"一节的总表。
> 4. 每一代报告都写着上一代做不好的地方：PaLM 约 20 次损失尖峰，原版 Muon 超过 1000 的注意力 logit，开头 token 被逐出后崩溃的窗口注意力，刷高 MMLU 却不提升生成式问答的选择题数据，DeepSeek-V4 重新出现的 MoE 离群值尖峰。
> 5. `[判断]` DeepSeek 押注稀疏与压缩（MoE、MLA、稀疏注意力、查表记忆），Kimi 押注 token 效率（Muon、改写数据、线性注意力）；2026 年两条线开始交汇，DeepSeek-V4 采用了 Kimi 规模化的 Muon。

本页是[大语言模型](../../README.md)领域的预训练方向。后训练分三个方向：[SFT](../posttraining/sft/README.md)、[偏好学习](../posttraining/preferences/README.md)、[强化学习](../posttraining/rl/README.md)；网络部件的细节在[架构与效率](../architecture/README.md)与[长上下文](../long-context/README.md)方向。

## 这个领域在解决什么

拿数万亿到数十万亿个从网页、书籍、代码、论文 PDF 里收集来的 token（词或词片段），让一个模型反复预测下一个 token（Llama 3 405B 训练了 15.6T token，Qwen3 用了 36T）。训练结束时，模型还不会按指令答题，但已经会续写各种文体，记住了大量事实，也能照着提示里的几个例子做新任务。本方向研究这一步怎样学得稳、学得省、学得多。

### 预训练与后训练的分工

结论：预训练决定模型知道什么、能表示什么，后训练决定模型怎样使用这些东西。

| 阶段 | 训练信号 | 主要改变什么 | 报告中的证据 |
|---|---|---|---|
| 预训练（含末段的退火与中段训练） | 无标注文本上的下一词预测；末段换成更高质量的数据 | 语言结构、世界知识、数学与代码的底子、长上下文 | Llama 3 第 2 节：预训练阶段模型学到语言结构，并获得大量关于世界的知识。GPT-4 第 4 节：考试能力主要来自预训练，RLHF 影响不显著 |
| SFT | 指令与示范回答 | 把基座在 few-shot 下的能力变成 zero-shot 的指令遵循 | DeepSeek LLM 第 5.1.2 节：对话模型 0-shot 的 MMLU 与基座 5-shot 相当；知识类任务的小幅波动不代表知识的得失 |
| 偏好学习与强化学习 | 回答之间的比较、可验证的奖励 | 把先验变成可执行的行为：推理、工具使用、安全 | Kimi K2 第 1 节：预训练提供通用先验，后训练把先验变成可执行的行为。DeepSeek-V2 第 4.4 节：RL 后 MATH、HumanEval 上升，BBH 从 81.3 降到 79.7（对齐税）。GPT-4 第 5 节：后训练明显损害了预训练模型良好的校准 |

两份 DeepSeek 报告说明知识的缺口最终要回到预训练补。DeepSeek LLM 的基座在数学与代码上欠拟合，SFT 让 HumanEval 和 GSM8K 提高 20 分以上，作者仍写明要全面掌握数学与代码，必须在预训练阶段加入更多样的数据。DeepSeek-V3.2 的后训练算力已超过预训练成本的 10%，作者仍把世界知识广度落后于闭源模型归因于总训练 FLOPs 较少，计划扩大预训练算力。

两个阶段之间多了一段过渡，预训练的末段越来越像是在为后训练准备材料：Llama 3 在最后用高质量数据退火（把学习率降到 0 的同时上采样高质量数据）；OLMo 2 把 5%–10% 的训练 FLOPs 划为中段训练（mid-training），用来注入新知识、修补能力短板；Qwen3 的第二阶段用约 5T 高质量的 STEM、代码与合成推理数据；DeepSeek-V4 在中段训练加入智能体数据。

`[判断]` 站在现在看，预训练的目的可以写成：为后训练准备合理的结构先验和尽量广的世界知识。下面"问题与手段"一节的六个问题，都是这个目的在大规模训练下派生出来的。

### 结构先验与世界知识分别落在哪里

`[经验]` 可解释性实验与架构消融指向同一个倾向：事实主要写在 FFN（也称 MLP，对每个位置独立做的两层变换）里，注意力决定从上下文的哪里读，并参与把事实读出来。完整的证据链与手算在[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)和[模型科学](../../../cross-domain/fields/model-science/README.md)。

| 证据 | 发现 | 边界 |
|---|---|---|
| [Induction Heads](../../../cross-domain/papers/arxiv-2209.11895/README.md)（小型纯注意力模型） | 上下文中"[A][B]…[A]→[B]"式的续写由两层注意力头组合完成：前一个头只按相对位置读取，后一个头按内容匹配并复制 | 大模型上只有相关性证据 |
| [ROME](../../../cross-domain/papers/arxiv-2202.05262/README.md)（GPT-2 XL） | 事实回忆集中在中间层、主语最后一个 token 的 MLP 上，平均间接效应峰值 6.6%，同一位置的注意力为 1.6% | 单一模型，约 1000 条事实的平均 |
| [Dissecting Recall](../../../cross-domain/papers/arxiv-2304.14767/README.md)（GPT-2、GPT-J） | 较早层 MLP 把主语的属性写进主语表示，上层注意力头把属性抽到预测位置；切断中高层对主语的注意力，正确答案概率最多下降约 60% | 抽取属性的注意力头参数里也编码了主语到属性的映射 |
| [DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) 16B | FFN 参数远多于注意力，知识密集任务（TriviaQA、NaturalQuestions）表现强，选择题弱；作者归因于注意力参数只有约 0.5B（DeepSeek 7B 为 2.5B） | 作者的归因，没有控制变量的消融 |
| [Engram](../../papers/arxiv-2601.07372/README.md) 27B | 推理时关掉 N-gram 查表记忆，事实知识类基准只保留 29%–44%，阅读理解类保留 81%–93% | 训练与推理不一致的事后消融 |

层的位置也成了设计变量。Engram 的消融显示，单个查表模块插在第 2 层最好，作者的解释是一轮注意力已足以为门控提供上下文，同时又早到能替代底层对局部模式的重建。其他报告在前几层和最后一层同样放了特定部件：DeepSeek-V3 前 3 层用稠密 FFN；DeepSeek-V4 前 3 个 MoE 层按 token ID 哈希路由（相当于静态查表），前两层只用滑动窗口注意力（Flash）或重度压缩注意力（Pro）；NSA 把第一层的 MoE 换回普通 MLP 以保证训练稳定；Kimi K3 的最后一层固定为全局注意力。

`[判断]` "结构主要靠注意力，世界知识主要在 FFN"可以作为读本页的主线，它是训练中形成的倾向。各家都在早期层放静态、局部的部件，深层保留全局读取，这与模型科学中"早期层处理局部、浅层的模式"的观察方向一致。边界写在批注。

## 问题与手段

结论：在"学到结构先验与世界知识"这个目的下，2023 年以后的技术报告集中回答六个问题；手段分七类，同一种手段常常同时服务几个问题。

| 问题 | 架构 | 优化器 | 损失与任务 | 数据组成 | 课程与退火 | 中途评估 | 精度 |
|---|---|---|---|---|---|---|---|
| ① 损失稳定 | QK-Norm（OLMo 2、Qwen3、Gemma 3、V4）；注意力输出门（Qwen）；mHC | 权重衰减（Moonlight）；QK-Clip（K2） | z-loss（PaLM、OLMo 2） | 删去含大量重复 n-gram 的文档（OLMo 2） | 早期用小批量（Llama 3） | 最大注意力 logit（K2）；尖峰自动检测（V4） | 细粒度 FP8 量化（V3） |
| ② 注意力不丢失 | 消除汇聚的门控（Qwen）；可学习的 sink（V4）；原生稀疏注意力（NSA） | — | 合成"必须读远处"的任务（Qwen2.5-1M、K3） | 长文档（V4、K3） | 稠密预热后转稀疏（V3.2、V4） | 首 token 注意力占比（Qwen） | — |
| ③ 更长更大的注意力 | MLA；局部/全局交错（Gemma）；CSA/HCA（V4）；KDA 混合（Kimi）；全局层不用位置编码（Kimi） | — | — | 长文档上采样（K3、Qwen2.5-Turbo） | 分阶段加长（各家） | 短上下文恢复 + 大海捞针（Llama 3） | FP8/FP4 的 KV 缓存（V4、V4.1） |
| ④ 更深更大的网络 | 细粒度与共享专家；mHC；AttnRes；LatentMoE | 按头正交化（K3） | 无辅助损失的负载均衡（V3） | — | 批量逐步增大（V3、Llama 3） | 稀疏度规模定律（K2）；残差增益（mHC） | FP8 训练（V3） |
| ⑤ 更多知识与更好泛化 | MoE 扩充 FFN；Engram 查表 | Muon 提高 token 效率（Moonlight、K2） | 知识蒸馏（Gemma 2/3） | 质量分类与配比（Llama 3、Qwen2.5）；改写（K2） | 高质量数据退火（Llama 3、Moonlight） | 选择题与生成题分开看（DeepSeek LLM） | — |
| ⑥ 训练方式保持简单 | — | 复用 AdamW 超参（Moonlight） | 下一词预测加 MTP、FIM（V3） | — | 阶梯学习率（DeepSeek LLM）；WSD 与余弦（K2、K3） | 超参规模定律（DeepSeek LLM、Qwen）；下游预测（Llama 3、GPT-4） | — |

表中 V3、V3.2、V4、V4.1 指 DeepSeek 各代，K2、K3 指 Kimi 各代。几个部件先给一句话：MoE（混合专家，每个 token 只激活少数几个专家 FFN）、MLA（多头潜在注意力，把每个 token 的 K、V 压成一个低维潜向量再缓存）、KDA（Kimi Delta Attention，一种带逐通道遗忘门的线性注意力）、CSA/HCA（DeepSeek-V4 的两种沿序列压缩 KV 的注意力）、mHC 与 AttnRes（两种改造残差连接的方法）、WSD（学习率先预热、再长时间恒定、末段衰减的调度）。下面先按问题讲，再讲三种贯穿几行的手段：优化器、数值精度、中途评估。

### ① 损失稳定：在数值被放大的地方加约束

结论：大模型的损失尖峰（训练损失突然跳高，严重时发散），多数能追到某个量在训练中失控放大：注意力 logit、输出 logit、残差流的增益、MoE 层的离群激活。各家的手段都是在放大的位置加约束，原理至今没有讲清。

- **问题怎样暴露**。PaLM 540B 训练中出现约 20 次损失尖峰，梯度裁剪开着也没用，小模型上没有出现。团队从尖峰前约 100 步的检查点重启、跳过 200–500 个批次；同样的批次从更早的检查点训练却不出尖峰，作者推断尖峰来自特定数据批次与特定参数状态的组合。PaLM 同时用了 z-loss（让输出 softmax 归一化项的对数 log Z 接近 0 的辅助损失），作者称它提高了稳定性。
- **搬到小模型上研究**。Google DeepMind 的 Wortsman 等（2023）在小模型上复现了两类不稳定：注意力 logit 增长、输出 logit 偏离对数概率。只要学习率够高，小模型同样出现，QK-Norm（计算注意力分数前对 Q、K 做归一化）和 z-loss 同样有效。此后 QK-Norm 成了常用部件：OLMo 2、Qwen3（替代 Qwen2 的 QKV 偏置）、Gemma 3（替代 Gemma 2 的 logit soft-capping）、DeepSeek-V4（对 Q 与压缩后的 KV 做 RMSNorm）。
- **MLA 让常用部件失效**。MLA 在推理时不显式构造 Key 矩阵，加不了 QK-Norm。Kimi K2 改在优化器里约束：QK-Clip 在每步更新后，把最大 logit 超过 100 的注意力头的 Q、K 权重按比例缩小。中等规模实验中原版 Muon 的最大 logit 很快超过 1000；K2 在 15.5T token 上没有出现一次损失尖峰。
- **门控也能稳住**。Qwen 团队在注意力输出后加 sigmoid 门，压低了模型中的大激活值；作者推测这让 BF16 训练少受数值误差影响。基线调高学习率时出现收敛问题，门控模型可以用更大的学习率。

做不好的场景：DeepSeek-V3 全程没有不可恢复的尖峰、没有回滚；到 1.6T 参数的 DeepSeek-V4，尖峰又出现了，回滚只能暂时恢复。作者把尖峰追到 MoE 层的离群值，用 Anticipatory Routing（用若干步之前的参数计算路由，只在检测到尖峰时启用）和 SwiGLU 截断（线性分量限制在 [−10, 10]）压住，并写明两者的原理尚未理解。Kimi K3 在 896 个专家的路由分支上也遇到内部激活爆炸，用 RMSNorm 修补。

### ② 注意力不丢失：开头的 token 为什么吸走注意力

结论：softmax 要求一行注意力权重加起来等于 1，当前位置找不到要读的内容时，多余的权重会倒在开头的 token 上，这叫注意力汇聚（attention sink）。它在训练长度之内基本无害；一旦截断缓存、外推位置或事后稀疏化，远处的信息就会丢失。

| 失败场景 | 原文证据 |
|---|---|
| 截断缓存 | StreamingLLM（2023）：只缓存最近 token 的窗口注意力，在开头 token 被逐出后困惑度崩溃；把开头 4 个 token 换成换行符仍然有效，说明模型依赖的是位置而非内容；保留 4 个开头 token 加滑动窗口即可恢复 |
| 信息在中间 | Lost in the Middle（2023）：多文档问答的准确率随相关文档位置呈 U 形；相关文档放在中间时，GPT-3.5-Turbo 的准确率低于完全不给文档的闭卷设置（56.1%） |
| 位置外推 | Gated Attention（2025）：用 YaRN 把上下文从 32K 扩到 128K 后，基线在原本 32K 内的 RULER（合成的多任务长上下文评测）得分从 79.50 跌到 37.94 |
| 事后稀疏化 | NSA（2025）引用的研究：top 20% 的注意力只覆盖约 70% 的注意力分数，预训练形成的检索头容易在推理时被剪掉 |

对注意力汇聚有两种相反的做法。一种是让它不再需要：[Gated Attention](../../papers/arxiv-2505.06708/README.md) 在注意力输出后加逐头的 sigmoid 门，落在第一个 token 上的注意力从平均 46.7% 降到 4.8%，扩到 128K 后 RULER 在 128K 上从 31.65 提高到 58.82。另一种是显式提供：StreamingLLM 在预训练时给每个样本开头加一个可学习的 sink token（160M 模型上验证）；[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) 在 softmax 分母里加一个可学习的 sink 项，使一个头的注意力总量可以小于 1，甚至接近 0。`[判断]` 两种做法都让一个头可以"什么也不读"，区别在于这个空位是学出来的还是写进结构的。

另外两种手段从训练方式入手。NSA 让稀疏注意力在预训练时就参与训练：27B 模型、260B token 上，LongBench（长文本理解评测集）平均分比全注意力高 0.032，64K 大海捞针全部位置找回。Engram 把局部的静态模式交给查表，作者认为注意力因此能把容量留给全局，多查询大海捞针从 84.2 提高到 97.0。

### ③ 更长更大的注意力：放到预训练末段分级加长

结论：各家都把长序列训练放在预训练末段，分几级加长，因为注意力的计算随长度平方增长；分歧在于怎样让每个 token 的注意力更便宜。

- **分级加长**。Llama 3 405B 用约 800B token 分六级从 8K 加到 128K，每一级以两条标准判断是否适应：短上下文评测完全恢复，大海捞针（在长文本中埋一句话让模型找回）在该长度上全部答对。DeepSeek-V2、V3 用 YaRN（一种调整 RoPE 频率的位置外推方法）从 4K 扩到 32K 再到 128K，每级 1000 步。Qwen2.5-Turbo 分四级扩到 262,144 token，每级 40% 的序列取当前最大长度。DeepSeek-V4 从 4K 加到 16K、64K、1M，前 1T token 用稠密注意力，64K 时转为稀疏；Kimi K3 在预训练中从 8K 加到 64K，在冷却期从 256K 加到 1M。
- **只有长度不够**。Kimi K3 写明仅有长度不能带来长程能力，长文档还要上采样，并合成只有读遍整个 1M 上下文才能解出的任务；[Qwen2.5-1M](../../papers/qwen2.5-1m/reading.md) 用填空、按位置检索、段落重排这类合成任务，让正确预测必须依赖远处的信息。

| 路线 | 代表 | 怎样省 | 代价或做不好的地方 |
|---|---|---|---|
| 压缩每个 token 的 KV | MLA（[DeepSeek-V2](../../papers/deepseek-v2/reading.md) 起，Kimi K2 沿用） | 每个历史位置只缓存一个低维潜向量，KV 缓存比 DeepSeek 67B 少 93.3% | 历史位置数不变，计算仍随长度平方增长；加不了 QK-Norm |
| 局部与全局交错 | Gemma 2（1:1，窗口 4096）→ Gemma 3（5:1，窗口 1024）→ Gemma 4（5:1，全局层 key 兼作 value） | 只有全局层看全长；Gemma 3 的消融中 7:1 的验证困惑度变化也很小 | 全局层仍按全长计算 |
| 训练时就稀疏 | NSA → DSA（DeepSeek-V3.2）→ CSA/HCA（[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)） | 每个查询只读选中的少量 KV 或压缩块；1M 上下文下 V4-Pro 的单 token 推理 FLOPs 为 V3.2 的 27% | DSA 的索引器本身仍是平方复杂度；V4.1-Flash 自述稀疏选择的误差可能在未测试的边界情形下损害能力 |
| 线性注意力混合 | [Kimi Linear](../../papers/arxiv-2510.26692/README.md)（3 层 KDA 接 1 层 MLA）→ [Kimi K3](../../papers/arxiv-2607.24653/README.md) | 大部分层用固定大小的递推状态，KV 缓存最多少 75% | 纯线性结构检索弱，仍保留四分之一的全注意力；7:1 时分布外验证明显变差 |

位置编码随之变化：Gemma 3 只把全局层的 RoPE 基频从 10K 提到 1M；Qwen 系列用 ABF 提高基频；Kimi Linear 与 K3 的全局层不用位置编码，位置信息交给 KDA，扩上下文时不必调整 RoPE。

做不好的场景：DeepSeek-V3.2 自述，即使有 128K 窗口，搜索类智能体流程仍常因长度上限被截断。大海捞针只检验检索，Llama 3 把它和"短上下文恢复"并列作为标准，Lost in the Middle 显示位置本身就会改变结果。

### ④ 更深更大的网络：稀疏专家与残差流

结论：网络变大主要靠 MoE（混合专家，每个 token 只激活少数几个专家 FFN），让总参数与每 token 计算分开；网络变深时的新瓶颈是残差流，DeepSeek 与 Kimi 在 2025–2026 年分别给出了约束混合矩阵与跨层注意力两种方案。

| 报告 | 总参数 / 激活参数 | 专家设置 | 负载均衡 |
|---|---|---|---|
| DeepSeek-V2（2024） | 236B / 21B | 2 个共享 + 160 个路由专家，激活 6 个 | 专家、设备、通信三项辅助损失 |
| DeepSeek-V3（2024） | 671B / 37B | 1 个共享 + 256 个路由专家，激活 8 个；前 3 层稠密 | 偏置调节（无辅助损失）+ 极小的序列级损失 |
| Kimi K2（2025） | 1.04T / 32B | 1 个共享 + 384 个，激活 8 个 | 本轮查阅的章节未写明 |
| DeepSeek-V4-Pro（2026） | 1.6T / 49B | 1 个共享 + 384 个，激活 6 个；前 3 层哈希路由 | 偏置调节 + 极小的序列级损失 |
| Kimi K3（2026） | 2.78T / 104B | 896 个，激活 16 个，路由专家在半宽潜空间里计算 | 按分位数设定偏置 |

- **专家怎样分**。[DeepSeekMoE](../../papers/arxiv-2401.06066/README.md) 把专家切细并隔离出共享专家，2B 模型与专家参数和计算量都是其 1.5 倍的 GShard 相当。负载均衡的辅助损失系数小了均衡不住，大了干扰语言建模；[无辅助损失均衡](../../papers/arxiv-2408.15664/README.md)改为给路由分数加按负载调整的偏置，1B 模型的验证困惑度从 9.56 降到 9.50。DeepSeek-V3 的消融进一步说明关键在约束范围：按整批而非按单个序列均衡，专家更能按领域分工（1B 模型验证损失：序列级辅助损失 2.258，批级辅助损失与无辅助损失均为 2.253）。
- **专家与注意力头怎样配**。Kimi K2 的稀疏度规模定律显示，固定激活参数时专家总数越多损失越低，于是专家从 256 增到 384；注意力头从 64 加到 128 只把验证损失降低 0.5%–1.2%，却让 128K 长度的推理 FLOPs 增加 83%，于是头数减半。Meta 走相反方向：Llama 3 为了最大化训练稳定性，选标准稠密结构而不用 MoE。
- **残差流成为瓶颈**。DeepSeek LLM 67B 把参数加在深度上（95 层）。Hyper-Connections 把残差流加宽成多条，但在 27B 模型上约第 12k 步出现损失突升，复合映射的最大增益峰值达到 3000；[mHC](../../papers/arxiv-2512.24880/README.md) 把混合矩阵约束为双随机矩阵（每行每列之和为 1），恢复恒等映射，额外开销 6.7%，DeepSeek-V4 采用。[Attention Residuals](../../papers/arxiv-2603.15031/README.md) 指出预归一化残差的隐藏状态幅度随层数线性增长、每层贡献被稀释，改用跨层注意力有选择地取回前面各层的输出，块级版本相当于基线多用 1.25 倍算力，Kimi K3 采用。

`[判断]` 两家处理的是同一个问题：残差流在几十上百层里既不能放大，也不能把早期信息稀释掉。DeepSeek 的办法是约束层间混合以保持恒等映射，Kimi 的办法是把深度方向的累加换成注意力。Attention Residuals 原文把 mHC 列为参照，Full 版本优于 mHC，块级版本与之相当、每层访存更少；这是一方的测量，尚无第三方的同条件对照。

### ⑤ 更多知识与更好泛化：算力、容量与知识 token

结论：模型能装多少知识，由预训练算力、承载知识的参数（FFN、专家、记忆表）和高质量知识 token 的数量共同决定；能把 benchmark 分数抬高的捷径，常常不带来泛化。

- **质量改变配比**。[DeepSeek LLM](../../papers/arxiv-2401.02954/README.md) 发现数据质量越高，新增算力越应分给模型：模型规模指数在早期自有数据上为 0.450，在质量更高的 OpenWebText2 上为 0.578。作者认为这可能解释了 Kaplan 等与 Chinchilla 结论不一致（见[训练科学](../../../cross-domain/fields/training-science/README.md)）。
- **配比靠分类器和小模型定**。Llama 3 用知识分类器下采样网页上过多的艺术与娱乐内容，再用小模型的规模定律比较候选配比，最终约 50% 通用知识、25% 数学与推理、17% 代码、8% 多语言。Qwen2.5 下采样电商、社交媒体、娱乐，上采样科技、科学与学术，总量从 7T 增到 18T。DeepSeek-V4 过滤批量自动生成和模板化的网页，以降低模型坍缩的风险，并扩充多语言语料以覆盖长尾知识。
- **高质量 token 不够时**。Kimi K2 写明单遍训练不足以吸收知识，多遍重复收益递减且易过拟合，于是改写知识语料：同一份 wiki 文本原样重复 10 遍，SimpleQA（简短事实问答）为 23.76；改写 10 次、每份只训一遍为 28.94。Qwen3 用视觉语言模型从 PDF 抽取文本，并合成数万亿 token。Gemma 2 写明小模型仍训练不足，用大模型的输出分布做知识蒸馏，在超过计算最优 50 倍的 token 量上训练 2B 与 9B 模型。
- **容量决定能装多少**。Engram 在总参数固定时，把约 20%–25% 的稀疏参数从 MoE 挪给查表记忆，验证损失最低；DeepSeek-V4-Flash 因参数较少，知识类评测明显弱于 V4-Pro，推理类在更多思考预算下可追平。

做不好的场景：DeepSeek LLM 在微调中加入 2000 万道中文选择题，MMLU 从 49.4 升到 60.9，生成式问答 TriviaQA 保持 57.9 不变，作者判断这是对 benchmark 的过拟合，于是预训练和微调都不用选择题数据；在预训练最后 10% 加入指令数据，基座分数上升，最终效果与在 SFT 阶段加入相同。Llama 3 用 GSM8k、MATH 的训练集做退火实验，8B 模型分别提高 24.0% 和 6.4%，405B 几乎没有提升，作者据此认为大模型不需要域内样本。

### ⑥ 训练方式保持简单：目标不变，变的是调度

结论：训练目标仍是下一词预测，新增的目标都以"加在旁边、推理时可以去掉"的形式出现；真正在变的是学习率与批量的调度，以及用小模型确定大模型的超参。

- **附加目标**。DeepSeek-V3 加了多 token 预测（MTP：在每个位置额外预测再下一个 token，保留完整的因果链），损失权重前 10T token 为 0.3、之后为 0.1；两个规模的消融中多数 benchmark 提升，推理时可直接丢弃，或用于投机解码（第二个 token 的接受率 85%–90%，生成速度 1.8 倍）。V4 原样沿用；V4.1-Flash 的骨干预训练去掉了 MTP，改在预训练之后单独训练草稿模块。V3 还以 0.1 的比例混入 FIM（把文档切成前缀、后缀、中间，让模型根据两侧补中间），此前 DeepSeek-Coder-V2 发现它不损害下一词预测。Gemma 2、3 的小模型直接以教师模型的分布为目标（Gemma 3 每个 token 采样 256 个 logit）。
- **学习率调度**。DeepSeek LLM 用三段阶梯学习率替代余弦衰减，效果相当，第一段可直接复用于继续训练；DeepSeek-V3 先恒定到 10T token，再余弦衰减 4.3T；Kimi K2 用 WSD（预热、长时间恒定、末段衰减）。Kimi K3 发现 WSD 与余弦的最优超参差别很大，各自独立调参后余弦衰减的最终损失更低，于是改回余弦。
- **批量与超参**。DeepSeek-V3 在前 469B token 把批量从 3072 增到 15360；Llama 3 早期用小批量以求稳定，再分两次加倍。DeepSeek LLM 拟合了最优批量与学习率随算力的幂律；Qwen2.5、Qwen3 为每个预训练阶段拟合超参规模定律；Kimi K3 的结构改动改变了最优区域，于是重新调批量、学习率、每参数 token 数与模型形状。

`[判断]` Meta 把简单本身当作押注：Llama 3 选稠密结构是为了稳定，后训练也选 SFT、拒绝采样、DPO 这类较简单的流程，而不用更难扩展的强化学习算法。

### 优化器：从 AdamW 到 Muon

结论：2025 年以前大模型几乎都用 AdamW；Kimi 证明 Muon 可以规模化，2026 年 DeepSeek-V4 也采用了它，但 Muon 带来的新不稳定需要新的约束。

Muon 把梯度动量矩阵近似正交化（拉平各方向奇异值的强弱）后再更新，机制见 [Muon 讲义](../../../foundations/lessons/modules/optimization/muon.md)。[Moonlight](../../papers/arxiv-2502.16982/README.md) 找到规模化需要的两处修改：加权重衰减，否则长训练中权重 RMS 持续增长、超出 bf16 的高精度范围；按矩阵形状缩放更新，使更新幅度与 AdamW 对齐，直接复用 AdamW 的超参。计算最优设定下，Muon 达到 AdamW 同样的损失约需 52% 的训练 FLOPs；Muon 训练出的权重奇异值分布更分散，路由器权重上差异最大。[Kimi K2](../../papers/arxiv-2507.20534/README.md) 加入 QK-Clip 压住 logit 爆炸；Kimi K3 改为按注意力头分块正交化，因为整矩阵正交化时梯度大的头会主导更新方向。DeepSeek-V4 把 Muon 用于多数矩阵参数，嵌入、输出头与归一化层仍用 AdamW；它对 Q 与 KV 做了 RMSNorm，因此不需要 QK-Clip。

做不好的场景：Moonlight 自述，AdamW 预训练的模型用 Muon 微调（或反过来）效果欠佳，大量现成的 AdamW 检查点因此难以直接受益。

### 数值精度：BF16 → FP8 → FP4

结论：降低精度能换来速度和显存，难点在离群值：一个异常大的数会挤占整个量化范围，让其他数失去精度。

DeepSeek LLM 已用 BF16 训练、FP32 累加梯度。[DeepSeek-V3](../../papers/arxiv-2412.19437/README.md) 首次在超大模型上验证 FP8 训练：每个线性层的三次矩阵乘法都用 FP8，激活按 1×128、权重按 128×128 的小块分别缩放以容纳离群值；H800 上 FP8 矩阵乘法的累加精度只有约 14 位，于是定期把部分和搬到 CUDA core 上用 FP32 累加。约 16B（1.33T token）和约 230B（0.9T token）两个规模上，FP8 相对 BF16 的损失相对误差低于 0.25%。DeepSeek-V4 把路由专家权重降到 FP4（在后训练中做量化感知训练），KV 缓存的位置维度用 BF16、其余用 FP8；V4.1-Flash 再把 KV 缓存降到 FP4，全局 KV 约 890 字节/token。精度问题也出现在别处：Kimi K3 训练时把注意力输出保留为 FP32，以纠正 flash attention 中有偏的舍入误差。混合精度的基础见[分布式训练讲义](../../../foundations/lessons/05a-distributed-training.md)第 8 节。

做不好的场景：DeepSeek-V3 尝试对激活梯度也按 128×128 块量化，约 16B 的 MoE 在约 300B token 后发散；作者推测原因是激活梯度在不同 token 之间极不均衡，形成与 token 相关的离群值。

### 中途评估：在花掉大部分算力之前看到结果

结论：大模型通常只训练一次，各家都在开训前用小模型预测终点，在训练中盯几个先兆量，并用便宜的实验评估新数据。

- **预测终点**。GPT-4 用算力少到万分之一的模型拟合规模定律，在训练刚开始时就准确预测了最终损失。DeepSeek LLM 用小实验预测 7B、67B（约 1000 倍算力）的验证损失。Llama 3 分两步预测下游表现：先拟合下游任务上正确答案的负对数似然与训练 FLOPs 的关系，再拟合负对数似然与准确率的关系。Kimi Linear 与 K3 用与预训练语料分布不同的验证集，能看出 7:1 混合比这类"训练损失相近、泛化变差"的情形。
- **评估新数据**。Llama 3 把训练到一半的 8B 模型在 40B token 上退火，新数据占 30%，用来判断一个小数据集值不值得加入，比逐个做规模定律实验便宜；OLMo 2 同样单独评估中段训练的各个数据源。
- **盯先兆量**。Kimi K2 监控每个头的最大注意力 logit；mHC 用复合映射的最大增益诊断残差流；DeepSeek-V4 自动检测损失尖峰，触发短回滚并临时启用 Anticipatory Routing；Gemma 3 在预训练中用若干标准 benchmark 作为探针检查通用能力。

做不好的场景：GPT-4 报告承认部分能力仍难预测，例如在 Inverse Scaling Prize 的 Hindsight Neglect 任务上，较小模型随规模变差，GPT-4 却扭转了这一趋势。DeepSeek LLM 提醒，不同数据集上拟合出的规模定律差别显著，跨数据集推广要谨慎。

## 主线历史

结论：2017–2023 年要回答的是"配方怎样收敛"；2024 年起，问题变成"大规模训练怎样稳定，每个 token、每个参数怎样学到更多"。每个阶段先写上一阶段留下的问题，再写它改变了什么，以及它做不好的场景。

### 1 基础：配方收敛到 decoder-only 与计算最优配比（2017–2023）

这一阶段确定了今天的基本配方：因果的 decoder-only 结构、下一词预测、按算力配平的模型与数据。评测目标随之迁移：从 WMT 机器翻译（BLEU），到 GLUE、SuperGLUE 这类微调后的理解任务，再到不微调的 few-shot 评测（MMLU、BIG-bench）。

| 节点 | 改变了什么 | 当时做不好的场景（原文） |
|---|---|---|
| Transformer（2017，Google） | 以注意力代替循环，整句并行训练；WMT14 英→德 28.4 BLEU，比此前最好的集成模型高 2 以上 | 每个任务仍要单独用标注数据训练；结论把高效处理图像、音频等大输入列为未来工作 |
| GPT、BERT（2018，OpenAI 与 Google） | 先在无标注文本上预训练，再逐任务微调；GLUE 平均 BERT-large 82.1、GPT 75.1 | GPT 在小数据集 RTE 上 56.0，低于多任务 BiLSTM 的 61.7；BERT 指出单向结构不利于问答这类逐 token 判断 |
| GPT-2、T5（2019） | GPT-2 检验不微调的 zero-shot；T5 在统一的文本到文本框架下比较，encoder–decoder 加去噪最好 | GPT-2 自述摘要等任务的 zero-shot 仍很初级；T5 自述用去噪目标获取通用知识可能效率不高 |
| Scaling Laws、GPT-3（2020，OpenAI） | 损失随参数、数据、算力幂律下降；175B 模型只靠提示中的例子完成任务（上下文学习） | GPT-3 自述在 WiC、ANLI、QuAC、RACE 等需要回看、比较两段文字的任务上较弱，预训练样本效率低；Scaling Laws 自述小数据区拟合差，算力估计没有计入上下文长度 |
| Wang 等、PaLM（2022） | 不微调的评测下，因果 decoder-only 加下一词目标最好；PaLM 540B few-shot 在 29 个英语 benchmark 中 28 个领先 | PaLM 约 20 次损失尖峰，作者没有找到有原则的缓解办法 |
| Chinchilla、LLaMA（2022–2023） | 固定算力下参数与 token 等比例增长：70B、1.4T token 的 Chinchilla 在 MMLU 上 67.6%，同算力的 280B Gopher 为 60.0%；LLaMA 把推理成本算进来，只用公开数据并发布权重 | Chinchilla 只分析了不到一个 epoch 的训练，高算力处前沿出现弯曲，可能高估大模型的最优大小；开源社区此后多训练固定尺寸模型，规模研究不足（DeepSeek LLM 第 1 节） |

`[判断]` 结构收敛到 decoder-only，原因是目标变了：评测从"微调后的成绩"换成"不微调的 few-shot 成绩"后，decoder-only 用一个下一词目标就能训练任意文本，训练形式又与生成形式一致。T5 的比较本身没有错，它的结论限定在微调设定下。跨模态的同类论证见[生成配方的收敛](../../../perspectives/generative-convergence.md)，规模化的总线见[深度学习规模化](../../../perspectives/scaling.md)。

### 2 稳定性成为一等问题（2022–2025）

留下的问题：PaLM 的尖峰只能靠回滚和跳批次绕过。改变：Wortsman 等在小模型上复现了 logit 增长与发散，QK-Norm 与 z-loss 成为常用部件；Llama 3 报告只有少数损失尖峰、无需干预，DeepSeek-V3 全程没有不可恢复的尖峰。做不好的场景：MLA 加不了 QK-Norm，Kimi 只能在优化器里另做 QK-Clip；稳定也受硬件约束，Llama 3 在 54 天内遇到 466 次作业中断，其中 419 次是意外，约 78% 与硬件有关。

### 3 开源团队把规模科学做细（2024）

留下的问题：Kaplan 与 Chinchilla 的配比结论不一致，也都没有交代超参数（DeepSeek LLM 第 1 节）。改变：DeepSeek LLM 拟合超参规模定律，发现配比随数据质量变化；Llama 3 用小模型规模定律选数据配比，用两步法预测下游表现，用退火评估数据；Qwen2.5 为稠密与 MoE 模型拟合超参。做不好的场景：不同数据集上的规模定律差别显著；选择题数据抬高 MMLU 却不提升生成式问答；退火对 8B 有效，对 405B 几乎无效；DeepSeek LLM 基座的数学与代码欠拟合。

### 4 稀疏化：用更少的激活参数装更多知识（2024）

留下的问题：稠密模型每个 token 都要过全部参数，扩大知识容量就要同比增加每 token 的计算与显存。改变：DeepSeekMoE 切细专家；[DeepSeek-V2](../../papers/deepseek-v2/reading.md) 合并 MLA 与 MoE，每训练 1T token 的成本比 DeepSeek 67B 低 42.5%；DeepSeek-V3（671B/37B，14.8T token）再加无辅助损失均衡、MTP 与 FP8，全部训练用 2.788M H800 GPU 小时。做不好的场景：DeepSeekMoE 16B 选择题偏弱，作者归因于注意力参数太少；辅助损失在均衡与质量之间两难；激活梯度的块级 FP8 量化导致发散；V3 自述推荐的部署单元较大，小团队负担重。

### 5 Token 效率：优化器与数据改写（2025）

留下的问题：高质量人类数据有限，同样的 token 要学到更多（Kimi K2 第 1 节）。改变：Moonlight 让 Muon 规模化，同样损失约需 AdamW 52% 的 FLOPs；Kimi K2 用 MuonClip 在 15.5T token 上零尖峰，用改写提高知识 token 的效用，用稀疏度规模定律把专家数提到 384。做不好的场景：原版 Muon 的权重 RMS 持续增长、注意力 logit 超过 1000；预训练与微调的优化器错配；K2 自述合成数据能否继续扩展仍待研究，难点是保持事实准确、减少幻觉。

### 6 为长程推理改造注意力与深度（2025–2026）

留下的问题：推理模型与智能体需要很长的上下文，原始注意力的平方复杂度成为瓶颈（DeepSeek-V4 第 1 节）；网络更深后，残差流的放大与稀释成为新瓶颈。改变：DeepSeek 一线从 NSA 到 DSA（V3.2）再到 CSA/HCA（V4，1M 上下文），加 mHC，V4.1-Flash 接入 Engram；Kimi 一线从 Kimi Linear 到 Attention Residuals 再到 K3；Qwen 用门控消除注意力汇聚；DeepSeek-V4 采用 Muon。评测目标也在迁移：基座评测加入 SimpleQA 一类事实问答、LongBench-V2 一类长文理解。做不好的场景：DeepSeek-V4 重新出现损失尖峰，稳定技巧原理不明，作者自述结构偏复杂；V4.1-Flash 自述新结构的鲁棒性边界尚未刻画清楚；DeepSeek-V3.2 自述知识广度落后；Kimi K3 自述总体仍落后于最强的闭源模型。

## 技术地基

- **下一词预测与因果 mask**：每个位置只能读之前的位置，一次前向就能并行计算所有位置的损失。[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 7、12 节，[自监督与生成目标](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)。
- **注意力的 A 与 V、KV 缓存**：A 决定读哪里，V 是读到的内容；生成时缓存历史的 K、V，长度越长缓存越大，问题②③都在这里。[QKV 讲义](../../../foundations/lessons/15-qkv-deep-dive.md)第 4–5 节，[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 12.4、14 节。
- **FFN、残差与归一化**：FFN 是逐位置的键值表，残差流把各层的更新累加起来，归一化控制尺度；问题①④⑤都发生在这三处。[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10 节。
- **MoE**：路由器为每个 token 选少数专家 FFN，总参数与每 token 计算分开。[SSM、GNN 与 MoE 讲义](../../../foundations/lessons/18-ssm-gnn-moe.md)第 4 节。
- **优化器**：AdamW 按坐标缩放，Muon 按矩阵正交化。[Adam 讲义](../../../foundations/lessons/modules/optimization/adam.md)、[Muon 讲义](../../../foundations/lessons/modules/optimization/muon.md)。
- **混合精度与并行**：[分布式训练讲义](../../../foundations/lessons/05a-distributed-training.md)第 8 节。规模定律与算力配比见[训练科学](../../../cross-domain/fields/training-science/README.md)。

## 主要路线与团队偏好

结论：几家团队在同一组问题上押注不同的手段。公开了详细技术报告的团队可以写出押注与代价；闭源模型只能写到报告公开的部分。

| 团队 | `[判断]` 押注 | 代表报告 | 代价与做不好的地方 |
|---|---|---|---|
| DeepSeek | 用稀疏和压缩降低每 token 的计算与显存，同时扩大参数与知识容量；每一代只换一两个部件，并把训练系统、数值精度和硬件写进设计 | DeepSeek LLM、DeepSeekMoE、V2、V3、NSA、V3.2、mHC、Engram、V4、V4.1-Flash | V4 自述结构偏复杂、稳定技巧原理不明；V3 部署单元大；V3.2 知识广度落后 |
| Kimi（Moonshot AI） | token 效率：更好的优化器、改写数据，并改造序列方向（线性注意力）与深度方向（跨层注意力）的信息流 | Moonlight、K2、Kimi Linear、Attention Residuals、K3 | Muon 带来 logit 爆炸与优化器错配；K3 仍落后最强闭源模型 |
| OpenAI | decoder-only、扩大规模、可预测地扩大规模 | GPT 系列、Scaling Laws、GPT-3、GPT-4 | 从 GPT-4 起不公开结构、算力、数据与训练方法 |
| Google | 系统比较与稳定性工程；MoE 的长期研究延续到 Gemini 1.5；开放的 Gemma 线押注局部/全局交错与知识蒸馏 | T5、PaLM、Wortsman 等、Gemma 2/3/4、Gemini 1.5 | Gemini 报告只给出 MoE 与长上下文结果，不给预训练配方；Gemma 2 自述小模型仍训练不足 |
| Meta | 稠密结构、公开权重，在数据配比与退火上做文章，以换取稳定与简单 | LLaMA、Llama 3 | 稠密模型每 token 计算随参数增长，Llama 3 405B 用了 3.8×10²⁵ FLOPs |
| Qwen（阿里巴巴） | 扩大数据规模、超参规模定律、分阶段预训练，并研究注意力的稳定性 | Qwen2.5、Qwen3、Gated Attention、Qwen2.5-1M | 报告未单列预训练局限 |

`[判断]` 收敛的部分：MoE 成为开源大模型的常用结构（DeepSeek、Kimi、Qwen3，Gemma 4 也有 MoE 版本），Gemini 1.5 Pro 同样是稀疏 MoE；QK 归一化或等价约束成为常用部件；长上下文都放在预训练末段；Muon 从 Kimi 传到 DeepSeek。分化的部分：注意力汇聚是消除还是显式提供（Qwen 对 DeepSeek-V4），残差流怎样改（mHC 对 Attention Residuals），长上下文是稀疏还是线性混合（DeepSeek 对 Kimi），以及 Meta 坚持稠密结构。

## 用什么衡量进展

结论：基座模型按四类 benchmark 评测（DeepSeek-V4 第 4.3.1 节的分法：世界知识、语言理解与推理、代码与数学、长上下文），训练中看留出集损失；评测口径的差异常常比模型之间的差异更大。

- **训练中**：留出集上的损失或 bits-per-byte（每字节的比特数，可以消除分词器不同带来的差异，DeepSeek LLM 与 DeepSeekMoE 用它比较不同模型）；Kimi Linear 与 K3 用分布外的验证集检查泛化。
- **世界知识**：MMLU 系列（多学科选择题）、TriviaQA、SimpleQA；2025 年以后 DeepSeek 与 Kimi 都用 SimpleQA 一类的事实问答度量知识。
- **长上下文**：大海捞针、RULER（合成的多任务长上下文评测）、LongBench、MRCR。
- **口径问题**：选择题与生成题会给出相反的结论（DeepSeek LLM 的选择题实验）；同一 benchmark 可以按困惑度打分或按生成结果打分（Kimi Linear 对 MMLU、GPQA 用困惑度打分）；DeepSeek 各代都在内部框架中统一重测对照模型，V4 把差距不超过 0.3 的分数视为同一水平；数据污染要单独处理（DeepSeek LLM 对 C-Eval 验证集与 CMMLU 测试集去重，Llama 3 的退火数据不含常用 benchmark 的训练集）；早期报告的口径问题（GPT-3 的数据重叠、Chinchilla 的训练与测试泄漏）见[综合表](synthesis.csv)。

## 当前开放问题

- **损失尖峰有没有统一的原理？** PaLM（2022）写明没有找到有原则的缓解办法，DeepSeek-V4（2026）写明两种新技巧的原理仍未充分理解，计划加强内部指标监控。入口：[DeepSeek-V4](../../papers/arxiv-2606.19348/README.md)、[Kimi K2](../../papers/arxiv-2507.20534/README.md)、[Gated Attention](../../papers/arxiv-2505.06708/README.md)、[Wortsman 等](https://arxiv.org/abs/2309.14322)。
- **知识能否从 FFN 里再拆出去？** Engram 的 U 形分配律、V4 结论中"更稀疏的嵌入模块"、V4.1-Flash 接入 Engram，以及把记忆表做成可移植部件的后续工作。入口：[Engram](../../papers/arxiv-2601.07372/README.md)、[Tokenizer-Agnostic Engram Module](../../papers/arxiv-2607.29065/README.md)、[Frozen Memory Is Not Enough](../../papers/arxiv-2608.17050/README.md)、[关系页](../../../foundations/relations/attention-ffn-division.md)第 8–9 节。
- **合成与改写数据能走多远？** K2 的改写在 SimpleQA 上有效，作者列出事实准确性、幻觉与规模三个难点；V4 过滤模板化内容以防模型坍缩。入口：[Kimi K2](../../papers/arxiv-2507.20534/README.md)、[Kimi K3](../../papers/arxiv-2607.24653/README.md)。
- **注意力汇聚该消除还是该保留？** Gated Attention 消除它后长度外推更好，DeepSeek-V4 显式保留可学习的 sink，两者没有同条件对照。入口：[Gated Attention](../../papers/arxiv-2505.06708/README.md)、[StreamingLLM](https://arxiv.org/abs/2309.17453)。
- **残差流的两种改法谁更好？** 入口：[mHC](../../papers/arxiv-2512.24880/README.md)、[Attention Residuals](../../papers/arxiv-2603.15031/README.md)。
- **闭源团队 2023 年以后怎样预训练？** GPT-4 报告声明不公开结构与训练细节，Gemini 1.5 只写明是稀疏 MoE；这一部分只能作为开放问题，不能写成事实。

## 阅读顺序

1. [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)：先建立"注意力读、FFN 存"的定位，本页的六个问题都建立在这个分工上。
2. [DeepSeek LLM](../../papers/arxiv-2401.02954/README.md) → [DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md) → [DeepSeek-V3](../../papers/arxiv-2412.19437/README.md)：从规模科学走到稀疏化，V2 精读里有 MLA 与 MoE 的手算。
3. [Muon 讲义](../../../foundations/lessons/modules/optimization/muon.md) → [Moonlight](../../papers/arxiv-2502.16982/README.md) → [Kimi K2](../../papers/arxiv-2507.20534/README.md)：优化器一线与 logit 爆炸。
4. [Gated Attention](../../papers/arxiv-2505.06708/README.md) → [Qwen2.5-1M 精读](../../papers/qwen2.5-1m/reading.md)：注意力汇聚与长上下文怎样训练。
5. [mHC](../../papers/arxiv-2512.24880/README.md) 与 [Attention Residuals](../../papers/arxiv-2603.15031/README.md)：深度方向的两种方案，对照着读。
6. [DeepSeek-V4](../../papers/arxiv-2606.19348/README.md) 与 [Kimi K3](../../papers/arxiv-2607.24653/README.md)：两条路线当前的汇合点。

"基础"一节的原文入口：[Transformer 精读](../../papers/transformer/reading.md)、[GPT-3 精读](../../papers/gpt3/reading.md)、[Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)。按问题排列的练习见[路线图](ROADMAP.md)，基线拆分见 [Baseline 页](BASELINES.md)，本方向收录的论文见[论文目录](PAPERS.md)。预训练之后怎样让模型服从指令，从 [InstructGPT 精读](../../papers/instructgpt/reading.md)开始。

## 批注

**易误读**

- "事实主要在 FFN"是倾向而非边界：Dissecting Recall 显示抽取属性的注意力头参数里也编码了主语到属性的映射；DeepSeekMoE 把选择题偏弱归因于注意力参数少，是作者的解释，所称 DeepSeek 7B 上的相关性来自未单独发表的内部研究；Engram 关掉查表是训练与推理不一致的事后消融（[关系页](../../../foundations/relations/attention-ffn-division.md)批注）。
- DeepSeek-V3 的原文措辞是没有"不可恢复的"损失尖峰、没有回滚，不等于损失曲线上完全没有波动（第 1 节）。
- Muon 的"约 52% FLOPs"来自计算最优设定下 Llama 架构稠密模型的规模定律拟合（Moonlight 第 3.2 节），不是任意规模、任意设定下的保证。
- Llama 3 的 24.0% 与 6.4% 来自把 GSM8k、MATH 训练集放进退火数据的实验（第 3.1.3 节），原文没有说明是相对还是绝对提升；最终的退火数据不含常用 benchmark 的训练集。
- DeepSeek-V2 的 42.5% 是每训练 1T token 的成本之比，不是两个项目的总开销之比（[V2 精读](../../papers/deepseek-v2/reading.md)第 7 节）。
- Gated Attention 的 RULER 差距出现在用 YaRN 扩展之后；在原训练长度 32K 以内，门控与基线相差很小（第 4.4 节）。
- DeepSeek-V4 的"27% FLOPs、10% KV 缓存"是图 1 中按等效 FP8 FLOPs 估算的单 token 推理开销，对照对象是 V3.2（第 1 节）。
- MoE 的总参数与激活参数是两个量；表中"激活"指每个 token 参与计算的参数。
- 基础一节沿用的口径：T5 的"encoder–decoder 最好"限定在其微调设定下（3.2.4 节）；BigScience 的结论分无监督预训练与多任务微调两半；Chinchilla 的 MMLU 摘要写 67.5%，表格写 67.6%，本页用表格数，且 Chinchilla 与 Gopher 还换了优化器、分词器与数据子集比例（4.1 节）；PaLM 的 28/29 是 few-shot 设定下与此前单检查点结果相比（6.1 节）；GPT-3 的 300B token 按采样次数计。

**判断的支撑论文**

- 预训练的目的是结构先验与世界知识：Llama 3 第 2 节、Kimi K2 第 1 节、GPT-4 第 4–5 节、DeepSeek LLM 第 5.1.2 节、DeepSeek-V3.2 第 5 节。边界：后训练也会增加能力，DeepSeek LLM 的 SFT 让 HumanEval、GSM8K 提高 20 分以上；OLMo 2 的中段训练用来修补数学这类技能，不只是知识。
- 层位置成为设计变量：Engram 第 6.2 节、DeepSeek-V3 第 4.2 节、DeepSeek-V4 第 2.1 节与第 4.2.1 节、NSA 第 4 节、Kimi K3 第 2.1 节。边界：没有一篇论文跨团队比较这些位置选择。
- 注意力汇聚的两种做法：Gated Attention 第 4.3–4.4 节、StreamingLLM 第 3 节、DeepSeek-V4 第 2.3.3 节。
- 残差流的两种方案：mHC 第 3–5 节、Attention Residuals 第 2–3 节与表 2。
- 团队偏好按"同一团队在两篇以上论文中、存在替代方案时重复同一选择"判断：DeepSeek 在 V2、V3、V4 中都保留 DeepSeekMoE，在 V2、V3 中保留 MLA，并在 NSA、V3.2、V4 中三次推进训练时稀疏的注意力；Kimi 在 Moonlight、K2、Kimi Linear 的规模实验与 K3 中都用 Muon，K2 与 K3 都改写知识语料；Gemma 2、3、4 都用局部/全局交错，Gemma 2、3 都用蒸馏；Meta 的 LLaMA 与 Llama 3 都用稠密结构并发布权重；OpenAI 从 GPT 到 GPT-4 都是下一词预测的 Transformer，GPT-4 第 3 节把可预测扩展列为项目核心；Qwen 从 Qwen2 的 7T、Qwen2.5 的 18T 到 Qwen3 的 36T 持续扩大数据。反例与边界：Kimi K3 把学习率调度从 K2 的 WSD 改回余弦，DeepSeek-V4.1-Flash 在骨干预训练中去掉了 V3、V4 都用的 MTP，Google 同时维护 MoE 的 Gemini 与以稠密为主的 Gemma。
- "收敛是因为目标变了"：T5 第 3.2.4 节、GPT-3 第 5 节、Wang 等第 4–5 节；PaLM 第 6.1.2 节写明同等训练成本下 encoder–decoder 在分类微调上通常更好，仍选择 decoder-only。

**与其他论文的关联**

- [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)与[模型科学](../../../cross-domain/fields/model-science/README.md)：本页"结构先验与世界知识"一节的完整证据；DeepSeekMoE 第 5 节"选择题偏弱归因于注意力参数少"可作为关系页第 7 节的新证据。
- [训练科学](../../../cross-domain/fields/training-science/README.md)：Kaplan 与 Chinchilla 的分歧；DeepSeek LLM 用数据质量解释这一分歧，可补进该页。
- [递推状态谱系](../../../foundations/relations/recurrent-state.md)：Kimi Linear 的 KDA 是线性注意力一支的最新节点；Attention Residuals 把"沿深度累加"类比为"沿时间递推"，与该页的状态方程视角相通。
- [Mamba 精读](../../papers/mamba/reading.md)与 [Switch Transformer](../../papers/arxiv-2101.03961/README.md)：分别是线性递推与 MoE 两条线的前作；Switch 附录 A 中专家化注意力在 bfloat16 下发散，是 MoE 只稀疏化 FFN 的稳定性原因之一。
- [InstructGPT 精读](../../papers/instructgpt/reading.md)与 [DeepSeek-R1](../../papers/arxiv-2501.12948/README.md)：后训练从本页的基座接手。

**未核实 / 待验证**

- 本轮只核实了各报告中与预训练有关的章节，后训练与评测细节未展开。Wortsman 等只读了摘要；Gemma 3、Gemma 4 的局限一节，Gemini 2.5 与 Kimi K2.5 的报告未打开。
- 本轮未检索到 Meta 在 Llama 3 之后发布的官方技术报告，Meta 的路线只写到 Llama 3；OpenAI 在 GPT-4 之后的预训练细节同样没有官方材料可引。
- DeepSeek-V4.1-Flash 的权重发布情况未核实。
- 沿用旧版的待验证项：GPT-2 完整模型的发布时间线；PaLM 自述局限的精确节号；Chinchilla 的 NeurIPS 正式版题名为 *An empirical analysis of compute-optimal large language model training*，与 arXiv 题名不同，本页数字两版一致、表号不同。
