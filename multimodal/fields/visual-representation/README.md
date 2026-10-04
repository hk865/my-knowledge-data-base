# 视觉表征

> 状态：领域入门页 · v1 · 依据 [synthesis.csv](synthesis.csv)（22 篇）

本页是[多模态总目录](../../README.md)下的一个方向。拆分后的基线见 [Baseline 页](BASELINES.md)，问题路线见[路线图](ROADMAP.md)，收录的全部论文见[论文目录](PAPERS.md)。

## 这个领域在解决什么

检测器要在街景里框出行人，医生要在电镜图里分割细胞，机器人要在没见过的厨房里找到杯子。三件事的输入都是像素，都要先把像素变成可用的特征：同一只杯子换了光照和角度，特征应当相近；杯子和碗，特征应当分开。视觉表征研究这一步怎样得到：特征由人设计还是从数据学出来；学的时候训练信号来自类别标注、图像自身，还是网上配对的文字；承载它的主干网络用卷积还是 Transformer。学到的主干随后交给检测、分割、[视觉语言模型](../vlm/README.md)和机器人策略使用，所以这个方向的每一次进展都会传到几乎所有视觉相关的领域。

## 主线历史

起点是 2000 年代的手工特征路线：Dalal 与 Triggs（2005，INRIA）的 HOG（梯度方向直方图：统计局部小格内各方向梯度的强弱）加线性 SVM，以及 Felzenszwalb、Girshick 等在 HOG 上搭建的可变形部件模型 DPM（2010）。特征由人设计，只有最后的分类器在学习。卷积网络在 1998 年的 LeNet 中已经能从标注里学卷积核，但只在文档识别这类小规模任务上落地。HOG 为什么相当于一个核固定的浅层 CNN、这些机制怎样一步步演化，见 [CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节；本节关心的是数据、benchmark 和训练信号怎样改变了这个领域。这条主线也是[深度学习规模化](../../../perspectives/scaling.md)在视觉中的一段：训练信号从人工设计，走到人工标注，再走到数据本身。

1. **ImageNet（2009，Princeton）与 ILSVRC（2010 起每年举办）**。上一阶段留下的问题：特征受限于人能设计出什么，可学习的深网络又缺少足够大的标注数据，各团队也缺一个共同比较的公开 benchmark（HOG 在 MIT 行人库上近乎完美分离后，作者另建了更难的 INRIA 行人库）。改变：以 WordNet 的名词概念为骨架、目标约 5000 万张图的标注图库，以及约 120 万训练图、1000 类的年度竞赛 ILSVRC。图像分类的主战场从此转到 ImageNet，检测仍以 PASCAL VOC 为主。
2. **AlexNet（2012，Toronto）**。留下的问题：有了数据，在高分辨率图像上大规模训练 CNN 仍然太贵。改变：两块 GPU、ReLU、dropout，加上 ImageNet 规模的数据，在 ILSVRC-2012 上 top-5 测试错误率 15.3%，第二名（Fisher 向量手工特征）为 26.2%。ILSVRC 组织者把 2012 年称为转折点：2013 年绝大多数、2014 年几乎全部参赛方法改用 CNN。[判断] 改变局面的是数据、算力和 benchmark，卷积机制在 LeNet 中已经具备。
3. **R-CNN（2013）与 DPM are CNNs（2014），UC Berkeley**。留下的问题：ImageNet 上学到的特征只在分类上得到证明，标注更贵的检测任务能否借用？PASCAL VOC 检测在 2010–2012 年停滞。改变：先在 ILSVRC 分类数据上预训练 CNN，再在检测数据上微调，VOC2007 mAP 从 HOG-DPM 的 33.7% 升到 54.2%（其中微调本身贡献 8.0 个百分点）；同一作者随后证明 DPM 可以逐步展开成一个 CNN，手工特征路线并入 CNN 路线。[判断] 从这里开始，"ImageNet 预训练的视觉主干"成为检测、分割等任务的默认起点，视觉表征的好坏开始用"迁移到下游任务的效果"来衡量。
4. **VGG、GoogLeNet（2014）→ ResNet（2015，Microsoft Research）**。留下的问题：主干决定下游的上限，ILSVRC 上的竞争变成"怎样做得更深"。VGG（Oxford）全部用 3×3 卷积做到 16–19 层，GoogLeNet（Google）在固定计算预算下加深加宽；更深的网络随即暴露出退化问题：训练误差反而上升。ResNet 让每段网络只学修正量 F(x)、输出 x+F(x)，ILSVRC 2015 集成模型 top-5 测试错误率 3.57%，并报告了 PASCAL VOC 与 COCO 检测上的迁移。更好的主干会直接传到下游：R-CNN 把主干从 AlexNet 换成 VGG16，VOC2007 mAP 从 58.5% 升到 66.0%（都含框回归），代价是前向耗时约 7 倍。
5. **MoCo（2019，FAIR）与 SimCLR（2020，Google）**。留下的问题：主干越做越大，有监督预训练依赖的人工标注却不随之增长；语言一侧已靠 GPT、BERT 式自监督预训练摆脱了逐任务标注（见 [LLM 预训练方向](../../../llm/fields/pretraining/README.md)）。改变：对比学习（把同一张图的两种随机增强当作正样本对、其他图当作负样本，训练编码器拉近正样本对）。MoCo 在 7 个检测/分割迁移任务上超过 ImageNet 有监督预训练；SimCLR 用 4 倍宽的 ResNet-50 做线性评测达到 76.5%，与有监督的标准 ResNet-50 相当。评测随之分成两种协议：冻结特征、只训练线性分类器的线性评测，以及迁移到 VOC、COCO 的检测与分割。
6. **ViT（2020，Google）**。留下的问题：卷积的局部性与平移等变是视觉必需的先验，还是可以从数据中学出来？ViT 把图像切成 16×16 的块，当作 token 序列直接交给 Transformer：只在 ImageNet 上预训练时不如同规模的 ResNet，在非公开的 JFT-300M 上预训练后反超。它自述的局限之一，是自监督预训练与大规模有监督预训练之间仍有很大差距。
7. **CLIP、MAE（2021）与 ConvNeXt（2022）：对 ViT 的三种回答**。ViT 留下的问题：它的优势要靠非公开的大规模标注换来，这份优势有多少属于架构本身也说不清。CLIP（OpenAI）换掉训练信号的来源：从网上收集 4 亿对图文做对比学习，分类时把类别名写成句子当作分类器，零样本（不用目标数据集的任何训练样本）在 ImageNet 上与原始 ResNet-50 相当，而没有用它的 128 万张训练图；评测也随之改为不训练任何参数、覆盖 30 多个数据集的零样本迁移。MAE（FAIR）换掉自监督目标：遮住 75% 的图像块、只编码可见块，再用轻量解码器重建像素，只用 ImageNet-1K 就让 ViT-Huge 微调到 87.8%，此前只用这一数据集的最好结果为 87.1%。ConvNeXt（FAIR 与 UC Berkeley）检验架构：只给 ResNet-50 换上 Transformer 式训练配方，ImageNet 精度就从 76.1% 升到 78.8%；再逐步借用 Transformer 的设计后，在相近计算量下全面超过 Swin（一种分层的视觉 Transformer）。[判断] CNN 与 Transformer 在视觉表征上的胜负，很大程度取决于数据规模和训练配方；Transformer 成为通用主干，更多是因为同一结构能处理多种模态、规模化行为可以预测，完整论证见[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)。

## 技术地基

- **卷积与它的归纳偏置**：小核在所有位置复用，带来局部性与平移等变；主线前四个节点都建立在它上面，它在小数据下的优势与大数据下的限制，也正是 ViT 之争的焦点。见 [CNN 讲义](../../../docs/foundations/11-cnn.md)第 2–5 节。
- **残差连接**：让上百层的网络可以训练，ResNet 之后的 CNN 和 ViT 的每个子层都沿用它。见 [CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节与 [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 10.2 节。
- **图像块 token 与自注意力**：ViT 把图像变成 token 序列，第一层就能让每个块读取全部块；MAE 能只编码可见块，也依赖这种表示。见 [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 13.4 节。
- **自监督与弱监督训练信号**：对比学习（MoCo、SimCLR）、遮蔽重建（MAE）、自蒸馏（DINO：学生网络去匹配由自身参数滑动平均得到的教师网络的输出）和图文对比（CLIP）是让数据自己出题的几种方式。架构与训练信号是两条独立的轴，同一个 ViT 可以用标签监督、遮蔽重建或自蒸馏来训练。见[自监督与生成目标](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)第 5–9 节。
- **预训练与迁移**：从 R-CNN 起，表征的价值由迁移到下游任务的效果决定；冻结主干只训任务头、部分微调、全量微调是几种不同的适配方式。见[迁移与元学习](../../../docs/foundations/05c-transfer-meta-learning.md)第 2–3 节。

## 主要路线与团队偏好

- **手工特征加浅层学习**（INRIA 的 HOG；Chicago、Berkeley 一系的 DPM）。押注：人对图像结构的先验（方向梯度、可变形部件）比从数据中学更可靠。代价：特征固定，进展受限于人能设计出什么，PASCAL VOC 上 2010–2012 年的停滞就是表现。[判断] Girshick 所在的一系在 DPM、R-CNN、DPM are CNNs 三篇中始终以 PASCAL VOC 检测为目标、以 DPM 为对照，转向 CNN 时选择证明"旧模型是新模型的特例"，而不是另起炉灶。
- **有监督预训练主干**（Toronto 的 AlexNet，Oxford 的 VGG，Google 的 GoogLeNet 与 ViT，Microsoft Research 的 ResNet）。押注：数据和算力足够时，深网络从像素学到的特征优于手工特征。代价：依赖大规模人工标注，结构选择长期围绕 ILSVRC 分类指标展开；ViT 的关键结论依赖非公开的 JFT-300M，外部团队无法复现同一条件。同一条路线上还有面向端侧的分支：Google 的 MobileNet（深度可分离卷积）与 EfficientNet（按统一系数同时缩放深度、宽度、分辨率），以及 UW 等的 YOLO（单个卷积网络一次完成检测），它们把 CNN 针对延迟和参数量做了系统优化。
- **视觉自监督**（FAIR 的 MoCo、MAE；Google 的 SimCLR；自蒸馏的 [DINO](../../papers/dino/README.md)）。押注：像语言一样让图像自己提供训练信号，方式是对比两种增强视图、重建遮住的块，或匹配教师网络的输出。代价：对比学习依赖强数据增强和大批量（SimCLR）或大字典（MoCo）；MAE 自述遮住的随机块通常不构成语义单元，重建目标是像素而不是语义实体。[判断] FAIR 一系（He、Girshick 等）在 MoCo 和 MAE 中都以 NLP 的 GPT、BERT 为参照提出问题，都把"迁移到检测、分割时能否超过 ImageNet 有监督预训练"作为主要评价；MoCo 结论中建议的下一步"遮蔽自编码"，由 MAE 实现。
- **图文弱监督**（OpenAI 的 [CLIP](../../papers/clip/README.md)）。押注：网上天然配对的图文比固定类别的标注更可扩展，并且直接得到一个用语言指定类别的接口。代价：CLIP 自述零样本只能在给定的概念中选择，细粒度分类和计数较弱，并估计还要约 1000 倍算力才能在零样本上整体达到最优。它的图像编码器后来成为[视觉语言模型](../vlm/README.md)和[图文对齐](../alignment/README.md)的常用起点。

## 用什么衡量进展

benchmark 的替换就是这个领域目标的迁移：

- **从行人库到 ImageNet**：MIT 行人库（HOG 近乎完美分离后饱和）→ INRIA 行人库 → PASCAL VOC 检测（DPM、R-CNN 的主战场）→ ImageNet / ILSVRC 分类（AlexNet 到 ResNet 的主战场）→ COCO 检测、ADE20K 语义分割等迁移任务（ResNet、MoCo、MAE、ConvNeXt 都报告）。ILSVRC 测的是 1000 类单标签分类；组织者自己记录了外界的批评：数据集不够难、细粒度类别有标注错误、外部数据规则太严。
- **自监督之后的评测协议**：线性评测（冻结特征，只训练一个线性分类器）衡量特征本身是否线性可分；全量微调衡量特征作为初始化的价值；迁移到检测分割衡量对密集任务的用处。三者给出的排序可以不同：MAE 原文中 MoCo v3 的线性评测更强，但只微调最后几层时就落后于 MAE（MAE 第 4.3 节、Fig.9）。
- **零样本迁移**：CLIP 把评测改成不训练任何参数、直接用类别名做分类，覆盖 30 多个数据集，衡量的是开放类别识别能力。它自述的口径问题是：开发中反复查看完整验证集，主结果所用的 27 个数据集与 CLIP 的开发共同演化。
- **跨论文比较的检查单**：骨干与分辨率、预训练数据（是否非公开、是否带文本或标签）、训练计算量、评测协议（零样本、k 近邻、线性、部分微调、全量微调）都要对齐，不同协议的最高数字不能放进同一张榜单。逐项清单见早期的[视觉基础路线图](../../../docs/roadmaps/visual-baselines.md)第四节。

## 当前开放问题

- **架构的差别与数据、训练配方、计算量怎样分开？** ViT 与 ConvNeXt 两组结果都说明，主干之争必须和数据规模、训练配方一起看。入口：[ViT 精读](../../papers/vit/reading.md)、[ConvNeXt 原文](https://arxiv.org/abs/2201.03545)、[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)。
- **哪种训练信号最适合哪类下游？** 遮蔽重建、对比学习、自蒸馏和图文对比在线性评测、微调、检索、局部对应上各有长处。入口：[MAE 精读](../../papers/mae/reading.md)、[DINO 精读](../../papers/dino/reading.md)、[CLIP 精读](../../papers/clip/reading.md)。
- **网上预训练的视觉特征够不够支撑机器人？** OpenVLA 的消融中，冻结视觉编码器使成功率从约 70% 降到 47%（较小的 SigLIP-only 变体上的结果）；世界模型一侧则在比较以重建为目标和以语义为目标的潜空间。入口：[OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)、[DINO-WM](../../papers/arxiv-2411.04983/README.md)、[Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](../../papers/arxiv-2605.06388/README.md)，以及[世界模型方向](../world-models/README.md)。

## 阅读顺序

1. [CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节：主线前四个节点的机制版本，先弄清卷积、残差和"预训练主干迁移"各自解决了什么。
2. [ViT 精读](../../papers/vit/README.md)：主干从卷积转向 Transformer 的节点，也是"归纳偏置与数据规模"这一问题的起点；建议手算一次 token 数 N = HW/P²。
3. [MAE 精读](../../papers/mae/README.md)：在同一个 ViT 上换成遮蔽重建，看为什么只编码可见块反而更好、为什么线性评测和微调会给出不同排序。
4. [DINO 精读](../../papers/dino/README.md)：把固定的像素目标换成动态的教师输出，与 MAE 对照阅读。
5. [CLIP 精读](../../papers/clip/README.md)：从单模态转到图文配对，理解零样本分类怎样由文本编码器生成分类权重。

读完 2–4 篇后可以做一个检验：把同一张图切成块，分别写出监督分类、MAE、DINO 三种目标要求模型预测什么、哪些分支参与梯度更新。四篇的横向对照表在[视觉基础路线图](../../../docs/roadmaps/visual-baselines.md)。

## 批注

**易误读**

- AlexNet 的 15.3% 对 26.2%，比较的是 ILSVRC-2012 测试集 top-5 错误率；AlexNet 的这个数字来自多个 CNN 的平均，其中两个用了额外的 ImageNet Fall 2011 数据预训练（AlexNet 第 6 节）。
- ViT 在 ImageNet-1k 上不如 ResNet、在 JFT-300M 上反超，比较对象是同等规模的 BiT ResNet，并且都经过迁移微调（ViT 4.3 节、Fig.3）。
- SimCLR 的 76.5% 用的是 4 倍宽的 ResNet-50；标准宽度时自监督为 69.3%，同结构有监督为 76.3%（SimCLR 附录 B.8）。MoCo 的线性评测为 60.6%，"超过有监督预训练"只指 7 个检测/分割迁移任务（MoCo 4.2 节）。
- MAE 的 87.8% 是 ViT-H 在 448 分辨率下微调的结果，224 分辨率为 86.9%（MAE 4.2 节、Table 3）。
- CLIP 的零样本 ImageNet 76.2% 的比较对象是原始的有监督 ResNet-50（CLIP 3.1 节、Table 1）。
- 特征可视化（例如 DINO 的注意力图）好看，不等于所有下游任务都更好；不同评测协议要分开报告。
- R-CNN 换成 VGG16 的 66.0% 出自 2014 年 10 月的 arXiv v5（第 3.3 节；该版说明称新增了更深网络的结果），晚于 2013 年 11 月的初版，用来说明"主干变强会传到下游"。

**判断的支撑论文**（各行见 [synthesis.csv](synthesis.csv)）

- "改变局面的是数据、算力和 benchmark"：AlexNet Sec.1、ILSVRC 综述 Sec.5.1。
- "ImageNet 预训练主干成为默认起点"：R-CNN Sec.1；MoCo Sec.1 把 ImageNet 有监督预训练作为要替代的对照。边界：MoCo、MAE 在检测与分割迁移上超过了 ImageNet 有监督预训练（MoCo Sec.4.2、MAE Sec.5），这个默认起点此后开始被自监督预训练替代。
- Girshick 一系的偏好：DPM（PAMI 2010）Sec.8、R-CNN Table 1–2、DPM are CNNs Table 1，三篇都以 PASCAL VOC 为目标、以 DPM 为对照。
- FAIR 一系在视觉自监督中的偏好：MoCo Sec.1、Sec.4.2、Sec.5；MAE Sec.1、Sec.5、Sec.6。边界：同属 FAIR 的 ConvNeXt 转而检验有监督 CNN 的上限，说明该团队并不只押注自监督。
- "胜负取决于数据规模和训练配方"：ViT Sec.4.3–4.4、ConvNeXt Sec.2.1 与 Sec.3；反向证据是 CLIP Sec.3.2 中 ViT 图像编码器的计算效率约为 ResNet 的 3 倍。

**与其他论文的关联**

- [CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节与本页主线前四个节点一致，讲的是机制；本页补上了团队与 benchmark 两个维度。两处如有出入，以 [synthesis.csv](synthesis.csv) 中的原文出处为准修改。
- U-Net（2015，Freiburg）的编码–解码结构后来成为扩散模型的去噪主干，见[视觉生成方向](../generation/README.md)；ViT 的切块思路被 DiT 用到图像生成里。
- CLIP 的图像编码器是 [LLaVA](../../papers/llava/README.md) 等视觉语言模型的视觉输入端，也是 DALL·E 2 生成图像时的条件（见[视觉生成方向](../generation/README.md)）。
- MoCo、MAE 都以 BERT、GPT 为参照提出问题，语言一侧的对应历史见 [LLM 预训练方向](../../../llm/fields/pretraining/README.md)；训练配方与规模定律见[训练科学](../../../cross-domain/fields/training-science/README.md)。
- MobileNet、EfficientNet、YOLO 都早于 ViT，没有与视觉 Transformer 做同条件对比；"CNN 在端侧仍占优"的讨论放在[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)。

**未核实 / 待验证**

- LeNet（LeCun 等 1998）全文没能打开，[synthesis.csv](synthesis.csv) 中该行除题录外都标为未核实；主线开头关于 LeNet 的一句沿用 CNN 讲义的写法。
- DINO 不在本页综合表中，它的团队与实验数字没有在本轮按原文核对，本页只描述其训练信号；细节以 [DINO 精读](../../papers/dino/reading.md)为准。
- "开放问题"第三条所链的两张世界模型文献卡目前只有题录，本页只引用其标题提出的问题。
- MobileNet 论文只写了"计划发布模型"，MAE 论文正文未声明代码发布，实际发布情况没有另查。
