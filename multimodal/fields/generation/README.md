# 视觉生成

> 状态：领域入门页 · v1 · 依据 [synthesis.csv](synthesis.csv)（11 篇）

本页是[多模态总目录](../../README.md)下的一个方向。拆分后的基线见 [Baseline 页](BASELINES.md)，问题路线见[路线图](ROADMAP.md)，收录的全部论文见[论文目录](PAPERS.md)。

## 这个领域在解决什么

给一句"一只戴墨镜的柴犬骑自行车"，生成一张从没存在过、却看起来像照片的图；给一段视频的前几帧，续写后面的画面。两件事都要求模型学到图像（或视频）的整个分布，再从中按条件抽样：抽出来的样本要逼真，不同样本之间要有多样性，还要服从给定的文字、类别或已知帧。视觉生成研究的就是怎样学这个分布、怎样高效地抽样，以及用什么网络来计算。这个方向在 2014–2019 年由对抗训练主导，2020 年后转向逐级去噪的扩散模型，目标也从生成单一类别的小图，迁移到按任意文字生成高分辨率图像和视频。

## 主线历史

1. **VAE（2013，Amsterdam）与 GAN（2014，Montréal）**。问题：深度生成模型的似然和后验难以计算，训练要靠近似推断或马尔可夫链采样。VAE 把变分下界重参数化，用一个神经网络编码器近似后验，整个模型可以直接用随机梯度训练；GAN 换一条路，让生成器与判别器对抗，只靠反向传播和前向采样，不需要写出似然。两者留下的问题不同：VAE 原文只在 MNIST 和 Frey Face 上验证；GAN 原文主实验用多层感知机，作者自述没有显式的分布表示，判别器与生成器必须同步训练，否则生成器会把许多输入映射到同一张图（模式坍缩）。
2. **DCGAN（2015，indico 与 FAIR）**。留下的问题：把 GAN 换成卷积网络、扩大到真实图像的尝试一直不成功，训练常常发散。改变：经大量探索找到一组能稳定训练的全卷积结构（去掉全连接和池化层、使用批归一化等），在 300 多万张 LSUN 卧室图上训练。作者仍自述训练更久时部分滤波器会坍缩。此后几年，GAN 在多数图像生成任务上保持最好的样本质量（ADM 第 1 节的概括），但多样性不足、训练常坍缩的问题一直存在。
3. **DDPM（2020，UC Berkeley）与 Score SDE（2020，Stanford 与 Google Brain）**。留下的问题：GAN 难训练、覆盖不全分布，而似然模型样本质量落后。DDPM 把生成拆成从纯噪声出发的逐级去噪，训练目标是预测加进去的噪声，CIFAR10 无条件生成 FID 3.17；去噪网络是卷积残差块为主、在 16×16 分辨率处加自注意力的 U-Net。Score SDE 把加噪写成连续时间的随机微分方程，证明 DDPM 与多噪声分数匹配是两种 SDE 的离散化，CIFAR-10 FID 降到 2.20，并首次用这类模型生成 1024×1024 的人脸。两篇留下同一个问题：采样要顺序调用网络很多次，比 GAN 慢；在 ImageNet、LSUN 这类更难的数据上仍不及 BigGAN-deep。
4. **ADM（2021，OpenAI）**。留下的问题：扩散模型只在 CIFAR-10 上领先。作者假设差距来自 GAN 的结构被反复打磨过，以及 GAN 能用多样性换保真度。改变：一轮 U-Net 结构消融，加上分类器引导（采样时用一个在带噪图像上训练的分类器的梯度，把样本推向目标类别）。ImageNet 256×256 类条件生成 FID 从 BigGAN-deep 的 6.95 降到 4.59。benchmark 的主战场随之从 CIFAR-10 迁到 ImageNet 类条件生成。
5. **LDM（2021，LMU Munich、Heidelberg 与 Runway）**。留下的问题：像素空间扩散训练常需数百 GPU 天，ADM 每次前向约 1120 Gflops（DiT 原文 Fig.2 的统计）。改变：先用自编码器把图像压到低维潜空间，再在潜空间里扩散；U-Net 仍以二维卷积为主，加交叉注意力（以图像特征为查询、以文本编码为键和值）接入条件，ImageNet 类条件 FID 3.60，计算更少，并在 LAION-400M 上训练了文本到图像模型。代码和模型公开，DiT 原文把它作为 Stable Diffusion 的出处引用。
6. **DALL·E 2（OpenAI）与 Imagen（Google），2022：目标转向文本到图像**。留下的问题：类别标签只能指定 1000 种东西，人想用任意文字描述画面。DALL·E 2 先由一个先验根据文字生成 CLIP 图像嵌入，再由扩散解码器根据嵌入生成图像；Imagen 改用只在文本上预训练的冻结 T5-XXL 作文本编码器，发现加大语言模型比加大图像扩散模型更能提升画质和图文对齐。在 MS-COCO 上零样本（不在 COCO 上训练）FID 分别为 10.39 和 7.27。评测随之从 ImageNet FID 迁到 COCO 零样本 FID 加人工评测，Imagen 另建了 DrawBench。同年 Google 的 [Video Diffusion](../../papers/video-diffusion/README.md) 把同一套方法扩到视频：把图像 U-Net 扩成空间与时间分解的 3D U-Net，图像和视频联合训练。
7. **DiT（2022 年 12 月 arXiv，UC Berkeley 与 NYU）**。留下的问题：从 DDPM 到 LDM，所有扩散模型都用卷积 U-Net 作主干，这种归纳偏置是否必要？改变：在 LDM 的潜空间里，把 U-Net 换成作用于潜变量块的标准 Transformer。12 个模型的计算量与 FID 相关系数为 −0.93，计算量越大样本越好；最大模型在 ImageNet 256×256 类条件生成上把 FID 从 LDM 的 3.60 降到 2.27。作者把"作为 DALL·E 2、Stable Diffusion 这类系统的主干"列为后续工作。

