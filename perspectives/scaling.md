# 深度学习走向规模化，靠的是算力、能随数据增长的训练信号和可预测的训练工程

> 状态：观点 · 草稿 · 2026-10-04

## 一句话

过去十五年，语言、视觉识别和图像生成沿着同一个方向变化：模型更大、数据更多，训练信号越来越多地由数据本身提供。[判断] 推动这一变化的是三件先后到位的事：硬件让大规模矩阵运算变便宜，自监督目标让训练信号随原始数据一起增长，训练工程的研究让很深、很大的网络能稳定训练、结果能事先估计。按训练信号的来源，这条总线分成三个阶段：手工特征加小数据、有监督深度学习、自监督预训练与生成。CNN 与 Transformer 的此消彼长是这条总线上的一段，单独论证见 [CNN 与 Transformer](cnn-vs-transformer.md)；生成模型怎样走到同一套配方，见[生成的收敛](generative-convergence.md)。

## 驱动力

**1. 算力与数据（2009 年起，视觉在先、语言在后）**

ImageNet（2009 年发布、按 WordNet 名词层级组织的大规模标注图库）和以它为基础的 ILSVRC 竞赛（2010 年起每年举办，约 120 万张训练图、1000 类）第一次给出了足以训练深网络的标注量和一个所有团队共用的 benchmark。AlexNet（2012）在两块 GPU 上训练，ILSVRC-2012 的 top-5 错误率为 15.3%，用 Fisher 向量手工特征的第二名为 26.2%（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)的 AlexNet 节点）。此后每一次扩大规模都由更多硬件承接：Goyal 等（2017）用 256 块 GPU、每批 8192 张图，在 1 小时内训完 ResNet-50，top-1 错误率与每批 256 张图的常规训练相当（[训练科学页](../cross-domain/fields/training-science/README.md)）；Video Diffusion Models（2022，Google）附录中的各个视频模型用 64 到 256 个 TPU-v4 芯片训练（[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)第 7 节）。语言一侧的数据来自互联网文本，规模大到 GPT-3 需要专门检查训练语料与测试集的重叠（[GPT-3 精读](../llm/papers/gpt3/reading.md)）。

**2. 能随数据增长的训练信号（语言 2018 年起，视觉 2019–2021 年，生成 2020 年起）**

人工标注的成本随数据量同步增长，原始文本和图像却几乎可以无限获取。于是预训练的信号换成了数据给自己出的题：下一词预测（GPT 系列）、遮蔽预测（BERT、MAE）、去噪（T5 的片段去噪、DDPM 的噪声预测）、对比学习（MoCo、SimCLR：把同一张图的两种随机增强当作正样本对，拉近它们的表示）、网页图文配对（CLIP）。收敛的是预训练阶段的信号，下游任务仍然多种多样；最后一步还常用少量标注或人类偏好，例如 InstructGPT 的 RLHF（先用人对回答的排序训练奖励模型，再用强化学习按奖励微调语言模型，见 [InstructGPT 精读](../llm/papers/instructgpt/reading.md)）。[判断] 视觉一侧的自监督与图文预训练工作在引言里都以语言的自监督预训练为参照，这是一次有意识的跨领域迁移（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)的 MoCo、SimCLR、CLIP、MAE 节点）。

**3. 训练工程的科学（2010 年起，作用于所有领域）**

四类研究让规模化可执行、可预测（推导与证据在[训练科学页](../cross-domain/fields/training-science/README.md)）：

- 让梯度穿过很深的网络：Glorot 与 Bengio（2010）的归一化初始化、He 等（2015）针对 ReLU 的初始化、批归一化（2015）、残差连接（2015）、层归一化（2016），以及把层归一化移到子层输入的 Pre-LN（Xiong 等 2020 证明它初始化时梯度更平稳，可以去掉学习率预热）。
- 让大批量、多机训练稳定：Adam（2014）、学习率预热与衰减、大批量的学习率线性缩放（Goyal 等 2017）、混合精度（半精度存储加单精度主权重与损失缩放）。
- 让结果可以事先估计：Kaplan 等（2020）的规模定律，即语言模型的测试交叉熵分别随参数量、数据量、算力呈幂律下降，跨越 7 个以上数量级；Hoffmann 等（2022）的 Chinchilla 把参数与数据的最优配比修正为等比例增长（[Chinchilla 文献卡](../cross-domain/papers/arxiv-2203.15556/README.md)）。
- 让后续训练不破坏已有能力：微调用更小的学习率、LoRA（冻结原权重，只训练一个低秩增量矩阵）、RLHF 中对 SFT 模型的 KL 惩罚（输出分布偏离监督微调模型越远，扣分越多）加上混入预训练梯度（[InstructGPT 精读](../llm/papers/instructgpt/reading.md)第 6、8、11 节）。

