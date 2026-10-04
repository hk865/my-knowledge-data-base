# 学术界的研究方向为什么会收敛

> 状态：思考笔记 · 2026-10-04 · 两个假说均未检验

## 我的问题

审阅观点页时，我提出了两个关于研究方向收敛的假说（2026-10-04）。

**假说一（审阅[深度学习的规模化](../scaling.md)时提出）。** 算力、研究人员的有效工作/注意力时间与数据三者的关系，决定了学术界方向的收敛，毕竟学术人员需要容易出成果，3 个月就要出一篇。这应该是可以量化的。

**假说二（审阅 [CNN 与 Transformer](../cnn-vs-transformer.md) 时提出）。** 那一页主要关注基础模型（在大规模数据上预训练、再供许多下游任务使用的模型），往后可能又会涉及团队路线的押注：Transformer 上有更多基础研究，而 CNN 为主的时期，研究多是网络架构的黑箱式探索，而不是可解释性研究（弄清网络内部学到了什么、靠什么做出预测），这使团队倾向于 Transformer。我自己的评价是：这是偏私货、证据不全的观点。

**假说三（审阅[生成式建模的收敛](../generative-convergence.md)时提出）。** 2022 年之后最热门的视频生成模型多在公司手中；世界模型的生力军团队本身多是视频生成出身，因而更关注可编辑、关键符号与物体在生成中保持不变等方向。

## 目前的判断

**假说本身**

1. [我] 算力、研究人员的有效工作/注意力时间和数据三者的关系，决定了学术界方向的收敛；动力是学术人员需要容易出成果（约 3 个月一篇）。这一关系应该可以量化。
2. [我] CNN 为主的时期，研究多为网络架构的黑箱式探索，而不是可解释性研究；Transformer 上的基础研究更多，这使团队倾向于 Transformer。这是偏私货、证据不全的观点。

- [我] 世界模型的主力团队多出自视频生成，所以更关注可编辑与关键物体保持不变。（假说三；与假说一同属"团队与资源决定方向"。[建议] 检验方法：统计主要世界模型报告的作者此前是否发表过视频生成工作，例如 Genie 3 的作者名单与视频生成论文的重合；已有线索见[生成式建模的收敛](../generative-convergence.md)中「从视频生成到世界模型」一节及其批注。）

- [我] 后面发现这些路线基本上都走向了大模型，任务基本上也统一为生成式及其变种。（假说四，2026-10-04 审阅观点页时提出；与《生成的收敛》的主论点相邻，但范围更大：不只是生成任务的配方收敛，而是理解、决策等任务也被改写成生成式。[建议] 检验方法：在各领域页里逐一标出 2024–2026 年的代表系统是否以一个预训练大模型为主干、输出是否用生成式（下一 token 或去噪）表达——例如 VLM 把理解写成文本生成，VLA 把动作写成 token 或流匹配生成（[VLA](../../robotics-embodied/fields/vla/README.md)），HunyuanImage 3.0、GPT-4o 图像生成把图像生成放进语言模型（[视觉生成](../../multimodal/fields/generation/README.md)节点 10），世界模型由视频生成模型改造（[世界模型](../../multimodal/fields/world-models/README.md)）；同时找反例：检测、分割、SLAM、底层控制里仍以判别式或优化为主的系统（[机器人感知](../../robotics-embodied/fields/perception/README.md)、[定位与建图](../../robotics-embodied/fields/localization-mapping/README.md)、[运动控制](../../robotics-embodied/fields/control-locomotion/README.md)）。已按用户同意写进[生成的收敛](../generative-convergence.md)的 2025–2026 部分。）

**仓库里与假说一相关的已有证据**

