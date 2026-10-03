# 架构与信息流：CNN 与 Transformer 两条线

> 状态：领域入门页 · 试点 v1 · 依据 [synthesis-cnn.csv](synthesis-cnn.csv)（15 篇）与 [synthesis-transformer.csv](synthesis-transformer.csv)（12 篇）

[回到基础模块](../../README.md) · [完整讲义目录](../../../docs/foundations/01-architectures.md)

## 这个领域在解决什么

给一张 224×224 的照片，判断里面是猫还是狗；给一句英文，生成它的法文译文。两件事都要先决定：输入的哪些部分之间应该交换信息、用多少参数、这些参数怎样从数据里学出来。架构就是对这些选择的回答。图像里相邻像素关系最紧，于是有了只看局部、处处共用同一个小核的卷积网络（CNN）；句子里相关的词可能相隔很远，于是有了按内容决定“读哪里”的注意力和 Transformer。这个方向关心的是：每一种结构在什么数据规模、什么目标下最好用，以及它们怎样一步步走到今天。

## 主线历史

每个节点先写“上一个节点留下的问题”，再写它改变了什么。完整论据和逐篇数字在两张综合表里。

**CNN 一线：从视觉皮层模型到预训练视觉主干**

1. **Neocognitron（1980，NHK，Fukushima）→ LeNet（1998，LeCun 等）**。问题：识别结果随图案平移和形变而改变。Neocognitron 按 Hubel–Wiesel 的简单/复杂细胞层级，交替堆叠“提取特征”和“容忍位置变化”的两种层，同一平面内的单元共用同一组连接，这就是卷积与权重共享的雏形。它靠无监督自组织学习，作者报告十类图案时结果对参数非常敏感。LeNet 改用标注数据和反向传播训练卷积核，在文档识别中落地（LeNet 原文本轮未能打开，见批注）。
2. **HOG（2005，INRIA）与 DPM（2010，Chicago/Berkeley 一系）**。这一时期视觉检测的主流是另一条路线：梯度方向直方图这类手工特征，加线性 SVM 或可变形部件模型。HOG 的流水线就是一个核固定的浅层 CNN（[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节）。它们留下的问题：特征由人设计，只有最后的分类器在学习；HOG 在 MIT 行人库上做到近乎完美分离后，作者另建了更难的 INRIA 数据集。
3. **ImageNet（2009，Princeton）与 ILSVRC（2010 起每年举办）**。留下的问题：可学习的深网络需要大规模标注数据，各团队也需要同一个公开 benchmark 来比较。改变：提供按 WordNet 组织、目标数千万张的标注图库，以及约 120 万训练图、1000 类的年度竞赛。
4. **AlexNet（2012，Toronto）**。留下的问题：CNN 在高分辨率图像上大规模训练一直太贵。改变：两块 GPU、ReLU、dropout，加上 ImageNet 规模的数据，在 ILSVRC-2012 上 top-5 错误率 15.3%，第二名（Fisher 向量手工特征）为 26.2%。ILSVRC 组织者把 2012 年称为转折点：2013 年绝大多数、2014 年几乎全部参赛方法改用 CNN。
5. **VGG、GoogLeNet（2014）→ ResNet（2015，Microsoft Research）**。留下的问题：ILSVRC 上的竞争变成“怎样做得更深”。VGG 专门研究深度，GoogLeNet 在固定计算预算下加深加宽；更深的网络随即暴露出退化问题，训练误差反而上升。ResNet 用残差学习解决这一点，ILSVRC 2015 top-5 测试错误率 3.57%。
6. **R-CNN（2013）与 DPM are CNNs（2014），Berkeley**。留下的问题：PASCAL VOC 检测在 2010–2012 年停滞。改变：把 ImageNet 预训练的 CNN 迁移到检测并微调，VOC2007 mAP 从 HOG-DPM 的 33.7% 升到 54.2%；同一作者随后证明 DPM 本身可以展开成 CNN，手工特征路线并入 CNN 路线。[判断] 从这里开始，“ImageNet 预训练的视觉主干”成为检测、分割等任务的默认起点。
7. **ViT（2020，Google Brain）↔ ConvNeXt（2022，FAIR）**。留下的问题：卷积的局部性是必需的先验，还是可以由数据学出来？ViT 把图像切块直接交给 Transformer：只在 ImageNet 上训练时不如 ResNet，在 JFT-300M 上预训练后反超。ConvNeXt 反过来，只给 ResNet-50 换上 Transformer 式训练配方就提升 2.7 个百分点，再借用 Transformer 的设计后全面追平并超过 Swin。

**Transformer 一线：从固定长度向量到 decoder-only 大模型**

1. **Seq2seq（2014，Google）**。问题：深度网络只能处理固定维度的输入输出，无法直接把序列映射到序列。改变：一个 LSTM 把源句压成一个固定长度向量，另一个 LSTM 从这个向量生成译文，在 WMT'14 英→法上超过短语统计翻译基线。
2. **Bahdanau 注意力（2014，Jacobs University Bremen 与 Montréal）**。留下的问题：整句信息都要经过一个固定长度向量，长句性能急剧下降。改变：解码每个词时按权重读取源句各位置（软对齐），长句不再退化。编码和解码仍是循环网络。
3. **Transformer（2017，Google）**。留下的问题：循环网络沿位置逐步计算，同一样本内部无法并行。改变：用注意力作为序列内和序列间交互的主体，去掉循环；目标仍是 WMT 机器翻译，英→德比此前最好集成模型高 2 BLEU 以上。
4. **GPT（2018，OpenAI）与 BERT（2018，Google）**。留下的问题：各任务的标注数据少，每个任务从头训练模型。两家给出两种预训练：GPT 取 decoder 一侧，用下一词预测预训练再微调；BERT 指出单向结构对问答等任务不利，改用 encoder-only 加遮蔽语言模型。目标从翻译迁移到 GLUE、SQuAD 这类理解型 benchmark。
5. **GPT-2（2019）与 T5（2019，Google）**。留下的问题：预训练加微调仍然要逐任务准备标注数据，各种方法也难以公平比较。GPT-2 改问“不微调、不改参数，语言模型能做多少任务”；T5 把所有任务统一成文本到文本，系统比较三种结构，结论是在其微调设定下 encoder–decoder 加去噪目标最好。
6. **GPT-3（2020，OpenAI）**。留下的问题：微调需要成千上万条样本，人只需看几个例子。改变：1750 亿参数的 decoder-only 模型只靠上下文中的示例完成任务（in-context learning，上下文学习：在提示里给几个例子，不更新权重）。它自述的局限正是 T5 的强项：没有双向结构和去噪目标。
7. **收敛：Wang 等（2022，BigScience）、PaLM（2022，Google）、LLaMA（2023，Meta）**。留下的问题：T5 与 GPT-3 的结论看起来互相矛盾。BigScience 的对照实验给出答案：只做无监督预训练后直接 zero-shot 评测，因果 decoder-only 最好；加多任务微调后，encoder–decoder 最好。此后 Google 的 PaLM、Meta 的 LLaMA 都是因果语言模型。

**两条线的交汇**：ViT 把 Transformer 带进视觉，Transformer 的每个子层又沿用 ResNet 的残差连接；两条线都采用“先在大数据上预训练、再迁移到具体任务”的流程（CNN 一线自 R-CNN，Transformer 一线自 GPT 与 BERT）。

## 技术地基

- **卷积与权重共享**：小核在所有位置复用，参数量与图像大小无关；CNN 一线的全部节点都建立在它上面。[CNN 讲义](../../../docs/foundations/11-cnn.md)第 2–3 节。
- **梯度训练与反向传播**：把“手工指定的核”变成“由数据决定的核”，是 Neocognitron 到 LeNet、HOG 到 AlexNet 两次转变的共同条件。[优化模块](../../../docs/foundations/02-optimization.md)。
- **残差连接**：让很深的网络可以训练，ResNet 提出后被 Transformer 每个子层沿用。[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节、[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 10.2 节。
- **注意力（Q、K、V）**：按内容决定读哪里、读什么，是 Transformer 一线从 Bahdanau 起的核心机制。[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 3–6 节、[QKV 讲义](../../../docs/foundations/15-qkv-deep-dive.md)。
- **可见性与因果 mask**：决定一个模型属于 encoder-only、decoder-only 还是 encoder–decoder，也决定它能否用下一词目标并行训练。[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 7、12、13 节。
- **预训练与迁移**：先在大数据上学通用表示，再迁移到具体任务；两条线在 2013 年之后都以此为默认流程。[迁移与元学习模块](../../../docs/foundations/05c-transfer-meta-learning.md)。

## 主要路线与团队偏好

- **手工特征加浅层学习**（Dalal 与 Triggs 的 HOG；Felzenszwalb、Girshick 等的 DPM）。押注：人对图像结构的先验（方向梯度、可变形部件）比从数据中学更可靠。代价：特征固定，进展受限于人能设计出什么；PASCAL VOC 上 2010–2012 年的停滞即是表现。[判断] Girshick 所在的一系在 DPM、R-CNN、DPM are CNNs 三篇中始终以 PASCAL VOC 检测为目标、以 DPM 为对照，并在转向 CNN 时选择证明“旧模型是新模型的特例”，而不是另起炉灶。
- **ImageNet 规模的有监督 CNN**（Toronto 的 AlexNet，Oxford 的 VGG，Google 的 GoogLeNet，Microsoft Research 的 ResNet）。押注：数据和算力足够时，深网络从像素学到的特征优于手工特征。代价：依赖大规模标注和 GPU，结构选择长期围绕 ILSVRC 的分类指标展开。
- **decoder-only 加扩大规模**（OpenAI 的 GPT、GPT-2、GPT-3 与 Scaling Laws）。押注：一个下一词目标、一个因果结构，规模足够大时可以覆盖各种任务。代价：GPT-3 自述在需要双向上下文的任务上较弱，训练与推理成本高。[判断] OpenAI 在四篇中都保留 decoder-only，同时对外开放程度逐步收紧：GPT-2 分阶段发布模型，GPT-3 只发布样本与数据重叠信息，未发布权重。
- **encoder-only / encoder–decoder 加系统比较**（Google 的 Transformer、BERT、T5）。押注：针对理解型 benchmark 和微调设定，双向可见性与去噪目标更有效。代价：生成与少样本使用不如 decoder-only 方便。[判断] Google 在这三篇中都发布了代码或权重（tensor2tensor、BERT、T5 与 C4 数据集），ViT 也发布了模型；2022 年的 PaLM 改用 decoder-only，论文中未见发布权重的声明。同一团队的路线随目标变化而调整。

## 用什么衡量进展

benchmark 的替换就是领域目标的迁移：

- **视觉**：MIT 行人库（HOG 近乎完美分离后饱和）→ INRIA 行人库 → PASCAL VOC 检测（DPM、R-CNN 的主战场）→ ImageNet / ILSVRC 分类（2010 起，AlexNet 到 ResNet 的主战场）→ COCO 检测、ADE20K 分割等迁移任务（ResNet、ConvNeXt 都报告）。ILSVRC 组织者自己记录了外界批评：数据集不够难、细粒度类别有标注错误、外部数据规则太严。ViT 的关键结论依赖 JFT-300M，这是非公开数据，外部团队无法复现同一条件。
- **语言**：WMT 机器翻译 BLEU（Seq2seq 到 Transformer）→ GLUE、SQuAD（GPT、BERT）→ SuperGLUE（T5 得 88.9，人类基线 89.8，接近饱和）→ 不微调的 zero-shot / few-shot 多任务评测（GPT-3 覆盖二十多个数据集，BigScience 用 LM Evaluation Harness 与 T0-Eval，LLaMA 报告 MMLU、GSM8k、HumanEval 等）。口径问题：评测从“微调后成绩”换成“不微调成绩”后，哪种结构最好的结论随之反转（见主线第 7 个节点）；大规模网络语料还带来训练数据与测试集重叠的问题，GPT-3 公开了它的重叠检查信息。

## 当前开放问题

- **架构差异与数据、训练配方差异怎样分开？** ViT 与 ConvNeXt 的对照显示，大部分差距可以由数据规模和训练配方解释。入口：[ViT 精读](../../../multimodal/papers/vit/reading.md)、[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节。
- **注意力的二次方成本，能否换成固定大小的递推状态？** 线性注意力、状态空间模型和 Mamba 都在回答这个问题。入口：[递推状态谱系](../../relations/recurrent-state.md)、[Mamba 精读](../../../llm/papers/mamba/reading.md)。
- **知识存在哪里，怎样扩容？** FFN 可以读成键值记忆，事实回忆研究和 MoE 都沿着这条分工展开。入口：[注意力与 FFN 的分工谱系](../../relations/attention-ffn-division.md)、[FFN 键值记忆](../../../cross-domain/papers/arxiv-2012.14913/README.md)、[Switch Transformer](../../../llm/papers/arxiv-2101.03961/README.md)。
- **双向理解与生成能否兼得？** GPT-3 在局限一节把“双向模型做到同等规模、并支持少样本”列为有前景的方向；BigScience 建议先训练因果 decoder，再做非因果适配和多任务微调。入口：[GPT-3 精读](../../../llm/papers/gpt3/reading.md)。

## 阅读顺序

1. [CNN 讲义](../../../docs/foundations/11-cnn.md)：先从一个 [−1,0,1] 核理解卷积，再读第 6 节的历史链和第 9 节的“从手工特征到可学习特征”。
2. [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)：手算一次注意力，再读第 13.5 节三条路线的收敛。
3. [QKV 讲义](../../../docs/foundations/15-qkv-deep-dive.md)：在讲义 14 的基础上，弄清匹配与内容为什么要分开，以及注意力与核回归、递推的结构关系。
4. [Attention Is All You Need 精读](../../../llm/papers/transformer/reading.md)：Transformer 一线第 3 个节点的原文。
5. [ViT 精读](../../../multimodal/papers/vit/reading.md)：两条线的交汇点，也是“架构与数据”这个开放问题的起点。
6. [GPT-3 精读](../../../llm/papers/gpt3/reading.md)：decoder-only 加规模这条路线的代表，它的局限一节连接到收敛问题。

同一方向的其余模块：[RNN](../../../docs/foundations/12-rnn.md) 与 [LSTM](../../../docs/foundations/13-lstm.md) 是 Transformer 之前的序列模型；[SSM、GNN 与 MoE](../../../docs/foundations/18-ssm-gnn-moe.md) 接在开放问题之后；[VAE](../../../docs/foundations/16-vae.md)、[扩散模型](../../../docs/foundations/17-diffusion.md) 与 [DDPM](../../../multimodal/papers/ddpm/README.md) 讨论生成建模，其中的去噪网络同样要在 CNN 与 Transformer 之间选择。

## 批注

**易误读**

- AlexNet 与第二名的 15.3% 对 26.2%，比较的是 ILSVRC-2012 测试集 top-5 错误率；AlexNet 的这个数字来自多个 CNN 的平均，其中两个用了额外的 ImageNet Fall 2011 数据预训练（原文第 6 节）。
- T5 的“encoder–decoder 最好”是在其任务组合与微调设定下（原文 3.2.4 节）；BigScience 的结论分两种设定，不能只引用其中一半（原文第 4 节）。
- ViT 在 ImageNet-1k 上不如 ResNet、在 JFT-300M 上反超，比较的是同等规模的 BiT ResNet，并且都经过迁移微调（原文 4.3 节、Fig.3）。

**判断的支撑论文**

- Girshick 一系的偏好：DPM（PAMI 2010）Sec.8、R-CNN Table 1–2、DPM are CNNs Table 1，三篇都以 PASCAL VOC 为目标、以 DPM 为对照。
- OpenAI 的路线与开放程度：GPT Sec.4.1、GPT-2 Sec.2.3 与 Sec.7 脚注、GPT-3 Sec.2.1 与 Sec.5、Scaling Laws Sec.2。
- Google 的开放与路线调整：Transformer Sec.7、BERT 代码仓库、T5 Sec.4.1、ViT Sec.1 脚注、PaLM Sec.2。
- “收敛是因为目标变了”：T5 Sec.3.2.4、GPT-3 Sec.5、Wang 等 2022 Sec.4–5。
- “改变局面的是数据、算力和 benchmark”：AlexNet Sec.1、ILSVRC 综述 Sec.5.1。
- “CNN 与 Transformer 的胜负很大程度取决于数据和配方”：ViT Sec.4.3、ConvNeXt Sec.2.1。
- Meta 的两篇（ConvNeXt 发布代码，LLaMA 向研究社区发布全部权重）都选择开放，但出自不同小组，按“同一团队两篇以上”的标准还不足以算作偏好，因此未写进正文。

**与其他论文的关联**

- [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 13.5 节、第 17 节，与本页 Transformer 一线一致；[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6、9 节，与本页 CNN 一线一致。两处如有出入，以综合表中的原文出处为准修改。
- [LLM 架构方向](../../../llm/fields/architecture/README.md) 从本页 Transformer 一线的终点接着往下讲。

**综合表说明**

- 两张表各一行一篇，列为年份、团队、论文（路线）、要解决的问题、对照的 baseline、benchmark、自述局限、代码/数据是否开放、来源 URL。“论文（路线）”一列是为了能识别每一行而加的。各格是原文的中文转述，并注明节号或表号，没有大段照录原文。
- 每一格都来自实际打开的原文；只经 ar5iv 页面摘要模型转述、没有逐字核对的格，表内标注“ar5iv 转述”。

**未核实 / 待验证**

- LeNet（LeCun 等 1998）全文本轮没能打开，synthesis-cnn.csv 中该行除题录外都标为未核实；主线第 2 个节点的描述沿用 CNN 讲义原有的写法。
- GPT-2 完整模型的发布时间线（OpenAI 博客无法访问）；PaLM 自述局限的精确节号。
- DPM（PAMI）发表年份按题录填写，所用 PDF 正文没有印出年份。