优化地形的研究给出一个与规模相关的解释。[判断] 在参数很多（过参数化）的网络里，阻碍训练的主要是鞍点与平台期；独立训练得到的不同解损失相近，并由一条低损失的路径相连（模式连通）。（这里的"参数很多"指参数量或宽度，与数据量、训练时长无关。）

## 阶段

### 阶段一：手工特征加小数据（1980–2011）

**上一阶段留下的问题。** 这是起点：模式识别的结果随图案的平移和形变而改变。Neocognitron（1980）交替堆叠"提取特征"和"容忍位置变化"两种层，同一平面内共用连接，这是卷积与权重共享的雏形（[CNN 讲义](../docs/foundations/11-cnn.md)第 6 节）。

**本阶段的变化。** 可学习的卷积网络已经出现（LeNet 1998，用反向传播训练卷积核，在文档识别中落地），视觉主流仍是人设计的特征加浅层分类器，只有分类器从少量标注中学习。

**各领域的表现。**

- 视觉表征：HOG（2005，梯度方向直方图）与 DPM（2010，可变形部件模型）加线性 SVM 主导检测。HOG 的流水线可以读成一个核固定的浅层 CNN（[CNN 讲义](../docs/foundations/11-cnn.md)第 6、9 节）。PASCAL VOC 检测（约 20 类物体的检测 benchmark）在 2010–2012 年停滞（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)）。
- 语言：序列建模用 [RNN](../docs/foundations/12-rnn.md) 与 [LSTM](../docs/foundations/13-lstm.md)，机器翻译的主流是短语统计翻译，它是 2014 年 Seq2seq 的对照基线（[预训练领域页](../llm/fields/pretraining/README.md)）。
- 训练科学：深网络要先做逐层无监督预训练才能训好，标准随机初始化直接做梯度下降效果差且原因不明。Glorot 与 Bengio（2010）把"难训"拆成逐层激活饱和与梯度方差两个可测量的量；5 个隐藏层的 tanh 网络在 Shapeset-3×2 上改用归一化初始化后，测试误差从 27.15% 降到 15.60%（[训练科学页](../cross-domain/fields/training-science/README.md)）。

**留下的问题。** 特征受限于人能设计出什么；可学习的深网络缺少数据和算力，也缺少稳定训练的办法。

### 阶段二：有监督深度学习（2009–2017）

**本阶段的变化。** 用大规模人工标注加 GPU，让网络直接从像素或词里学特征。

**各领域的表现。**

- 视觉表征：ImageNet 与 ILSVRC → AlexNet（2012）→ VGG、GoogLeNet（2014）→ ResNet（2015）。ILSVRC 上的竞争变成"怎样做得更深"，更深的网络暴露出训练误差反而上升的退化问题，ResNet 用残差学习解决，ILSVRC 2015 top-5 测试错误率 3.57%。R-CNN（2013）把 ImageNet 预训练的 CNN 迁移到检测再微调，PASCAL VOC2007 的 mAP（各类别检测平均精度的均值）从 HOG-DPM 的 33.7% 升到 54.2%（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)）。[判断] 从这里开始，"先在大数据上预训练、再迁移到具体任务"成为视觉的默认流程。
- 语言：Seq2seq（2014）用两个 LSTM 做序列到序列翻译；Bahdanau 注意力（2014）让解码时按权重读取源句各位置；Transformer（2017）用注意力取代循环，同一样本内部可以并行计算，目标是 WMT 机器翻译 benchmark（[Transformer 精读](../llm/papers/transformer/reading.md)、[预训练领域页](../llm/fields/pretraining/README.md)）。
- 生成：GAN（2014）让生成器与判别器对抗训练，DCGAN（2015）找到一组能稳定训练的全卷积结构；两篇都自述训练不稳定，以及生成器把许多输入映射到同一张图的模式坍缩（[视觉生成领域页](../multimodal/fields/generation/README.md)的 GAN 节点）。
- 训练科学：He 等（2015）报告 30 层 ReLU 网络用 Glorot 初始化完全停滞，改用他们的初始化后可以收敛；批归一化让 Inception 网络的一个变体达到原模型精度所需的训练步数少 14 倍；Adam、大批量线性缩放与预热、混合精度和层归一化都在这一阶段出现（[训练科学页](../cross-domain/fields/training-science/README.md)）。

