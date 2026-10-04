# 视觉表征

> 状态：领域入门页 · v2 · 依据 [synthesis.csv](synthesis.csv)（28 篇）
>
> 速览：
> - 视觉表征是编码器对一张图的输出 z = f(x)；这个方向没有专属 benchmark，好坏由使用它的任务和评测协议定义，换一个协议排名会翻转（例如 ViT-L 上 MAE 的线性评测低于 MoCo v3，全量微调却高于它）。
> - 每种方法是"训练信号 × 架构 × 数据"三条轴上的一个点：训练信号决定表征偏向哪些性质，架构决定先验和可扩展性，数据决定信号能放大到多大。
> - 主线历史是这三条轴的依次移动：手工特征 → ImageNet 与有监督 CNN → 预训练加微调（R-CNN）→ 自监督对比学习 → ViT → CLIP、MAE、DINO 与 ConvNeXt 对 ViT 的四种回答 → DINOv2 的冻结即用。
> - [判断] 四个趋势：从追求不变性走向逐像素；与语言对齐；从逐任务微调走向一个冻结编码器服务多个任务；训练信号的来源从人转向数据本身。
> - [判断] 实践中的终点更像按性质组合多种表征，例如 OpenVLA 拼接语义特征（SigLIP）与空间特征（DINOv2）。

## 什么是视觉表征

视觉表征是编码器（把图像变成向量的网络，下游使用时也叫主干）对一张图的输出，写成 z = f(x)：x 是像素，f 是事先在 ImageNet、网上图文对或无标注图像上训练好的网络，z 可以是代表整张图的一个向量，也可以是一张特征图（每个位置或每个图像块各有一个向量）。检测器要在街景里框出行人，医生要在电镜图里分割细胞，机器人要在没见过的厨房里找到杯子：三件事都先把像素交给某个 f，再在 z 上接各自的任务模块。f 用卷积还是 Transformer 搭建，机制见 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 2–6 节与 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.2、13.4 节。

这个方向没有自己专属的任务和 benchmark。一个 z 好不好，由使用它的任务（下一节）和评测协议（冻结特征只训线性分类器、全量微调、零样本等，见再下一节）来定义；同一个 f 换一个任务或协议，评价可以完全不同。所以本页先讲任务和测量，再讲方法和历史。学到的主干随后交给检测、分割、[视觉语言模型](../vlm/README.md)、[视觉生成](../generation/README.md)和机器人策略使用，这个方向的每一次进展都会传到几乎所有视觉相关的领域。本方向属于[多模态总目录](../../README.md)。

## 从任务看

结论：各任务要求的性质互相拉扯，"最好的表征"只能相对某个任务来说。

先说几个词。**不变性**：输入做某种变换（平移、换光照、换纹理）后特征保持不变；**等变性**：输入变换后特征做对应的变换，例如物体右移，特征图上的响应也右移（[CNN 讲义](../../../foundations/lessons/11-cnn.md)第 5 节）。**线性可分**：不同类别的特征能用一个线性分类器分开。使用方式有四种：**线性头**（冻结 f，只训一层线性分类器）、**全量微调**（f 的参数随下游任务一起训练）、**适配器**（冻结 f，只训插在 f 与下游模型之间的小模块，例如 LLaVA 的投影矩阵）、**多尺度特征**（取 f 中不同深度、不同分辨率的特征图组合起来，让检测器同时处理大小不同的物体）。冻结、部分微调与全量微调的一般原理见[迁移与元学习](../../../foundations/lessons/05c-transfer-meta-learning.md)第 2–3 节。