3. [建议] [深度学习的规模化](../scaling.md)把整个领域走向规模化归于三件事：算力、能随数据增长的训练信号、可预测的训练工程。它描述的是全领域的走向，没有把学术界和工业界分开，也没有涉及研究周期，所以它是假说一的背景，不是检验。
4. [建议] [视觉表征领域页](../../multimodal/fields/visual-representation/README.md)的「主要路线与团队偏好」记录了数据与算力的门槛：ViT 的关键结论依赖 Google 内部、非公开的 JFT-300M，外部团队无法复现同一条件；CLIP 自估还要约 1000 倍算力才能在零样本上整体达到最优。同一页里，MAE 只用公开的 ImageNet-1K 训练，就超过了此前只用这一数据集的最好结果（87.8% 对 87.1%）。这些材料说明数据和算力的可得性会决定谁能做哪类实验，但都出自工业实验室，没有比较学术机构。
5. [建议] [模型科学](../../cross-domain/fields/model-science/README.md)的开放问题一节提到，[OLMo](../../llm/papers/arxiv-2402.00838/README.md) 与权重一起公开了训练数据、训练代码和评测代码，让机制研究能在已知训练条件下做。这是"数据可得性决定研究方向"的一个具体例子，可以作为假说一中"数据"一项的入口。
6. [建议] 仓库里的证据都来自单篇论文的内容，没有一条统计过论文的机构类型、算力预算或研究周期。假说一在仓库内目前既没有支持，也没有反驳，需要下一节的外部数据。

**仓库里与假说二相关的已有证据**

7. [建议] [模型科学](../../cross-domain/fields/model-science/README.md)的主线历史和「不同模态的差异」一节显示：语言一侧（以 Transformer 为主）从 2020 年的 FFN 键值记忆读法，推进到 2022 年的 ROME 因果追踪与 Induction Heads 电路，再到 2023 年的 Dissecting Recall，已经到达干预层级；视觉一侧的证据集中在第一层卷积核的可视化和 ViT 的注意力距离。这与假说二的前半句方向一致，但比较的对象同时换了模态（语言对视觉）和架构，两者混在一起。
8. [建议] [视觉表征领域页](../../multimodal/fields/visual-representation/README.md)「从内部看」一节记录了以 CNN 为对象的可解释性研究：Zeiler 与 Fergus（2013）用反卷积网络和遮挡实验分析 ImageNet 上训练的 CNN 各层学到了什么，Kornblith 等（2019）提出用 CKA 比较层与层的表示。仓库外还有两例：Network Dissection（Bau 等，CVPR 2017）给 CNN 隐藏单元与语义概念的对齐打分；Distill 的 Circuits 系列（2020 年 3 月起）以 InceptionV1（一个 CNN）为对象拆解神经元与电路。CNN 时期确有可解释性研究，所以假说二需要检验的是比例和证据层级，而不是有无。
9. [建议] [CNN 与 Transformer](../cnn-vs-transformer.md) 批注里为"Transformer 成为通用主干"列出的支撑理由是通用性与可规模化：ViT 的预训练计算效率、CLIP 中 ViT 编码器约 3 倍的计算效率、Whisper 选用 Transformer 是因为它已被验证能可靠扩展、DiT 的统一配方。这份理由清单里没有可解释性一项；这些原文的其他章节是否提到可解释性，没有逐篇核对。
10. [建议] 按仓库里已有的年份，视觉转向 Transformer 的节点（ViT 2020、CLIP 2021、DiT 2022）与语言侧机制研究的主要节点（2020–2023）大致同期。假说二的后半句要成立，至少需要后者在时间上先于或伴随前者的决策，这需要按月份逐篇核对。

## 待验证

两张表中的数据源都在 2026-10-04 打开官方页面或实际调用核实过。混杂因素（同时影响指标和结论、会制造假相关的因素）一列写每个指标最可能被误读的地方。

### 假说一：算力、注意力时间与数据怎样决定学术方向的收敛

[建议] 把假说拆成三个可以单独检验的部分：(a) 学术机构可用的算力与前沿的差距在扩大；(b) 学术研究向单次实验便宜、周期短的方向集中；(c) 这种集中表现为共用少数开源权重和少数 benchmark（公开的标准评测集）。