**留下的问题。** 每个新任务、新类别都要重新标注，标注量跟不上模型对数据的需求；语言里各任务的标注数据更少。

### 阶段三：自监督预训练与生成（2018 年起）

**本阶段的变化。** 数据本身提供预训练信号，再加少量有监督微调或人类偏好对齐。下一词预测和去噪既是自监督信号，本身也是生成过程，所以这一阶段的表示学习与生成模型用的是同一类目标。

**各领域的表现。**

- 语言（[预训练领域页](../llm/fields/pretraining/README.md)）：GPT 与 BERT（2018）给出两种预训练，目标从翻译迁移到 GLUE、SQuAD 这类理解型 benchmark（多个分类任务的组合与抽取式问答）；T5（2019）把所有任务统一成文本到文本，在其微调设定下 encoder–decoder 加去噪最好；GPT-3（2020）的 1750 亿参数 decoder-only 模型只靠提示中的几个示例完成任务（in-context learning，不更新权重，见 [GPT-3 精读](../llm/papers/gpt3/reading.md)）；BigScience 的对照实验（Wang 等 2022）显示，只做无监督预训练后直接零样本评测时因果 decoder-only 最好，此后 PaLM、LLaMA 都是因果语言模型。
- 视觉表征（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)）：MoCo（2019）在 7 个检测与分割迁移任务上超过 ImageNet 有监督预训练；ViT（2020）在 JFT-300M（Google 内部约 3 亿张图的标注数据集）上预训练后反超 ResNet（[ViT 精读](../multimodal/papers/vit/reading.md)）；CLIP（2021）用 4 亿对网页图文做对比预训练，在 ImageNet 上零样本（不用该数据集任何训练样本）达到原始 ResNet-50 的水平（[CLIP 精读](../multimodal/papers/clip/reading.md)）；MAE（2021）遮住 75% 的图像块再重建，只用 ImageNet-1K 时把此前最好的 87.1% 提到 87.8%（[MAE 精读](../multimodal/papers/mae/reading.md)）。
- 生成（[视觉生成领域页](../multimodal/fields/generation/README.md)）：DDPM（2020）把生成拆成从噪声出发的逐级去噪，训练目标是预测加进去的噪声（[DDPM 精读](../multimodal/papers/ddpm/reading.md)）；LDM（2021）把扩散搬到自编码器的低维潜空间；DiT（2022）用 Transformer 替换去噪 U-Net；Video Diffusion Models（2022）把图像扩散扩展到视频块。详见[生成的收敛](generative-convergence.md)。
- 训练科学（[训练科学页](../cross-domain/fields/training-science/README.md)）：规模定律把"模型多大、数据多少"变成可计算的预算，Chinchilla（70B 参数、1.4T token）与算力相同的 Gopher（DeepMind 此前的语言模型，280B 参数、300B token）相比，MMLU（覆盖多个学科的多选题知识基准）高 7 个百分点；Aghajanyan 等（2020）测到 RoBERTa-Large 在 MRPC（判断两句话是否同义的小规模数据集）上只训练 200 个参数就达到全参数微调 90% 的效果，LoRA（2021）以这类本征维度结果为依据，可训练参数比全参数微调少约 10000 倍。

**留下的问题。** 见下文"当前开放问题"。

## 收敛与分化

**走向同一种做法的地方**

- 流程：两条主干线都采用"大数据预训练、再迁移"的流程，CNN 一线自 R-CNN 起，Transformer 一线自 GPT 与 BERT 起，并在阶段三把预训练信号换成了数据本身。
- 主干部件：Transformer 的每个子层沿用 ResNet 的残差连接，Transformer 又从语言进入视觉识别（ViT）和图像生成（DiT）。论证见 [CNN 与 Transformer](cnn-vs-transformer.md)。
- 训练配方：残差加归一化、Adam 一族优化器、学习率预热与衰减，在语言、视觉和生成中通用；Video Diffusion 附录的超参数表用的也是 Adam。

**仍然不同的地方**