**与语言生成的对照**。语言生成走的是另一种生成过程：decoder-only Transformer 在离散 token 上逐个预测下一个词（见 [LLM 预训练方向](../../../llm/fields/pretraining/README.md)）；图像生成收敛到在连续潜空间里逐级去噪。两边的共同点在生成过程之外：训练目标都由数据自己提供（下一词、加进去的噪声），主干在 DiT 之后都是 Transformer，计算量越大样本越好；语言模型还直接进入图像生成，Imagen 用 T5-XXL 作文本编码器，DALL·E 2 的先验就是一个带因果 mask 的 decoder-only Transformer。[判断] 两种模态收敛的是主干、训练信号和规模化方式，生成过程本身仍然不同；完整论证见[观点页：生成为何收敛到同样的配方](../../../perspectives/generative-convergence.md)，规模化的总线见[深度学习的规模化](../../../perspectives/scaling.md)。

## 技术地基

- **潜变量模型与变分下界**：VAE 的 ELBO 是理解 DDPM 训练目标的起点（DDPM 可以读成编码器固定为加噪链、只学解码方向的多层 VAE），LDM 的自编码器也带 KL 正则。见 [VAE 讲义](../../../foundations/lessons/16-vae.md)第 4 节。
- **扩散：加噪、预测噪声、逐步采样**：训练时一步造出任意噪声等级的样本，生成时从纯噪声顺序去噪；预测噪声与估计分数只差一个缩放，这是 DDPM 与 Score SDE 能统一的原因。见[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 2–6 节。
- **去噪主干：U-Net 与 Transformer**："怎样生成"和"用什么网络计算"是两层选择。U-Net 的收缩–扩张结构与跨层拼接见 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节；DiT 的切块与自注意力、LDM 的交叉注意力见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 13 节。
- **引导**：分类器引导用外部分类器的梯度推动采样；无分类器引导把同一模型的条件预测与无条件预测按权重组合，沿两者之差多走一步。两者都以多样性换保真度和条件遵循，类条件与文本条件的最好结果几乎都用了它。公式与一个视频上的例子见 [Video Diffusion 精读](../../papers/video-diffusion/reading.md)第 5 节。

## 主要路线与团队偏好

- **对抗训练**（Montréal 的 GAN，indico 与 FAIR 的 DCGAN）。押注：一次前向就出样本，样本锐利。代价：训练不稳定、模式坍缩；ADM 第 1 节指出 GAN 覆盖的多样性少于似然模型，难以扩展到新领域。
- **像素空间扩散加级联超分辨率**（UC Berkeley 的 DDPM，OpenAI 的 ADM，Google 的 Imagen 与 Video Diffusion）。押注：直接在像素上去噪，用多级超分辨率模型提高分辨率。代价：计算量大，采样慢。[判断] Imagen 与 Video Diffusion 出自同一批 Google 作者（Ho、Salimans、Chan、Norouzi、Fleet 同时署名两篇），在潜空间方案 LDM 已发表之后，两篇仍都留在像素空间，并都以滥用和偏见风险为由不发布模型或代码。
- **潜空间扩散**（LMU Munich、Heidelberg 与 Runway 的 LDM；UC Berkeley 与 NYU 的 DiT 沿用它的潜空间）。押注：先压缩，把大部分计算放在低维潜空间里，降低训练和采样成本。代价：LDM 自述需要像素级精度时，自编码器的重建能力会成为瓶颈。这条路线的两篇都公开了代码（LDM 还公开了模型），但出自不同团队，按"同一团队两篇以上"的标准不算团队偏好。
- **借判别模型的表示来控制生成**（OpenAI 的 ADM 与 DALL·E 2）。押注：用一个现成的判别模型（分类器、CLIP）提供条件和方向。代价：ADM 的分类器引导只适用于有标注的数据；DALL·E 2 自述 CLIP 嵌入不显式绑定属性与物体，在要把两种颜色分别绑定到两个方块的提示上会弄混（Sec.7、Fig.14）。[判断] Dhariwal 与 Nichol 同时署名两篇：ADM 在第 7 节提出用带噪 CLIP 以文字引导生成，DALL·E 2 则直接以 CLIP 图像嵌入为条件，同一团队在两篇中重复了"让判别模型的表示驱动生成"这一选择。

## 用什么衡量进展

benchmark 的替换就是这个领域目标的迁移：

- **FID**（生成样本与真实样本在 Inception 网络特征空间中的分布距离，越低越好）是贯穿全线的指标，测试对象却一路在变：CIFAR-10 无条件生成（DDPM 3.17、Score SDE 2.20）→ ImageNet 256×256 类条件生成（BigGAN-deep 6.95 → ADM-G 4.59 → LDM 3.60 → DiT 2.27）→ MS-COCO 零样本文本到图像（DALL·E 2 10.39、Imagen 7.27）。
- **文本条件之后的人工评测**：Imagen 指出 FID 与人的感知不完全一致，CLIP 分数（用 CLIP 衡量图文相似度）不善于计数，于是加入人工评测，并新建 DrawBench，按组合、计数、空间关系、长文本、罕见词等类别出题，衡量条件遵循。DALL·E 2 与 GLIDE 的人工对比也分写实度、描述匹配、多样性三项。
- **视频**：Video Diffusion 在 UCF101 无条件生成、BAIR 机器人推动与 Kinetics-600 视频预测上报告 FVD（FID 在视频上的对应：在视频动作识别网络的特征空间里比较分布）与 Inception Score。
- **口径问题**：FID 对参考集和实现细节敏感，DDPM 的 3.17 相对训练集计算，相对测试集为 5.24，DiT 统一用 ADM 的评测代码重算；类条件和文本条件的最好结果都用了引导，引导强度改变的是保真度与多样性之间的取舍；Video Diffusion 自述各论文的数据预处理不总一致。生成质量、条件遵循和物理一致性是三种能力，各需单独的评测。

## 当前开放问题

- **采样能否少走几步？** 每一篇扩散论文都自述采样比 GAN 慢。Score SDE 给出的概率流 ODE 可以用通用求解器自适应采样；flow matching 直接回归把噪声推向数据的速度场，直线路径训练和采样更快，机器人里的 π0.5 已用它生成连续动作。入口：[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6.1 节、[Flow Matching 原文](https://arxiv.org/abs/2210.02747)、[VLA 讲义](../../../robotics-embodied/fields/vla.md)第六节。
- **自动指标怎样跟上条件生成？** FID 衡量分布距离，衡量不了是否听懂了文字。DALL·E 2 第 7 节自述属性绑定和文字渲染较弱；Imagen 第 3 节指出 FID 与感知不完全一致、CLIP 分数不善于计数，于是转向人工评测和 DrawBench。入口：[Imagen 原文](https://arxiv.org/abs/2205.11487)、[DALL·E 2 原文](https://arxiv.org/abs/2204.06125)。
- **视频生成能否成为可以规划的世界模型？** 好看的视频不等于符合物理、能跟随动作；世界模型要建模"执行某个动作之后会发生什么"。入口：[Video Diffusion 精读](../../papers/video-diffusion/reading.md)第 7 节、[世界模型方向](../world-models/README.md)、[LaDi-WM](../../papers/arxiv-2505.11528/README.md)、[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](../../papers/arxiv-2603.17808/README.md)。

## 阅读顺序

1. [VAE 讲义](../../../foundations/lessons/16-vae.md)：先弄清变分下界里的重建项和 KL 项，DDPM 的训练目标从这里来。
2. [扩散讲义](../../../foundations/lessons/17-diffusion.md)：用一个数字走一遍加噪、预测噪声和逐步采样，再读第 6 节的分数与 flow matching。
3. [DDPM 精读](../../papers/ddpm/README.md)：主线第 3 个节点的原文。读完可以做一个检验：用单个带噪样本说明 DDPM 要预测什么，再说明条件输入会怎样改变采样过程。
4. [Video Diffusion 精读](../../papers/video-diffusion/README.md)：同一套方法扩到视频，并把分类器无关引导和重建引导讲清楚；它也接到[视频与时序方向](../video-temporal/README.md)。
5. [Diffusion Policy 精读](../../../robotics-embodied/papers/diffusion-policy/README.md)：被去噪的对象从图像换成机器人动作序列，看同一个生成机制在控制中要额外处理什么。

## 批注

**易误读**

- DDPM 的 FID 3.17 相对训练集计算，相对测试集为 5.24（DDPM Table 1、Sec.4.1）。
- ADM-G 的 4.59 是 250 步采样的结果；与上采样扩散模型结合后为 3.94（ADM Table 5、Abstract）。DiT 的 2.27 用了无分类器引导（DiT Table 2）。
- Imagen 的 7.27 与 DALL·E 2 的 10.39 都是 MS-COCO 零样本 FID，但前者是 FID-30K、引导权重按 Imagen Table 1 的设置；两篇的人工评测协议不同，不能直接合并比较。
- GAN 原文的主实验用多层感知机，只有一个 CIFAR-10 版本用了卷积判别器和"反卷积"生成器（GAN Fig.2）；能稳定训练的卷积 GAN 结构来自 DCGAN。
- DDPM 中的中间状态 xₜ 与图像同维，不是 LDM 那样压缩后的潜变量；"潜空间扩散"专指 LDM 一类先压缩再扩散的做法。
- 扩散时间与视频帧时间是两根不同的时间轴（Video Diffusion 精读开头的图）。

**判断的支撑论文**（各行见 [synthesis.csv](synthesis.csv)）

- Google 一批作者留在像素空间并不发布模型：Imagen Sec.1、Sec.4.1、Sec.6；Video Diffusion Sec.1、Sec.6（首页作者均为 google.com 邮箱）。边界：DDPM 的 Ho 当时在 UC Berkeley，DDPM 公开了代码，所以"不发布"是这批作者 2022 年的选择，不是同一个人一贯的做法。
- OpenAI 借判别模型表示驱动生成：ADM Sec.4、Sec.7；DALL·E 2 Abstract、Sec.2、Sec.7。反例：同属 OpenAI 的 CLIP 本身公开了权重，而 DALL·E 2 未声明发布，开放程度并不一致。
- "与语言生成收敛在主干与规模化"：DiT Sec.1 与 Fig.8（Transformer 主干、计算量与 FID 相关 −0.93）、Imagen Sec.1（语言模型规模比扩散模型规模更重要）、DALL·E 2 Sec.2.2（decoder-only Transformer 先验）。边界：LDM、Imagen、Video Diffusion 仍是卷积 U-Net 主干，收敛发生在 2022 年末之后。

**与其他论文的关联**

- U-Net 本是为几十张图的医学分割设计的编码–解码结构，见[视觉表征方向](../visual-representation/README.md)与 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节；DDPM、LDM、Imagen、Video Diffusion 都沿用它作去噪主干，DiT 才换成 Transformer。
- DALL·E 2 以 [CLIP](../../papers/clip/README.md) 的图像嵌入为条件，视觉表征方向的图文弱监督由此进入生成。
- [Diffusion Policy](../../../robotics-embodied/papers/diffusion-policy/README.md) 把 DDPM 的去噪机制用于动作序列；[VLA 讲义](../../../robotics-embodied/fields/vla.md)第六节讲 π0.5 的 flow matching 动作头。
- [DDPM 精读](../../papers/ddpm/reading.md)第 3 节写出了噪声预测与分数的缩放关系，是主线第 3 个节点"两篇可以统一"的推导。

**未核实 / 待验证**

- Stable Diffusion 本身的发布材料（模型卡、训练数据）没有打开；本页只按 DiT 原文的引用，把 LDM 视为它的出处。
- DCGAN 论文正文未声明代码发布，实际发布情况没有另查。DALL·E 2 论文未声明代码或权重发布。
- DiT 的正式发表会议没有核实，本页只写 arXiv 时间 2022 年 12 月。
- Video Diffusion 首页没有印出单位，本页按作者邮箱写作 Google。
- GLIDE、DDIM、无分类器引导原文（Ho 与 Salimans）本轮没有打开，本页只引用其他论文对它们的描述。
