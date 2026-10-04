# 预训练

> 状态：领域入门页 · v1 · 依据 [synthesis.csv](synthesis.csv)（13 篇）

本页是[大语言模型](../../README.md)领域的预训练方向。主线是 Transformer 一线怎样从机器翻译走到今天通用的大语言模型配方；预训练之后的指令微调与偏好对齐属于后训练方向，网络结构本身的改进属于[架构与效率方向](../architecture/README.md)。

## 这个领域在解决什么

拿几千亿个从网页、书籍里收集来的 token（词或词片段），不加任何人工标注，训练一个模型去预测被遮住或尚未出现的文字。训练完以后，同一个模型既能经过微调（在预训练权重上继续用少量任务数据训练）去做问答，也能只看提示里的几个例子就把一句英文译成法文。为此要做四个选择：训练信号用下一词预测、遮蔽预测还是去噪；结构让每个位置看到哪些位置（encoder-only、decoder-only 还是 encoder–decoder）；模型多大、训练多少 token；数据从哪里来、怎样清洗。本方向关心这四个选择怎样一步步收敛到今天的通用做法：因果 decoder-only 结构、下一词预测目标，以及按算力预算配平的模型大小与数据量。

## 主线历史

这条线是[深度学习规模化](../../../perspectives/scaling.md)在语言上的展开：Transformer 让训练可以在整段文本上并行，此后训练信号从人工标注转向文本本身，再往后，问题变成同样的算力该怎样分给模型和数据。每个节点先写上一个节点留下的问题，再写它改变了什么；逐篇出处在[综合表](synthesis.csv)。