- 预训练目标的形式。语言收敛到下一词预测；视觉表征至今有对比学习、遮蔽重建、图文配对和自蒸馏（[DINO 精读](../multimodal/papers/dino/reading.md)）几种目标并存；连续信号的生成用逐级去噪。[判断] 原因在数据的形态：文本天然是离散 token 序列，一个下一词目标就同时覆盖理解与生成；图像没有同样自然的离散单位，各家只能从不同角度定义"数据给自己出的题"。
- 规模定律的成熟度。语言有拟合出的幂律和经过修正的最优配比（Kaplan、Chinchilla）；视觉与生成在本库的证据里只有平滑的趋势：CLIP 的迁移表现是算力的平滑函数，DiT 的 12 个模型中计算量与 FID 的相关系数为 −0.93。
- 评测口径。语言从"微调后成绩"转向零样本与少样本；视觉表征用线性评测（冻结特征，只训练一个线性分类器）、迁移检测与零样本；生成用 FID（生成样本与真实样本在 Inception 网络特征空间中的分布距离，越低越好）。评测口径一换，哪种做法最好的结论可以反转（BigScience 的两种设定）。
- 端侧与实时场景仍多用经过系统优化的 CNN（见 [CNN 与 Transformer](cnn-vs-transformer.md)）。

## 当前开放问题

- **规模定律能外推多远，能否搬到语言以外的模态？** Kaplan 等自述规律没有可靠的理论解释，并在约 10^12 参数处两条规律相互矛盾；Chinchilla 换学习率调度、纳入更大模型后配比就变了。入口：[训练科学页](../cross-domain/fields/training-science/README.md)、[Chinchilla 文献卡](../cross-domain/papers/arxiv-2203.15556/README.md)。
- **数据会先于算力用完吗？** Chinchilla 的分析假设每条数据只训练一遍，数据不够、需要重复使用时不在它的覆盖范围内。入口：[训练科学页](../cross-domain/fields/training-science/README.md)。
- **人工标注退到哪一步为止？** 预训练已经不靠标注，后训练仍靠人类偏好；InstructGPT 报告单纯调大 KL 系数收不回 DROP、SQuAD 上的能力回退，混入预训练梯度效果更好。入口：[InstructGPT 精读](../llm/papers/instructgpt/reading.md)。
- **规模的另一条轴：推理时投入的算力。** 入口：[Test-Time Compute 精读](../llm/papers/test-time-compute/reading.md)。
- **少量参数为什么就够？** 数据一侧的流形假说与参数一侧的本征维度、低秩更新是否同源。入口：[训练科学页](../cross-domain/fields/training-science/README.md)。

## 批注

**判断的支撑论文与反例**

- **三件事共同推动规模化。** 支撑：AlexNet Sec.1 与 ILSVRC 综述 Sec.5.1（改变局面的是数据、算力和 benchmark）；GPT-2 Sec.2.3、Goyal 等 Sec.1、Kaplan 等 Sec.1、Hoffmann 等 Sec.1（训练工程是扩大规模的前提）。反例或边界：ResNet 说明光加规模不够，2014 年的深度竞赛直接撞上退化问题，需要新的结构；三者的先后也不同步，硬件与标注数据在 2012 年到位，自监督信号在语言 2018 年、视觉 2019–2021 年才到位。
- **视觉的自监督是有意识的跨领域迁移。** 支撑：MoCo Sec.1、SimCLR Sec.1、MAE Sec.1 与 Sec.6、CLIP Sec.1 都以 NLP 的自监督预训练为参照。反例或边界：ViT 的关键结果依赖 JFT-300M 上的大规模有监督预训练，ViT 自述自监督与它之间仍有很大差距（ViT Sec.5）；CLIP 用的是网页图文对，属于弱监督。
- **过参数化网络里阻碍训练的主要是鞍点。** 支撑：Dauphin 等 2014（随机场模型的理论加小网络实测）、Choromanska 等 2014（自旋玻璃模型下低临界值集中在全局最小之上的窄带）、Garipov 等 2018 与 Draxler 等 2018（CIFAR 上 ResNet、DenseNet 的模式连通）。反例或边界：Safran 与 Shamir 证明两层 ReLU 网络在学生与教师宽度相同时坏局部极小很常见，轻度过参数化后才大幅减少；对一般的非线性网络没有证明。
- **"预训练再迁移"成为视觉默认流程。** 支撑：R-CNN Sec.1、MoCo Sec.1（把 ImageNet 有监督预训练当作要替代的默认起点）。反例或边界：U-Net（2015）面向只有几十张训练图的医学分割，从头训练。
- **目标形式的分化源于数据形态。** 支撑：MAE Sec.1 把视觉遮蔽自编码此前落后的原因之一归于卷积不便加入遮蔽标记；DiT Sec.1、LDM Sec.1 都在连续潜空间里做去噪。反例或边界：视频也有先离散化、再用 Transformer 自回归生成的路线（Video Diffusion 对照表中的 VideoGPT，题名即"用 VQ-VAE 与 Transformer 生成视频"），语言也有扩散式生成的尝试（[DFlash 文献卡](../llm/papers/arxiv-2602.06036/README.md)），见[生成的收敛](generative-convergence.md)。

