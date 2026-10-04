# 图文对齐

> 状态：领域入门页 · v2
>
> 速览：
> - 图文对齐训练一座图像编码器和一座文本编码器，把图和句子放进同一个向量空间，配对的图文靠得近。训练好之后，一句话就能检索图片，也能当场把类别名变成分类器（零样本分类）；它的图像编码器后来成了视觉语言模型（VLM）和文生图的视觉入口。
> - 2021 年 CLIP（OpenAI）与 ALIGN（Google）证明，网页上天然配对的图文加对比损失可以规模化。此后两年最大的提升来自数据，而不是损失或结构：同样的 ViT-L/14、同样看 130 亿个样本、同样的算力，只把训练集换成筛选过的 DataComp-1B，ImageNet 零样本就从 CLIP 的 75.5% 升到 79.2%。
> - 各家押注不同：OpenAI 用关键词表平衡私有数据；Google Zürich 一组复用预训练图像塔、改用 sigmoid 损失、追求少量芯片就能训练；LAION 与华盛顿大学一系公开数据，并把"怎样选数据"做成 benchmark；Meta 公开复现 CLIP 的选数方法，不用任何模型做过滤。
> - 对比目标只奖励"整句与整图配上了"，模型因此可以像词袋一样忽略词序和关系：Winoground 上 CLIP 的组得分 8.0%，低于随机的 16.7%，人是 85.5%。这类缺陷后来随图像编码器一起传进了 VLM。
> - 2023 年之后的修补方向，是在对比目标之外加上描述生成、自蒸馏与遮蔽预测，并按 VLM 视觉塔的需要支持多分辨率、多语言和逐块特征（SigLIP 2）。

本页是[多模态总目录](../../README.md)下的一个方向，按 STYLE §3 的任务驱动模板来写，而不用视觉表征页的 §3.6 变体。理由是：图文对齐有自己的任务（给一张图，在一堆文字里找出配对的那句，或者反过来）和专门的 benchmark（Flickr30K、MS-COCO 检索，ImageNet 零样本，Winoground、ARO 这类组合性考题），好坏可以直接在相似度排序上测；视觉表征没有专属任务，才需要先定义对象。图像编码器作为通用主干的性质，见[视觉表征方向](../visual-representation/README.md)；作为 VLM 视觉塔之后的事，见[视觉语言模型方向](../vlm/README.md)。拆分后的基线见 [Baseline 页](BASELINES.md)，问题路线见[路线图](ROADMAP.md)，收录论文见[论文目录](PAPERS.md)。

## 这个领域在解决什么

结论：图文对齐要的是一个"图和文字能直接比较"的接口，有了它，类别、查询、条件都可以用自然语言临时写出来。

两个具体任务。在相册里搜"雪地里戴红围巾的狗"：系统要在几万张图里按与这句话的相似度排序（图文检索）。把一个 1000 类的识别器换成 200 种鸟的识别器而不重新训练：把 200 个鸟名各写成一句"a photo of a {鸟名}"，交给文本编码器得到 200 个向量，就是一个新的分类器（零样本分类，"零样本"指不用目标数据集的任何训练样本）。在 CLIP 之前，识别器只认训练时定好的类别，图文检索模型则在约千万对的人工清洗数据上训练（ALIGN §1 的统计）。

### 先看这里：双塔、相似度矩阵和三种训练目标

**双塔**。图像塔（ResNet 或 ViT）把一张图变成一个向量，文本塔（Transformer）把一句话变成一个向量，两者都归一化成长度为 1，相似度就是点积（余弦相似度）。两座塔互不通信，所以所有图片的向量可以提前算好存起来，检索时只算一次查询句的向量，这是双塔能用于大规模检索的原因（ALIGN §2 指出带交叉注意力的模型慢几个数量级）。

