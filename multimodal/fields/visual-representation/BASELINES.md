# 视觉表征的基线

> 状态：Baseline 页 · v2 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 基线是谁、为什么是它

结论：视觉表征的基线不是单个模型，而是"主干 + 训练信号 + 评测协议"的组合。本方向先后有三个基线：ImageNet 有监督 ResNet-50 定义了 2015–2021 年的对照与迁移协议；ViT-B/L 加 ImageNet-1K 定义了 2021 年起"同一骨干上比训练信号"的实验骨架；CLIP 与 DINOv2 两种冻结的大编码器定义了 2023 年以后"一个编码器服务多个任务"的对照。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| ImageNet 有监督 ResNet-50（[ResNet](../../papers/arxiv-1512.03385/README.md)，2015，Microsoft Research） | 接口：一张 224×224 的图 → 多个阶段的特征图（步长 4 到 32）与一个全局向量。训练：ImageNet-1K 的 1000 类交叉熵。评测：ImageNet top-1；作为初始化迁移到 PASCAL VOC、COCO 的检测与分割，全量微调 | MoCo 以"超过 ImageNet 有监督预训练"作为检测迁移的目标（MoCo §4.2）；SimCLR 附录 B.8 与 DINO Table 2 都把同结构的有监督 ResNet-50 放在对照第一行；ConvNeXt 从它出发检验训练配方 |
| ViT-B/16、ViT-L/16 + ImageNet-1K（[ViT](../../papers/vit/README.md) 的结构，[DeiT](../../papers/arxiv-2012.12877/README.md) 的只用 ImageNet 的配方） | 接口：224×224 的图切成 14×14 = 196 个 16×16 的块，加一个 [CLS]，输出 197 个向量。训练信号可换：标签、对比、自蒸馏、遮蔽预测。评测：线性评测与全量微调两套数字都报 | [BEiT](../../papers/arxiv-2106.08254/README.md) Table 1、[MAE](../../papers/mae/README.md) Table 3、[I-JEPA](../../papers/arxiv-2301.08243/README.md) Table 1 都在这两个尺寸上、只用 ImageNet-1K 对比各种信号；DeiT-B 的 81.8% 是同结构有监督训练的参照 |
| 冻结的大编码器：[CLIP](../../papers/clip/README.md) ViT-L/14（2021，OpenAI，图文对比）与 [DINOv2](../../papers/arxiv-2304.07193/README.md) ViT-g/14（2023，Meta，自蒸馏） | 接口：主干冻结，输出全局向量与逐块特征网格；下游只训线性头、解码头或适配器。评测：同一套冻结特征同时测分类、分割、深度、检索，以及作为视觉语言模型（VLM）视觉塔的问答 | [Registers](../../papers/arxiv-2309.16588/README.md) 在 DINOv2 与 OpenCLIP 上找伪影；[Web-SSL](../../papers/arxiv-2504.01017/README.md) 在同一份数据上对照 CLIP 与 DINOv2 式模型；[Perception Encoder](../../papers/arxiv-2504.13181/README.md) 的逐层分析以 DINOv2 为空间任务一端的参照；[DINOv3](../../papers/arxiv-2508.10104/README.md) Table 7 对照 DINOv2、SigLIP 2、PEcore；[MMVP](../../papers/arxiv-2401.06209/README.md) 用 CLIP 与 DINOv2 的相似度之差出题 |

三个基线之前有一个原点：[HOG](../../papers/hog/README.md)（2005，INRIA）的"人设计的特征 + 线性 SVM"。[判断] 后来的线性评测协议保留了这个形式，只是把特征换成学到的；有标签监督的 [AlexNet](../../papers/alexnet/README.md)（2012）第一次让"特征也由数据学出"在 ILSVRC 上胜出。

