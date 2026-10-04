# Transformer 靠通用性与可规模化成为通用主干，CNN 在数据少、算力小和端侧场景仍然占优

> 状态：观点 · 草稿 · 2026-10-04

## 一句话

CNN 与 Transformer 用同一套残差连接传递梯度，真正的差别在归纳偏置（结构里预先写入的关于数据的假设）：卷积把局部性和平移等变写进每一层，数据少时帮忙，数据多时成为限制；自注意力在第一层就让每个位置读取全部位置，并把文本、图像块、音频统一成 token。[判断] Transformer 成为通用主干，主要靠跨模态的统一和大规模下可以预测的扩展，单看精度解释不了；在 ImageNet 规模下，配上现代训练配方的 CNN 仍能追平，两者差距的相当部分来自训练配方与数据。这是[深度学习的规模化](scaling.md)总线上的一段。

## 驱动力

**1. 数据规模改变了归纳偏置的价值（2020 年起，视觉识别）**

- `[结构]` 卷积核只连局部、在所有位置共用，因此平移等变：输入平移几个像素，特征图跟着平移同样的距离。感受野随层数线性增长：每层 3×3、步长 1 的卷积向外多看 1 个像素，L 层的感受野是 (2L+1)×(2L+1)；要覆盖 224 像素宽，需要 2L+1 ≥ 224，即 L = 112 层，实际网络靠下采样加快扩张。自注意力第一层就让每个图像块读取全部图像块。ViT 原文 3.1 节写的正是这一区别：CNN 的每一层都内置局部性、二维邻域和平移等变，ViT 中只有 MLP 层是局部的（[ViT 精读](../multimodal/papers/vit/reading.md)）。
- `[经验]` 先验在小数据时帮忙，在大数据时成为限制：在 JFT-300M（Google 内部约 3 亿张图的标注数据集）的随机子集上预训练，9M 张时 ViT-B/32 明显差于计算量相近的 ResNet50，90M 张以上反超（ViT 4.3 节、Fig.4）。
- `[经验]` 第一层的全局读取确实被用上：ViT 测量了注意力距离（作用类似 CNN 的感受野），最低层已有一些头关注图像的大部分区域，另一些头只看邻近区域；在前面接 ResNet 的混合模型中这类局部头较少，作者据此推测它们承担了 CNN 早期卷积层的作用（ViT 4.5 节、Fig.7）。

**2. 跨模态的统一（2020–2022 年，视觉、生成、音频）**

同一结构处理多种输入：文本 token、图像块（ViT）、图像潜变量块（DiT，见[视觉生成领域页](../multimodal/fields/generation/README.md)的 DiT 节点）、音频频谱（Whisper，OpenAI 2022 年的语音识别模型，选用 encoder–decoder Transformer 的理由是这种结构已被充分验证能可靠地扩展）。`[经验]` token 化的结构也方便自监督：MAE 作者把视觉遮蔽自编码此前落后于语言的原因之一，归于卷积在规则网格上运算、不便加入遮蔽标记和位置嵌入，ViT 消除了这一障碍（MAE 第 1 节，[MAE 精读](../multimodal/papers/mae/reading.md)）。

**3. 可预测的扩展与大规模下的计算效率（2020 年起）**

- 语言模型的损失随参数、数据、算力呈幂律下降（Kaplan 等 2020，见[训练科学页](../cross-domain/fields/training-science/README.md)）；CLIP 的迁移表现是算力的平滑函数（[CLIP 精读](../multimodal/papers/clip/reading.md)）；DiT 的 12 个模型中，计算量（Gflops）与 FID（生成样本与真实样本在 Inception 特征空间中的分布距离，越低越好）的相关系数为 −0.93。
- ViT 达到同样迁移表现所需的预训练计算约为 ResNet 的 1/4 到 1/2（ViT 4.4 节）；CLIP 中 ViT 图像编码器的计算效率约为 ResNet 的 3 倍。