1. **Transformer（2017，Google）**。留下的问题：Seq2seq（2014，Google）用一个 LSTM 把整句源文压成固定长度的向量，再由另一个 LSTM 生成译文；Bahdanau 注意力（2014，Jacobs University Bremen 与 Montréal）让解码每个词时按权重回读源句各位置（软对齐），长句不再退化，但编码和解码仍是循环网络，同一个样本内部只能沿位置逐步计算。改变：以注意力作为序列内和序列间交互的主体，去掉循环，整句可以并行训练。目标仍是 WMT 机器翻译（年度机器翻译评测，用 BLEU 即译文与参考译文的 n-gram 重合度打分）：英→德 28.4 BLEU，比此前最好的集成模型高 2 BLEU 以上。并行训练是后面在几千亿 token 上预训练的前提。
2. **GPT 与 BERT（2018，OpenAI 与 Google）**。留下的问题：Transformer 仍要为每个任务单独用标注数据训练，多数任务的标注很少，无标注文本却很多。改变：先在无标注文本上预训练，再逐任务微调。GPT 取 decoder 一侧（12 层、带因果 mask），用下一词预测预训练，在 12 个数据集中的 9 个上达到当时最好。BERT 指出单向结构对问答这类逐 token 判断的任务不利，改用 encoder-only 加遮蔽语言模型（随机遮住一部分 token，让模型从两侧上下文还原）；在 GLUE（一组句子级理解任务的合集）上平均分 BERT-large 82.1，GPT 75.1。目标随之从翻译迁移到 GLUE、SQuAD（从给定段落中标出答案片段的问答集）这类理解型 benchmark。
3. **GPT-2 与 T5（2019，OpenAI 与 Google）**。留下的问题：预训练加微调仍要为每个任务准备标注，各家方法也难以公平比较。两家朝相反方向回答。GPT-2 问"不微调、不改参数，语言模型能做多少任务"：zero-shot（不给任何任务样本）在 8 个语言建模数据集中的 7 个上达到当时最好，摘要等任务上作者自述仍很初级。T5 把所有任务统一成"输入文本→输出文本"，在同一框架下系统比较结构与目标：在它的微调设定下，encoder–decoder 加去噪目标（把输入的一部分弄坏，让模型还原）最好，去噪目标总优于语言模型目标；最终模型在 SuperGLUE（比 GLUE 更难的理解任务合集）上得 88.9，人类基线 89.8。
4. **规模定律与 GPT-3（2020，OpenAI）**。留下的问题：微调要成千上万条样本，人看几个例子就能做新任务；GPT-2 的 zero-shot 又太弱。改变分两步。Kaplan 等的 Scaling Laws 发现，语言模型的交叉熵损失随参数量、数据量、算力（训练用的浮点运算总次数，FLOPs）呈幂律下降，跨越 7 个以上数量级，对深度、宽度等形状只有弱依赖。GPT-3 依据这一分析"训练更大的模型、用比常规更少的 token"（原文图 2.2）：8 个规模的模型都训练 300B token，最大的有 1750 亿参数。它展示了 in-context learning（上下文学习：在提示里给几个例子，不更新权重）：SuperGLUE few-shot 得 71.8，超过微调的 BERT-Large（69.0），离微调最好结果（89.0）仍远。GPT-3 自述的局限正是 T5 的强项：只研究了自回归模型，没有双向结构和去噪目标，在需要回看、比较两段文字的任务上较弱。这个节点留下两个问题，分别由下面两个节点回答。
5. **结构收敛（2022，BigScience 与 Google）**。留下的问题：T5 的结论是 encoder–decoder 加去噪最好，GPT-3 却靠 decoder-only 走得最远。BigScience（Hugging Face、Google、LightOn 等多家机构参与的开放合作）的 Wang 等做了对照：因果 decoder、非因果 decoder（前缀部分双向可见）、encoder–decoder 三种结构，各配三种目标，decoder 约 4.8B、encoder–decoder 约 11B 参数，训练 168B token。只做无监督预训练、直接 zero-shot 评测时，因果 decoder-only 加下一词目标最好；再加多任务微调后，用遮蔽目标训练的 encoder–decoder 最好。同年 Google 的 PaLM（5400 亿参数）采用 decoder-only，few-shot 在 29 个英语 NLP benchmark 中的 28 个上超过此前最好结果；它在微调 SuperGLUE 时承认 encoder–decoder 在同等训练成本下通常更好，并用规模缩小差距。[判断] 收敛的原因是目标变了，而不是 T5 的比较错了：评测从"微调后的成绩"换成"不微调的 zero-shot / few-shot 成绩"后，decoder-only 用一个下一词目标就能训练任意文本，训练形式又与生成形式一致。图像、视频生成后来也收敛到相近的配方，跨模态的论证见[生成配方的收敛](../../../perspectives/generative-convergence.md)。
6. **Chinchilla（2022，DeepMind）到 LLaMA（2023，Meta）：重新分配预算**。留下的问题：按 Kaplan 等的配比，算力增加 10 倍时模型应增大 5.5 倍、token 只增 1.8 倍（Chinchilla 第 1 节的概括），于是 GPT-3、Jurassic、Gopher 这些 1750 亿到 2800 亿参数的模型都只训练约 300B token。改变：Hoffmann 等训练了 400 多个模型（7000 万到 160 亿以上参数，5B 到 500B token），用三种方法拟合，结论是固定算力下模型大小与训练 token 数应按相同比例增长。他们用 DeepMind 自己的 Gopher（2800 亿参数、300B token）的算力，训练了 700 亿参数、1.4 万亿 token 的 Chinchilla：MMLU（57 个学科的考试式选择题）5-shot 平均 67.6%，Gopher 为 60.0%。按每个参数分到的训练 token 算，GPT-3 约 1.7 个（300B ÷ 175B），Chinchilla 为 20 个（1.4T ÷ 70B）；按 Chinchilla 的估计，175B 的模型要训练约 3.7 万亿 token 才达到计算最优。LLaMA 接着指出 Chinchilla 只算了训练预算：模型要服务大量用户时，达到同样性能，训练更久的小模型推理更便宜。LLaMA 把 7B、13B 训练到 1.0T token，33B、65B 训练到 1.4T，只用公开数据，13B 在多数 benchmark 上超过 GPT-3，并向研究社区发布权重；它也是因果语言模型，与上一个节点的收敛一致。规模定律的完整内容、外推边界与双下降见[训练科学](../../../cross-domain/fields/training-science/README.md)。

## 技术地基

