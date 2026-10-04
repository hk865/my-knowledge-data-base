# 架构与信息流：规模化之中的 CNN 与 Transformer

> 状态：领域入门页 · 试点 v2 · 依据 [synthesis-cnn.csv](synthesis-cnn.csv)（26 篇）与 [synthesis-transformer.csv](synthesis-transformer.csv)（14 篇）

[回到基础模块](../../README.md) · [完整讲义目录](../../../docs/foundations/01-architectures.md) · [训练工程方向页](../optimization/README.md)

## 这个领域在解决什么

给一张 224×224 的照片，判断里面是猫还是狗；给一句英文，生成它的法文译文。两件事都要先决定：输入的哪些部分之间应该交换信息、用多少参数、这些参数怎样从数据里学出来。架构就是对这些选择的回答。图像里相邻像素关系最紧，于是有了只看局部、处处共用同一个小核的卷积网络（CNN）；句子里相关的词可能相隔很远，于是有了按内容决定“读哪里”的注意力和 Transformer。

架构选哪一种，取决于三样外部条件：有多少数据，训练信号来自人工标注还是数据本身，硬件擅长哪种计算。卷积网络的机制在 1998 年的 LeNet 里已经齐备，到 2012 年配上 ImageNet 和 GPU 才改变视觉领域，差别全在这三样条件上。这个方向关心的是：每一种结构在什么数据规模、什么训练信号下最好用，以及它们怎样一步步走到今天。

## 主线历史

CNN 与 Transformer 两条机制史共用一条总线：规模化。GPU（AlexNet 用了两块）和后来的 TPU 集群提供算力，互联网提供图像与文本；训练信号则从人工标注逐步转向数据本身，因为标注成本随数据量增长，原始数据却几乎可以无限获取。按训练信号的来源，两条线可以放进三个阶段，每个阶段回答上一阶段留下的问题。阶段内的每个节点也先写上一个节点留下的问题，再写它改变了什么；完整论据和逐篇数字在两张综合表里。

### 阶段一：手工特征加小数据（1980–2011）

视觉的主流是人设计的特征加浅层分类器，只有分类器从少量标注中学习；LeNet 已经能从标注中学卷积核，但只在文档识别这类小规模任务上落地。这一阶段留下的问题：特征受限于人能设计出什么，而可学习的深网络缺少数据和算力。