## 阶段

### 阶段一：CNN 是视觉的默认主干（2012–2019）

**上一阶段留下的问题**：手工特征（HOG、DPM）只让最后的分类器学习，PASCAL VOC 检测在 2010–2012 年停滞。**变化**：AlexNet、VGG、GoogLeNet、ResNet 在 ILSVRC（以 ImageNet 约 120 万张图、1000 类为数据的年度分类竞赛）上逐年加深，R-CNN 把 ImageNet 预训练的 CNN 迁移到检测。生成侧，DCGAN 找到能稳定训练的全卷积 GAN，U-Net 的编码–解码结构后来成为扩散模型的去噪主干。**各领域的表现**：视觉识别与生成全部以卷积为主（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)、[视觉生成领域页](../multimodal/fields/generation/README.md)）；Transformer（2017）此时只在语言里，用来解决循环网络无法在同一样本内并行的问题（[Transformer 精读](../llm/papers/transformer/reading.md)）。**留下的问题**：卷积的局部性先验是必需的，还是可以由数据学出来？

### 阶段二：Transformer 进入视觉识别，CNN 用新配方追平（2020–2022）

**变化**：ViT 把图像切块直接交给 Transformer，只在 ImageNet 上训练时不如同规模的 ResNet，在 JFT-300M 上预训练后反超。CLIP 用网页图文对预训练，ViT 编码器比 ResNet 编码器更省算力；MAE 用遮蔽重建让 ViT 在只用 ImageNet-1K 的条件下超过此前最好结果（87.8% 对 87.1%）。随后 ConvNeXt（2022，FAIR）只给 ResNet-50 换上 Transformer 式的训练配方就提升 2.7 个百分点，再借用 Transformer 的若干设计后，在 ImageNet-1K/22K 规模上追平并超过 Swin（一种分层的视觉 Transformer），推理吞吐相当或更高（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)的 ViT 与 ConvNeXt 节点）。**留下的问题**：两者的差距有多少来自架构本身？图像生成的主干此时仍是卷积 U-Net。

### 阶段三：Transformer 进入生成（2022 年起）

**变化**：DDPM 与 LDM 的去噪 U-Net 以卷积残差块为主，只在低分辨率处插入自注意力，LDM 还用交叉注意力接入文本（[DDPM 精读](../multimodal/papers/ddpm/reading.md)）。DiT（2022）在 LDM 的潜空间里把 U-Net 换成标准 Transformer，最大模型在 ImageNet 256×256 类条件生成上把 FID 从 LDM 的 3.60 降到 2.27（[视觉生成领域页](../multimodal/fields/generation/README.md)的 DiT 节点）。**各领域的表现**：视频生成在 Video Diffusion Models（2022）里仍是把图像 U-Net 扩成空间–时间分解的 3D U-Net（[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)第 2 节）；后续走向见[生成的收敛](generative-convergence.md)。

## 收敛与分化

**两类主干共用的部分**

- `[结构]` 梯度通路相同。ResNet 的残差块输出 y = x + F(x)，Transformer 每个子层输出 LayerNorm(x + Sublayer(x))（Transformer 原文 3.1 节），加法跳连是同一形式。对纯加法形式求导，∂y/∂x = I + ∂F/∂x，恒等项 I 给梯度留了一条不经过 F 的通路；F 是卷积分支还是注意力分支，这条通路都存在。归一化放在加法之后（Post-LN）还是分支之内（Pre-LN），影响的是训练稳定性，见[训练科学页](../cross-domain/fields/training-science/README.md)。
- `[结构]` ViT 的切块嵌入就是一个卷积。原文式 (1) 把每个 P×P×C 的图像块展平，乘同一个矩阵 E，这等价于核大小 P×P、步长 P、输出 D 个通道的卷积。以 ViT-B/16 为例：224×224×3 的图像切成 14×14 = 196 块，每块展平为 16·16·3 = 768 维，乘 768×D 的 E；把 E 的每一列重排成 16×16×3 的卷积核，以步长 16 滑过图像，得到 14×14×D 的特征图，逐位置读出就是 196 个块嵌入。
- `[经验]` 混合结构很常见：ViT 原文就定义了从 CNN 特征图切块的混合模型；DiT 用现成的卷积 VAE 把图像压成潜变量；Whisper 的编码器前端是两层卷积。卷积留在了新结构的入口处。