- **可见性与因果 mask**：每个位置能读哪些位置，决定模型属于 encoder-only、decoder-only 还是 encoder–decoder，也决定能否在一次前向里对所有位置并行计算下一词损失。节点 2–5 的争论都落在这里。[Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 7、12、13 节。
- **注意力（Q、K、V）**：按内容决定读哪里、读什么，是节点 1 取代循环的机制。同一讲义第 3–6 节、[QKV 讲义](../../../docs/foundations/15-qkv-deep-dive.md)；更早的序列模型见 [RNN](../../../docs/foundations/12-rnn.md) 与 [LSTM](../../../docs/foundations/13-lstm.md) 讲义。
- **自监督训练目标**：下一词预测、遮蔽预测、去噪是让文本自己出题的三种方式，节点 2–5 就是在它们之间选择。[自监督与生成目标](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)、[目标分区](../../../foundations/fields/objectives/README.md)。
- **迁移的两种用法**：微调更新权重，in-context learning 只改输入、权重不变；评测采用哪一种，决定了哪种结构胜出（节点 5）。[迁移与元学习讲义](../../../docs/foundations/05c-transfer-meta-learning.md)、[GPT-3 精读](../../papers/gpt3/reading.md)第 2 节。
- **数据配方**：去重、质量过滤、各来源的采样比例；训练 token 数按采样次数计，高质量来源会被重复看到。[GPT-3 精读](../../papers/gpt3/reading.md)第 3 节、[数据分区](../../../foundations/fields/data/README.md)。
- **规模定律与计算预算**：损失随参数量、数据量、算力的幂律变化，以及固定算力下二者怎样配比，决定了节点 4 和节点 6。[训练科学](../../../cross-domain/fields/training-science/README.md)。

## 主要路线与团队偏好

- **decoder-only 加扩大规模**（OpenAI 的 GPT、GPT-2、Scaling Laws、GPT-3）。押注：一个下一词目标、一个因果结构，规模足够大时可以覆盖各种任务；Scaling Laws 把这一押注变成可以计算的预算，GPT-3 原文写明按它的分析决定模型与数据规模。代价：GPT-3 自述在需要双向上下文的任务上较弱，训练与推理成本高；按 Chinchilla 的结论，这一配比下的模型训练 token 偏少。[判断] OpenAI 在四篇中都保留 decoder-only，同时语言模型的对外开放程度逐步收紧：GPT-2 分阶段发布模型，GPT-3 只发布样本与数据重叠信息，没有发布权重。
- **双向可见性加系统比较**（Google 的 Transformer、BERT、T5）。押注：针对理解型 benchmark 和微调设定，encoder-only 或 encoder–decoder 加遮蔽、去噪目标更有效。代价：开放式生成和少样本使用不如 decoder-only 方便。[判断] Google 在这三篇中都发布了代码或权重（tensor2tensor、BERT、T5 与 C4 数据集）；2022 年的 PaLM 改用 decoder-only，论文中未见发布权重的声明。同一团队的路线随目标变化而调整。
- **按算力与推理预算配平模型和数据**（DeepMind 的 Chinchilla，Meta 的 LLaMA）。押注：同样的算力，花在更小的模型、更多的数据上更划算；LLaMA 再把推理成本算进来，多花训练算力换一个推理便宜的小模型。代价：数据需求随之大增，Chinchilla 在结论中提出今后要更重视扩大数据集，并推测只有高质量数据才值得扩大，而它的分析只覆盖训练数据还没过完一遍（单 epoch）的情形。两篇的开放程度相反：Chinchilla 的代码与训练数据（MassiveText，与 Gopher 相同）都是专有的，模型不公开；LLaMA 只用公开数据并发布权重。

## 用什么衡量进展

benchmark 的替换就是本方向目标的迁移：

- **从翻译到理解，再到不微调**：WMT 机器翻译 BLEU（Seq2seq 到 Transformer）→ GLUE、SQuAD（GPT、BERT）→ SuperGLUE（T5 得 88.9，人类基线 89.8，接近饱和）→ 不微调的 zero-shot / few-shot 多任务评测：GPT-3 覆盖二十多个数据集，BigScience 用 EleutherAI 的 LM Evaluation Harness（开源评测框架，31 个数据集）与 T0-Eval（11 个数据集的 zero-shot 评测集合），Chinchilla 与 LLaMA 报告 MMLU、BIG-bench（多种推理与知识任务的合集，Chinchilla 用其中 62 项）、GSM8k（小学数学应用题）、HumanEval（按函数说明写 Python 代码）等。
- **预训练本身**：留出集上的交叉熵或困惑度（交叉熵的指数，越低越好）。规模定律拟合的就是这个量，下游能力要另用上面的 benchmark 检验。
- **口径问题**：评测从微调成绩换成不微调成绩后，哪种结构最好的结论随之反转（节点 5）。网络语料越大，训练数据越容易与测试集重叠：GPT-3 公开了重叠检查信息；Chinchilla 的训练数据是 Gopher 的 4 倍，作者提醒语言建模 benchmark 可能因此被抬高，所以更看重 MMLU 和 BIG-bench。跨论文的数字常常来自不同的评测实现，例如 Chinchilla 表中 GPT-3 的 MMLU 43.9% 取自 MMLU 原作者的测量。

## 当前开放问题

- **双向理解与生成能否兼得？** GPT-3 在局限一节把"双向模型做到同等规模、并支持少样本"列为有前景的方向；BigScience 建议先训练因果 decoder，再做非因果的遮蔽目标适配和多任务微调。入口：[GPT-3 精读](../../papers/gpt3/reading.md)、综合表中 Wang 等一行。
- **数据会不会先于算力成为瓶颈？** 等比例结论意味着算力增加时数据要同比增加；Chinchilla 的分析只覆盖单 epoch，作者呼吁收集更大的高质量数据集。LLaMA 已在 Wikipedia 与 Books 两部分上训练约两个 epoch。入口：[Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)、[训练科学](../../../cross-domain/fields/training-science/README.md)。
- **推理成本怎样进入训练决策？** LLaMA 把模型训练到计算最优点之外，换取推理便宜；结构一侧用稀疏专家（MoE：每个 token 只激活一部分 FFN）和固定大小状态的递推模型压低每个 token 的推理成本。入口：[架构与效率方向](../architecture/README.md)、[DeepSeek-V2 精读](../../papers/deepseek-v2/reading.md)、[Switch Transformer](../../papers/arxiv-2101.03961/README.md)、[Mamba 精读](../../papers/mamba/reading.md)、[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)。
- **长上下文能力在预训练的哪一步获得？** Qwen2.5-1M 在 Qwen2.5 的中间检查点上接续最长 256K 的长上下文预训练，推理时再用位置外推扩到 1M。入口：[Qwen2.5-1M 精读](../../papers/qwen2.5-1m/reading.md)、[长上下文方向](../long-context/README.md)。

## 阅读顺序

1. [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 7、12、13 节：可见性、因果训练为什么能并行、三种结构；第 13.5 节是本页节点 1–5 的机制版。
2. [自监督与生成目标](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)第 1–5 节：下一词与遮蔽两种出题方式。读完做一个小练习：用一段短文本标出输入 token、预测目标和参与损失的位置。
3. [Attention Is All You Need 精读](../../papers/transformer/reading.md)（[文献卡](../../papers/transformer/README.md)）：节点 1 的原文。
4. [GPT-3 精读](../../papers/gpt3/reading.md)（[文献卡](../../papers/gpt3/README.md)）：节点 4，也是本方向的基线，先读数据与 few-shot 评估设置（第 3–4 节）。基线拆分见 [Baseline 页](BASELINES.md)。
5. [Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)，配合[训练科学](../../../cross-domain/fields/training-science/README.md)的规模定律一节：节点 6 与预算问题。
6. [Qwen2.5-1M 精读](../../papers/qwen2.5-1m/reading.md)（[文献卡](../../papers/qwen2.5-1m/README.md)）：把预训练延伸到百万长度的上下文。

按问题排列的阅读路线见[路线图](ROADMAP.md)，本方向收录的全部论文见[论文目录](PAPERS.md)。预训练之后怎样让模型服从指令，见 [SFT](../posttraining/sft/README.md) 与[偏好学习](../posttraining/preferences/README.md)方向，代表是 [InstructGPT 精读](../../papers/instructgpt/reading.md)。

## 批注

**易误读**

- T5 的"encoder–decoder 最好"是在其任务组合与微调设定下（原文 3.2.4 节）；BigScience 的结论分两种设定，引用时要两半一起引（原文第 4 节）。
- few-shot 上下文示例、参数更新和持续预训练是三种不同操作；规模报告中的数据量、token 数和计算预算也不是同一个量。GPT-3 的"300B token"按采样次数计，各来源按权重重复采样（[GPT-3 精读](../../papers/gpt3/reading.md)第 3 节）。
- Chinchilla 与 Gopher 算力相同，但两者的差别不只在模型大小与 token 数：Chinchilla 还换了优化器（AdamW 替代 Adam）、分词器（不做 NFKC 归一化）和数据子集比例（原文 4.1 节）。
- Chinchilla 的 MMLU：摘要写 67.5%、"高 7%"，4.2 节正文与表格写 67.6%、比 Gopher 高 7.6 个百分点，本页用表格数。"175B 需要约 3.7 万亿 token"来自表 3（方法 1）；同页正文举例写"超过 4.2 万亿 token"，两者来自不同的估计方法。
- Chinchilla 的配比针对训练损失、单 epoch、只算训练算力。LLaMA 引用 Hoffmann 等"10B 模型训练 200B token"的建议（Chinchilla 表 3 为 205.1B），并报告 7B 模型在 1T token 之后仍在提升（LLaMA 第 1 节）：计算最优点是"给定训练算力的最优分配"，下游性能在此之后还能继续提高。
- PaLM 的 28/29 是 few-shot 设定下与此前大语言模型的单检查点结果相比，表中排除了经过微调或多任务适配的模型（原文 6.1 节）。

**判断的支撑论文**

- OpenAI 的路线与开放程度：GPT Sec.4.1、GPT-2 Sec.2.3 与 Sec.7 脚注、GPT-3 Sec.2.1 与 Sec.5、Scaling Laws Sec.2；GPT-3 图 2.2 的说明与作者贡献一节（Kaplan、McCandlish 用规模定律指导模型与数据规模的决定）。
- Google 的开放与路线调整：Transformer Sec.7、BERT 代码仓库、T5 Sec.4.1、PaLM Sec.2。
- "收敛是因为目标变了"：T5 Sec.3.2.4、GPT-3 Sec.5、Wang 等 2022 Sec.4–5；PaLM Sec.6.1.2 在微调 SuperGLUE 时引用 T5，写明同等训练成本下 encoder–decoder 在分类微调上通常优于 decoder-only，PaLM 微调后在 SuperGLUE 测试集上得 90.4，略低于 encoder–decoder 的 ST-MoE-32B（91.2）。同一团队在知道这一结论的情况下选择 decoder-only，说明决定选择的是 few-shot 这一目标。
- 第三条路线没有写团队偏好：Chinchilla 与 LLaMA 出自不同团队，各只有一篇，按"同一团队两篇以上"的标准还不足以算作偏好。

**与其他论文的关联**

- 节点 1 之前的两步：Seq2seq 在 WMT'14 英→法上，5 个反转源句的 LSTM 集成得 34.81 BLEU，短语统计翻译基线 33.30；只反转源句一项就让 BLEU 从 25.9 升到 30.6。Bahdanau 注意力在全部句子上 RNNsearch-50 得 26.75，同规模无注意力的 RNNencdec-50 为 17.82，并且在 50 词以上的长句上不退化（原文图 2）。机制展开见 [RNN](../../../docs/foundations/12-rnn.md)、[LSTM](../../../docs/foundations/13-lstm.md) 与 [Attention 与 Transformer](../../../docs/foundations/14-attention-transformer.md) 讲义。
- [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 13.5 节与本页节点 1–5 讲同一件事；两处如有出入，以综合表中的原文出处为准修改。
- [架构与效率方向](../architecture/README.md)从本页的终点接着讲：LLaMA 在原始 Transformer 上做的三处改动，预归一化（把归一化移到每个子层的输入端）、SwiGLU（一种带门控的 FFN 激活函数）、RoPE（旋转位置编码），原文分别注明借自 GPT-3、PaLM 与 GPT-Neo（LLaMA 2.2 节），后续的 MoE、MLA 与 Mamba 都在这个结构上改部件。
- [InstructGPT 精读](../../papers/instructgpt/reading.md)：GPT-3 自述下一词目标不区分重要性、缺少目标导向，后训练从这里接手。
- [深度学习规模化](../../../perspectives/scaling.md)把本页放进跨领域的三阶段总线；[训练科学](../../../cross-domain/fields/training-science/README.md)展开 Kaplan 与 Chinchilla 的分歧。Chinchilla 作者把分歧归于两点：Kaplan 等让所有模型共用固定的训练 token 数与学习率调度，以及其拟合以较小的模型为主（Chinchilla 第 2 节）。[Chinchilla 文献卡](../../../cross-domain/papers/arxiv-2203.15556/README.md)目前只有题录，补精读时"它要解决的问题"应与本页节点 6 一致。

**未核实 / 待验证**

- GPT-2 完整模型的发布时间线（OpenAI 博客无法访问）。
- PaLM 自述局限的精确节号与权重发布情况，综合表中为 ar5iv 转述；Wang 等 2022 的局限一格同样为 ar5iv 转述。
- Chinchilla 的 NeurIPS 2022 正式版题名为 *An empirical analysis of compute-optimal large language model training*，与 arXiv 题名 *Training Compute-Optimal Large Language Models* 不同；本页引用的数字在两版中一致，表号不同（例如 MMLU 表在 arXiv 版为表 6，正式版为表 A8）。