| 指标 | 数据源 | 检验哪一部分 | 混杂因素 |
|---|---|---|---|
| 学术机构与工业机构的训练算力随年份的差距；学术机构在重要模型中所占比例 | Epoch AI（研究 AI 发展趋势的机构）的 [AI Models 数据库](https://epoch.ai/data/ai-models)，CC BY 许可，CSV 下载。其中 Notable AI models 表 2026-10-04 有 1078 条，字段包括 `Training compute (FLOP)`（训练用的浮点运算总次数）、`Publication date`、`Organization categorization`（取值有 Academia、Industry、Research collective、Government，合作模型可同时带多个） | (a) | 只收"重要"模型（达到最好水平、高引用或有历史意义），学术界大量低算力工作不在表内，会夸大差距；算力多为估计值，官方标注 Confident 的记录误差在 3 倍以内，Speculative 可达 30 倍 |
| 学术机构的重要模型中，在别人的基座上微调、或发布开放权重的比例 | 同一张表的 `Base model`、`Finetune compute (FLOP)`、`Model accessibility`、`Open model weights?` 字段 | (b)(c)：算力不足时转向复用别人的预训练权重 | 同上的入选偏差；微调类记录很稀疏，比例可能只反映 Epoch 的收录习惯 |
| 引用某个开源预训练权重发布论文的论文，占同期机器学习论文的比例（按年） | [OpenAlex](https://api.openalex.org)（开放的学术文献元数据库）的 works 接口：`filter=cites:<作品 ID>` 加 `group_by=publication_year`，已实际调用确认可用 | (c)：方向是否收敛到共用的几套权重上（例如 ResNet、BERT、CLIP 的发布论文） | 引用不等于使用权重，需要抽样读全文校准；分母（同期论文总数）本身快速增长，只能看比例 |
| benchmark 从提出到饱和（接近人类水平或不再提升）的时间 | Dynabench（[Kiela 等 2021](https://arxiv.org/abs/2104.14337)）Fig.1：MNIST、Switchboard、ImageNet、SQuAD 1.1、SQuAD 2.0、GLUE 的成绩按"初始 = −1、人类水平 = 0"归一化后画在同一时间轴上，正文指出新数据集往往几年内就达到人类水平的估计。逐个 benchmark 的历年最好成绩可取自 Papers with Code 的存档（Hugging Face 上 [pwc-archive](https://huggingface.co/pwc-archive) 的 evaluation-tables，CC-BY-SA） | (b)：集体投入越集中、越容易出成果，饱和越快 | 饱和快也可能是 benchmark 本身容易或有捷径；人类水平的估计口径不一；Papers with Code 由社区填报，覆盖不全，并止于原站停更前的最后快照 |
| 投稿量与发表节奏：分类别的每月新论文数，作者的年均论文数，会议投稿量 | arXiv 官方的 [OAI-PMH 与 API](https://info.arxiv.org/help/bulk_data.html)（标题、作者、分类、摘要，每日更新）；OpenAlex 作者记录的 `counts_by_year`；OpenReview 的 API 可取 ICLR 等会议的投稿，官方文档写明需要 OpenReview 账号登录 | (b)：检验"约 3 个月一篇"的节奏是否存在、是否随时间变快 | 署名膨胀（人均篇数不等于人均第一作者篇数）；OpenAlex 的作者消歧会合并同名者，例如名为 "T. Kobayashi" 的一条作者记录有 270 万篇；投稿量增长主要由领域人数增长驱动 |
| 研究人员的有效工作/注意力时间 | 没有找到直接的数据源 | 三者关系中的"时间"一项 | [建议] 用代理量：每篇论文的作者数、arXiv 首版到会议录用的间隔、同一作者相邻两篇第一作者论文的间隔；它们同时受导师、经费和会议截稿日期影响 |

[建议] 组合成一次可以被否定的检验：假说一预测，学术与工业的算力差距扩大之后，学术论文中复用开源权重、集中于少数 benchmark 的比例上升，并且在低算力方向（微调、评测、分析）中学术机构的占比更高。如果算力差距扩大了，学术论文的方向分布却没有变化，假说一的"算力"一项就不成立。

### 假说二：可解释性研究的多少是否影响了架构选择

[建议] 拆成两部分：(a) 前半句，CNN 为主的时期可解释性研究少、以黑箱式架构探索为主；(b) 后半句，Transformer 上更多的基础研究使团队倾向于它。(a) 是计数问题，(b) 是因果问题，后者更难检验。

| 指标 | 数据源 | 检验哪一部分 | 混杂因素 |
|---|---|---|---|
| 各时期可解释性论文研究的架构分布：按年统计含 interpretability、visualization、probing、circuit 等关键词的论文中，研究对象是 CNN 还是 Transformer；分母用同期研究该架构的全部论文 | arXiv API 的摘要检索，或 OpenAlex works 接口的 `search` 参数（全文检索，按 `publication_year` 分组） | (a) 的数量 | 术语变化（早期多叫 visualization、saliency，后来叫 interpretability、mechanistic）；CNN 主要在视觉，Transformer 先在语言，两个社区的研究习惯不同；可解释性的动机（例如 AI 安全的投入）可能独立于架构 |
| 同一批论文按证据层级分类：观察、探针、干预（沿用[模型科学](../../cross-domain/fields/model-science/README.md)的三层） | 上一行检索结果的人工抽样标注 | (a) 的深度：两种架构上可解释性研究的差别是在数量还是在层级 | 标注主观，需要两人独立标注再看一致率 |
| 语言侧专门 venue 中研究对象的变化（RNN、LSTM 到 Transformer） | ACL Anthology 收录的 BlackboxNLP 历届论文集（全称 Analyzing and Interpreting Neural Networks for NLP，专门做 NLP 模型的分析与解释） | (a) 在语言内部的时间线，这样架构变了而模态不变 | 只覆盖语言，不能直接与视觉对比 |
| 架构选型论文的自述理由与时间顺序 | 转向 Transformer 的代表论文（ViT、CLIP、DiT、Whisper 等）的引言与方法；对照可解释性主要成果的发表月份 | (b)：选型理由里有没有可解释性；转向发生在相关成果之前还是之后 | 自述理由不等于真实动机；团队内部决策多不公开，2023 年之后的公司模型尤其如此 |

[建议] (b) 很难只靠公开论文定论。比较可行的是先做 (a)：如果统计显示 CNN 时期可解释性论文的比例并不低，只是停在观察层级，假说二可以改写成"Transformer 上的研究更容易推进到干预层级"，再去看这一点与架构结构（离散 token、残差流、注意力权重可直接读出）的关系。

## 相关页面

- [深度学习的规模化](../scaling.md)：假说一所针对的观点页，算力、训练信号与训练工程三条驱动力。
- [CNN 与 Transformer](../cnn-vs-transformer.md)：假说二所针对的观点页，批注中列有 Transformer 胜出的支撑理由与反例。
- [模型科学](../../cross-domain/fields/model-science/README.md)：语言与视觉两侧可解释性证据的层级对照。
- [视觉表征领域页](../../multimodal/fields/visual-representation/README.md)：「从内部看」一节的 CNN 可解释性研究，「主要路线与团队偏好」一节的数据与算力门槛。
- [训练科学](../../cross-domain/fields/training-science/README.md)：规模定律与算力预算。

## 批注

**易误读**
- Epoch AI 数据库按"重要模型"收录，统计结果描述的是重要模型，不能直接推到全部学术论文（入选标准见其 [AI Models 页面](https://epoch.ai/data/ai-models)）。
- Dynabench Fig.1 的纵轴以人类水平为 0，"饱和"指达到人类水平的估计，不是模型能力的上限。

**出处（本库没有单篇目录）**
- Network Dissection：https://arxiv.org/abs/1704.05796 ；Distill Circuits 系列：https://distill.pub/2020/circuits/ ；Dynabench：https://arxiv.org/abs/2104.14337 ；BlackboxNLP：https://aclanthology.org/venues/blackboxnlp/ ；OpenAlex 过滤与检索说明：https://help.openalex.org/api-entities/works/filter-works ；OpenReview API 说明：https://docs.openreview.net/getting-started/using-the-api ；Papers with Code 数据仓库：https://github.com/paperswithcode/paperswithcode-data

**未核实 / 待验证**
- OpenReview API 未登录调用时返回验证要求，本笔记没有实际取到会议投稿数据；需要用户自己的账号来跑。
- Papers with Code 原站的停更时间，以及 pwc-archive 快照截止的具体日期，没有从官方声明中核实。
- 第 10 条所说的年份同期，只按仓库各页记录的年份比较，没有核对月份。