| 任务 | 需要的性质 | 常见使用方式 | 本库中的证据 |
|---|---|---|---|
| 识别 / 分类 | 对姿态、光照、背景不变；全局；语义；线性可分 | 线性头、k 近邻（在已标注样本中找特征最近的 k 个投票），或全量微调 | ILSVRC；[DINO](../../papers/dino/README.md) 的 ViT-S/8 特征只用 k 近邻就达到 ImageNet top-1 78.3% |
| 目标检测 | 对类别内差异不变、对位置等变；多尺度；依赖物体形状 | 全量微调加多尺度特征 | R-CNN 起检测都微调主干；MAE 把单一尺度的 ViT 块堆平均分成 4 段，用卷积上下采样出步长 4–32 的 4 张特征图，再接 FPN（特征金字塔网络） |
| 语义分割 | 逐像素；等变；语义 | 分割解码头加全量微调，或冻结特征加逐块线性头 | [MAE](../../papers/mae/README.md) 迁移到 ADE20K；DINOv2（DINO 团队 2023 年的大规模后续版本）用冻结特征加线性头做分割 |
| 深度与几何 | 逐像素；几何信息而非类别语义 | 冻结特征加线性头或 DPT 解码头（Ranftl 等 2021 提出的稠密预测解码器） | DINOv2 冻结特征的单目深度估计超过已有的自监督与图文弱监督特征，作者认为靠图像描述学到的特征抓不住这类细微模式（DINOv2 §7.4） |
| 检索与对应 | 区分具体实例；局部对应 | 冻结特征，按相似度最近邻 | DINO 在 DAVIS 视频分割上用冻结的逐块特征，按最近邻把首帧掩码逐帧传下去 |
| 生成：作为条件 | 与文本语义对齐 | 冻结编码器的嵌入作为生成条件 | DALL·E 2 以 CLIP 图像嵌入为条件，它自述 CLIP 嵌入不显式绑定属性与物体（见[视觉生成方向](../generation/README.md)） |
| 生成：作为潜空间 | 能还原像素细节 | 在自编码器的潜变量上做扩散 | LDM 自述需要像素级精度时，自编码器的重建能力成为瓶颈 |
| VLM 的视觉输入 | 逐块网格特征；与语言对齐；保留局部细节 | 冻结编码器加适配器 | [LLaVA](../../papers/llava/README.md) 取 CLIP ViT-L/14 的网格特征，经线性投影接入语言模型；取倒数第二层比取最后一层在 ScienceQA（科学问答 benchmark）上高约 1 个百分点（90.92% 对 89.96%），作者推测最后一层更偏全局、抽象的性质 |
| 机器人策略 | 空间细节与语义兼得；能随闭环控制调整 | 两种编码器拼接，并全量微调 | [OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 拼接 DINOv2 与 SigLIP（CLIP 式图文对比训练的编码器）两路特征；冻结视觉编码器使成功率从约 70% 降到 47%（较小的 SigLIP-only 变体上的消融）。[世界模型方向](../world-models/README.md)中，[DINO-WM](../../papers/arxiv-2411.04983/README.md) 与 [Back to the Features](../../papers/arxiv-2507.19468/README.md) 以预训练 DINO 特征为世界模型的状态空间（据标题） |

[判断] 拉扯集中在三对性质上。**不变与等变**：分类要丢掉位置，检测和分割要保留位置。**全局与局部**：CLIP 的训练目标只用整张图的一个向量，LLaVA 却从倒数第二层取局部细节。**语义与几何、可重建**：DALL·E 2 用 CLIP 嵌入提供语义，LDM 用可重建的自编码器潜变量当画布，DINOv2 认为图文特征抓不住深度。一个训练目标在一对性质上偏向一边，就会在另一类任务上付出代价，所以 OpenVLA 把两种编码器拼在一起用。

## 从测量看

结论：评测协议决定"好"指什么；同一个方法换一个协议，排名会翻转。

| 协议 | 做法 | 测的是什么 |
|---|---|---|
| 线性评测 | 冻结 f，在 ImageNet 训练集上只训一个线性分类器 | 语义是否已经线性可分 |
| k 近邻 | 冻结 f，不训练任何参数，在训练集里找特征最相似的 k 个样本投票（DINO 取 k = 20） | 特征空间里的距离本身是否有语义 |
| 少样本 | 每类只给极少标注，例如 1% 的标签，或每类 4 张 | 标注极少时的效率 |
| 微调 | 全量微调，或只调最后几块 | 作为初始化的价值；允许非线性地重组特征 |
| 迁移到检测与分割 | 在 PASCAL VOC、COCO、ADE20K 上带任务头训练 | 对定位和逐像素任务的用处 |
| 零样本 | 不用目标数据集的任何训练样本，把类别名写成句子，用它的文本嵌入当分类器 | 开放类别识别 |
| 鲁棒性与分布外 | 在人工损坏（ImageNet-C 的 15 种噪声、模糊、天气、数字损坏）或自然分布偏移（ImageNet-R、ObjectNet 等）的测试集上测 | 训练分布之外能否保持 |

排名翻转的四个例子：

1. **对比学习与有监督**。标准宽度 ResNet-50 上，SimCLR 线性评测 69.3%，同结构有监督 76.3%（SimCLR 附录 B.8）；MoCo 的线性评测只有 60.6%，迁移到 VOC、COCO 等 7 个检测与分割任务时却超过了 ImageNet 有监督预训练（MoCo §4.2）。
2. **遮蔽重建与对比学习**。同为 ViT-L，MoCo v3 线性评测 77.6%，MAE 75.8%（MAE 附录 B）；全量微调时 MAE 85.9%，MoCo v3 84.1%（MAE Table 3，224 分辨率）。在 MAE 的默认消融设置下，只微调最后 1 个 Transformer 块，准确率就从线性评测的 73.5% 升到 81.0%，微调最后 4 块时领先 MoCo v3 2.6 个百分点（MAE §4.3、Fig.9）。作者的解释是：线性评测错过了强但非线性的特征。
3. **线性评测与 k 近邻**。DINO Table 2 的 ResNet-50 上，OBoW 线性 73.8% 高于 Barlow Twins 的 73.2%，k 近邻却是 61.9% 对 66.0%；SwAV 与 DINO 线性同为 75.3%，k 近邻 65.7% 对 67.5%。有监督 ResNet-50 两种协议都是 79.3%。
4. **分布内与分布外**。CLIP 零样本 ImageNet 76.2%；在同样的 CLIP 特征上用 ImageNet 训练集拟合一个线性头，ImageNet 升到 85.4%，自然分布偏移上的平均表现却略降，其中 ImageNet-R 降 4.7、ObjectNet 降 3.8 个百分点（CLIP §3.3）。

**性质诊断**换一个问法：先构造专门的测试，问表征依赖哪种线索。Geirhos 等（2019，ICLR，University of Tübingen）用风格迁移把一张图的形状和另一张图的纹理合成"线索冲突"图像，让人和 CNN 分类。人类 95.9% 的判断按形状；ImageNet 训练的 ResNet-50 只有 22.1% 按形状（VGG-16 为 17.2%，AlexNet 为 42.9%）。把训练集换成用风格迁移去掉局部纹理线索的 Stylized-ImageNet 后，ResNet-50 按形状的比例升到 81%；与 ImageNet 混合训练的 Shape-ResNet 作为 Faster R-CNN（R-CNN 的后续检测器）主干，VOC2007 检测 mAP50（预测框与真值重叠过半即算检出时的平均精度）从 70.7 升到 75.1，ImageNet-C 平均损坏误差从 76.7 降到 69.3。作者据此认为纹理偏向由 ImageNet 训练数据诱导，而非由 CNN 结构决定。所以表征依赖什么线索，要靠这类专门构造的诊断测试来回答。

benchmark 的替换就是这个方向目标的迁移：MIT 行人库（HOG 近乎完美分离后饱和）→ INRIA 行人库 → PASCAL VOC 检测 → ILSVRC 分类 → COCO 检测、ADE20K 分割等迁移任务 → 30 多个数据集上的零样本（CLIP）→ 冻结特征同时覆盖图像级与像素级任务（DINOv2）。跨论文比较时，骨干与分辨率、预训练数据（是否非公开、是否带文本或标签）、训练计算量和评测协议都要对齐，逐项清单见[视觉基础路线图](../../../docs/roadmaps/visual-baselines.md)第四节。

## 从内部看

结论：视觉模型第一层的权重和注意力图都落在图像空间里，可以直接画出来看，这是视觉相对语言的便利；看到的结构要回到上一节的协议去检验它对下游的用处。探针、因果干预、词表投影这些通用技术见[模型科学](../../../cross-domain/fields/model-science/README.md)，那里的"不同模态的差异"一节对照了视觉与语言。

| 看什么 | 技术 | 视觉中的发现 |
|---|---|---|
| 第一层卷积核 | 把权重直接画成图片 | `[经验]` AlexNet 第一层学到对频率和方向有选择性的核与颜色斑块（§6.1），形状与手工设计的方向滤波器（Gabor 状）相似（[CNN 讲义](../../../foundations/lessons/11-cnn.md)第 9 节）。Zeiler 与 Fergus（2013，NYU）发现 AlexNet 第一层的核集中在极高和极低频、缺少中频，第二层有第一层步长 4 造成的混叠；把第一层改成 7×7 核、步长 2 后，单模型 ImageNet top-5 测试错误率比 AlexNet 低 1.7 个百分点 |
| ViT 切块嵌入 | 对切块投影的滤波器做主成分分析 | 主成分像描述块内细节结构的一组基函数（ViT §4.5、Fig.7） |
| 中间层特征 | 反卷积网络：把某个特征的激活沿网络反向映射回像素空间 | 第 2 层响应角点和边缘与颜色的组合，第 3 层捕捉相似的纹理，第 4 层更偏类别（狗脸、鸟腿），第 5 层是姿态各异的整个物体；小幅平移和缩放对第一层特征影响很大，对顶层影响小（Zeiler 与 Fergus §4） |
| 遮挡敏感性 | 用灰块依次遮住图像各处，看正确类别的概率 | 遮住物体本身时概率显著下降，模型依赖物体的局部结构而不只是场景上下文（Zeiler 与 Fergus §4.2） |
| 注意力图 | 取最后一层 [CLS] 对各图像块的注意力，保留 60% 注意力质量得到掩码，与真值算 Jaccard（交集除以并集） | PASCAL VOC12 上 ViT-S/16：随机权重 22.0，有监督 27.3，DINO 45.9（DINO Fig.4）；附录中 MoCo v2、BYOL、SwAV 训练的 ViT-S 也在 46–48，物体布局是自监督 ViT 共有的性质 |
| 注意力距离 | 按注意力权重平均出的、信息被整合的图像空间距离，作用类似 CNN 的感受野 | ViT 最低层已有一部分头看向图像的大部分区域，另一部分只看邻近区域；前面接 ResNet 的混合模型里局部头较少（ViT §4.5）。高层的头全是全局的；只在 ImageNet 上训练时，低层也学不出局部头（Raghu 等 2021 §5） |
| 层与层的表示相似度 | CKA（中心核对齐：在同一批输入上，分别算两层表示的样本相似度矩阵，再比较这两个矩阵；两层维度可以不同） | Kornblith 等（2019，Google Brain）的检验：10 个结构相同、初始化不同的 CNN，按最大相似度找对应层，线性 CKA 找对 99.3%，CCA 1.4%，SVCCA 最多 15.1%。Raghu 等（2021，Google Research，NeurIPS）用它比较 ViT 与 ResNet：ViT 各层表示更均匀，低层与高层更相似，ResNet 则按阶段分块；ViT 的残差连接影响更大；带 [CLS] 的 ViT 比 ResNet 更好地保留空间位置 |
| 探针 | 冻结某一层，在它上面训练线性分类器 | Raghu 等发现更大的 ViT 需要更大的预训练数据才能得到强的中间层表示；LLaVA 选倒数第二层，是同一思路在下游的应用 |

`[经验]` 这些发现拼出一条与 CNN 讲义一致的层级：早期层处理局部的方向、频率和颜色，越往上越抽象、越不变。ViT 的差别在于局部性要从数据学：数据足够时，一部分低层注意力头学出类似卷积的局部处理。

## 方法谱系

结论：每种方法是"训练信号 × 架构 × 数据"三条轴上的一个点，三条轴可以独立替换，同一个 ViT 可以用标签、遮蔽重建或自蒸馏来训练（[自监督与生成目标](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 5–9 节）。训练信号决定表征偏向上面哪些性质，架构决定先验和可扩展性，数据决定信号能放大到多大。按部件拆分的基线见 [Baseline 页](BASELINES.md)。

**训练信号**

| 训练信号 | 信号从哪里来 | 换来的性质 | 代价 | 代表（架构 × 数据） |
|---|---|---|---|---|
| 有标签监督 | 人工给每张图标一个类别 | 类别语义，线性可分；长期是检测、分割的默认初始化 | 标注随数据量线性增长；只保留预定义类别的信息（DINO 引言：图像级标签把图中丰富的信息归结为几千类中的一个概念）；ImageNet 训练诱导纹理偏向 | AlexNet、VGG、ResNet（CNN × ImageNet）；[ViT](../../papers/vit/README.md)（ViT × JFT-300M）；ConvNeXt（CNN × ImageNet） |
| 对比学习 | 同一张图的两种随机增强为正样本对，其他图为负样本，拉近正样本对 | 对所选增强不变；检测与分割迁移强 | 依赖强数据增强和大批量（SimCLR）或大字典（MoCo）；不变性的种类由人选的增强决定 | MoCo、SimCLR（ResNet × ImageNet）；MoCo v3（ViT × ImageNet） |
| 自蒸馏 | 学生网络去匹配教师网络（学生参数的滑动平均）对同一张图另一裁剪的输出 | 冻结特征的 k 近邻强；注意力显出物体布局；逐块特征可做对应 | 要靠对教师输出做中心化与锐化防止坍缩（所有图输出同一个向量）；小切块更好但更贵：ViT-S/8 每图 785 个 token、约 180 图/秒，ViT-S/16 为 197 个、约 1007 图/秒（DINO Table 1） | [DINO](../../papers/dino/README.md)（ViT 与 ResNet × ImageNet）；DINOv2（ViT × 1.42 亿张筛选过的无标注图像） |
| 遮蔽重建 | 遮住 75% 的图像块，从可见块重建被遮的像素 | 微调和密集任务迁移强；编码器只处理可见块，训练更省 | 线性评测弱于对比学习；遮住的随机块通常不构成语义单元，重建目标是像素而非语义实体（MAE §6） | [MAE](../../papers/mae/README.md)（ViT × ImageNet-1K） |
| 图文对齐 | 网上天然配对的图像与文字，做图文对比 | 与语言共用一个空间，可用类别名零样本分类 | 细粒度分类和计数弱，只能在给定概念中选择（CLIP §6）；DINOv2 认为图文特征抓不住深度这类细微模式 | [CLIP](../../papers/clip/README.md)（ResNet 与 ViT × 4 亿图文对） |

**架构与数据**

| 轴 | 取值 | 带来什么 | 代价 |
|---|---|---|---|
| 架构 | CNN | 局部性与平移等变写在结构里，数据少时有优势 | 全局信息要靠堆深层才能汇集 |
| | ViT | 第一层就能读取全部图像块；与语言模型共用一种结构；可以只编码可见块 | 局部性要从数据中学：只在 ImageNet 上预训练时不如同规模 ResNet，在 JFT-300M 上反超（ViT §4.3） |
| | 混合（ResNet 前端 + Transformer） | 早期的局部处理交给卷积，小计算预算下略好于纯 ViT | 模型变大后优势消失（ViT §4.4） |
| 数据 | ImageNet（约 128 万张训练图，1000 类人工标注） | 公开，是所有方法共用的比较基准 | 规模受人工标注限制 |
| | JFT-300M（3.03 亿张图、1.8 万类，标签带噪声） | 让 ViT 反超 CNN | 非公开，外部团队无法复现同一条件 |
| | 网上图文对（CLIP 自建 4 亿对） | 规模随网络增长，并自带语言接口 | 数据集未声明发布 |
| | 筛选过的无标注图像（DINOv2 的 LVD-142M） | 不需要任何标注或文字 | 筛选以 ImageNet-22k 等已有数据集为检索查询，分布仍由它们锚定 |

## 主线历史

每个节点写成"哪条轴移动了"，并说明上一个节点留下的问题。起点是 2000 年代的手工特征：Dalal 与 Triggs（2005，INRIA）的 HOG（梯度方向直方图：统计局部小格内各方向梯度的强弱）加线性 SVM，以及在 HOG 上搭建的可变形部件模型 DPM（2010）。特征由人设计，只有最后的分类器在学习。HOG 与浅层 CNN 的结构对应见 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节。这条主线也是[深度学习规模化](../../../perspectives/scaling.md)在视觉中的一段。

1. **ImageNet（2009）与 AlexNet（2012）：数据轴与信号轴一起移动**。留下的问题：特征受限于人能设计出什么，可学习的深网络又缺少足够大的标注数据，各团队也缺一个共同比较的 benchmark（HOG 在 MIT 行人库上近乎完美分离后，作者另建了更难的 INRIA 行人库）。改变：Princeton 以 WordNet 的名词概念为骨架建 ImageNet，ILSVRC 每年用约 120 万训练图、1000 类比赛；Toronto 的 AlexNet 用两块 GPU、ReLU、dropout，在 ILSVRC-2012 上 top-5 测试错误率 15.3%，第二名（Fisher 向量手工特征）为 26.2%。ILSVRC 组织者把 2012 年称为转折点，2014 年几乎所有参赛队伍改用 CNN。[判断] 改变局面的是数据、算力和 benchmark，卷积机制在 1998 年的 LeNet 中已经具备。
2. **R-CNN（2013）与 DPM are CNNs（2014），UC Berkeley：使用方式移到"预训练加微调"**。留下的问题：ImageNet 上学到的特征只在分类上得到证明，PASCAL VOC 检测在 2010–2012 年停滞。改变：先在 ILSVRC 分类数据上预训练，再在检测数据上微调，VOC2007 mAP 从 HOG-DPM 的 33.7% 升到 54.2%（其中微调贡献 8.0 个百分点）；同一作者随后证明 DPM 可以逐步展开成 CNN。[判断] 从这里开始，表征的好坏用迁移到下游任务的效果来衡量。
3. **VGG、GoogLeNet（2014）→ ResNet（2015，Microsoft Research）：架构轴在 CNN 内部加深**。留下的问题：主干决定下游的上限，ILSVRC 上的竞争变成怎样做得更深，而更深的网络训练误差反而上升。改变：ResNet 让每段网络只学修正量 F(x)、输出 x + F(x)，ILSVRC 2015 集成模型 top-5 测试错误率 3.57%。更强的主干直接传到下游：R-CNN 把主干从 AlexNet 换成 VGG16，VOC2007 mAP 从 58.5% 升到 66.0%，代价是前向耗时约 7 倍。
4. **MoCo（2019，FAIR）与 SimCLR（2020，Google）：信号轴从人工标签移到图像自身**。留下的问题：主干越做越大，人工标注却不随之增长；语言一侧已靠 GPT、BERT 式自监督预训练摆脱了逐任务标注（见 [LLM 预训练方向](../../../llm/fields/pretraining/README.md)）。改变：对比学习；MoCo 在 7 个检测与分割迁移任务上超过 ImageNet 有监督预训练。评测随之分成线性评测与迁移两种协议，两者给出的排序不同（见[从测量看](#从测量看)）。
5. **ViT（2020，Google）：架构轴从 CNN 移到 Transformer，数据轴移到 JFT-300M**。留下的问题：卷积的局部性与平移等变是必需的先验，还是可以从数据中学出来？改变：把图像切成 16×16 的块当作 token 序列交给 Transformer，只在 ImageNet 上预训练时不如同规模 ResNet，在 JFT-300M 上反超。它留下两个问题：优势要靠非公开的大规模标注换来；它试的遮蔽块预测自监督只到 ImageNet 79.9%，比有监督预训练低 4 个百分点（ViT §4.6）。
6. **CLIP、MAE、DINO（2021）与 ConvNeXt（2022）：对 ViT 的四种回答**。CLIP（OpenAI）同时换掉信号和数据：4 亿对网上图文做对比学习，零样本 ImageNet 76.2%，与原始 ResNet-50 相当而没有用它的 128 万张训练图，评测也移到 30 多个数据集上的零样本。MAE（FAIR）只换信号：遮住 75% 的块再重建像素，只用 ImageNet-1K 就让 ViT-H 微调到 87.8%，此前只用这一数据集的最好结果为 87.1%。DINO（FAIR 与 Inria）问"Transformer 在视觉中的成功有限，是否因为预训练用了监督"，改用自蒸馏，得到 k 近邻 78.3% 和能分出物体的注意力图。ConvNeXt（FAIR 与 UC Berkeley）回头检验架构：只给 ResNet-50 换上 Transformer 式训练配方，ImageNet 精度就从 76.1% 升到 78.8%，再逐步借用 Transformer 的设计后，在相近计算量下全面超过 Swin（一种分层的视觉 Transformer）。[判断] CNN 与 Transformer 在视觉表征上的胜负，很大程度取决于数据规模和训练配方，完整论证见[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)。
7. **DINOv2（2023，Meta AI Research 与 Inria）：数据轴移到筛选过的大规模无标注图像，使用方式移到"冻结即用"**。留下的问题：2021 年的几种信号各在不同协议上领先，下游往往要为每个任务微调或换编码器；DINO 的结论把"在随机、未筛选的图像上预训练大 ViT"列为下一步。改变：DINOv2 发现需要筛选：从 12 亿张网页图中检索出与 ImageNet-22k 等已筛选数据集相近的 1.42 亿张，训练 10 亿参数的 ViT 再蒸馏成小模型。冻结特征在图像级和像素级的多数 benchmark 上超过 OpenCLIP（CLIP 的开源复现），ImageNet 线性评测比此前最好的自监督特征（iBOT ViT-L/16）高 4.2 个百分点。作者把效果归于四个因素：更好的训练配方、更大的模型、更大的数据和蒸馏。

## 趋势

以下四条都是跨论文的 `[判断]`，支撑论文和反例列在批注里。观点层从[观点层索引](../../../perspectives/README.md)链接到这里。

**1. 从追求不变性走向逐像素。** 早期的两种训练信号都在制造不变性：类别标签要求同类图像得到相同输出，对比学习要求一张图的不同增强得到相同特征，评测也以线性评测这类图像级协议为主。之后，评测和使用一步步移到逐像素：R-CNN 把表征用到检测，MoCo、MAE 以 COCO 等检测与分割迁移为主要评价，DINO 展示注意力图能分出物体、逐块特征能做视频对应，DINOv2 直接在冻结的逐块特征上做分割和深度，LLaVA 取网格特征并选保留更多局部细节的倒数第二层。原因在下游：检测、VLM、机器人和生成都需要知道"东西在哪里、长什么样"。Geirhos 等的结果说明，只用 ImageNet 标签追求不变性，网络可以靠纹理这样的捷径达到目标，而形状更强的表征检测也更好。

**2. 与语言对齐。** CLIP 让视觉特征和文本落在同一个空间里，此后它的编码器成为 [VLM](../vlm/README.md)（LLaVA）的视觉输入、文本到图像生成的条件（DALL·E 2）、机器人策略的语义通路（OpenVLA 中的 SigLIP），DINOv2 的作者也把"让语言系统像读词一样读视觉特征"列为下一步。对齐的代价是几何细节：图文对比只用整张图的一个向量，DINOv2 认为图文特征抓不住深度，DALL·E 2 自述 CLIP 嵌入不绑定属性与物体，OpenVLA 因此再拼上 DINOv2 补空间信息。

**3. 从"预训练后逐任务微调"走向"一个冻结编码器服务多个任务"。** R-CNN 时代每个下游任务都微调主干；CLIP 用零样本省掉了下游训练；DINOv2 把目标直接写成无需微调就能跨图像分布、跨任务使用的通用特征，分类、分割、深度都只在冻结特征上训练线性头或解码头。这一趋势在精细控制上遇到边界：OpenVLA 冻结视觉编码器后成功率明显下降，MAE 也论证线性评测会错过非线性的特征。

**4. 训练信号的来源从人转向数据本身，规模由数据收集和筛选决定。** 数据轴依次是人设计的特征（HOG）、人工类别标签（ImageNet，约 128 万张）、带噪声的大规模标签（JFT-300M）、网上天然图文对（CLIP，4 亿对）、无标注但经过筛选的图像（DINOv2，1.42 亿张）。每一步都把"出题的人"往后撤一层，与[深度学习规模化](../../../perspectives/scaling.md)中语言一侧的路线一致。人的作用从标注转到了筛选：DINOv2 用 ImageNet-22k 等人工整理的数据集作检索查询。

由这四条可以得出一个推论：实践中的终点更像"按性质组合多种表征"，而不是找到唯一最好的表征。OpenVLA 拼接语义特征（SigLIP）与空间特征（DINOv2）；文本到图像生成同时使用可重建的潜空间（LDM 的自编码器）和语义条件（CLIP 或文本编码器）。

## 主要路线与团队偏好

- **手工特征加浅层学习**（INRIA 的 HOG；Chicago、Berkeley 一系的 DPM）。押注：人对图像结构的先验（方向梯度、可变形部件）比从数据中学更可靠。代价：特征固定，进展受限于人能设计出什么，PASCAL VOC 上 2010–2012 年的停滞就是表现。[判断] Girshick 所在的一系在 DPM、R-CNN、DPM are CNNs 三篇中始终以 PASCAL VOC 检测为目标、以 DPM 为对照，转向 CNN 时选择证明"旧模型是新模型的特例"，而不是另起炉灶。
- **有监督预训练主干**（Toronto 的 AlexNet，Oxford 的 VGG，Google 的 GoogLeNet 与 ViT，Microsoft Research 的 ResNet）。押注：数据和算力足够时，深网络从像素学到的特征优于手工特征。代价：依赖大规模人工标注，结构选择长期围绕 ILSVRC 分类指标展开；ViT 的关键结论依赖非公开的 JFT-300M，外部团队无法复现同一条件。同一条路线上还有面向端侧的分支：Google 的 MobileNet（深度可分离卷积）与 EfficientNet（按统一系数同时缩放深度、宽度、分辨率），以及 UW 等的 YOLO（单个卷积网络一次完成检测），它们把 CNN 针对延迟和参数量做了系统优化。
- **视觉自监督**（FAIR 的 MoCo、MAE；Google 的 SimCLR；FAIR 与 Inria 的 DINO、DINOv2）。押注：像语言一样让图像自己提供训练信号，方式是对比两种增强视图、重建遮住的块，或匹配教师网络的输出。代价：对比学习依赖强数据增强和大批量（SimCLR）或大字典（MoCo）；MAE 自述遮住的随机块通常不构成语义单元，重建目标是像素而不是语义实体；DINOv2 需要一套检索筛选流程来准备数据。[判断] FAIR 内部两支选择了不同的评测协议，并且各自选的正好是自己方法占优的协议：He、Girshick 一支（MoCo、MAE）都以 NLP 的 GPT、BERT 为参照提出问题，以"迁移到检测、分割和微调时能否超过 ImageNet 有监督预训练"为主要评价，MAE 还明确批评线性评测；Bojanowski、Joulin、Jégou、Misra、Mairal 同时署名的 DINO 与 DINOv2，以冻结特征的 k 近邻和线性评测为主，DINOv2 把目标定为无需微调的通用特征。MoCo 结论中建议的下一步"遮蔽自编码"由 MAE 实现，DINO 结论中的"更大规模的无筛选预训练"由 DINOv2 实现（改成了筛选数据）。
- **图文弱监督**（OpenAI 的 [CLIP](../../papers/clip/README.md)）。押注：网上天然配对的图文比固定类别的标注更可扩展，并且直接得到一个用语言指定类别的接口。代价：CLIP 自述零样本只能在给定的概念中选择，细粒度分类和计数较弱，并估计还要约 1000 倍算力才能在零样本上整体达到最优。它的图像编码器后来成为[视觉语言模型](../vlm/README.md)和[图文对齐](../alignment/README.md)的常用起点。
- **表征分析**（Google Brain 与 Google Research：Kornblith 等 2019 的 CKA，Raghu 等 2021 的 ViT 与 CNN 比较）。押注：用一个对层宽度和随机初始化都稳健的相似度指标，量化比较不同层、不同架构学到的表示。代价：Raghu 等自述 CKA 把比较压缩成一个标量，更细粒度的方法可能看到更多差异。[判断] Kornblith 同时署名两篇，后一篇的作者还包括 ViT 第一作者 Dosovitskiy：同一团队先提出度量，再用它分析自己提出的架构。

## 当前开放问题

- **架构的差别与数据、训练配方、计算量怎样分开？** ViT 与 ConvNeXt 两组结果都说明，主干之争必须和数据规模、训练配方一起看。入口：[ViT 精读](../../papers/vit/reading.md)、[ConvNeXt 原文](https://arxiv.org/abs/2201.03545)、[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)。
- **哪种训练信号最适合哪类下游，一个编码器能否兼顾？** 遮蔽重建、对比学习、自蒸馏和图文对比在线性评测、微调、检索、局部对应上各有长处；DINOv2 押注单个冻结编码器，OpenVLA 选择拼接两个。入口：[MAE 精读](../../papers/mae/reading.md)、[DINO 精读](../../papers/dino/reading.md)、[CLIP 精读](../../papers/clip/reading.md)、[DINOv2 原文](https://arxiv.org/abs/2304.07193)。
- **网上预训练的视觉特征够不够支撑机器人？** OpenVLA 的消融中，冻结视觉编码器使成功率从约 70% 降到 47%（较小的 SigLIP-only 变体上的结果）；世界模型一侧则在比较以重建为目标和以语义为目标的潜空间。入口：[OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)、[DINO-WM](../../papers/arxiv-2411.04983/README.md)、[Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](../../papers/arxiv-2605.06388/README.md)，以及[世界模型方向](../world-models/README.md)。
- **视觉模型内部的机制能否推进到干预层面？** 视觉一侧的证据目前以可视化、注意力距离、CKA 和探针为主，语言一侧已经能定位并编辑事实所在的 MLP。ViT 的 MLP 能否读成键值记忆、视觉中有没有可干预的电路，入口见[模型科学](../../../cross-domain/fields/model-science/README.md)的"不同模态的差异"与开放问题两节。

## 阅读顺序

1. [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节：主线前三个节点的机制版本，先弄清卷积、残差和"预训练主干迁移"各自解决了什么。
2. [ViT 精读](../../papers/vit/README.md)：主干从卷积转向 Transformer 的节点，也是"归纳偏置与数据规模"这一问题的起点；建议手算一次 token 数 N = HW/P²。
3. [MAE 精读](../../papers/mae/README.md)：在同一个 ViT 上换成遮蔽重建，看为什么只编码可见块反而更好、为什么线性评测和微调会给出不同排序。
4. [DINO 精读](../../papers/dino/README.md)：把固定的像素目标换成动态的教师输出，与 MAE 对照阅读，重点看 k 近邻与注意力图两类证据。
5. [CLIP 精读](../../papers/clip/README.md)：从单模态转到图文配对，理解零样本分类怎样由文本编码器生成分类权重。
6. [模型科学](../../../cross-domain/fields/model-science/README.md)的"不同模态的差异"一节：把"从内部看"放回视觉与语言的对照中。

读完 2–4 篇后可以做一个检验：把同一张图切成块，分别写出监督分类、MAE、DINO 三种目标要求模型预测什么、哪些分支参与梯度更新。按问题组织的阅读步骤见[路线图](ROADMAP.md)，四篇的横向对照表在[视觉基础路线图](../../../docs/roadmaps/visual-baselines.md)，本方向收录的全部论文见[论文目录](PAPERS.md)。

## 批注

**易误读**

- AlexNet 的 15.3% 对 26.2%，比较的是 ILSVRC-2012 测试集 top-5 错误率；AlexNet 的这个数字来自多个 CNN 的平均，其中两个用了额外的 ImageNet Fall 2011 数据预训练（AlexNet 第 6 节）。
- ViT 在 ImageNet-1k 上不如 ResNet、在 JFT-300M 上反超，比较对象是同等规模的 BiT ResNet，并且都经过迁移微调（ViT 4.3 节、Fig.3）。JFT-300M 的"标签带噪声"出自 Sun 等 2017 的摘要（3 亿张图、3.75 亿个有噪声的标签）；ViT §4.1 只写了 1.8 万类、3.03 亿张图。
- SimCLR 的 76.5% 用的是 4 倍宽的 ResNet-50；标准宽度时自监督为 69.3%，同结构有监督为 76.3%（SimCLR 附录 B.8）。MoCo 的线性评测为 60.6%，"超过有监督预训练"只指 7 个检测/分割迁移任务（MoCo 4.2 节）。
- MAE 的 87.8% 是 ViT-H 在 448 分辨率下微调的结果，224 分辨率为 86.9%（MAE 4.2 节、Table 3）。MAE 线性评测有两个数：73.5% 是 Table 1 默认消融设置（800 epoch）下的 ViT-L，75.8% 是附录 B 的最终设置；与 MoCo v3 的 77.6% 对比时，"微调最后 4 块领先 2.6 个百分点"用的是前一个设置（MAE §4.3、附录 B）。
- CLIP 的零样本 ImageNet 76.2% 的比较对象是原始的有监督 ResNet-50（CLIP 3.1 节、Table 1）；85.4% 是在同一 CLIP 特征上用 ImageNet 训练集拟合线性头的结果，属于线性评测，不能当作零样本成绩（CLIP §3.3、附录 A.3）。
- DINO 的 Jaccard 有两套阈值：正文 Fig.4 保留 60% 注意力质量，图中展示的是各模型最好的头；附录 D 比较 MoCo v2、BYOL、SwAV 时文字写的是 80%，表中又重复了正文的数值。本页只把附录数值用来说明"自监督方法都有这一性质"，不与正文数值排名。
- Geirhos 等的形状偏好是在 16 个 ImageNet 大类的线索冲突图像上测的，只统计判对形状或纹理之一的试次；检测提升（70.7 → 75.1）用的是 Stylized-ImageNet 与 ImageNet 联合训练、再在 ImageNet 上微调的 Shape-ResNet，单独在 Stylized-ImageNet 上训练的模型 ImageNet 精度更低（Geirhos §3.2–3.3、Table 2）。
- Kornblith 等的 99.3% 是 CIFAR-10 上 10 个 10 层 CNN 的对应层识别准确率；同一检验用在 Transformer 编码器上时，所有指标都通过（Kornblith §6.1、附录 F.1）。
- 特征可视化（例如 DINO 的注意力图）好看，不等于所有下游任务都更好；不同评测协议要分开报告。
- R-CNN 换成 VGG16 的 66.0% 出自 2014 年 10 月的 arXiv v5（第 3.3 节；该版说明称新增了更深网络的结果），晚于 2013 年 11 月的初版，用来说明"主干变强会传到下游"。
- ILSVRC 测的是 1000 类单标签分类；组织者自己记录了外界的批评：数据集不够难、细粒度类别有标注错误、外部数据规则太严（ILSVRC 综述 Sec.7.2）。CLIP 自述的口径问题是：开发中反复查看完整验证集，主结果所用的 27 个数据集与 CLIP 的开发共同演化（CLIP Sec.6）。

**判断的支撑论文**（各行见 [synthesis.csv](synthesis.csv)）

- "各任务要求的性质互相拉扯"：LLaVA §5.2 Table 8（最后一层与倒数第二层）；DINOv2 §7.4（图文特征的深度估计较弱）；DALL·E 2 Sec.7 与 LDM（见[视觉生成方向](../generation/README.md)）；OpenVLA Table 1。反例：DINOv2 用一个冻结编码器在分类、分割、深度上都超过 OpenCLIP，说明拉扯可以靠规模和数据部分化解。
- "改变局面的是数据、算力和 benchmark"：AlexNet Sec.1、ILSVRC 综述 Sec.5.1。
- "表征好坏开始用迁移效果衡量"：R-CNN Sec.1；MoCo Sec.1 把 ImageNet 有监督预训练作为要替代的对照。边界：MoCo、MAE 在检测与分割迁移上超过了 ImageNet 有监督预训练（MoCo Sec.4.2、MAE Sec.5），这个默认起点此后开始被自监督预训练替代。
- "胜负取决于数据规模和训练配方"：ViT Sec.4.3–4.4、ConvNeXt Sec.2.1 与 Sec.3；反向证据是 CLIP Sec.3.2 中 ViT 图像编码器的计算效率约为 ResNet 的 3 倍。
- 趋势 1（走向逐像素）：R-CNN；MoCo Sec.4.2；MAE Sec.5、附录 A.3–A.4；DINO Fig.4、Table 5；DINOv2 Sec.7.4；LLaVA §4.1；Geirhos Table 2。反例：CLIP 的训练目标只用全局向量，却仍是 VLM 最常用的视觉输入之一。
- 趋势 2（与语言对齐）：CLIP；LLaVA §4.1；DALL·E 2；OpenVLA Sec.3.1；DINOv2 Sec.10（未来工作）。反例与边界：DINOv2 §7.4 中 iBOT ViT-L 的深度估计好于 OpenCLIP ViT-G；OpenVLA 额外拼接 DINOv2。
- 趋势 3（冻结即用）：CLIP Sec.3.1；DINOv2 摘要与 Sec.7。反例：OpenVLA Table 1（冻结视觉 47.0%，全参数微调 69.7%）；MAE §4.3；DINOv2 自己也在 Sec.7.1 检验了微调。
- 趋势 4（信号来源从人转向数据）：ImageNet、ViT §4.1、CLIP Sec.2.2、DINOv2 Sec.3。反例：DINOv2 的筛选以 ImageNet-22k、ImageNet-1k、Google Landmarks 和若干细粒度数据集为查询，人工整理的数据仍决定分布。
- Girshick 一系的偏好：DPM（PAMI 2010）Sec.8、R-CNN Table 1–2、DPM are CNNs Table 1，三篇都以 PASCAL VOC 为目标、以 DPM 为对照。
- FAIR 两支自监督的协议偏好：MoCo Sec.1、Sec.4.2、Sec.5；MAE Sec.1、§4.3、Sec.5；DINO Sec.1、Table 2、Sec.6；DINOv2 摘要、Sec.7.1。边界：DINO 也报告了迁移微调（Table 6），MAE 也报告了线性评测（附录 B），偏好指的是主要论据放在哪个协议上；同属 FAIR 的 ConvNeXt 转而检验有监督 CNN 的上限。
- 表征分析团队：Kornblith 2019 与 Raghu 2021 的作者列表。只有两篇，证据偏弱。

**与其他论文的关联**

- [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节与本页主线前三个节点一致，讲的是机制；本页补上了团队、benchmark 与评测协议。两处如有出入，以 [synthesis.csv](synthesis.csv) 中的原文出处为准修改。
- 第一层 Gabor 状卷积核与 ViT 注意力距离，在[模型科学](../../../cross-domain/fields/model-science/README.md)中被放进"早期层在做什么"的跨模态对照；语言一侧的对应证据是 FFN 键值记忆的低层浅层模式（见[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)）。
- U-Net（2015，Freiburg）的编码–解码结构后来成为扩散模型的去噪主干，见[视觉生成方向](../generation/README.md)；ViT 的切块思路被 DiT 用到图像生成里。
- CLIP 的图像编码器是 [LLaVA](../../papers/llava/README.md) 等视觉语言模型的视觉输入端，也是 DALL·E 2 生成图像时的条件（见[视觉生成方向](../generation/README.md)）；SigLIP 与 DINOv2 分别延续 CLIP 与 DINO 两条路线，在 [OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 中拼接使用。
- MoCo、MAE、DINO 都以 BERT、GPT 为参照提出问题，语言一侧的对应历史见 [LLM 预训练方向](../../../llm/fields/pretraining/README.md)；训练配方与规模定律见[训练科学](../../../cross-domain/fields/training-science/README.md)。
- MobileNet、EfficientNet、YOLO 都早于 ViT，没有与视觉 Transformer 做同条件对比；"CNN 在端侧仍占优"的讨论放在[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)。

**未核实 / 待验证**

- LeNet（LeCun 等 1998）全文没能打开，[synthesis.csv](synthesis.csv) 中该行除题录外都标为未核实；主线开头关于 LeNet 的一句沿用 CNN 讲义的写法。
- "从任务看"一表中世界模型一行所链的 DINO-WM、Back to the Features 两张文献卡目前只有题录，本页只引用其标题所述的做法；"开放问题"第三条所链的 Reconstruction or Semantics? 同样只引用标题提出的问题。
- Zeiler 与 Fergus 一般引作 ECCV 2014，本页只核对了 arXiv 版（2013 年 11 月）；Raghu 等的 NeurIPS 2021 出处来自论文首页脚注与 NeurIPS 论文集页面。
- MoCo v3 的 77.6% 与 84.1% 转引自 MAE 原文（Fig.9、附录 B、Table 3），没有另查 MoCo v3 原文。
- DINOv2 的 LVD-142M 数据是否发布，论文未声明；MobileNet 论文只写了"计划发布模型"，MAE 论文正文未声明代码发布，实际发布情况没有另查。
- ImageNet-R、ObjectNet 只按 CLIP §3.3 的结果引用，两个数据集的构造方式没有打开原文核对。