1. **Neocognitron（1980，NHK，Fukushima）→ LeNet（1998，LeCun 等）**。问题：识别结果随图案平移和形变而改变。Neocognitron 按 Hubel–Wiesel 的简单/复杂细胞层级，交替堆叠“提取特征”和“容忍位置变化”的两种层，同一平面内的单元共用同一组连接，这就是卷积与权重共享的雏形。它靠无监督自组织学习，作者报告十类图案时结果对参数非常敏感。LeNet 改用标注数据和反向传播训练卷积核，在文档识别中落地（LeNet 原文本轮未能打开，见批注）。
2. **HOG（2005，INRIA）与 DPM（2010，Chicago/Berkeley 一系）**。这一时期视觉检测的主流是梯度方向直方图这类手工特征，加线性 SVM 或可变形部件模型。HOG 的流水线就是一个核固定的浅层 CNN（[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节）。它们留下的问题：特征由人设计，只有最后的分类器在学习；HOG 在 MIT 行人库上做到近乎完美分离后，作者另建了更难的 INRIA 数据集。

这一阶段的序列建模用的是 [RNN](../../../docs/foundations/12-rnn.md) 与 [LSTM](../../../docs/foundations/13-lstm.md)，Transformer 一线从阶段二开始。

### 阶段二：有监督深度学习（2009–2017）

上一阶段留下的问题是特征靠人设计。这一阶段的回答：用大规模人工标注加 GPU，让网络直接从像素或词里学特征。它留下的问题：每个新任务、新类别都要重新标注，标注量跟不上模型对数据的需求。

**CNN 一线**

3. **ImageNet（2009，Princeton）与 ILSVRC（2010 起每年举办）**。留下的问题：可学习的深网络需要大规模标注数据，各团队也需要同一个公开 benchmark 来比较。改变：提供按 WordNet 组织、目标数千万张的标注图库，以及约 120 万训练图、1000 类的年度竞赛。
4. **AlexNet（2012，Toronto）**。留下的问题：CNN 在高分辨率图像上大规模训练一直太贵。改变：两块 GPU、ReLU、dropout，加上 ImageNet 规模的数据，在 ILSVRC-2012 上 top-5 错误率 15.3%，第二名（Fisher 向量手工特征）为 26.2%。ILSVRC 组织者把 2012 年称为转折点：2013 年绝大多数、2014 年几乎全部参赛方法改用 CNN。
5. **VGG、GoogLeNet（2014）→ ResNet（2015，Microsoft Research）**。留下的问题：ILSVRC 上的竞争变成“怎样做得更深”。VGG 专门研究深度，GoogLeNet 在固定计算预算下加深加宽；更深的网络随即暴露出退化问题，训练误差反而上升。ResNet 用残差学习解决这一点，ILSVRC 2015 top-5 测试错误率 3.57%。
6. **R-CNN（2013）与 DPM are CNNs（2014），Berkeley**。留下的问题：PASCAL VOC 检测在 2010–2012 年停滞。改变：把 ImageNet 预训练的 CNN 迁移到检测并微调，VOC2007 mAP 从 HOG-DPM 的 33.7% 升到 54.2%；同一作者随后证明 DPM 本身可以展开成 CNN，手工特征路线并入 CNN 路线。[判断] 从这里开始，“ImageNet 预训练的视觉主干”成为检测、分割等任务的默认起点。
7. **U-Net（2015，Freiburg）**。留下的问题：生物医学分割要逐像素定位，训练图像往往只有几十张。改变：收缩路径提取上下文，对称的扩张路径恢复分辨率，跨层拼接补回细节。这个编码–解码结构后来成为扩散模型的去噪主干（本线第 14、15 个节点）。

**Transformer 一线**

1. **Seq2seq（2014，Google）**。问题：深度网络只能处理固定维度的输入输出，无法直接把序列映射到序列。改变：一个 LSTM 把源句压成一个固定长度向量，另一个 LSTM 从这个向量生成译文，在 WMT'14 英→法上超过短语统计翻译基线。
2. **Bahdanau 注意力（2014，Jacobs University Bremen 与 Montréal）**。留下的问题：整句信息都要经过一个固定长度向量，长句性能急剧下降。改变：解码每个词时按权重读取源句各位置（软对齐），长句不再退化。编码和解码仍是循环网络。
3. **Transformer（2017，Google）**。留下的问题：循环网络沿位置逐步计算，同一样本内部无法并行。改变：用注意力作为序列内和序列间交互的主体，去掉循环；目标仍是 WMT 机器翻译，英→德比此前最好集成模型高 2 BLEU 以上。

### 阶段三：自监督预训练与生成（2018 起）

上一阶段留下的问题是标注不随规模扩展。这一阶段的回答：让数据本身提供训练信号，即下一词预测、遮蔽预测、对比学习、去噪，再加少量有监督微调或人类偏好对齐（例如 [InstructGPT](../../../llm/papers/instructgpt/reading.md) 的 RLHF：先用人类对回答的排序训练一个奖励模型，再用强化学习按奖励微调语言模型）。收敛的是预训练阶段的训练信号，下游任务仍然多种多样。下一词预测和去噪既是自监督信号，本身也是生成过程，所以这一阶段的表示学习与生成模型用的是同一类目标。

**语言：Transformer 一线**

4. **GPT（2018，OpenAI）与 BERT（2018，Google）**。留下的问题：各任务的标注数据少，每个任务从头训练模型。两家给出两种预训练：GPT 取 decoder 一侧，用下一词预测预训练再微调；BERT 指出单向结构对问答等任务不利，改用 encoder-only 加遮蔽语言模型。目标从翻译迁移到 GLUE、SQuAD 这类理解型 benchmark。
5. **GPT-2（2019）与 T5（2019，Google）**。留下的问题：预训练加微调仍然要逐任务准备标注数据，各种方法也难以公平比较。GPT-2 改问“不微调、不改参数，语言模型能做多少任务”；T5 把所有任务统一成文本到文本，系统比较三种结构，结论是在其微调设定下 encoder–decoder 加去噪目标最好。
6. **GPT-3（2020，OpenAI）**。留下的问题：微调需要成千上万条样本，人只需看几个例子。改变：1750 亿参数的 decoder-only 模型只靠上下文中的示例完成任务（in-context learning，上下文学习：在提示里给几个例子，不更新权重）。它自述的局限正是 T5 的强项：没有双向结构和去噪目标。
7. **收敛：Wang 等（2022，BigScience）、PaLM（2022，Google）、LLaMA（2023，Meta）**。留下的问题：T5 与 GPT-3 的结论看起来互相矛盾。BigScience 的对照实验给出答案：只做无监督预训练后直接 zero-shot 评测，因果 decoder-only 最好；加多任务微调后，encoder–decoder 最好。此后 Google 的 PaLM、Meta 的 LLaMA 都是因果语言模型。

**视觉：CNN 一线（续），主干转入 Transformer**

8. **MoCo（2019，FAIR）与 SimCLR（2020，Google）**。留下的问题：语言已靠 GPT、BERT 式预训练摆脱逐任务标注，视觉仍以 ImageNet 有监督预训练为主。改变：对比学习（把同一张图的两种随机增强当作一对正样本，其他图当作负样本，训练编码器拉近正样本对）在 ResNet-50 上接近了有监督：MoCo 在 7 个检测/分割任务上超过 ImageNet 有监督预训练，SimCLR 用 4 倍宽的 ResNet-50 做线性评测（冻结学到的特征，只训练一个线性分类器）达到 76.5%，与有监督的标准 ResNet-50 相当。
9. **ViT（2020，Google Brain）**。留下的问题：卷积的局部性是必需的先验，还是可以由数据学出来？ViT 把图像切块直接交给 Transformer：只在 ImageNet 上训练时不如 ResNet，在 JFT-300M 上预训练后反超。它自述的局限之一，是自监督预训练与大规模有监督预训练之间仍有很大差距。
10. **CLIP（2021，OpenAI）**。留下的问题：视觉预训练仍依赖固定类别的人工标注（ImageNet、非公开的 JFT）。改变：从网上收集 4 亿对图文，用对比学习把配对的图像和文字编码到相近位置；分类时把类别名写成句子当作分类器，零样本（不用目标数据集的任何训练样本）在 ImageNet 上与原始 ResNet-50 相当，而没有用它的 128 万张训练图。同一篇论文里，ViT 图像编码器的计算效率约为 ResNet 的 3 倍。
11. **MAE（2021，FAIR）**。留下的问题：ViT 要靠大规模标注才能超过 CNN，视觉的遮蔽式自监督仍落后于语言。改变：遮住 75% 的图像块，只编码可见块，再用轻量解码器重建像素；只用 ImageNet-1K 训练，ViT-Huge 微调到 87.8%，此前只用这一数据集的最好结果为 87.1%。
12. **ConvNeXt（2022，FAIR）**。留下的问题：视觉 Transformer 的优势有多少来自架构本身？只给 ResNet-50 换上 Transformer 式训练配方就提升 2.7 个百分点，再借用 Transformer 的设计后全面追平并超过 Swin（一种分层的视觉 Transformer）。

**生成：CNN 一线（续），去噪主干从卷积 U-Net 换成 Transformer**

13. **GAN（2014，Montréal）→ DCGAN（2015，indico 与 FAIR）**。留下的问题：深度生成模型的似然难以计算，需要近似推断或马尔可夫链。GAN 让生成器与判别器对抗训练，只靠反向传播，原文主实验用多层感知机；DCGAN 找到一组能稳定训练的全卷积结构。两篇都自述训练不稳定，生成器会把许多输入映射到同一张图（模式坍缩）。
14. **DDPM（2020，UC Berkeley）**。留下的问题：GAN 的训练不稳定与模式坍缩。改变：把生成拆成从纯噪声出发的逐级去噪，训练目标是预测加进去的噪声，这本身就是一种自监督信号；CIFAR10 无条件生成的 FID（生成样本与真实样本在 Inception 网络特征空间中的分布距离，越低越好）为 3.17。去噪网络是 PixelCNN++ 式的 U-Net，以卷积残差块为主，在 16×16 分辨率处加自注意力。
15. **LDM（2021，LMU Munich、Heidelberg 与 Runway）**。留下的问题：像素空间扩散的训练常需数百 GPU 天，采样要顺序走很多步。改变：先用自编码器把图像压到低维潜空间再做扩散；U-Net 以二维卷积为主，加交叉注意力（以图像特征为查询、以文本等条件的编码为键和值）接入条件，在 LAION-400M 上训练了文本到图像模型。DiT 原文把这篇作为文本到图像模型 Stable Diffusion 的出处引用。
16. **DiT（2022 年 12 月 arXiv，UC Berkeley 与 NYU，作者在 Meta FAIR 实习期间完成）**。留下的问题：所有扩散模型都用卷积 U-Net 作主干，这种归纳偏置是否必要。改变：在 LDM 的潜空间里，把 U-Net 换成作用于潜变量块的标准 Transformer；计算量（Gflops）越大 FID 越低，最大模型在 ImageNet 256×256 类条件生成上把 FID 从 LDM 的 3.60 降到 2.27。

**两条线的交汇**：ViT 把 Transformer 带进视觉识别，DiT 把它带进图像生成，Transformer 的每个子层又沿用 ResNet 的残差连接。两条线都采用“先在大数据上预训练、再迁移到具体任务”的流程（CNN 一线自 R-CNN，Transformer 一线自 GPT 与 BERT），并在阶段三把预训练信号换成了数据本身。卷积留在新结构的入口处：ViT 的切块嵌入、DiT 所用的图像自编码器、Whisper 的音频前端都是卷积（见下一节）。

**训练工程是规模化的前提**：上面每一次扩大规模，都要求梯度能传过几十到上百层，大模型训练的结果可以预期，后续训练阶段不破坏已经学到的能力。对应的研究包括残差连接与归一化、Adam 与学习率预热、大批量训练的学习率线性缩放（Goyal 等 2017 用 8192 张图的批量、256 块 GPU 在一小时内训完 ResNet-50），损失随参数量、数据量和算力呈幂律变化的规模定律（Kaplan 等 2020），以及微调时用小学习率、LoRA（冻结原权重，只训练低秩增量矩阵）或 RLHF 中对参考模型的 KL 惩罚（新模型的输出分布偏离微调前的模型越远，扣分越多）来保住已有能力。推导与证据见[训练工程方向页](../optimization/README.md)。

## 为什么 Transformer 成为通用主干、CNN 仍在哪里占优

每条标注关系类型：`[结构]` 在正文写推导，`[经验]` 引用做出发现的实验，`[判断]` 的支撑论文列在批注。

**两类主干用同一套办法传递梯度**

- `[结构]` ResNet 的残差块输出 x + F(x)，Transformer 每个子层输出 LayerNorm(x + Sublayer(x))（原文 3.1 节），加法跳连是同一形式。对纯加法形式求导，∂y/∂x = I + ∂F/∂x，恒等项给梯度留了一条不经过 F 的通路；F 是卷积分支还是注意力分支，这条通路都存在。归一化放在加法之后还是分支之内，影响的是训练稳定性，见[训练工程方向页](../optimization/README.md)。

**真正的差别在归纳偏置与感受野**

- `[结构]` 归纳偏置（结构里预先写入的关于数据的假设）。卷积核只连局部、在所有位置共用，因此平移等变：输入平移几个像素，特征图跟着平移同样的距离。感受野随层数线性增长：每层 3×3、步长 1 的卷积向外多看 1 个像素，L 层的感受野是 (2L+1)×(2L+1)，要覆盖 224 像素宽需要 112 层，实际网络靠下采样加快扩张。自注意力在第一层就让每个图像块读取全部图像块。ViT 原文 3.1 节写的正是这一区别：CNN 的每一层都内置局部性、二维邻域和平移等变，ViT 中只有 MLP 层是局部的。
- `[经验]` 先验在小数据时帮忙，在大数据时成为限制：ViT 在 JFT-300M 的随机子集上，9M 张时 ViT-B/32 明显差于计算量相近的 ResNet50，90M 张以上反超（ViT 4.3 节、Fig.4）。
- `[经验]` 第一层的全局读取确实被用上：ViT 测量注意力距离（作用类似 CNN 的感受野），最低层已有一些头关注图像的大部分区域，另一些头只看邻近区域；在前面接 ResNet 的混合模型中这类局部头较少，作者据此推测它们承担了 CNN 早期卷积层的作用（ViT 4.5 节、Fig.7）。
- `[经验]` token 化的结构方便自监督：MAE 作者把视觉遮蔽自编码此前落后的原因之一归于卷积在规则网格上运算，不便加入遮蔽标记和位置嵌入，ViT 消除了这一障碍（MAE 第 1 节）。

**生成任务分语言和图像两种情况**

- 语言生成由 decoder-only Transformer 主导（Transformer 一线第 7 个节点）。
- `[经验]` 图像生成的主干长期以卷积为主：DCGAN 是全卷积 GAN；DDPM 与 LDM 的去噪 U-Net 以卷积残差块为主，在低分辨率处插入自注意力，LDM 还用交叉注意力接入文本。DiT 把 U-Net 换成 Transformer 后，12 个模型的 Gflops 与 FID 相关系数为 −0.93，最大模型优于此前所有扩散模型（DiT 5.1 节、Fig.8）。

**[判断] Transformer 胜出主要靠通用性与可规模化**

- 同一结构处理多种输入：文本 token、图像块（ViT）、潜变量块（DiT）、音频频谱（Whisper 选用 encoder–decoder Transformer，理由是这种结构已被充分验证能可靠地扩展）。
- 规模化行为可以预测：语言模型的损失随参数、数据、算力呈幂律下降（Scaling Laws）；CLIP 的迁移表现是算力的平滑函数；DiT 的 FID 随 Gflops 稳定改善。
- 大规模预训练下计算效率更高：ViT 达到同样迁移表现所需的预训练计算约为 ResNet 的 1/4 到 1/2（ViT 4.4 节）；CLIP 中 ViT 的计算效率约为 ResNet 的 3 倍。
- 边界：ConvNeXt 表明，在 ImageNet-1K/22K 规模下，配上现代训练配方与设计的纯 CNN 能追平或超过 Swin，推理吞吐相当或更高。两者的差距相当一部分来自训练配方与数据；Transformer 的优势集中在跨模态的统一和更大规模下可预测的扩展。

**CNN 仍然占优或常用的地方**

- `[经验]` 数据有限时：ImageNet-1K 或 JFT 的 9M 子集上，ResNet 优于同等计算的 ViT（见上）；U-Net 本来就是为只有几十张训练图的医学分割设计的。
- `[经验]` 计算预算小时：ViT 的对照中，前面接 ResNet 的混合模型在小计算预算下略优于纯 ViT，规模变大后差别消失（ViT 4.4 节）。
- `[判断]` 端侧与实时场景：MobileNet 用深度可分离卷积为手机和嵌入式设备做低延迟模型；EfficientNet 用复合缩放让 B7 在与 GPipe 同为 84.3% 的精度下小 8.4 倍、快 6.1 倍；YOLO 用单个卷积网络在 VOC 2007 上以每秒 45 帧达到 63.4% mAP。三篇都早于 ViT，体现的是 CNN 针对延迟与参数量做过的系统优化。
- `[结构]` ViT 的切块嵌入就是一个卷积。原文式 (1) 把每个 P×P×C 的图像块展平，乘同一个矩阵 E，这等价于核大小 P×P、步长 P、输出 D 个通道的卷积。以 ViT-B/16 为例：224×224×3 的图像切成 14×14 = 196 块，每块展平为 16·16·3 = 768 维，乘 768×D 的 E；把 E 的每一列重排成 16×16×3 的卷积核，以步长 16 滑过图像，得到 14×14×D 的特征图，逐位置读出就是 196 个块嵌入。
- `[经验]` 混合结构很常见：ViT 原文就定义了从 CNN 特征图切块的混合模型；DiT 用现成的卷积 VAE 把图像压成潜变量；Whisper 的编码器前端是两层卷积。

## 技术地基

- **卷积的归纳偏置**：小核在所有位置复用，参数量与图像大小无关，并带来局部性与平移等变；CNN 一线的全部节点都建立在它上面，它在小数据下的优势与大数据下的限制也决定了 ViT 之争。[CNN 讲义](../../../docs/foundations/11-cnn.md)第 2–3 节。
- **反向传播与残差连接**：反向传播把“手工指定的核”变成“由数据决定的核”，是 Neocognitron 到 LeNet、HOG 到 AlexNet 两次转变的共同条件；残差连接让很深的网络可以训练，被 Transformer 每个子层沿用。[优化模块](../../../docs/foundations/02-optimization.md)、[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节、[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 10.2 节。
- **注意力（Q、K、V）**：按内容决定读哪里、读什么，是 Transformer 一线从 Bahdanau 起的核心机制，也让第一层就能全局读取。[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 3–6 节、[QKV 讲义](../../../docs/foundations/15-qkv-deep-dive.md)。
- **可见性与因果 mask**：决定一个模型属于 encoder-only、decoder-only 还是 encoder–decoder，也决定它能否用下一词目标并行训练。[Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 7、12、13 节。
- **自监督训练信号与迁移**：下一词预测、遮蔽预测、对比学习、去噪是让数据给自己出题的四种方式，阶段三的每个节点都建立在其中一种上；预训练得到的表示再迁移到具体任务。[自监督与生成目标](../../../docs/foundations/modules/objectives/03-pretraining-objectives.md)、[扩散讲义](../../../docs/foundations/17-diffusion.md)、[迁移与元学习模块](../../../docs/foundations/05c-transfer-meta-learning.md)。
- **训练工程**：初始化、归一化、学习率调度、规模定律与参数高效微调，让规模化可以执行和预测。[训练工程方向页](../optimization/README.md)。

## 主要路线与团队偏好

- **手工特征加浅层学习**（Dalal 与 Triggs 的 HOG；Felzenszwalb、Girshick 等的 DPM）。押注：人对图像结构的先验（方向梯度、可变形部件）比从数据中学更可靠。代价：特征固定，进展受限于人能设计出什么；PASCAL VOC 上 2010–2012 年的停滞即是表现。[判断] Girshick 所在的一系在 DPM、R-CNN、DPM are CNNs 三篇中始终以 PASCAL VOC 检测为目标、以 DPM 为对照，并在转向 CNN 时选择证明“旧模型是新模型的特例”，而不是另起炉灶。
- **ImageNet 规模的有监督 CNN**（Toronto 的 AlexNet，Oxford 的 VGG，Google 的 GoogLeNet，Microsoft Research 的 ResNet）。押注：数据和算力足够时，深网络从像素学到的特征优于手工特征。代价：依赖大规模标注和 GPU，结构选择长期围绕 ILSVRC 的分类指标展开。
- **decoder-only 加扩大规模**（OpenAI 的 GPT、GPT-2、GPT-3 与 Scaling Laws）。押注：一个下一词目标、一个因果结构，规模足够大时可以覆盖各种任务。代价：GPT-3 自述在需要双向上下文的任务上较弱，训练与推理成本高。[判断] OpenAI 在四篇中都保留 decoder-only，同时语言模型的对外开放程度逐步收紧：GPT-2 分阶段发布模型，GPT-3 只发布样本与数据重叠信息，未发布权重。
- **encoder-only / encoder–decoder 加系统比较**（Google 的 Transformer、BERT、T5）。押注：针对理解型 benchmark 和微调设定，双向可见性与去噪目标更有效。代价：生成与少样本使用不如 decoder-only 方便。[判断] Google 在这三篇中都发布了代码或权重（tensor2tensor、BERT、T5 与 C4 数据集），ViT 也发布了模型；2022 年的 PaLM 改用 decoder-only，论文中未见发布权重的声明。同一团队的路线随目标变化而调整。
- **视觉自监督与图文弱监督**（FAIR 的 MoCo、MAE；Google 的 SimCLR；OpenAI 的 CLIP）。押注：像语言一样让数据自己提供视觉训练信号，方式是对比两种增强视图、重建遮住的块，或对齐网上的图文对。代价：对比学习依赖强数据增强和大批量（SimCLR）或大字典（MoCo）；CLIP 自述零样本只能在给定概念中选择，并估计还要约 1000 倍算力才能整体达到最优。[判断] FAIR 一系（He、Girshick 等）在 MoCo 和 MAE 中都以 NLP 的 GPT、BERT 为参照提出问题，都把“迁移到检测、分割时能否超过 ImageNet 有监督预训练”作为主要评价；MoCo 结论中提出的下一步“遮蔽自编码”由 MAE 实现。
- **扩散生成**（UC Berkeley 的 DDPM，LMU Munich、Heidelberg 与 Runway 的 LDM，UC Berkeley 与 NYU 的 DiT）。押注：逐级去噪的似然模型比对抗训练稳定，样本质量随主干和算力扩大持续提升。代价：采样要顺序走很多步，比 GAN 慢（LDM 自述）；潜空间方案受自编码器的重建精度限制。[判断] 主干转向 Transformer 的理由，DiT 自述为分享“架构统一”带来的训练配方与规模化性质，与 Whisper 选用 Transformer 的理由一致。

## 用什么衡量进展

benchmark 的替换就是领域目标的迁移：

- **视觉识别**：MIT 行人库（HOG 近乎完美分离后饱和）→ INRIA 行人库 → PASCAL VOC 检测（DPM、R-CNN 的主战场）→ ImageNet / ILSVRC 分类（2010 起，AlexNet 到 ResNet 的主战场）→ COCO 检测、ADE20K 分割等迁移任务（ResNet、ConvNeXt 都报告）。ILSVRC 组织者自己记录了外界批评：数据集不够难、细粒度类别有标注错误、外部数据规则太严。ViT 的关键结论依赖 JFT-300M，这是非公开数据，外部团队无法复现同一条件。
- **视觉表示**：自监督预训练出现后，评测改为两种协议：冻结特征、只训练线性分类器的 ImageNet 线性评测，以及迁移到 VOC、COCO 的检测与分割（MoCo、SimCLR、MAE 都报告）。CLIP 再改为不训练任何参数的零样本评测，覆盖 30 多个数据集；它自述的口径问题是开发中反复查看完整验证集，主结果所用的 27 个数据集与 CLIP 的开发共同演化。
- **图像生成**：FID 从 CIFAR10 无条件生成（DDPM 3.17）转到 ImageNet 256×256 类条件生成（LDM 3.60 → DiT 2.27）。口径问题：FID 对实现细节敏感，DiT 统一用 ADM 的评测代码导出样本重算；DDPM 的 3.17 相对训练集计算，相对测试集为 5.24；类条件的最好结果都用了无分类器引导（采样时沿条件预测与无条件预测之差的方向多走一步，让样本更符合给定类别）。
- **语言**：WMT 机器翻译 BLEU（Seq2seq 到 Transformer）→ GLUE、SQuAD（GPT、BERT）→ SuperGLUE（T5 得 88.9，人类基线 89.8，接近饱和）→ 不微调的 zero-shot / few-shot 多任务评测（GPT-3 覆盖二十多个数据集，BigScience 用 LM Evaluation Harness 与 T0-Eval，LLaMA 报告 MMLU、GSM8k、HumanEval 等）。口径问题：评测从“微调后成绩”换成“不微调成绩”后，哪种结构最好的结论随之反转（见 Transformer 一线第 7 个节点）；大规模网络语料还带来训练数据与测试集重叠的问题，GPT-3 公开了它的重叠检查信息。

## 当前开放问题

- **架构差异与数据、训练配方、计算量怎样分开？** ViT 与 ConvNeXt、U-Net 与 DiT 两组对照都显示，主干的差别要与数据规模、训练配方和计算量一起看。入口：[ViT 精读](../../../multimodal/papers/vit/reading.md)、[MAE 精读](../../../multimodal/papers/mae/reading.md)、[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6 节。
- **注意力的二次方成本，能否换成固定大小的递推状态？** 线性注意力、状态空间模型和 Mamba 都在回答这个问题。入口：[递推状态谱系](../../relations/recurrent-state.md)、[Mamba 精读](../../../llm/papers/mamba/reading.md)。
- **知识存在哪里，怎样扩容？** FFN 可以读成键值记忆，事实回忆研究和 MoE 都沿着这条分工展开。入口：[注意力与 FFN 的分工谱系](../../relations/attention-ffn-division.md)、[FFN 键值记忆](../../../cross-domain/papers/arxiv-2012.14913/README.md)、[Switch Transformer](../../../llm/papers/arxiv-2101.03961/README.md)。
- **双向理解与生成能否兼得？** GPT-3 在局限一节把“双向模型做到同等规模、并支持少样本”列为有前景的方向；BigScience 建议先训练因果 decoder，再做非因果适配和多任务微调。入口：[GPT-3 精读](../../../llm/papers/gpt3/reading.md)。

## 阅读顺序

1. [CNN 讲义](../../../docs/foundations/11-cnn.md)：先从一个 [−1,0,1] 核理解卷积，再读第 6 节的历史链和第 9 节的“从手工特征到可学习特征”。
2. [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)：手算一次注意力，再读第 13.5 节三条路线的收敛；想弄清匹配与内容为什么分开，接着读 [QKV 讲义](../../../docs/foundations/15-qkv-deep-dive.md)。
3. [Attention Is All You Need 精读](../../../llm/papers/transformer/reading.md)：Transformer 一线第 3 个节点的原文。
4. [ViT 精读](../../../multimodal/papers/vit/reading.md)：两条线的交汇点，也是“归纳偏置与数据规模”这一问题的起点。
5. [CLIP 精读](../../../multimodal/papers/clip/reading.md)与 [MAE 精读](../../../multimodal/papers/mae/reading.md)：阶段三视觉一侧的两种训练信号，图文对比与遮蔽重建。
6. [GPT-3 精读](../../../llm/papers/gpt3/reading.md)：decoder-only 加规模这条路线的代表，它的局限一节连接到收敛问题。

同一方向的其余模块：[RNN](../../../docs/foundations/12-rnn.md) 与 [LSTM](../../../docs/foundations/13-lstm.md) 是 Transformer 之前的序列模型；[SSM、GNN 与 MoE](../../../docs/foundations/18-ssm-gnn-moe.md) 接在开放问题之后；[VAE](../../../docs/foundations/16-vae.md)、[扩散模型](../../../docs/foundations/17-diffusion.md) 与 [DDPM 精读](../../../multimodal/papers/ddpm/reading.md) 讨论生成建模，对应本页的生成一侧；[DINO 精读](../../../multimodal/papers/dino/reading.md) 是另一种自监督 ViT（自蒸馏）；[训练工程方向页](../optimization/README.md) 讲规模化的训练条件。

## 批注

**易误读**

- AlexNet 与第二名的 15.3% 对 26.2%，比较的是 ILSVRC-2012 测试集 top-5 错误率；AlexNet 的这个数字来自多个 CNN 的平均，其中两个用了额外的 ImageNet Fall 2011 数据预训练（原文第 6 节）。
- T5 的“encoder–decoder 最好”是在其任务组合与微调设定下（原文 3.2.4 节）；BigScience 的结论分两种设定，不能只引用其中一半（原文第 4 节）。
- ViT 在 ImageNet-1k 上不如 ResNet、在 JFT-300M 上反超，比较的是同等规模的 BiT ResNet，并且都经过迁移微调（原文 4.3 节、Fig.3）。
- SimCLR 的 76.5% 用的是 4 倍宽的 ResNet-50；标准宽度时自监督为 69.3%，同结构有监督为 76.3%（附录 B.8）。MoCo 的线性评测为 60.6%，“超过有监督预训练”只指 7 个检测/分割迁移任务（Sec.4.2）。
- MAE 的 87.8% 是 ViT-H 在 448 分辨率下微调的结果，224 分辨率为 86.9%（Sec.4.2）。DiT 的 2.27 用了无分类器引导（Table 2）。
- GAN 原文的主实验用多层感知机，只有一个 CIFAR-10 版本用了卷积判别器和“反卷积”生成器（Fig.2）；能稳定训练的卷积 GAN 结构来自 DCGAN。
- 残差一条的推导针对纯加法形式。原始 Transformer 是 Post-LN（LayerNorm 在加法之后），恒等通路要经过 LayerNorm；Pre-LN 把它移进分支，Xiong 等（2020）证明后者初始化时梯度更平稳，可以去掉学习率预热。
- 硬件契合度：Transformer 相对循环网络的硬件优势是同一样本内可以并行（Transformer 第 1 节）。相对 CNN，ConvNeXt 在 V100、A100 上测得相近 FLOPs 下推理吞吐相当或更高（Table 1、附录 E），所以“大矩阵乘法更契合 GPU”单独解释不了 Transformer 取代 CNN。
- MobileNet、EfficientNet、YOLO 都早于 ViT，没有与视觉 Transformer 做同条件对比，所以“端侧与实时场景 CNN 占优”标为 [判断]。
- OpenAI 的 CLIP 与 Whisper 都发布了权重和代码；“开放程度逐步收紧”只针对其语言模型一线。

**判断的支撑论文**

- Girshick 一系的偏好：DPM（PAMI 2010）Sec.8、R-CNN Table 1–2、DPM are CNNs Table 1，三篇都以 PASCAL VOC 为目标、以 DPM 为对照。
- OpenAI 的路线与开放程度：GPT Sec.4.1、GPT-2 Sec.2.3 与 Sec.7 脚注、GPT-3 Sec.2.1 与 Sec.5、Scaling Laws Sec.2；CLIP 与 Whisper 的 Abstract（发布权重）。
- Google 的开放与路线调整：Transformer Sec.7、BERT 代码仓库、T5 Sec.4.1、ViT Sec.1 脚注、PaLM Sec.2。
- “收敛是因为目标变了”：T5 Sec.3.2.4、GPT-3 Sec.5、Wang 等 2022 Sec.4–5。
- “改变局面的是数据、算力和 benchmark”：AlexNet Sec.1、ILSVRC 综述 Sec.5.1。
- “ImageNet 预训练主干成为默认起点”：R-CNN Sec.1、MoCo Sec.1（把 ImageNet 有监督预训练作为要替代的对照）。
- 三阶段的划分（训练信号从人工标注转向数据本身）：MoCo Sec.1、SimCLR Sec.1、MAE Sec.1 与 Sec.6、CLIP Sec.1 都以 NLP 的自监督预训练为参照，指出视觉仍依赖有监督预训练；GPT Sec.1、BERT Sec.1。
- Transformer 胜出靠通用与可规模化：ViT Sec.4.4、CLIP Sec.1 与 Sec.3.2、DiT Sec.1 与 Fig.8、Whisper Sec.2.2、Scaling Laws Abstract；限制它的反向证据是 ConvNeXt Sec.3、Sec.4 与附录 E。
- CNN 在端侧与实时场景：MobileNet Sec.1 与 Table 8、EfficientNet Fig.1 与 Table 2、YOLO Table 1；小计算预算下的混合模型结果见 ViT Sec.4.4。
- FAIR 一系在视觉自监督中的偏好：MoCo Sec.1、Sec.4.2、Sec.5；MAE Sec.1、Sec.5、Sec.6。
- 扩散主干转向 Transformer 的理由：DiT Sec.1；Whisper Sec.2.2。
- Meta 的两篇（ConvNeXt 发布代码，LLaMA 向研究社区发布全部权重）都选择开放，但出自不同小组，按“同一团队两篇以上”的标准还不足以算作偏好，因此未写进正文。

**与其他论文的关联**

- [Attention 与 Transformer 讲义](../../../docs/foundations/14-attention-transformer.md)第 13.5 节、第 17 节，与本页 Transformer 一线一致；[CNN 讲义](../../../docs/foundations/11-cnn.md)第 6、9 节，与本页 CNN 一线一致。两处如有出入，以综合表中的原文出处为准修改。
- [LLM 架构方向](../../../llm/fields/architecture/README.md) 从本页 Transformer 一线的终点接着往下讲。
- [MAE 精读](../../../multimodal/papers/mae/reading.md) 与 [CLIP 精读](../../../multimodal/papers/clip/reading.md) 展开 CNN 一线第 10、11 个节点；[DINO 精读](../../../multimodal/papers/dino/reading.md) 是同期另一条自监督 ViT 路线，MAE Table 3 把它作为对照。
- [DDPM 精读](../../../multimodal/papers/ddpm/reading.md) 与[扩散讲义](../../../docs/foundations/17-diffusion.md)展开 CNN 一线第 14 个节点；去噪 U-Net 的结构来源是本页阶段二的 U-Net。
- [InstructGPT 精读](../../../llm/papers/instructgpt/reading.md) 第 6 节的 KL 惩罚，是阶段三“偏好对齐不破坏已有能力”的做法；[Chinchilla](../../../cross-domain/papers/arxiv-2203.15556/README.md) 修正了 Scaling Laws 中参数与数据的最优配比。两者在[训练工程方向页](../optimization/README.md)中展开。
- [递推状态谱系](../../relations/recurrent-state.md) 是开放问题第二条的展开，也说明 Transformer 一线之前的 RNN 怎样以 SSM 的形式回到这一方向。

**综合表说明**

- 两张表各一行一篇，列为年份、团队、论文（路线）、要解决的问题、对照的 baseline、benchmark、自述局限、代码/数据是否开放、来源 URL。“论文（路线）”一列是为了能识别每一行而加的。各格是原文的中文转述，并注明节号或表号，没有大段照录原文。
- 视觉自监督、生成与端侧 CNN 的论文放在 synthesis-cnn.csv（视觉一线），DiT 与 Whisper 放在 synthesis-transformer.csv（Transformer 扩展到生成与音频）。
- 每一格都来自实际打开的原文；只经 ar5iv 页面摘要模型转述、没有逐字核对的格，表内标注“ar5iv 转述”。

**未核实 / 待验证**

- LeNet（LeCun 等 1998）全文本轮没能打开，synthesis-cnn.csv 中该行除题录外都标为未核实；阶段一第 1 个节点的描述沿用 CNN 讲义原有的写法。
- GPT-2 完整模型的发布时间线（OpenAI 博客无法访问）；PaLM 自述局限的精确节号。
- DPM（PAMI）发表年份按题录填写，所用 PDF 正文没有印出年份。
- Stable Diffusion 本身的发布材料（模型卡、训练数据）本轮没有打开；本页只按 DiT 原文的引用，把 LDM 视为它的出处。
- MobileNet 论文只写了“计划发布模型”；MAE、DCGAN 论文正文未声明代码发布。实际发布情况没有另查。
- DiT 的正式发表会议（arXiv 页面只给出代码与项目页，没有写会议），本页只写 arXiv 时间 2022 年 12 月。