第三个基线到 2026 年仍是参照：NVIDIA 2026 年 1 月的 [C-RADIOv4](https://arxiv.org/abs/2601.17237) 直接以 SigLIP 2、DINOv3、SAM 3 三个编码器为教师做多教师蒸馏；Meta 2026 年 3 月的 [V-JEPA 2.1](https://arxiv.org/abs/2603.14482) 在冻结评测中以 DINOv3 为图像与密集任务的对照。

## 基线的结构拆分

结论：一个视觉表征方法可以拆成五个可替换的部件。[入门页](README.md)的方法谱系用"训练信号 × 架构 × 数据"三条轴；本页再单独拆出两个部件："训练配方"和"读出接口"。DeiT、AugReg、ConvNeXt 说明，信号、架构、数据都不变，只改配方，结果能相差几个百分点；Perception Encoder 与 LLaVA 说明，同一个编码器，取哪一层、是否再对齐，下游表现差别很大。

| 部件 | 含义 | 有监督 ResNet-50 | ViT + ImageNet-1K | 冻结大编码器（CLIP / DINOv2） |
|---|---|---|---|---|
| 训练信号 | 损失从哪里来，决定表征偏向哪些性质 | 1000 类交叉熵 | 本基线的变量：标签、对比、自蒸馏、遮蔽预测 | CLIP：图文批内对比；DINOv2：图像级自蒸馏 + iBOT 块级遮蔽目标 + KoLeo 正则 |
| 架构 | 先验与可扩展性 | 卷积，4 个阶段 | ViT-B/16（86M 参数）或 ViT-L/16（307M） | CLIP ViT-L/14；DINOv2 ViT-g/14（约 10 亿参数） |
| 数据 | 用哪些图，是否带标签或文字 | ImageNet-1K，约 128 万张 | 同一批 ImageNet-1K 图像（自监督时不用标签） | CLIP 自建 4 亿图文对；DINOv2 的 LVD-142M（从 12 亿张网页图中检索筛选） |
| 训练配方 | 增强、正则、优化器、训练长度、分辨率、蒸馏 | ResNet 原文式的 SGD 配方；ConvNeXt 换成 300 epoch、AdamW、Mixup/CutMix 等后从 76.1% 升到 78.8% | DeiT 配方：300 epoch、AdamW、RandAugment、Mixup、CutMix、随机擦除、随机深度、重复增强 | DINOv2：大模型训练后蒸馏出小模型，最后一段用 416 分辨率 |
| 读出接口 | 下游从哪一层、以什么方式取特征 | 全局池化向量，或多阶段特征图接 FPN（特征金字塔），通常全量微调 | [CLS] 向量做线性评测，或全量微调 | 冻结；全局向量 + 逐块网格；[LLaVA](../../papers/llava/README.md) 取 CLIP 倒数第二层的网格特征 |

部件之间有依赖。训练信号决定读出接口能取到什么：图像级目标（标签、对比、DINO）的信息集中在 [CLS] 上，线性评测好；逐块目标（BEiT、MAE）的信息分散在各块，要微调才能发挥（BEiT-B 线性 56.7%、微调 83.2%）。架构决定配方的敏感度：ViT 缺少卷积的先验，去掉随机擦除或随机深度，DeiT 就训练不收敛。数据和模型规模会改变信号的副作用：DINO 的图像级目标在 ViT-B 以下看不出问题，到 ViT-L 以上、训练更久时出现高范数伪影（Registers）和密集特征退化（DINOv3）。下表按部件分行，同一篇论文改了几个部件，就在几行出现。

## 后续工作在改哪个部件

没有单篇目录的论文链接到原文，数字取自 [synthesis.csv](synthesis.csv) 对应行。

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 原点 | 梯度方向直方图 + 线性 SVM | [HOG](../../papers/hog/README.md) | 误检率比 Haar 小波检测器低一个数量级以上，MIT 行人库近乎完美分离；代价：特征固定，只有分类器在学 |
| 原点 | 在 HOG 上加可变形部件与 latent SVM（DPM） | [DPM](https://cs.brown.edu/people/pfelzens/papers/lsvm-pami.pdf) | VOC2008 的 20 类中 9 类第一；代价：VOC 检测在 2010–2012 年停滞，VOC2007 上 HOG-DPM 为 33.7% |
| 原点之前 | 交替的特征提取层与池化层；卷积加梯度训练 | [Neocognitron](https://www.cs.princeton.edu/courses/archive/spr08/cos598B/Readings/Fukushima1980.pdf)、[LeNet](https://leon.bottou.org/papers/lecun-98h) | 卷积与层级结构已经具备；代价：Neocognitron 十类图案时对参数非常敏感，缺少大规模数据与算力（LeNet 原文未核实） |
| 训练信号 | 1000 类人工标签，端到端训练深层 CNN | [AlexNet](../../papers/alexnet/README.md) | ILSVRC-2012 top-5 15.3% 对第二名 26.2%；代价：依赖人工标注；ImageNet 标签会诱导纹理偏向（[Geirhos 等](https://arxiv.org/abs/1811.12231)：ResNet-50 只有 22.1% 的判断按形状，人类 95.9%） |
| 训练信号 | 对比学习：队列字典 + 动量编码器 | [MoCo](../../papers/arxiv-1911.05722/README.md) | 7 个检测与分割迁移任务超过 ImageNet 有监督预训练；代价：ResNet-50 线性评测只有 60.6% |
| 训练信号 | 对比学习：批内负样本 + 非线性投影头 + 强增强 | [SimCLR](../../papers/arxiv-2002.05709/README.md) | 4 倍宽 ResNet-50 线性 76.5%，与有监督相当；代价：批 4096–8192；标准宽度 69.3% 对有监督 76.3% |
| 训练信号 | 遮蔽约 40% 的块，预测 DALL·E 分词器给出的离散视觉 token | [BEiT](../../papers/arxiv-2106.08254/README.md) | 只用 ImageNet-1K，ViT-L 微调 85.2%；代价：多一个外部分词器；ViT-B 线性只有 56.7% |
| 训练信号 | 遮蔽 75% 的块重建像素，编码器只处理可见块 | [MAE](../../papers/mae/README.md) | ViT-H 微调 87.8%（448 分辨率）；代价：线性评测弱于对比学习，随机块通常不构成语义单元 |
| 训练信号 | 自蒸馏：学生匹配动量教师对另一裁剪的输出 | [DINO](../../papers/dino/README.md) | ViT-S/8 k 近邻 78.3%，注意力图 Jaccard 45.9（有监督 27.3）；代价：靠中心化与锐化防坍缩；8×8 切块吞吐约为 16×16 的 1/5.6 |
| 训练信号 | 在表示空间里从上下文块预测目标块的表示，不用视图增强 | [I-JEPA](../../papers/arxiv-2301.08243/README.md) | ViT-H/14 线性 79.3%（MAE 77.2%），Clevr 距离 72.4（DINO 53.4）；代价：每次迭代比 MAE 慢约 7%，计数 86.7 低于 MAE 的 90.5 |
| 训练信号 | 自蒸馏 + iBOT 块级遮蔽目标 + Sinkhorn-Knopp 中心化 + KoLeo | [DINOv2](../../papers/arxiv-2304.07193/README.md) | 冻结线性比 iBOT ViT-L 高 4.2 个百分点，略高于 OpenCLIP ViT-G；代价：大模型出现高范数伪影 token |
| 训练信号 | 自蒸馏 + Gram anchoring（块特征相似度矩阵贴近早期教师） | [DINOv3](../../papers/arxiv-2508.10104/README.md) | 修复约 20 万次迭代后的密集特征退化，冻结主干 ADE20k 63.0 mIoU；代价：文字类分类弱于 PEcore（GTSRB 87.5% 对 94.8%） |
| 训练信号 | 网上图文对的批内对比 | [CLIP](../../papers/clip/README.md)、[ALIGN](../../papers/arxiv-2102.05918/README.md) | 零样本 ImageNet 76.2%（ALIGN 76.4%）；代价：细粒度分类与计数弱，只能在给定概念中选 |
| 训练信号 | 逐对 sigmoid 代替批级 softmax | [SigLIP](../../papers/arxiv-2303.15343/README.md) | 批小于 16k 时明显更好；代价：批加到 32k 左右两种损失都饱和 |
| 训练信号 | sigmoid 对比 + 描述与定位解码 + 自蒸馏与遮蔽预测 | [SigLIP 2](../../papers/arxiv-2502.14786/README.md) | So400m/14 零样本 83.2% → 84.1%，多语言检索 26.6 → 57.5；代价：NaFlex 变体外推不好 |
| 训练信号（视频） | 管道遮蔽 90%–95% 后重建像素 | [VideoMAE](../../papers/arxiv-2203.12602/README.md) | SSv2 69.6%（从零训练 32.6%）；代价：Kinetics 上时间建模作用不明显 |
| 训练信号（视频） | 遮掉大块时空区域，在特征空间预测 | [V-JEPA](../../papers/arxiv-2404.08471/README.md) | 冻结评测 SSv2 71.4%（DINOv2 50.6%）；代价：外观为主的 K400 上 82.0% 低于 DINOv2 的 83.4% |
| 训练信号（图像与视频） | 可见块与被遮块都计入的密集预测损失，在多个中间层加自监督，图像与视频统一训练 | [V-JEPA 2.1](https://arxiv.org/abs/2603.14482)（2026） | 冻结 ADE20K 从 V-JEPA 2 的 24.4 升到 47.9，NYUv2 线性深度 RMSE 0.307（DINOv3 0.309），SSv2 77.7%（DINOv3 71.1%）；代价：ADE20K 与 ImageNet（85.5% 对 88.1%）仍低于 DINOv3 |
| 训练信号 | 多教师蒸馏：同时模仿图文、自监督、分割三类编码器 | [C-RADIOv4](https://arxiv.org/abs/2601.17237)（2026） | 412M 与 631M 两个尺寸，以 SigLIP 2、DINOv3、SAM 3 为教师，密集任务上与 DINOv3-7B 有竞争力；代价：进步要靠教师更新（作者自述"更好的教师带来更好的学生"），SAM 3 当教师在所选 benchmark 上没有带来提升 |
| 架构 | 全部用 3×3 卷积，堆到 16–19 层 | [VGG](https://arxiv.org/abs/1409.1556) | 单网络 top-5 7.0%；R-CNN 换成 VGG16 后 VOC2007 58.5% → 66.0%；代价：前向耗时约 7 倍 |
| 架构 | 多分支 Inception 模块，22 层 | [GoogLeNet](https://arxiv.org/abs/1409.4842) | ILSVRC 2014 top-5 6.67%，第一；代价：作者自述设计原则是否真起作用仍需分析 |
| 架构 | 残差连接 x + F(x) | [ResNet](../../papers/arxiv-1512.03385/README.md) | 34 层 top-1 从普通网络的 28.54% 降到 25.03%，152 层集成 3.57%；代价：1202 层比 110 层差（过拟合） |
| 架构 | 编码–解码 + 跨层拼接 | [U-Net](https://arxiv.org/abs/1505.04597) | ISBI 细胞追踪 IOU 92%（第二名 83%）；后来成为扩散模型的去噪主干（见[视觉生成方向](../generation/README.md)） |
| 架构 | 面向端侧：深度可分离卷积、复合缩放、单网络检测 | [MobileNets](https://arxiv.org/abs/1704.04861)、[EfficientNet](https://arxiv.org/abs/1905.11946)、[YOLO](../../../robotics-embodied/papers/arxiv-1506.02640/README.md) | MobileNet 精度与 VGG16 相近、参数少 32 倍；EfficientNet-B7 84.3%，比 GPipe 小 8.4 倍；YOLO 45 FPS、VOC2007 63.4%；代价：都早于 ViT，没有同条件比较 |
| 架构 | 图像切成 16×16 的块交给 Transformer | [ViT](../../papers/vit/README.md) | 在 JFT-300M 上反超同规模 BiT ResNet；代价：只用 ImageNet 时不如 ResNet；遮蔽块预测自监督只到 79.9% |
| 架构 | 输入序列加 4 个不对应图块的寄存器 token | [Registers](../../papers/arxiv-2309.16588/README.md) | 消除约 2% 的高范数伪影 token，LOST 物体发现 35.3 → 55.4；代价：计算量增加不到 2% |
| 架构 | 按 Transformer 的设计逐步现代化 ResNet | [ConvNeXt](https://arxiv.org/abs/2201.03545) | 相近复杂度下 ImageNet、COCO、ADE20K 持平或超过 Swin；代价：深度卷积在同 FLOPs 下的速度与显存问题 |
| 数据 | 以 WordNet 为骨架的百万级标注图像 + 年度竞赛 | [ImageNet](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf)、[ILSVRC 综述](https://arxiv.org/abs/1409.0575) | 第一个所有团队共用的大规模 benchmark，2014 年几乎所有参赛队伍改用 CNN；代价：单标签 1000 类，外界批评不够难、细粒度类别有标注错误 |
| 数据 | 3 亿张带噪声标签的非公开图像（JFT-300M） | [ViT](../../papers/vit/README.md) | 让 ViT 反超 CNN；代价：外部团队无法复现同一条件 |
| 数据 | 公开的 ImageNet-21K + 更强的增强与正则 | [AugReg](../../papers/arxiv-2106.10270/README.md) | 追平或超过 JFT-300M 上的同规模 ViT，相当于数据扩大 10 倍；代价：所需计算差不多 |
| 数据 | 网上图文对：CLIP 自建 4 亿对；ALIGN 18 亿对只做词频过滤 | [CLIP](../../papers/clip/README.md)、[ALIGN](../../papers/arxiv-2102.05918/README.md) | 规模随网络增长并自带语言接口；ALIGN 中 300 万对时噪声数据差于清洗数据，1200 万对时反超；代价：数据集未发布 |
| 数据 | 以已整理的数据集为查询，从 12 亿张中检索出 1.42 亿张 | [DINOv2](../../papers/arxiv-2304.07193/README.md) | 同样迭代数下 iNaturalist 线性 68.0 → 82.3；代价：分布由查询数据集锚定，ADE20k 上未筛选数据反而略高（48.5 对 47.7） |
| 数据 | 约 170 亿张图分层聚类后平衡采样 16.89 亿张 | [DINOv3](../../papers/arxiv-2508.10104/README.md) | 支撑 7B 模型的训练；代价：低收入组比最高收入组低 23% |
| 数据 | 与 CLIP 同一份 20 亿图像，按含文字比例过滤 | [Web-SSL](../../papers/arxiv-2504.01017/README.md) | 自监督到 7B 未饱和，CLIP 约 3B 后饱和；只用 1.3% 的文档图表类图像，OCR 与图表问答反超全量 CLIP 4.3 个百分点；代价：没有零样本分类 |
| 数据 | 54 亿对公开图文 + 视频数据引擎合成的描述 | [Perception Encoder](../../papers/arxiv-2504.13181/README.md) | 零样本 ImageNet 鲁棒性平均 86.6、Kinetics-400 76.9 |
| 训练配方 | 只用 ImageNet 的强增强与正则 + 向 CNN 教师学习的蒸馏 token | [DeiT](../../papers/arxiv-2012.12877/README.md) | DeiT-B 81.8%，蒸馏后 85.2% 超过 JFT 预训练的 ViT-B（84.15%）；代价：配方极敏感，换 SGD 降到 74.5% |
| 训练配方 | 系统扫描增强与正则 × 数据量 × 计算 | [AugReg](../../papers/arxiv-2106.10270/README.md) | 发布 5 万多个模型；增强比正则更常有用；代价：没有简单规则，小模型或短训练时加 AugReg 反而有害 |
| 训练配方 | 给 ResNet-50 换上 Transformer 式配方 | [ConvNeXt](https://arxiv.org/abs/2201.03545) | 76.1% → 78.8%，结构不变 |
| 训练配方 | 大模型训练后蒸馏成小模型；高分辨率收尾 | [DINOv2](../../papers/arxiv-2304.07193/README.md)、[DINOv3](../../papers/arxiv-2508.10104/README.md) | 一个旗舰模型派生出一族部署用的小模型；代价：DINOv2 的 416 分辨率阶段约为 224 的 3 倍计算 |
| 训练配方 | 强化纯对比配方：渐进分辨率、LAMB、RoPE、注意力池化等 | [Perception Encoder](../../papers/arxiv-2504.13181/README.md) | 冻结特征 COCO 检测的最好层比原始 CLIP 高近 10 mAP；代价：渐进分辨率与注意力池化把最好的层推向网络深处，最后一层仍需对齐 |
| 读出接口 | ImageNet 预训练后在检测数据上微调整个主干 | [R-CNN](https://arxiv.org/abs/1311.2524)、[DPM are CNNs](https://arxiv.org/abs/1409.5403) | VOC2007 从 HOG-DPM 的 33.7% 升到 54.2%，其中微调贡献 8.0 个百分点；代价：每张图约 13 秒 |
| 读出接口 | 冻结 CLIP，取倒数第二层网格特征，经线性投影接语言模型 | [LLaVA](../../papers/llava/README.md) | ScienceQA 上比取最后一层高约 1 个百分点（90.92% 对 89.96%） |
| 读出接口 | 取中间层，再做语言对齐或空间对齐 | [Perception Encoder](../../papers/arxiv-2504.13181/README.md) | PElang 取第 47 层（共 50 层），DocVQA 94.6；PEspatial 对齐第 41 层与 SAM 2.1，COCO 66.0 box mAP |
| 读出接口 | 把图像压成可变长度的 1D token 序列，按需取前若干个 | [RADIO1D](https://arxiv.org/abs/2607.03624)（2026） | 接 9B 语言模型时，10 项 VLM benchmark 平均从 1 个 token 的 51.5 到 256 个 token 的 73.3，可按延迟取舍；出发点是 VLM 训练会让视觉特征越来越抽象、空间一致性下降 |
| 读出接口 | 两种编码器拼接，并随策略全量微调 | [OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) | 语义（SigLIP）与空间（DINOv2）兼得；冻结视觉 47.0% 对全量微调 69.7%（较小的 SigLIP-only 变体） |
| 读出接口 | 冻结 DINO 特征作为世界模型的状态空间 | [DINO-WM](../../papers/arxiv-2411.04983/README.md)、[Back to the Features](../../papers/arxiv-2507.19468/README.md)、[Reconstruction or Semantics?](../../papers/arxiv-2605.06388/README.md) | DINO-WM 在 Push-T 成功率 0.90（离线训练的 DreamerV3 0.30）；语义型潜空间在规划与策略上普遍好于重建型；代价：需要动作标注，只在少数简单环境验证 |
| 评测协议 | 以视觉指令微调后的问答作为评测，比较 23 个视觉骨干 | [Cambrian-1](../../papers/arxiv-2406.16860/README.md)、[Web-SSL](../../papers/arxiv-2504.01017/README.md) | 发现多数 benchmark 测不到视觉能力、组合多种编码器有益；代价：结果依赖所选语言模型与指令数据 |
| 评测协议 | 找 CLIP 相似度高于 0.95、DINOv2 相似度低于 0.6 的图像对出题 | [MMVP](../../papers/arxiv-2401.06209/README.md) | GPT-4V 38.7%、LLaVA-1.5 24.7%（随机 25%），CLIP 的盲区随视觉塔传进 VLM；交错 DINOv2 特征改善定位 |
| 评测协议 | 诊断工具：反卷积可视化、线索冲突图像、CKA 与注意力距离 | [Zeiler 与 Fergus](https://arxiv.org/abs/1311.2901)、[Geirhos 等](https://arxiv.org/abs/1811.12231)、[Kornblith 等](https://arxiv.org/abs/1905.00414)、[Raghu 等](https://arxiv.org/abs/2108.08810) | 不改部件，测部件：AlexNet 第一层缺中频，改成 7×7、步长 2 后 top-5 低 1.7 个百分点；Stylized-ImageNet 训练使检测 mAP50 70.7 → 75.1；线性 CKA 找对应层 99.3%；更大的 ViT 要更大的数据才有强中间层 |

精读的位置：[ViT 精读](../../papers/vit/reading.md)位于"架构 = 切块 Transformer"与"数据 = JFT-300M"两格，它的配方问题由同一表中"训练配方"的 DeiT、AugReg 两行修正；[MAE 精读](../../papers/mae/reading.md)与 [DINO 精读](../../papers/dino/reading.md)位于"训练信号"中相邻的两行，后续的 I-JEPA、DINOv2、Registers、DINOv3 分别从信号、数据、架构三个部件修补它们；[CLIP 精读](../../papers/clip/reading.md)位于"训练信号 = 图文对比"，它在读出接口上的问题由 LLaVA、Perception Encoder 两行接上。

## 四篇奠基论文的分类轴

结论：ViT、CLIP、MAE、DINO 常被并列，但它们回答的是不同层级的问题：ViT 是骨干架构，另外三篇是可以放在同一个骨干上的三种训练信号。下表的"默认"均指原论文的主要设置；CLIP 的图像塔也试过 ResNet，DINO 也能训练 ResNet。

| 观察轴 | ViT | CLIP | MAE | DINO |
|---|---|---|---|---|
| 回答的问题 | 骨干能否不用卷积 | 训练信号能否来自网上的文字 | 遮蔽重建能否在图像上扩展 | 不用标签的 ViT 会学出什么 |
| 输入组织 | 图像块序列 + [CLS] | 图像编码器 + 文本 token 序列，两塔互不查看 | 只把约 25% 的可见块送进编码器，轻量解码器补全 | 同一张图的 2 个全局裁剪与若干局部裁剪 |
| 训练目标来自 | 人工类别标签 | 配对的文本与批内的匹配关系 | 被遮挡块的像素 | 动量教师对另一裁剪的输出分布 |
| 损失形式 | 分类交叉熵 | N×N 相似度矩阵上按行、按列各一次的交叉熵 | 只在被遮位置计算的像素均方误差 | 教师分布对学生分布的交叉熵 |
| 训练后丢掉什么 | 预训练分类头（迁移时换成新的任务头） | 不丢：零样本时由文本塔生成类别向量，候选固定时可缓存 | 解码器与遮蔽流程，下游送入完整图像 | 投影头与学生–教师的训练流程，下游取骨干特征 |
| 典型下游接口 | 图像特征 + 新训练的任务头 | 图像向量与类别或查询文本的向量比相似度 | 图像特征 + 任务微调 | 全局与逐块特征，用于 k 近邻、检索、线性评测或微调 |

[判断] 这张表说明比较时要先分清层级：把 MAE 与 ViT 比，是把一种训练信号与一种架构比；把 MAE 与 DINO 比，才是同一层级的比较，而且必须固定骨干和协议（见下一节）。

## 跨论文比较前的检查单

结论：本方向最常见的错误比较，是把不同协议、不同分辨率、不同数据条件下的最高数字放进同一张表。比较两篇论文之前，先逐项对齐下面七件事。

1. **骨干与读出**：参数量、切块大小、分辨率，以及取的是哪一层的特征。MAE 的 87.8% 是 448 分辨率，224 分辨率为 86.9%；LLaVA 取倒数第二层，Perception Encoder 取第 47 层。
2. **数据条件**：数据规模，是否带标签或文字，是否非公开，是否用了外部分词器或教师（BEiT 依赖 DALL·E 分词器，DeiT 蒸馏时用 RegNetY 教师），预训练数据与评测集是否重叠（AugReg：在 ImageNet-1K 上预训练会抬高它的验证集分数；DINOv2 用 ImageNet-22k 等作检索查询）。
3. **计算**：训练步数、实际处理的 token 或视图数、硬件成本，只比 epoch 不够。DeiT 的"300 epoch"实际是 100 个 epoch、每个重复增强 3 次；I-JEPA 每次迭代比 MAE 慢约 7%，但迭代约少 5 倍；DINO 的 8×8 切块每图 785 个 token，16×16 为 197 个。
4. **协议分开记**：零样本、k 近邻、线性评测、部分微调、全量微调、作为 VLM 视觉塔的问答，各自单独成列。BEiT-B 线性 56.7%、微调 83.2%；同一个 MoCo v3-B，线性 76.7%、微调同为 83.2%。
5. **调参与模板**：下游增强、类别文本模板、超参搜索预算。CLIP 的零样本结果依赖提示模板，并且作者承认开发中反复查看了完整验证集；AugReg 指出好的增强与正则组合随模型大小和训练长度变化，没有简单规则。
6. **基线本身的配方**：同为有监督 ResNet-50，ConvNeXt 报告的原始配方为 76.1%，SimCLR 附录 B.8 为 76.3%，DINO Table 2 为 79.3%；"超过有监督"要先看超过的是哪一个。
7. **证据类型**：区分论文直接报告的数字、作者对机制的假说、本库的分析；一张注意力热图或补全样例代替不了定量评测（DINO 的干净注意力图到了 DINOv2 的大模型上被伪影破坏，见 Registers）。

## 批注

**易误读**

- 四篇对照表中的"默认"指 ViT §3–4、CLIP §2–3、MAE §3–5、DINO §3–5 的主要设置；ViT 原文也试了遮蔽块预测的自监督（§4.6），CLIP 的图像塔也有 ResNet 版本。
- 四篇各自容易被过度推断的地方：ViT 并不说明所有 ViT 都需要上亿张标签图（DeiT、AugReg）；CLIP 的零样本分数是在给定候选集合上的相对相似度，不是校准过的置信度；MAE 的重建图更清晰不代表特征更强；DINO 的注意力热图不是完整的分割器（Jaccard 45.9 是与真值掩码的重叠）。
- DeiT 的 81.8% 是 224 分辨率，83.1% 是 384 分辨率微调后；85.2% 用了 CNN 教师蒸馏，不是同条件的有监督数字（DeiT Table 5、Table 8）。
- BEiT 与 MoCo v3 的线性评测数字出自 BEiT 附录 Table 9，两者用的特征层与聚合方式不同：BEiT 对各块特征做平均池化，并取中间层（BEiT-B 第 9 层、BEiT-L 第 14 层，最后一层更差），作者指出没有预训练全局聚合的方法做线性评测本来就吃亏。这也是"最好的特征不在输出层"的一个早期例子，与 Perception Encoder 的发现一致。
- I-JEPA 的 81.1% 来自 448 分辨率预训练的 ViT-H/16，与 iBOT ViT-L/16 的 81.0% 并非同分辨率比较（I-JEPA Table 1）。
- Web-SSL 的"追平 CLIP"指冻结编码器、固定 Llama-3 8B 的 16 项问答平均分；它不比较零样本分类，因为自监督模型没有文本塔。
- DINOv3 的 COCO 66.1、ADE20k 63.0 是在冻结主干上接专门训练的检测器（Plain-DETR）与分割解码器的结果；只用线性头的 ADE20k 为 55.9（DINOv3 §1、§6.1）。
- Perception Encoder 的 COCO 66.0 来自 arXiv v2 的更新（页面注释），v1 的数字不同。

**与其他论文的关联**

- [入门页](README.md)的"方法谱系"按三条轴组织，本页多出的"训练配方"与"读出接口"两个部件，在入门页里分别散在"主线历史"第 6 节点（ConvNeXt）与"从任务看"一节（LLaVA 倒数第二层）。
- "训练配方"一行与[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)的论证同源：DeiT、AugReg 修正 ViT 一侧，ConvNeXt 修正 CNN 一侧。
- "训练信号 = 图文对比"诸行的展开在[图文对齐方向](../alignment/BASELINES.md)；"读出接口"中 VLM 相关的几行在 [VLM 方向](../vlm/BASELINES.md)；视频两行在[视频与时序方向](../video-temporal/BASELINES.md)；世界模型一行在[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)。
- "评测协议"最后一行的四种诊断工具，在入门页"从内部看"一节有完整的数字；通用技术见[模型科学](../../../cross-domain/fields/model-science/README.md)。

**未核实 / 待验证**

- 没有单篇目录的论文（DPM、Neocognitron、LeNet、VGG、GoogLeNet、U-Net、MobileNets、EfficientNet、ConvNeXt、R-CNN、DPM are CNNs、ImageNet、ILSVRC 综述、Zeiler 与 Fergus、Geirhos、Kornblith、Raghu）的数字取自 [synthesis.csv](synthesis.csv)，那些行由打开过的原文填写；LeNet 一行除题录外未核实。
- 同为有监督 ResNet-50 的 76.1%、76.3%、79.3% 三个数字分别来自三篇论文的表格，各自的训练配方细节没有逐项核对。
- MoCo v3 的线性与微调数字转引自 BEiT 附录 Table 9 与 MAE 原文，没有另查 MoCo v3 原文。
- BEiT 的正式发表出处（通常引作 ICLR 2022）本轮没能打开 OpenReview 页面核对。
- V-JEPA 2.1、C-RADIOv4、RADIO1D 三行只核对了 arXiv PDF 的摘要、引言与首页图表（V-JEPA 2.1 Fig.2、C-RADIOv4 摘要与 Table 1 标题、RADIO1D 摘要与 Fig.1），本库还没有单篇目录。
