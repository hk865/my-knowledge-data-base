# 模型科学：训练出来的网络内部发生了什么

> 状态：跨方向入门页 · v1 · 证据以语言模型为主

## 这个领域在解决什么

给 GPT-2 XL 输入"The Space Needle is located in the city of"，它会接"Seattle"（ROME 论文引言里的例子）。模型科学追问三件事：这条事实写在哪些参数里；推理时它经过哪些层、哪些位置，被送到预测位置；能不能只改这一条，例如让模型改答"Paris"，而别的事实不受影响。视觉模型里有同样的问题：在 ImageNet 上训练好的卷积网络，第一层学到了什么样的卷积核；ViT 的注意力头在最低一层看多远。

研究对象是训练结束后的网络本身。证据分三个层级：**观察**（直接看权重，或把内部向量投影到输出词表上，看它偏向哪些词）、**预测**（探针：在冻结的内部表示上训练一个简单分类器，看能否读出某个性质）、**干预**（改动某处的激活或权重，看输出怎样变）。只有干预能说明模型实际依赖某个部件，所以这个方向的进展，大多是把观察到的现象推进成可以干预的机制。研究训练过程本身（优化地形、规模定律、遗忘）的工作在[训练科学](../training-science/README.md)；两个方向在"机制何时形成"上交汇，例如 induction head 的形成时刻。本方向属于[跨方向方法与探索](../../README.md)。

## 主线历史

每个节点先写上一个节点留下的问题，再写它改变了什么。语言一侧四个节点的完整证据与手算在[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)。

1. **AlexNet 的第一层卷积核（2012，Toronto 的 Krizhevsky、Sutskever、Hinton）**。第一层有 96 个 11×11×3 的卷积核，形状与彩色图像块相同，可以直接画成图片。网络学到了多种对频率和方向有选择性的核，以及各种颜色斑块（原文 §6.1）；Yosinski 等 2014 把这一现象概括为：在自然图像上训练的网络，第一层学到类似 Gabor 滤波器（按特定方向和频率响应的带通滤波器）的特征和颜色斑块。它改变的是：学出来的特征第一次可以直接看，而且与手工设计的方向滤波器相似（[CNN 讲义](../../../foundations/lessons/11-cnn.md)第 9 节）。留下的问题：只有第一层的权重与像素处在同一个空间；更深的层，以及输入是离散 token 的语言模型，都没有现成的"图片"可看。
2. **FFN 键值记忆（Geva、Schuster、Berant、Levy，2020 年 arXiv，EMNLP 2021；Tel Aviv University 与 AI2）**。它给深层参数提供了一种读法：在 FFN(x) = f(xW_1)W_2 中，W_1 的每一列是一个 key，W_2 的每一行是一个 value（推导见关系页第 4 节）。key 用训练集中让它激活最强的 25 个前缀来读，value 投影到输出词表上来读。在一个 16 层、WikiText-103 上训练的语言模型里，key 对应人能读懂的模式，低层以浅层模式为主（例如以同一个词结尾），高层以语义模式为主（例如同一话题）；高层 value 把概率集中在紧跟该模式之后可能出现的词上。留下的问题：这些都是相关性的观察，某一次具体预测是否用到了这些记忆，观察回答不了。
3. **ROME（Meng、Bau、Andonian、Belinkov 2022；MIT CSAIL、Northeastern University、Technion）**。ROME 的相关工作一节写明了转向的理由：探针一类方法的主要局限是与网络的实际行为脱节，因果效应可以避开这类误导性的相关。它的因果追踪（先给输入中的主语加噪声，再把某一层某个位置的激活恢复成干净值，看正确答案的概率恢复多少）在 GPT-2 XL 中发现，事实回忆集中在中间层、主语最后一个 token 的 MLP 上：该位置 MLP 的平均间接效应峰值为 6.6%，同一位置的注意力为 1.6%。ROME 据此把这一层 MLP 当作键值表，用一次秩一更新（只加一个外积矩阵）写入新事实。它把研究从观察推进到干预，并且让干预本身可以用来编辑模型。留下的问题：高层注意力在提示最后一个 token 上的作用同样很大，注意力怎样把事实搬到预测位置，作者只给出了假设。
4. **Induction Heads（Olsson 等 2022，Anthropic）**。上一节点留下的是注意力一侧的问题：多个注意力头怎样跨层配合，完成一个说得清楚的功能。作者把每个头拆成两个电路（电路：几个跨层配合、合起来实现一个可描述算法的部件）：QK 电路决定看哪里，OV 电路决定看到之后写出什么。上下文学习（不更新参数、只靠提示中的例子学会新模式）中的 [A][B] … [A] → [B] 续写，由前一层的"前一 token 头"与后一层的 induction head 组合完成。这类头形成的时刻，正是训练早期（约 25 亿到 50 亿 token 之间）上下文学习能力骤升的时刻；只有一层的模型两者都不出现。它改变的是：分析单位从单个部件变成跨层组合的电路，一个机制第一次同时对应到一项能力和一个训练时刻。留下的问题：因果证据在小型纯注意力模型上最强，带 MLP 的大模型上是相关性证据（原文摘要）；它研究的是上下文中的复制，与事实回忆还没有接上。
5. **Dissecting Recall（Geva、Bastings、Filippova、Globerson 2023；Google DeepMind、Tel Aviv University、Google Research）**。它把前两个节点接起来：在 GPT-2（1.5B）和 GPT-J（6B）上用注意力敲除（在一段层内切断预测位置对某些位置的注意力，看正确答案的概率下降多少）追踪事实被取出的路径。取出分三步：较早层的 MLP 把大量与主语相关的属性写进主语最后一个 token 的表示；关系词的信息传到预测位置；上层注意力头再从这份富集后的表示中抽取属性。切断中高层对主语位置的注意力，正确答案的概率最多下降约 60%。结论是**事实主要存于 MLP，由注意力参与读出**，并且存储的重点比 ROME 所说的中间层更靠前。留下的问题：这种"MLP 存储、注意力读出"的分工，是训练找到的倾向，还是可以直接写进架构？
6. **Engram（Cheng 等 2026，北京大学与 DeepSeek-AI）**。它从架构一侧回答上一个问题：用当前 token 与前几个 token 组成的 N-gram 做哈希，从一张大嵌入表里直接取出向量，把静态模式交给查表。推理时关掉 Engram、主干不变，事实知识类基准只保留原性能的 29%–44%，阅读理解类保留 81%–93%（论文 Figure 6）。作者在相关工作中把 FFN 键值记忆和因果追踪列为"知识怎样存储"的背景。模型科学的发现在这里回流成了架构设计（关系页第 8–9 节）。