**对比损失（softmax 形式，CLIP、ALIGN）**。一批 N 对图文组成 N×N 的相似度矩阵，对角线是真配对。每一行做一次 softmax，要求第 i 张图在 N 句话里选中第 i 句；每一列再做一次，要求每句话选中自己的图，两个交叉熵相加。示例数值：两对图文，相似度矩阵为 [[0.8, 0.1], [0.2, 0.7]]，温度系数（放大相似度差距的倍数，可学习）取 10，第一行的 softmax 给真配对 e⁸/(e⁸+e¹) ≈ 0.999。负样本就是同一批里的其他图文，所以批越大负样本越多，ALIGN 把 1024 个 TPU 核上的向量拼成 16384 的批。手算全过程见[自监督与生成目标讲义](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 7、9 节与 [CLIP 精读](../../papers/clip/reading.md)第四节。

**sigmoid 损失（SigLIP）**。把矩阵里每一格当作一个独立的"配不配"二分类：对角线标 +1，其余标 −1，逐格算二元交叉熵，不再按行或列归一化（为什么多标签不能共用一个 softmax，见[分类与概率讲义](../../../foundations/lessons/modules/objectives/02-classification-probabilities.md)第 4–5 节）。负样本远多于正样本，所以加一个可学习的偏置 b，初值 −10，让训练一开始就接近"大多数格都不配"的先验。同一个例子里，若温度 10、偏置 −10，真配对那格的打分是 10×0.8 − 10 = −2，损失约 2.1，下一步就把它往上推；与 softmax 不同，这一格的损失不依赖同一行的其他格，各设备只需交换小块向量，不必拼出整张矩阵（SigLIP §3.3）。

**描述生成（captioning）**。让模型看图逐词写出配对的文字，与语言模型的下一词预测相同。CLIP 最早试的就是这个，结果比对比目标慢得多（见主线第 2 个节点）；后来 CoCa、BLIP、SigLIP 2 把它作为辅助目标加回来，用来补对比目标丢掉的细节。

**零样本分类与提示模板**。类别名先套进模板句（"A photo of a {类名}."），多个模板的文本向量取平均再归一化。ALIGN 照 CLIP 的做法，模板集成让 ImageNet top-1 提高 2.9 个百分点（ALIGN §5.2），所以零样本成绩同时取决于模板、候选类别集和预训练数据有没有覆盖这些概念。

## 方法谱系

结论：每个方法都可以放在"训练目标 × 数据怎样来 × 图像塔怎样初始化"三条轴上；2021 年之后，三条轴里对结果影响最大的是数据轴。

| 轴 | 取值 | 代表 | 换来什么 | 代价 |
|---|---|---|---|---|
| 训练目标 | softmax 对比 | CLIP、ALIGN | 训练效率高，直接得到检索与零样本接口 | 需要大批量；只奖励整体匹配，词序与关系可以被忽略（ARO） |
| | sigmoid 对比 | SigLIP | 批小于 16k 时明显更好，省内存，对数据噪声更稳健 | 批增大后与 softmax 的差距消失，二者在 32k 左右都饱和 |
| | 对比 + 描述生成 | CoCa、BLIP、SigLIP 2 | 细粒度文字信号，可直接写描述、回答问题；定位与 OCR 更好 | 多一个解码器；BLIP 还要图文匹配头 |
| | 对比 + 图像自监督 | SigLIP 2（自蒸馏、遮蔽预测，训练最后 20%） | 逐块特征更好，分割、深度、指代定位提升 | 训练更复杂，需要分阶段控制算力 |
| 数据 | 关键词表平衡（私有） | CLIP 的 WIT（50 万个查询词，每个最多 2 万对） | 覆盖面广、头部概念不占满 | 方法只写了一段，数据不公开 |
| | 最少过滤的海量噪声数据 | ALIGN（18 亿对）、LiT（40 亿对） | 规模弥补噪声 | 私有；同等规模下比清洗过的数据差 |
| | 用 CLIP 打分过滤 | LAION-5B（ViT-B/32 余弦阈值 0.28） | 公开、可复现 | 继承过滤模型的偏差，过滤器决定了数据分布 |
| | 把选数据做成可比较的实验 | DataComp、MetaCLIP | 固定训练代码只比数据，同算力下明显更好 | DataComp 最好的过滤以 ImageNet 为锚；MetaCLIP 的元数据仍来自英文维基与 WordNet |
| | 生成合成描述 | BLIP 的 CapFilt | 把噪声 alt-text（网页图片的替代文字）换成描述器写的句子并过滤 | 依赖描述器本身的质量 |
| 图像塔初始化 | 从头训练 | CLIP、ALIGN、DataComp | 图像特征完全由图文数据塑造 | 算力最贵 |
| | 冻结预训练图像塔 | LiT | 只训文本塔，零样本分类强，算力省 | 依赖一个强的有监督图像塔（ViT-g/14）；检索上优势不明显 |
| | 用遮蔽建模预训练的塔初始化 | EVA-CLIP | 少用样本、训练更稳 | 多一个预训练阶段 |

## 主线历史

每个节点写三件事：上一个节点留下的问题、这一节点改变了什么、它自己做不好的场景。

1. **CLIP 之前：小规模清洗数据与交叉注意力模型**。视觉–语言预训练要么用双塔视觉–语义嵌入，要么用带交叉注意力的融合模型（UNITER 等）。数据集如 Conceptual Captions 要经过繁重的人工标注、解析、清洗，规模约千万对，比视觉侧的 JFT-300M 小一个数量级以上（ALIGN §1）。**做不好**：交叉注意力模型每对图文都要联合前向一次，ALIGN §2 说它们慢几个数量级，无法用于真实检索系统；数据规模卡在人工清洗上，类别只能来自训练集。

2. **CLIP（2021 年 1 月，OpenAI）与 ALIGN（2021，Google Research）：从清洗数据转到网页规模的配对数据**。留下的问题：图文数据规模被清洗流程卡住。CLIP 用 50 万个查询词（英文维基高频词、高互信息二元组、维基条目名、WordNet（英文词汇语义网络）同义词集）检索出 4 亿对图文，每个查询最多保留 2 万对。它先试过让模型逐词写出配对文字，6300 万参数的语言模型学会识别 ImageNet 类别的速度只有"预测词袋"基线的三分之一；把预测目标换成对比目标，效率又提高 4 倍（CLIP §2.3）。零样本 ImageNet 76.2%。ALIGN 走另一条路：放松 Conceptual Captions 的几乎全部清洗步骤，只做基于词频的简单过滤，得到 18 亿对，用 EfficientNet-L2 加 BERT-Large 从头训练，零样本 ImageNet 76.4%。ALIGN 的消融说明规模能弥补噪声：同为 300 万对时，噪声数据训练的模型在 MS-COCO 图到文检索 R@1（第一名就是正确答案的比例）只有 8.1，清洗过的 CC-3M 为 18.9；噪声数据加到 1200 万对时升到 23.8，反超 CC-3M（ALIGN Table 10）。**做不好**：CLIP §6 自述细粒度分类（车型、花种、机型）弱，计数这类系统性任务弱，"到最近那辆车的距离"这种预训练里少见的任务接近随机；手写数字 MNIST 只有 88%，比直接在像素上做逻辑回归还差，最近邻检索显示预训练数据里几乎没有类似图片；零样本只能在给定的类别中选择；从零样本加几张样本改成线性探针，准确率反而下降；估计还要约 1000 倍算力才能在零样本上整体达到最优。OpenAI 的 Goh 等（2021）在同年发现，CLIP 能"读字"：给物体贴上写着错误类名的纸条，零样本分类就会被带偏（排版攻击）。ALIGN 自述文本–文本、图像–图像的相似度任务略差于专门方法，原因是目标只管跨模态匹配（§5.1）。

3. **LiT（2021 年 11 月）、CoCa 与 BLIP（2022）：复用预训练、加回生成目标**。留下的问题：CLIP、ALIGN 从头训两座塔，算力昂贵；对比目标只要整句匹配，写不出描述、答不了问题；网页 alt-text 噪声大。三篇各改一个部件。
   - LiT（Google Brain Zürich）冻结一个已有监督预训练的 ViT-g/14 图像塔，只训文本塔，"教文本模型读出好的图像表征"。零样本 ImageNet 85.2%，ObjectNet（刻意打乱背景、角度的测试集）82.5%，比 CLIP 高 10.2 个百分点。作者给出的原因：解冻图像塔后，对比训练让它在图文数据上的损失更低，却在分布外数据和少样本线性评测上更差，图像特征被对齐数据"专门化"了（LiT §5.2、Fig.4）。
   - CoCa（Google Research）把文本解码器拆成两半：前半不看图，输出的句子向量与图像向量做对比；后半用交叉注意力看图，逐词生成描述。标签数据（JFT-3B）的类名和 ALIGN 的 alt-text 都当作文字。消融中，只用对比目标时零样本 ImageNet 70.7%、VQA（看图回答问题的 benchmark）59.2%，两个目标一起时 71.6%、69.0%，训练成本只多 18%（CoCa Table 8b）。完整模型零样本 ImageNet 86.3%。这正是 CLIP §6 当年建议的"把对比目标与生成目标联合训练"。
   - BLIP（Salesforce）一个模型三种用法：单模态编码器做对比（ITC），带交叉注意力的编码器判断图文是否匹配（ITM），解码器写描述（LM）。它的 CapFilt 先用描述器给网页图片写新句子，再用过滤器去掉不匹配的原 alt-text 与合成句。在 1400 万张图上，两步都用时 COCO 检索微调后的图到文 R@1 从 78.4 升到 80.6（BLIP Table 1）；用随机采样（nucleus sampling）写的描述噪声更多，效果反而好于集束搜索，作者认为多样性更重要（§4.3）。
   
   **做不好**：LiT 自述只测了分类和检索；在检索上冻结图像塔的优势不明显，训练足够长时解冻反而追上（§6）；它的强项建立在私有的大规模有监督预训练上。CoCa 未声明公开代码或权重，自述可能对现有评测没覆盖的图像损坏仍然脆弱。BLIP 的 ITM 判断在词序测试上接近随机（见下一节点）。

4. **Winoground、ARO 与 SugarCrepe（2022–2023）：评测目标从"检索得准"迁到"组合得对"**。留下的问题：检索和零样本分数越来越高，模型到底是否理解"谁对谁做了什么"。Winoground（Hugging Face 与 FAIR）给两张图、两句用词完全相同只是顺序不同的话（"植物围着灯泡"与"灯泡围着植物"），要求配对。CLIP ViT-B/32 的文本得分 30.75%、图像得分 10.50%、组得分（两张图、两句话全部配对正确）8.00%，随机水平分别为 25%、25%、16.67%，众包人类为 89.50%、88.50%、85.50%（Winoground Table 3）。ARO（Stanford）用 5 万多个测试项拆开属性、关系和词序，发现模型像词袋：CLIP 在属性题上 62%，接近 50% 的随机水平；把 COCO、Flickr30K 检索集的词序或图块顺序打乱，检索成绩几乎不掉，说明现有检索 benchmark 不需要组合信息就能做好，对比预训练也就没有学它的动力（ARO §3）。ARO 的补救是在批里加入"打乱词序的句子"和"最近邻图片"作为难负样本（NegCLIP），COCO 词序题从 46% 升到 86%，下游分类与检索基本不掉。**做不好**：这些考题自己也有漏洞。SugarCrepe（华盛顿大学与 AI2）发现，Winoground、ARO 等基准里用规则生成的负样本句子常常不通顺、不合常理，一个完全不看图、只判断句子是否通顺的模型就能胜过最好的 CLIP；换成用大语言模型生成的通顺负样本后，NegCLIP 这类方法的提升被大幅高估了。

5. **LAION-5B、OpenCLIP 缩放定律与 EVA-CLIP（2022–2023）：数据公开之后，规模化可以被外部复现和测量**。留下的问题：CLIP、ALIGN、LiT、CoCa 的数据全部私有，外部团队无法研究规模和数据的作用（LAION-5B §1）。LAION（与 UC Berkeley、华盛顿大学、Jülich 等）从 Common Crawl（公开的网页抓取存档）的约 500 亿张图出发，用 OpenAI 的 CLIP ViT-B/32 给每对图文打分，英文对余弦相似度低于 0.28 的丢掉，去掉约 90%，剩下 58.5 亿对（其中英文 23.2 亿）。同一批作者用公开的 OpenCLIP 代码在 LAION 上训练到 340 亿个样本，得到零样本分类、检索、线性探针、微调都服从的幂律（性能随算力按幂函数提升）；同为 ViT-L/14，OpenAI 的模型 ImageNet 零样本 75.5%、COCO 文到图 R@5 61.1%，LAION-2B 上的模型分别是 75.2%、71.1%：WIT 训练的模型在分类上随规模提升更快，LAION 训练的在检索上更快。作者在结构与配方对齐的前提下，把差异归于训练数据：WIT 的整理方式可能更贴近 ImageNet，LAION 由 CLIP 打分过滤，可能更适合检索（缩放定律论文 Discussion）。同期 Fang 等（2022，华盛顿大学）逐项控制训练集规模、语言监督、对比损失等五个因素，结论是 CLIP 在分布偏移上的稳健性主要来自更多样的训练分布。EVA-CLIP（北京智源研究院）用遮蔽图像建模预训练过的 EVA 初始化图像塔，加上 LAMB 优化器（面向大批量训练的逐层自适应优化器）和训练时随机丢掉 50% 图像块，EVA-02-CLIP-L/14 只看 40 亿个样本就达到 ImageNet 零样本 79.8%，同尺寸的 OpenCLIP 看了 320 亿个样本为 74.0%（EVA-CLIP Table 1）。**做不好**：LAION-5B 自述用小的 ViT-B/32 过滤，会留下弱相关的图文、误删好样本，并继承 CLIP 的缺陷与偏差（§6）；用 CLIP 过滤再训练 CLIP，数据分布由上一代模型决定。安全问题在发布后才暴露：LAION 官方 2024 年 8 月发布 Re-LAION-5B，按 Stanford Internet Observatory 2023 年 12 月的报告与儿童保护机构提供的哈希清单，删去 2236 个疑似儿童性虐待内容的链接。缩放定律论文自述采样点稀疏、大规模下无法充分调参，OpenAI 一侧因数据私有只有三个点。

6. **DataComp、MetaCLIP 与 SigLIP（2023）：把数据当作主要的研究对象，把损失改得更省**。留下的问题：LAION 只是"一种"过滤方式，过滤方式本身怎样影响模型没人系统比较过；CLIP 的 WIT 怎样整理的仍是一段话。DataComp（华盛顿大学、哥伦比亚大学、LAION、Apple 等十余个单位）反转 benchmark 的惯例：训练代码、模型和算力全部固定，参赛者只能改训练集，在 38 个下游任务上评分。从 128 亿对的候选池里，用 CLIP ViT-L/14 的分数保留最高的约 30%、再与"图像落在 ImageNet 类别聚类附近"的子集取交集，得到 DataComp-1B：ViT-L/14 看 130 亿个样本，ImageNet 零样本 79.2%，比同条件的 CLIP 高 3.7 个百分点，比同条件的 LAION-2B（73.1%）高 6.1。随机抽取子集几乎无益，更小但筛得更严的数据集反而更好。MetaCLIP（Meta FAIR）不用任何模型过滤，而是重建 CLIP 的 50 万个元数据条目，用子串匹配建倒排索引，再按 t = 2 万的上限平衡：头部条目（例如 "photo" 在池中出现 5400 万次）只保留 2 万对，尾部全部保留。400M 规模、ViT-B 时 ImageNet 零样本 70.8%，高于 CLIP 的 68.3%；只做匹配不做平衡时明显更差（ViT-B/32 固定步数下 60.8% 对 65.5%，MetaCLIP Fig.1）。SigLIP（Google DeepMind Zürich，与 LiT 同一组作者）把 softmax 换成逐格 sigmoid：批小于 16k 时明显更好；批一路加到 100 万，两种损失都在 32k 左右饱和；冻结图像塔的 SigLiT 用 4 块 TPUv4 训练 2 天达到零样本 ImageNet 84.5%；人为加入图像、文本、配对错乱等噪声时，sigmoid 训练的模型更稳健（§4.10）。**做不好**：DataComp 最好的过滤以 ImageNet 训练图的聚类为锚，作者自己也观察到 ImageNet 精度与平均成绩高度相关，但与单个数据集精度的相关性差异很大、有时为负（§5.3）；SigLIP 2 在比较表中注明，DFN 这一过滤方法用的过滤网络在 ImageNet、COCO、Flickr 上微调过，正是主要考题。MetaCLIP 统计到 50 万个条目中有 11.4 万个在 16 亿对的池里一次都没匹配上，3.2% 的头部条目占了 94.5% 的匹配次数，长尾概念从源头就缺数据（§3.3）。DataComp 用的模型在地理多样性上好于 ImageNet 训练的模型，但不及在多样化人工数据上微调的模型，人脸分类还暴露出人口统计偏差（§5.3）。

7. **SigLIP 2（2025，Google DeepMind）与 Eyes Wide Shut（2024，NYU 与 Meta）：对齐编码器成为 VLM 的视觉塔，需求随之改变**。留下的问题：对比编码器被大量用作 VLM 的视觉输入（例如 [LLaVA](../../papers/llava/README.md) 用 CLIP ViT-L/14 的网格特征，[OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 拼接 SigLIP 与 DINOv2），而它的训练目标只关心全局匹配。Eyes Wide Shut 找出"CLIP 盲对"：CLIP 嵌入余弦相似度超过 0.95、DINOv2（纯视觉自监督编码器）嵌入相似度低于 0.6 的图片对，据此出 150 对、300 道题（MMVP）。人类答对 95.7%，GPT-4V 38.7%，LLaVA-1.5 24.7%，随机 25%；9 类视觉模式（朝向、计数、视角等）中有 7 类任何规模的 CLIP 模型都解决不了，CLIP 在哪类模式上失败，VLM 也在哪类上失败。把 DINOv2 特征与 CLIP 特征按图块交错送进 VLM，视觉定位明显变好而指令遵循不掉。SigLIP 2 在 SigLIP 的 sigmoid 损失上加入带解码器的描述、密集描述与指代表达预测（LocCa），训练最后 20% 再加自蒸馏与遮蔽预测，并用主动数据筛选蒸馏小模型；训练数据 90% 英文、10% 非英文网页，并做去偏过滤。同尺寸同分辨率（So400m/14，384 像素）下 ImageNet 零样本从 83.2% 升到 84.1%，36 种语言的 XM3600 图到文检索 R@1 从 26.6% 升到 57.5%；作者还按 PaliGemma 2（Google 的开放 VLM）式的配方把它接到语言模型上，在多项 VLM 任务上好于 SigLIP。另一个 NaFlex 变体保留原图长宽比、支持多种序列长度，在文档、屏幕截图类检索上更好。**做不好**：NaFlex 在训练过的分辨率之间插值尚可，外推到更大分辨率效果不好（Fig.3）；文化多样性的总体指标有提升（L/16 在 Dollar Street（地理与收入多样的日常物品识别集）上零样本 52.1%→55.2%），但按收入水平和地区拆开看各组之间的差距，几乎没有缩小（§3.5）。VLM 一侧怎样补视觉细节，交给[视觉语言模型方向](../vlm/README.md)。

[判断] 把这七个节点连起来看，图文对齐的瓶颈依次落在三处：先是数据规模（清洗卡住规模），再是数据分布（同样的规模、不同的整理方式给出不同的缩放曲线），最后是目标本身（整体对比学不到组合与空间细节）。前两处靠数据工程推进，第三处要改训练目标，并且是在下游 VLM 暴露问题之后才被重视。

### 后继节点：全球数据、内部特征与混合模态检索（2025–2026）

CLIP 的整体图文匹配接口留下了三件事：数据覆盖谁、局部特征是否被输出层掩盖、查询是否只能是一段短文字。接着读以下三篇，各自改变一个问题：

- **[Meta CLIP 2](../../papers/arxiv-2507.22062/README.md)，必读。** 旧 MetaCLIP 用英文元数据控制训练分布；后继把匹配和平衡扩到多语言，同时补足英语样本曝光与模型容量。关键证据是不同容量下结果不同：数据覆盖变广，并不自动保证原语言能力不掉。
- **[Perception Encoder](../../papers/arxiv-2504.13181/README.md)，必读。** SigLIP 2 用更多训练目标补局部信息，PE 则先追问“信息是不是已在中间层，只是最后一层不适合读”。它强化对比训练，再分别做语言与空间对齐，使“读哪一层、怎样读出”成为单独的设计变量。
- **[Qwen3-VL-Embedding / Reranker](../../papers/arxiv-2601.04720/README.md)，选读。** VLM 反过来充当检索编码器：查询与文档都可混合文字、图片和视频，先独立编码做大库召回，再联合编码逐对重排。它继承双塔的缓存优势，同时把精细匹配的额外计算留给少数候选。

`[判断]` 对齐方向的推进不能只写成“更大的 CLIP”：全球覆盖依赖数据与容量，局部迁移依赖读出，而复杂检索重新引入查询–候选交互。三个问题的评测也不同，应分别看分语言结果、冻结局部任务与检索/重排协议。

## 技术地基

- **交叉熵与 softmax、sigmoid 的区别**：对比损失是"在一批候选里选对的那个"的交叉熵；sigmoid 损失是每一格独立的二分类。见[分类与概率讲义](../../../foundations/lessons/modules/objectives/02-classification-probabilities.md)第 2–5 节。
- **对比学习与温度**：正样本拉近、负样本推远，温度控制相似度差距被放大多少，批越大负样本越多。CLIP 的 N×N 矩阵与 SimCLR 的批内候选见[自监督与生成目标讲义](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 7–9 节。
- **Transformer 编码器、因果解码器与交叉注意力**：文本塔是 Transformer；CoCa、BLIP 的描述解码器用因果 mask 逐词生成，用交叉注意力读取图像特征（查询来自文字，键和值来自图像）。见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 7、13 节。
- **ViT 与切块**：主流图像塔是 ViT；FLIP 式丢图块（训练时随机丢掉一部分图块以省算力）、NaFlex 的可变序列长度都建立在"图像是一串图块 token"之上。见 [ViT 精读](../../papers/vit/README.md)。
- **冻结、微调与迁移**：LiT 冻结图像塔、只训文本塔；VLM 一般冻结或部分微调对齐好的图像塔。原理见[迁移与元学习讲义](../../../foundations/lessons/05c-transfer-meta-learning.md)第 2–3 节。
- **幂律缩放**：误差 E 与算力 C 满足 E = βC^α；OpenCLIP 论文在 ImageNet 零样本上测得 α 为 −0.11（LAION）与 −0.16（WIT）。规模定律的总线见[观点页：深度学习的规模化](../../../perspectives/scaling.md)。

## 主要路线与团队偏好

结论：四个主要团队在"数据从哪来、公不公开、图像塔从头训还是复用"上各自重复同一种选择。

| 团队 | 代表工作 | 数据 | 图像塔 | 公开什么 | 押注与代价 |
|---|---|---|---|---|---|
| OpenAI | CLIP | 私有 WIT，按 50 万个查询词平衡 | 从头训练 | 代码与权重，不公开数据 | 押注自然语言监督加大规模；代价是数据整理方法外界只能猜，直到 MetaCLIP 复现 |
| Google Zürich（Zhai、Beyer、Kolesnikov、Mustafa 等） | LiT → SigLIP → SigLIP 2 | 私有（LiT 40 亿对，SigLIP 系列用 WebLI） | 复用预训练图像塔，或从头训练时讲究效率 | 权重与 big_vision 代码 | 押注训练效率与可用性（少芯片、向后兼容、多尺寸）；代价是数据始终不公开，结论外部无法在同一数据上复现 |
| Google Research（另一批作者） | ALIGN、CoCa | 私有：18 亿对 alt-text，JFT-3B 标签 | 从头训练，模型很大 | 论文未声明公开 | 押注规模弥补噪声、一个模型统一多种用法；代价是外部只能读数字 |
| LAION 与华盛顿大学（Schmidt、Jitsev、Cherti、Beaumont、Wortsman 等） | LAION-5B → 缩放定律 → DataComp | 公开的 Common Crawl 数据 | 从头训练，固定配方 | 数据、代码、模型、评测全部公开 | 押注开放与可测量；代价是早期依赖 OpenAI CLIP 做过滤，安全问题由社区事后发现 |
| Meta FAIR | MetaCLIP | 公开方法，元数据加平衡，不用模型过滤 | 从头训练 | 选数代码与数据分布 | 押注透明的选数流程；代价是元数据仍是英文维基与 WordNet，长尾概念缺失 |

[判断] **Google Zürich 一组在三篇中重复"让对齐更便宜、更好用"**：LiT 冻结图像塔以省掉图像侧训练，SigLIP 改损失以省内存、降低对批大小的依赖（摘要称 4 块 TPUv4 两天），SigLIP 2 强调与 SigLIP 结构相同、可直接替换权重，并发布四种尺寸。三篇都发布权重。与之相对，ALIGN、CoCa 虽同属 Google，却押注"更大的模型、更多的私有数据"，且未声明发布，说明"Google"并不是一个统一的偏好单位。

[判断] **LAION 与华盛顿大学一系在三篇中重复"公开数据加受控测量"**：LAION-5B 公开数据；缩放定律论文公开模型与评测流程，并把 OpenAI 与 OpenCLIP 的差异归于数据；DataComp 干脆把数据当成唯一的变量。它的自我修正也在同一系里发生：LAION-5B 自述用小 CLIP 过滤是局限，DataComp 改用 ViT-L/14 打分并证明更严的过滤更好。

[判断] **MetaCLIP 与模型打分筛选路线的分歧在"选数据用不用模型"**：CLIP 的 WIT 只用查询词匹配和计数平衡，MetaCLIP 认为这是 CLIP 成功的主因，并指出 LAION、DataComp 用 CLIP 过滤，本质上是在蒸馏 WIT 的信息；DataComp 一侧则用实验说明模型打分过滤有效。两者在 ViT-L/14 上的结果接近（MetaCLIP 2.5B 数据 79.2%，DataComp-1B 79.2%），所以这组当时的结果没有给这场分歧分出胜负，差别在于可控性：MetaCLIP 的分布可以按元数据检查和调整，模型过滤的偏差藏在过滤模型里。

其他团队：北京智源研究院的 EVA-CLIP 押注"先用遮蔽图像建模预训练图像塔，再做对比"，以少得多的样本追平或超过同尺寸模型；Salesforce 的 BLIP 押注"用模型自己写描述来清洗数据"，SigLIP 2 的相关工作一节把"用 VLM 重写训练图像的描述"列为提高训练信号质量的一类做法。

## 用什么衡量进展

结论：评测从"检索与零样本分类的平均分"一步步移到"组合性考题"和"作为 VLM 视觉塔的表现"，每次迁移都是因为旧指标掩盖了某类失败。

- **零样本分类**：ImageNet 及其分布偏移版本（ImageNetV2、-R、-A、-Sketch、ObjectNet），以及 CLIP 的 27 个、DataComp 的 38 个下游数据集。下表是 SigLIP 2 Table 1 汇总的 ViT-L/14、224 像素、ImageNet 零样本，用来看"同一结构、不同数据与配方"的差距：

  | 模型 | 训练数据 | ImageNet 零样本 |
  |---|---|---|
  | OpenCLIP | LAION-2B | 74.0% |
  | CLIP | WIT（私有） | 75.5% |
  | MetaCLIP | 元数据平衡的 Common Crawl | 79.2% |
  | EVA-CLIP | LAION-2B 与 COYO 混合，遮蔽建模初始化 | 79.8% |
  | DFN | 用微调过的过滤网络筛选 | 82.2% |

- **图文检索**：Flickr30K（1000 张测试图）、MS-COCO（5000 张）的 R@1、R@5。ARO 证明打乱词序或图块后检索成绩几乎不变，所以检索分高不代表理解了组合。
- **组合性考题**：Winoground（400 组，人工精选）、ARO（5 万多题，规则生成负样本）、SugarCrepe（大语言模型生成通顺负样本，修补前两者能被"盲模型"刷分的漏洞）。考题本身的偏差会高估方法的提升。
- **作为 VLM 视觉塔**：SigLIP 2 按 PaliGemma 式配方接语言模型后在多项 VLM 任务上评分；MMVP 用"CLIP 盲对"出题，直接测视觉塔的盲区。
- **校准与公平性**：零样本给出的概率能否当作置信度，结论取决于口径。Minderer 等（2021，Google）在 ImageNet 及其分布偏移测试集上发现 CLIP"相对其精度校准良好"；LeVine 等（2023，Scale AI，ICLR 研讨会论文）跨提示、数据集、结构测量，结论是 CLIP 零样本推断校准不良，并提出每个模型学一个温度来修正。公平性方面，SigLIP 2 报告把"随机图片更常被关联到 men 而非 women"的表示偏差从 35.5% 降到 7.3%（L/16，256 像素）。
- **口径问题**：零样本分数受模板集成影响（ALIGN 报告 +2.9 个百分点）；各家去重测试集的方法不同，缩放定律论文自述只做了简单的重复检查；比较时要对齐结构、分辨率、看过的样本数和训练算力，不能只比数据集大小（DataComp 与 EVA-CLIP 都按样本数报告）；LiT、CoCa 的高分用到私有的 JFT 有监督预训练，缩放定律论文指出 JFT 中有 973 个类能人工对应到 ImageNet 的 1000 类。

## 当前开放问题

- **对比目标能否学到组合与空间关系，还是必须加别的目标？** NegCLIP 的难负样本在 ARO 上有效，SugarCrepe 却显示提升被高估；SigLIP 2 加入描述与指代表达预测后定位变好，但 MMVP 一类的盲区是否消失还没有在同一协议下检验。入口：[ARO](../../papers/arxiv-2210.01936/README.md)、[SugarCrepe](../../papers/arxiv-2306.14610/README.md)、[SigLIP 2](../../papers/arxiv-2502.14786/README.md)、[Eyes Wide Shut](../../papers/arxiv-2401.06209/README.md)。
- **数据筛选在优化通用性，还是在优化考题？** DataComp-1B 以 ImageNet 聚类为锚，DFN 的过滤器在主要考题上微调过，MetaCLIP 则刻意不用模型。入口：[DataComp](../../papers/arxiv-2304.14108/README.md)、[MetaCLIP](../../papers/arxiv-2309.16671/README.md)、[缩放定律](../../papers/arxiv-2212.07143/README.md)。
- **长尾概念与非英语世界怎样覆盖？** MetaCLIP 的 50 万个条目中 11.4 万个无匹配；[Meta CLIP 2](../../papers/arxiv-2507.22062/README.md)开始控制多语言覆盖、曝光量与模型容量；SigLIP 2 的多语言检索大幅提升，不同收入水平、不同地区之间的识别差距却几乎没有缩小。入口：[SigLIP 2](../../papers/arxiv-2502.14786/README.md)、[LAION-5B](../../papers/arxiv-2210.08402/README.md)。
- **VLM 需要什么样的视觉塔？** 早期系统常用对比编码器提供语义、自监督编码器补细节：Eyes Wide Shut 交错 CLIP 与 DINOv2，OpenVLA 拼接 SigLIP 与 DINOv2，SigLIP 2 则试图在一个编码器里兼顾；[Perception Encoder](../../papers/arxiv-2504.13181/README.md)进一步表明，对比模型中间层也可提供强局部特征，输出层的表现不代表整个编码器。入口：[视觉语言模型方向](../vlm/README.md)、[视觉表征方向](../visual-representation/README.md)的"从任务看"一节。

## 阅读顺序

1. [自监督与生成目标讲义](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 7–9 节：先手算一次批内对比损失，弄清 softmax 沿哪一维做、正例从哪来。
2. [CLIP 精读](../../papers/clip/reading.md)：本方向的基线。重点读第五节的数据、第六节的零样本分类器怎样由文本生成，以及第九节的边界。读完可以做一个检验：把 N 个训练配对改成 K 个候选类别，说出哪些向量可以缓存。
3. [SigLIP](../../papers/arxiv-2303.15343/README.md)，对照 [LiT](../../papers/arxiv-2111.07991/README.md)：只改损失或只改图像塔初始化，各换来什么。
4. [CoCa](../../papers/arxiv-2205.01917/README.md) 与 [BLIP](../../papers/arxiv-2201.12086/README.md)：加回生成目标的两种做法。
5. [DataComp](../../papers/arxiv-2304.14108/README.md) 与 [MetaCLIP](../../papers/arxiv-2309.16671/README.md)：同一个问题（怎样选数据）的两种答案，对照读；接 [Meta CLIP 2](../../papers/arxiv-2507.22062/README.md) 看全球数据如何改变配方。
6. [Winoground](../../papers/arxiv-2204.03162/README.md)、[ARO](../../papers/arxiv-2210.01936/README.md) 与 [Eyes Wide Shut](../../papers/arxiv-2401.06209/README.md)：对齐空间做不到什么，以及这些缺陷怎样传进 VLM；接着对照 [SigLIP 2](../../papers/arxiv-2502.14786/README.md) 与 [Perception Encoder](../../papers/arxiv-2504.13181/README.md)，再转到[视觉语言模型方向](../vlm/README.md)；做检索时续读 [Qwen3-VL-Embedding](../../papers/arxiv-2601.04720/README.md)。

## 批注

**易误读**

- CLIP 的 76.2% 与 ALIGN 的 76.4% 用了不同结构、不同数据和同一套提示模板集成（ALIGN Table 4），只说明两条数据路线在当时打平，不是受控比较。
- DataComp-1B 的 79.2% 与 CLIP 的 75.5% 是同结构（ViT-L/14）、同样看 130 亿个样本、同训练算力（1.1×10²¹ MACs）的比较（DataComp Table 1）；MetaCLIP 的 79.2% 是 25 亿对数据上的 ViT-L，两个 79.2% 只是数值巧合。
- MetaCLIP 的 70.8% 对 68.3% 是 ViT-B/16（摘要写"ViT-B models"）在 4 亿对上的结果；60.8% 对 65.5% 出自 Fig.1 的 ViT-B/32 固定步数曲线，两组数字的设置不同。
- LiT 的 85.2% 用私有的 40 亿对图文和以私有 JFT 数据预训练的 ViT-g/14；在公开数据上，LiT 的主要说法是相对从头训练的改进（Fig.1 左）。
- CoCa 的 70.7%→71.6% 是缩小模型（CoCa-Base、12 层解码器、批 4096）上的消融，86.3% 是完整模型。
- SigLIP 的"批 32k 足够"出自 SigLiT（冻结图像塔）和 SigLIP 在 90 亿样本上的实验（Fig.2）；批小于 16k 时 sigmoid 明显好于 softmax，大批时两者接近。
- Winoground 的随机水平：文本、图像得分 25%，组得分 16.67%；ARO 的 VG 关系与属性题是二选一，随机 50%，词序题五选一，随机 20%。
- EVA-CLIP 的"40 亿个样本"指训练中看过的样本数，训练集是 20 亿对的 Merged-2B（16 亿 LAION-2B 加 4 亿 COYO-700M）。
- LAION 的 0.28 阈值只用于英文对，多语言与无特定语言的对阈值为 0.26（LAION-5B §3.1）。
- SigLIP 2 的 83.2%→84.1% 与 XM3600 的 26.6%→57.5% 均为 So400m/14、384 像素、729 个 token 的同配置比较（Table 1）；XM3600 一列是图到文 R@1。

**后继节点的边界**

- Meta CLIP 2 的语言收益依赖容量；正式版 §3.4、Table 1 与 Appendix G 保留了较小模型的反例。PE 的“纯对比预训练”与后续语言/空间对齐分开理解，PEspatial 还使用额外空间教师。
- Qwen3-VL-Embedding 的训练包含相关性监督与排序器蒸馏，不能拿它的检索成绩直接论证 CLIP 零样本分类被替代；重排也要计入逐对推理成本。

**判断的支撑论文与反例**（各行见 [synthesis.csv](synthesis.csv)）

- "瓶颈依次是规模、分布、目标"：ALIGN §1 与 Table 10（规模弥补噪声）；缩放定律论文 Discussion（分布决定缩放曲线）；Fang 等 2022（稳健性来自训练分布）；ARO §3、Winoground Table 3、Eyes Wide Shut §3（目标学不到组合与细节）。反例：CLIP §6 早在 2021 年就把计数、细粒度列为局限，并建议联合生成目标，"目标"这一瓶颈并非事后才被意识到，只是事后才被系统测量。
- Google Zürich 的效率偏好：LiT Abstract 与 §5.2、SigLIP Abstract 与 Table 1、SigLIP 2 §1（向后兼容、四种尺寸）；作者列表中 Zhai、Beyer、Mustafa 三篇均署名，Kolesnikov 署名前两篇。边界：SigLIP 2 的训练流程比 SigLIP 复杂得多，效率偏好在第三篇中让位给能力。
- LAION 与华盛顿大学一系的开放偏好：LAION-5B §1、缩放定律 Abstract、DataComp §1 与 §6；三篇作者重叠（Schmidt、Jitsev、Cherti、Beaumont、Wortsman）。边界：DataComp 的作者来自十余个单位，团队边界较松。
- 元数据筛选与模型打分筛选的分歧：CLIP §2.2；MetaCLIP §1、§2、§3.4；DataComp 的数据筛选比较。CLIP/WIT 与 MetaCLIP 同属元数据匹配一侧，DataComp/LAION 使用模型打分。边界：这里只比较选数方法，不能据此推断公司整体偏好。
- "评测迁移因旧指标掩盖失败"：ARO §3.1（检索掩盖组合缺陷）、SugarCrepe §1（组合考题被盲模型刷分）、Eyes Wide Shut §1（VLM 的视觉缺陷来自 CLIP）。

**与其他论文的关联**

- [CLIP](../../papers/clip/reading.md) 是本方向的基线，它在[视觉表征方向](../visual-representation/README.md)中作为"图文弱监督"一路出现，那里讨论它的图像特征作为通用主干的长处与代价（深度、几何弱）。
- CLIP 的图像嵌入是 DALL·E 2 的生成条件，DALL·E 2 自述 CLIP 嵌入不绑定属性与物体，与本页 ARO 的发现是同一个问题的两面，见[视觉生成方向](../generation/README.md)；ARO §2 也推测 Imagen 组合性更好是因为它用 T5 而非 CLIP 作文本编码器。
- [LLaVA](../../papers/llava/README.md) 取 CLIP ViT-L/14 倒数第二层的网格特征作视觉输入；[OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 拼接 SigLIP 与 DINOv2，冻结视觉编码器时成功率明显下降。VLM 一侧的后续由[视觉语言模型方向](../vlm/README.md)接手。
- SigLIP 2 的自蒸馏与遮蔽预测来自 DINO、iBOT 一系（[DINO 精读](../../papers/dino/README.md)），EVA-CLIP 的初始化来自遮蔽图像建模（[MAE 精读](../../papers/mae/README.md)是同类方法）：对比学习与视觉自监督在 2023 年后合流。
- DataComp、缩放定律与 LAION 的"数据决定缩放曲线"，与[观点页：深度学习的规模化](../../../perspectives/scaling.md)中数据质量的讨论相呼应。

**出处（本库没有单篇目录的论文与材料）**

- Fang 等 2022，Data Determines Distributional Robustness in CLIP：https://arxiv.org/abs/2205.01397
- Goh 等 2021，Multimodal Neurons in Artificial Neural Networks（Distill，排版攻击一节）：https://distill.pub/2021/multimodal-neurons/
- Minderer 等 2021，Revisiting the Calibration of Modern Neural Networks：https://arxiv.org/abs/2106.07998 ；LeVine 等 2023，Enabling Calibration in the Zero-Shot Inference of Large Vision-Language Models：https://arxiv.org/abs/2303.12748
- LAION 官方博客，Re-LAION-5B（2024-08-30）：https://laion.ai/blog/relaion-5b/

**未核实 / 待验证**

- Goh 等的排版攻击只核对了 Distill 页面中"Typographic Attacks"一节的图注与正文片段（CLIP RN50-4x，零样本方式下攻击较稳定有效），没有核对其中的成功率数字。
- DFN（Data Filtering Networks）原文未打开，本页只引用 SigLIP 2 Table 1 的数值和注释。FLIP、COYO-700M、WebLI、PaliGemma 原文未打开，只按引用它们的论文描述。
- ALIGN、CoCa 是否公开权重，论文未声明，没有另查；LiT 的公开模型见其脚注中的仓库链接，未逐一核对发布了哪些尺寸。
- 各论文的正式发表会议：ALIGN（ICML 2021）、ARO（ICLR 2023）、DataComp（NeurIPS 2023 数据集与 benchmark 赛道）取自 PDF 首页，其余只核对了 arXiv 版本。
- Stanford Internet Observatory 2023 年 12 月的报告本身没有打开，相关事实只取自 LAION 官方博客。