**CNN 仍然占优或常用的地方**

- `[经验]` 数据有限时：ImageNet-1K 或 JFT 的 9M 子集上，ResNet 优于同等计算的 ViT（见驱动力 1）；U-Net 本来就是为只有几十张训练图的医学分割设计的。
- `[经验]` 计算预算小时：ViT 的对照中，前面接 ResNet 的混合模型在小计算预算下略优于纯 ViT，规模变大后差别消失（ViT 4.4 节）。
- [判断] 端侧与实时场景：MobileNet 用深度可分离卷积为手机和嵌入式设备做低延迟模型；EfficientNet 用复合缩放，让 B7 在与 GPipe 同为 84.3% 的 ImageNet 精度下小 8.4 倍、快 6.1 倍；YOLO 用单个卷积网络在 PASCAL VOC 2007 上以每秒 45 帧达到 63.4% mAP（各类别检测平均精度的均值）。三者体现的是 CNN 针对延迟与参数量做过的系统优化（[视觉表征领域页](../multimodal/fields/visual-representation/README.md)的综合表）。

## 当前开放问题

- **架构差异与数据、训练配方、计算量怎样分开？** ViT 与 ConvNeXt、U-Net 与 DiT 两组对照都显示，主干的差别要和数据规模、训练配方、计算量一起看。入口：[ViT 精读](../multimodal/papers/vit/reading.md)、[MAE 精读](../multimodal/papers/mae/reading.md)、[视觉表征领域页](../multimodal/fields/visual-representation/README.md)。
- **端侧与实时场景的 CNN 优势，在与视觉 Transformer 同条件对比时还成立吗？** 本库现有的三篇证据都早于 ViT。入口：[视觉表征领域页](../multimodal/fields/visual-representation/README.md)。
- **注意力的二次方成本，能否换成固定大小的递推状态？** 线性注意力、状态空间模型和 Mamba 都在回答这个问题。入口：[递推状态谱系](../foundations/relations/recurrent-state.md)、[Mamba 精读](../llm/papers/mamba/reading.md)。
- **视频生成的主干会不会也从卷积 U-Net 转向 Transformer？** 入口：[生成的收敛](generative-convergence.md)。

## 批注

**判断的支撑论文与反例**

- **Transformer 胜出主要靠通用性与可规模化。** 支撑：ViT Sec.4.4（预训练计算效率）、CLIP Sec.1 与 Sec.3.2（迁移表现随算力平滑变化，ViT 编码器约 3 倍计算效率）、DiT Sec.1 与 Fig.8（主干统一带来的配方与规模化性质；Gflops 与 FID 相关）、Whisper Sec.2.2（选用 Transformer 是因为它已被验证能可靠扩展）、Kaplan 等 Abstract。反例或边界：ConvNeXt Sec.3、Sec.4 与附录 E，ImageNet-1K/22K 规模下纯 CNN 追平或超过 Swin，推理吞吐相当或更高；LDM Sec.1 认为扩散模型的生成能力部分来自 U-Net 对图像类数据的归纳偏置。
- **差距的相当部分来自训练配方与数据。** 支撑：ConvNeXt（只换训练配方，ResNet-50 提升 2.7 个百分点）；ViT 4.3 节、Fig.3–4（排名随预训练数据量反转）。反例或边界：在 JFT-300M 这类更大规模上，ViT 达到同样表现所需的计算只有 ResNet 的 1/4 到 1/2（ViT 4.4 节），这部分优势在 ConvNeXt 的 ImageNet-22K 规模对照里没有被检验。
- **端侧与实时场景 CNN 占优。** 支撑：MobileNet Sec.1 与 Table 8、EfficientNet Fig.1 与 Table 2、YOLO Table 1。反例或边界：三篇都早于 ViT，没有与视觉 Transformer 做同条件对比；ViT 4.4 节的混合模型只说明小算力下"卷积前端加 Transformer"略优，横轴是预训练计算量，与部署延迟是两回事。