## 技术地基

- **注意力的 A 与 V**：A = softmax(QKᵀ/√d_k) 决定每个位置从哪里读、读多少，V 是被读出的内容。induction head 的 QK 与 OV 电路、读出事实的注意力头，都在这两条通路上分析。[QKV 讲义](../../../foundations/lessons/15-qkv-deep-dive.md)第 4–5 节、[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 4–6 节。
- **FFN**：对每个位置独立做的两层变换，是键值记忆读法和 ROME 编辑的对象。[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.1 节。
- **残差连接与残差流**：每个子层把输出加回输入，各层在同一条主表示上逐层累加更新，这条主表示称为残差流。因果追踪恢复的、注意力敲除切断的、投影到词表上读的，都是残差流上的向量。[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.2 节。
- **输出层把向量变成词的分布**：把中间层的向量也乘上输出矩阵，就能读出它偏向哪些词，这就是词表投影（logit lens）。[Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 11 节。
- **卷积核与感受野**：卷积核在所有位置共用，第一层核的形状与图像块相同；感受野（能影响一个输出的输入区域）随层数扩大。ViT 的"注意力距离"就是拿它作参照的。[CNN 讲义](../../../foundations/lessons/11-cnn.md)第 2–4 节。
- **MoE**：路由器为每个 token 只选少数几个专家，稀疏化的对象正是 FFN，是"FFN 存知识"在架构上的近邻。[SSM、GNN 与 MoE 讲义](../../../foundations/lessons/18-ssm-gnn-moe.md)第 4 节。

## 主要路线与团队偏好

- **词表投影与记忆读法**（Geva 一系：FFN 键值记忆 2021 → Dissecting Recall 2023）。押注：把参数和中间表示投影到输出词表上就能读出它们编码了什么，再用干预确认。代价：投影在早期层只是近似，Dissecting Recall 在局限一节自述了这一点。[判断] Geva 的单位从 Tel Aviv University 与 AI2 换到 Google DeepMind，两篇都以投影到词表为主要读法（2021 读 value，2023 读主语表示和注意力的输出），研究对象从单个子层扩展到子层之间的信息流。
- **因果干预与编辑**（Meng、Bau、Andonian、Belinkov 的 [ROME](../../papers/arxiv-2202.05262/README.md)）。押注：改动内部状态后输出随之改变，才算定位到了机制；定位准确，就能直接改写权重。代价：ROME 一次只编辑一条事实，而且关联有方向，"西雅图的标志性建筑是 Space Needle"与"Space Needle 是西雅图的标志性建筑"要分两次编辑（原文 §3.7）。[判断] Belinkov 参与的 ROME 与 2025 年的 FUR（从参数中遗忘推理步骤，见开放问题）都以"改动参数后预测是否改变"为证据标准。
- **电路逆向工程**（Anthropic：Elhage 等 2021 的数学框架 → Olsson 等 2022 的 [Induction Heads](../../papers/arxiv-2209.11895/README.md)）。押注：先在小型纯注意力模型里把机制完整拆开，再到大模型里找同一机制的迹象。代价：大模型上只有相关性证据，作者在六条论据中逐条标明了证据强弱。[判断] 两篇都从两层以内的纯注意力模型起步，都把头拆成 QK 与 OV 两个电路来分析。
- **探针**（HSE University 的 Troshin、Chirkova 2022 [Probing Pretrained Models of Source Code](../../../llm/papers/arxiv-2202.08975/README.md)；Free University of Bozen-Bolzano 与 University of Bordeaux 的 Karmakar、Robbes 2023 [INSPECT](../../papers/arxiv-2312.05092/README.md)）。押注：在冻结表示上训练简单分类器，逐层、逐模型比较哪些性质可以读出，并做成可复用的基准。INSPECT 定义 15 个探针任务，测 8 个代码模型并以自然语言模型 BERT 作基线，框架与数据开源；结果是融入结构信息的模型（如 GraphCodeBERT）对代码特征表示得更好，BERT 在部分任务上与代码模型不相上下。代价：探针说明信息存在于表示中，模型是否用到它要靠干预检验。

## 用什么衡量进展

这个方向没有统一的排行榜。进展体现在：用哪一层级的证据、在多大的模型上、复现出同一个机制。常用的量：

- **因果追踪的间接效应**：恢复某一层某个位置的激活后，正确答案的概率恢复了多少。ROME 的 6.6% 对 1.6%，是 GPT-2 XL 上同一位置（主语最后一个 token、中间层）MLP 与注意力的平均间接效应峰值，平均自约 1000 条事实陈述。附录把同一实验做到 GPT-J（6B）和 GPT-NeoX（20B），曲线形状相似，但主语最后一个 token 上早期层注意力的作用更明显。
- **注意力敲除后的概率下降**：Dissecting Recall 的约 60%。口径：切断的是一段层，因为只切单层时，信息仍可能在更早的层里传过去（原文局限一节）。
- **编辑基准**：zsRE（由零样本关系抽取数据改造的编辑任务）与 ROME 作者新建的 CounterFact（21,919 条反事实记录）。CounterFact 分三项打分：编辑成功（新答案的概率超过原答案）、换一种说法仍成功（泛化）、相邻主语不受影响（特异性），再取三者的调和平均。作者新建它的理由是：已有编辑基准常常只测模型原本就认为可能的答案，低估了难度。
- **上下文学习分数**：同一段文本中第 50 个 token 与第 500 个 token 的平均损失之差，差越大说明模型越会利用前文。Olsson 等说明这两个位置选得有些随意，换成其他位置结论不变。
- **探针准确率**：要和基线对照着读。INSPECT 用 BERT 作基线；Troshin 与 Chirkova 用 3 层 MLP 复核线性探针的结果。
- **视觉一侧**：卷积核的可视化，以及 ViT 的平均注意力距离（按注意力权重平均出的、信息被整合的图像空间距离，作用类似 CNN 的感受野；ViT 原文 §4.5）。

## 不同模态的差异

语言一侧已经有从观察到干预的完整链条；视觉一侧的证据目前集中在第一层的可视化和 ViT 的注意力距离。下面按三个问题对照。

**早期层在做什么**

- `[经验]` 视觉 CNN：第一层学到对频率和方向有选择性的核与颜色斑块（AlexNet §6.1），Yosinski 等称之为 Gabor 状。手工的 HOG 把方向梯度写死在第一步，可学习的 CNN 由数据把它重新学了出来（[CNN 讲义](../../../foundations/lessons/11-cnn.md)第 9 节）。
- `[经验]` 视觉 ViT：切块嵌入滤波器的主成分，看上去像描述块内细节结构的一组基函数；最低层里一些头已经看向图像的大部分区域，另一些头始终只看邻近区域；前面接 ResNet 的混合模型里这种局部头较少，作者据此推测它们承担了 CNN 早期卷积层的作用（ViT §4.5、Fig.7；[ViT 精读](../../../multimodal/papers/vit/reading.md)）。
- `[经验]` 语言：FFN 键值记忆中，低层 key 以浅层模式为主，高层以语义模式为主（Geva 2021）；Engram 的机制分析显示，主干早期层原本也在花容量重建静态的局部模式（关系页第 8 节）。
- `[判断]` 三处呈现同一种分层：早期层处理局部、浅层的模式，越往上越抽象。承担者不同：CNN 由卷积结构规定局部性，ViT 由一部分注意力头学出局部性，语言模型由低层 FFN 记忆承担，Engram 再把其中的静态部分交给查表。

**怎样看到内部**

- `[结构]` 卷积第一层的核与输入图像块同形（AlexNet 是 96 个 11×11×3 的核），权重本身就能画成图片；从第二层起，核的输入是上一层的特征图，权重对应的是特征通道。语言模型的输入是离散 token，经嵌入表才变成向量，所以语言一侧发展出了词表投影、因果追踪和注意力敲除。

**知识存放与复制**

- 语言：事实主要写在 MLP 里，由注意力头读出（ROME、Dissecting Recall）；上下文中的复制由 induction head 完成（Olsson 2022）。
- 视觉：ViT 的 MLP 能否读成键值记忆，视觉模型里有没有类似 induction head 的复制电路，列为下一节的开放问题。

## 当前开放问题

- **这些机制在更大的现代模型上是否成立？** ROME 的定位主要在 GPT-2 XL 上完成，附录扩到 20B 的 GPT-NeoX；Dissecting Recall 只覆盖 GPT-2 与 GPT-J；induction head 在大模型上只有相关性证据。训练数据和训练代码完整公开的模型让这类研究能在已知的训练条件下做，例如 [OLMo](../../../llm/papers/arxiv-2402.00838/README.md)，它与权重一起发布了训练数据、训练代码和评测代码。入口：[ROME](../../papers/arxiv-2202.05262/README.md)、[Dissecting Recall](../../papers/arxiv-2304.14767/README.md)、[Induction Heads](../../papers/arxiv-2209.11895/README.md)。
- **存储与读出的分工，是训练找到的倾向还是架构边界？** Dissecting Recall 发现，读出事实的注意力头参数里也编码了主语到属性的映射；Engram 把静态模式移到查表之后模型表现更好，后续工作又把记忆表做成可以跨分词器、跨模型移植的部件。入口：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 6–9 节、[Engram](../../../llm/papers/arxiv-2601.07372/README.md)、[Tokenizer-Agnostic Engram Module](../../../llm/papers/arxiv-2607.29065/README.md)、[Frozen Memory Is Not Enough](../../../llm/papers/arxiv-2608.17050/README.md)。
- **模型写出的推理步骤，是它实际用到的计算吗？** 这是解释的忠实性问题。Paul 等（Findings of EMNLP 2024）对 12 个大模型做因果中介分析，发现模型生成答案时并不可靠地使用自己写出的中间步骤，并提出训练框架 FRODO；Tutek 等（EMNLP 2025）提出 FUR，把推理步骤所含的信息从参数中遗忘掉，用预测的变化度量推理链对模型参数知识的忠实程度。入口：[Making Reasoning Matter](../../../llm/papers/url-https-aclanthology.org-2024.findings-emnlp.882/README.md)、[Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](../../../llm/papers/url-https-aclanthology.org-2025.emnlp-main.504/README.md)。
- **视觉模型的知识存在哪里？** ViT 的 MLP 层能否读成键值记忆，视觉 Transformer 里有没有与 induction head 对应的复制电路，因果追踪一类的干预用在视觉模型上会定位到哪里，这三个问题在本方向还没有对应的论文。入口：[ViT 精读](../../../multimodal/papers/vit/reading.md)、[视觉表示方向](../../../multimodal/fields/visual-representation/README.md)。

## 阅读顺序

1. [QKV 讲义](../../../foundations/lessons/15-qkv-deep-dive.md)第 4–5 节与 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.1 节：先手算一次 A 与 V 的分工和 FFN，本页的机制都发生在这两种子层上。
2. [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)：语言一侧的主干，把下面四篇串成一条链，每个节点都有手算或原文证据。
3. [FFN 键值记忆](../../papers/arxiv-2012.14913/README.md)：学会把参数读成键值表，这是 ROME 编辑与 Engram 查表的共同出发点。
4. [ROME](../../papers/arxiv-2202.05262/README.md)：从观察到干预的转折，也是理解编辑基准的入口。
5. [Induction Heads](../../papers/arxiv-2209.11895/README.md)：电路这一分析单位，以及机制形成与训练时刻的对应；训练动态一侧接[训练科学](../training-science/README.md)。
6. [Dissecting Recall](../../papers/arxiv-2304.14767/README.md)：把存储与读出接成一条完整路径。

接着读 [Baseline 页](BASELINES.md)，看后续工作分别在改基线的哪个部件；[路线图](ROADMAP.md)给出检验理解的练习；[论文目录](PAPERS.md)列出本方向全部文献。视觉一侧从 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 9 节与 [ViT 精读](../../../multimodal/papers/vit/reading.md)开始。

## 批注

**易误读**

- ROME 的 6.6% 对 1.6% 是平均间接效应的峰值，比较的是同一位置上的 MLP 与注意力，反映的是该位置的因果贡献，不等于两种子层对事实回忆的总贡献（原文 §2、Figure 2）。
- 两篇对"哪几层存事实"的说法不同：ROME 指中间层 MLP，Dissecting Recall 指较早层的 MLP 是主语富集的主要来源（§1）。引用时写明出处。
- "Gabor 状"一词出自 Yosinski 等 2014 的摘要；AlexNet 原文 §6.1 的措辞是"对频率和方向有选择性的核"与"颜色斑块"。
- Olsson 等发现，相变之后从两层小模型到 13B 模型，上下文学习分数都大致在 0.4 nats；它度量的是前后位置损失的相对下降，作者提醒在更低的起点上降同样多，可能需要更多的机制（原文 Argument 1 与"Seemingly Constant In-Context Learning Score"一节）。
- ViT 的注意力距离是按头、按层、跨图像平均的结果（Fig.7 中每个点是某一层某一个头的平均值），不对应单张图像。
- 探针能读出某个性质，说明信息存在于表示中；ROME 相关工作一节引用 Belinkov 2021 指出探针与网络行为脱节，这是本方向把干预当作更强证据的原因。

**判断的支撑论文**

- Geva 一系的读法：FFN 键值记忆 §3–4（value 投影到词表）；Dissecting Recall §1、§6（主语表示投影到词表）与局限一节。
- 因果干预一系：ROME 相关工作一节与 §3.7；FUR 摘要（从参数中遗忘推理步骤，看预测变化）。
- Anthropic 电路一系：Olsson 等的摘要与 Key Concepts；Elhage 等 2021 的内容依据 [Induction Heads 文献卡](../../papers/arxiv-2209.11895/README.md)的转述。
- 早期层分层：AlexNet §6.1、Yosinski 等 2014 摘要、ViT §4.5 与 Fig.7、Geva 2021 §3、Engram §6.1。边界：四处测量的对象不同（卷积核、注意力头的平均距离、FFN key 的触发前缀、整模型的 logit lens 与 CKA，后者是比较两个模型各层表示相似度的指标），"同一种分层"是形状上的类比；没有一篇论文在两种模态之间做过同条件的对照。
- 架构回流：[关系页](../../../foundations/relations/attention-ffn-division.md)"这条链解释了什么"第 3 条。

**与其他论文的关联**

- [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)：本页语言一侧主线的完整证据；其中 MoE 一节说明为什么稀疏化的对象一直是 FFN。
- [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 9 节"从手工特征到可学习特征"：视觉一侧"第一层学到方向滤波器"的完整论证。
- [训练科学](../training-science/README.md)：induction head 的形成与上下文学习能力骤升同时发生，是训练动态与内部机制交汇的例子。
- [ShortGPT](../../../llm/papers/arxiv-2403.03853/README.md)：用 Block Influence 衡量每层的重要性，发现大模型中许多层彼此高度相似、有些层几乎不影响网络功能，直接删层就超过了此前的剪枝方法。它在层的粒度上问"每层在做什么"，可与本页按子层分析的工作对照。
- [Naturalness of Attention](../../../llm/papers/arxiv-2311.13508/README.md) 与 [Probing Pretrained Models of Source Code](../../../llm/papers/arxiv-2202.08975/README.md)：都问代码模型捕获了哪些语法结构，前者拆开注意力内部的权重与被读出的向量，后者读整层表示。

**未核实 / 待验证**

- Elhage 等 2021 *A Mathematical Framework for Transformer Circuits* 原文未打开。
- 视觉模型上关于 FFN 记忆、复制电路和因果定位的研究未检索。
- 团队偏好的三条 [判断] 各只有两篇论文支撑。
- OLMo、ShortGPT、FRODO、FUR 四篇只核对了摘要。