**易误读**

- 常见说法"大规模训练下模型反而不容易陷入局部最优"，证据支持的准确版本是驱动力 3 末尾那一句；Choromanska 等的"SGD 收敛到低值带"在原文中是猜想。
- 阶段的年份按训练信号划分，有重叠：GAN（2014）不用标注，时间上属于阶段二，它的训练信号已经来自数据本身；阶段三的变化是生成式目标同时成为表示学习的预训练信号，并被扩大规模。
- Kaplan 等"主要加参数"的配比已被 Chinchilla 修正，引用时要注明是哪一篇。
- AlexNet 的 15.3% 来自多个 CNN 的平均，其中两个用了额外数据预训练（AlexNet Sec.6）。MAE 的 87.8% 是 448 分辨率下的结果。

**与其他页面的关联**

- [CNN 与 Transformer](cnn-vs-transformer.md) 展开"主干部件"一条；[生成的收敛](generative-convergence.md) 展开阶段三的生成一侧。
- [训练科学页](../cross-domain/fields/training-science/README.md) 是驱动力 3 的全部证据来源；[架构概念地图](../foundations/fields/architectures/README.md) 与[优化概念地图](../foundations/fields/optimization/README.md) 讲各机制怎么算。
- [递推状态谱系](../foundations/relations/recurrent-state.md) 说明阶段一的 RNN 怎样以状态空间模型的形式回到规模化之后的架构讨论。

**出处（本库没有单篇目录的论文，正文链接到领域页节点）**

- AlexNet：https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ImageNet：https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf ；ILSVRC 综述：https://arxiv.org/abs/1409.0575
- ResNet：https://arxiv.org/abs/1512.03385 ；R-CNN：https://arxiv.org/abs/1311.2524 ；HOG：https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf ；Neocognitron：https://www.cs.princeton.edu/courses/archive/spr08/cos598B/Readings/Fukushima1980.pdf
- MoCo：https://arxiv.org/abs/1911.05722 ；SimCLR：https://arxiv.org/abs/2002.05709 ；GAN：https://arxiv.org/abs/1406.2661 ；DCGAN：https://arxiv.org/abs/1511.06434 ；LDM：https://arxiv.org/abs/2112.10752 ；DiT：https://arxiv.org/abs/2212.09748
- Seq2seq：https://arxiv.org/abs/1409.3215 ；Bahdanau 注意力：https://arxiv.org/abs/1409.0473 ；BERT：https://arxiv.org/abs/1810.04805 ；T5：https://arxiv.org/abs/1910.10683 ；GPT：https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf ；Wang 等 2022：https://arxiv.org/abs/2204.05832
- Glorot 与 Bengio：https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf ；He 初始化：https://arxiv.org/abs/1502.01852 ；批归一化：https://arxiv.org/abs/1502.03167 ；Adam：https://arxiv.org/abs/1412.6980 ；层归一化：https://arxiv.org/abs/1607.06450 ；Goyal 等：https://arxiv.org/abs/1706.02677 ；Xiong 等：https://arxiv.org/abs/2002.04745 ；Kaplan 等：https://arxiv.org/abs/2001.08361 ；Aghajanyan 等：https://arxiv.org/abs/2012.13255 ；LoRA：https://arxiv.org/abs/2106.09685
- Dauphin 等：https://arxiv.org/abs/1406.2572 ；Choromanska 等：https://arxiv.org/abs/1412.0233 ；Garipov 等：https://arxiv.org/abs/1802.10026 ；Draxler 等：https://arxiv.org/abs/1803.00885 ；Safran 与 Shamir：https://arxiv.org/abs/1712.08968

**未核实 / 待验证**

- LeNet（1998）全文本轮没能打开，正文对它的描述沿用 CNN 讲义的写法。
- TPU 与大规模集群在语言模型训练中的具体用量，本页只引用了 Video Diffusion 附录的芯片数；其他论文的硬件规模没有逐篇核对。
- "端侧与实时场景多用 CNN"所依据的 MobileNet、EfficientNet、YOLO 都早于 ViT，没有同条件对比，见 [CNN 与 Transformer](cnn-vs-transformer.md) 的批注。
- 本页链接的领域页与训练科学页和本页同期写成；领域页定稿后，需要回头核对各节点的名称与本页一致。