**易误读**

- "CNN 的损失传递受限，所以输给 Transformer"不准确：ResNet 与归一化之后，CNN 的梯度传递已经解决，Transformer 用的是同一套残差（见"收敛与分化"第一条）。
- "CNN 不适应生成任务"要分开说：语言生成由 decoder-only Transformer 主导；图像生成的主干从 DCGAN 到 DDPM、LDM 长期以卷积为主，DiT（2022）之后才转向 Transformer。
- 残差一条的推导针对纯加法形式。原始 Transformer 是 Post-LN，恒等通路要经过 LayerNorm；Pre-LN 把它移进分支，Xiong 等（2020）证明后者初始化时梯度更平稳，可以去掉学习率预热。
- "大矩阵乘法更契合 GPU"单独解释不了 Transformer 取代 CNN：Transformer 相对循环网络的硬件优势是同一样本内可以并行（Transformer 第 1 节）；相对 CNN，ConvNeXt 在 V100、A100 上测得相近 FLOPs 下推理吞吐相当或更高（Table 1、附录 E）。
- ViT 在 ImageNet-1k 上不如 ResNet、在 JFT-300M 上反超，比较的是同等规模的 BiT ResNet，并且都经过迁移微调（ViT 4.3 节、Fig.3）。DiT 的 2.27 用了无分类器引导（Table 2）。

**与其他页面的关联**

- [CNN 讲义](../docs/foundations/11-cnn.md)第 2–3 节讲卷积的局部性与权重共享，第 6 节讲从 LeNet 到 ViT、ConvNeXt 的机制史；[Transformer 讲义](../docs/foundations/14-attention-transformer.md)第 10.2 节讲残差与 LayerNorm 怎样接成一个块。
- [架构概念地图](../foundations/fields/architectures/README.md) 列出两类主干各自依赖的机制；[注意力与 FFN 的分工谱系](../foundations/relations/attention-ffn-division.md) 讲 Transformer 块内部的分工。
- [深度学习的规模化](scaling.md) 给出本页所在的总线；[生成的收敛](generative-convergence.md) 展开生成一侧的主干变化。

**出处（本库没有单篇目录的论文，正文链接到领域页节点）**

- ResNet：https://arxiv.org/abs/1512.03385 ；ConvNeXt：https://arxiv.org/abs/2201.03545 ；MobileNet：https://arxiv.org/abs/1704.04861 ；EfficientNet：https://arxiv.org/abs/1905.11946 ；YOLO：https://arxiv.org/abs/1506.02640 ；U-Net：https://arxiv.org/abs/1505.04597 ；DCGAN：https://arxiv.org/abs/1511.06434
- LDM：https://arxiv.org/abs/2112.10752 ；DiT：https://arxiv.org/abs/2212.09748 ；Whisper：https://arxiv.org/abs/2212.04356 ；Kaplan 等：https://arxiv.org/abs/2001.08361 ；Xiong 等：https://arxiv.org/abs/2002.04745

**未核实 / 待验证**

- Whisper 目前没有对应的领域页节点或单篇目录，本页只在正文中引用它的自述理由；音频方向建页后应改为链接。
- MobileNet 论文只写了"计划发布模型"，实际发布情况没有另查。
- DiT 的正式发表会议没有核对，本页只按 arXiv 时间写 2022 年。
