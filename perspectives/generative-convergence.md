# 语言、图像、视频的生成收敛到相近的配方：由数据出题的生成式目标、Transformer 主干、规模化

> 状态：观点 · 草稿 · 2026-10-04

## 一句话

三种模态的生成在 2018–2022 年间先后收敛到三个共同成分：一个由数据本身出题、同时就是生成过程的训练目标，一个可以规模化的主干，以及大规模预训练。[判断] 收敛发生在训练配方上，生成过程本身按数据形态分成两类：离散的 token 序列用自回归逐个生成，连续的信号（图像、视频、机器人动作）用从噪声出发的逐级去噪。主干的收敛在语言里最早完成，在图像里到 DiT（2022）才完成；视频在本库现有的证据里停在"卷积 U-Net 加时空注意力"这一步，再往后是开放问题。

## 驱动力

**1. 生成式目标本身就是自监督信号（语言 2018 年起，图像 2020 年起，视频 2022 年起）**

下一词预测不需要标注：文本的下一个词就是答案，训练时预测下一词，使用时也是逐词生成，训练形式与使用形式一致。扩散模型的训练目标是预测加进图像里的噪声，答案同样由数据和人为加的噪声给出，生成时把这个预测反复用于去噪（[DDPM 精读](../multimodal/papers/ddpm/reading.md)、[扩散讲义](../foundations/lessons/17-diffusion.md)）。Video Diffusion Models（2022，Google）的作者写明，视频生成基本沿用标准的高斯扩散形式，改动只在为适应加速器内存而做的结构调整上（[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)第 1–3 节）。这一点让生成模型直接接上了[规模化](scaling.md)的总线：训练数据的量只受原始数据限制。

**2. 主干统一带来可共享的训练配方和规模化性质（2022 年起）**

DiT 的作者把"架构统一"列为用 Transformer 替换 U-Net 的理由：图像生成可以沿用其他领域为 Transformer 积累的训练配方，并继承它的规模化性质（[视觉生成领域页](../multimodal/fields/generation/README.md)的 DiT 节点）。同年的 Whisper（OpenAI 的语音识别模型）给出同样的理由：选用 encoder–decoder Transformer，是因为这种结构已被验证能可靠地扩展。

**3. 规模化行为可以预测（2020 年起）**

语言模型的损失随参数、数据、算力呈幂律下降（Kaplan 等 2020，见[训练科学页](../cross-domain/fields/training-science/README.md)）；DiT 的 12 个模型中，计算量（Gflops）与 FID（生成样本与真实样本在 Inception 网络特征空间中的分布距离，越低越好）的相关系数为 −0.93。可预测的扩展让"把同一配方做大"成为一个可以规划的投入。

**4. 压缩到潜空间，让高维连续信号的生成算得起（2021 年起）**

像素空间的扩散训练常需数百 GPU 天。LDM（2021）先用自编码器把图像压到低维潜空间再做扩散，DiT 又在这个潜空间里把潜变量切块成 token。[判断] 潜空间加切块，在连续信号上起到了文本分词的作用：把原始数据变成长度可控、可以交给同一个主干的序列。视频一侧，Video Diffusion 留在像素空间，靠把注意力分解成空间和时间两步来控制计算量。

## 阶段

### 阶段一：各模态各用各的生成器（2014–2019）

**上一阶段留下的问题**：深度生成模型的似然难以计算，要靠近似推断或马尔可夫链；语言的序列到序列任务需要专门的结构。

**本阶段的变化与各领域的表现**：

- 语言：Seq2seq（2014）与 Transformer（2017）都是 encoder–decoder，做的是以源句为条件的翻译生成（[Transformer 精读](../llm/papers/transformer/reading.md)）。2018–2019 年三条路线并存：GPT 用 decoder-only 加下一词预测，BERT 用 encoder-only 加遮蔽预测，T5 把所有任务统一成文本到文本，在其微调设定下 encoder–decoder 加去噪最好（[预训练领域页](../llm/fields/pretraining/README.md)）。
- 图像：GAN（2014）让生成器与判别器对抗训练，只靠反向传播；DCGAN（2015）找到能稳定训练的全卷积结构。两篇都自述训练不稳定和模式坍缩（生成器把许多不同输入映射到同一张图）（[视觉生成领域页](../multimodal/fields/generation/README.md)的 GAN 节点）。
- 视频：Video Diffusion 在 BAIR 机器人推物数据集（给 1 帧、预测后 15 帧的视频预测 benchmark）上的对照表里同时列着两类此前的方法：GAN 一类（DVD-GAN、TrIVD-GAN）和"先离散化、再用 Transformer 自回归生成"一类（VideoGPT，题名即"用 VQ-VAE 与 Transformer 生成视频"）。

**留下的问题**：图像生成的对抗训练不稳定；语言里哪种结构和目标最好，结论随评测设定而变。

### 阶段二：目标收敛（2019–2022）

**本阶段的变化与各领域的表现**：

- 语言收敛到 decoder-only。GPT-3（2020）的 1750 亿参数 decoder-only 模型只靠提示中的几个示例完成任务（in-context learning，不更新权重），它自述的局限正是 T5 的强项：没有双向结构和去噪目标（[GPT-3 精读](../llm/papers/gpt3/reading.md)）。BigScience 的对照实验（Wang 等 2022）解开了 T5 与 GPT-3 看起来矛盾的结论：只做无监督预训练后直接零样本评测，因果 decoder-only 最好；加多任务微调后，encoder–decoder 最好。此后 PaLM、LLaMA 都是因果语言模型（[预训练领域页](../llm/fields/pretraining/README.md)）。
- 图像收敛到扩散。DDPM（2020）用逐级去噪替代对抗训练，CIFAR10 无条件生成的 FID 为 3.17（相对训练集）；去噪网络是 PixelCNN++ 式的 U-Net（一种对称的编码–解码卷积网络，跨层拼接补回细节），以卷积残差块为主，在 16×16 分辨率处加自注意力。LDM（2021）在潜空间里保留这种卷积主干，用交叉注意力接入文本等条件，在 LAION-400M（公开的约 4 亿对网页图文数据集）上训练了文本到图像模型（[视觉生成领域页](../multimodal/fields/generation/README.md)）。
- 视频沿用图像的配方。Video Diffusion Models（2022）把图像扩散的 U-Net 扩成在空间和时间上分解的 3D U-Net：每个 3×3 卷积改成只在帧内运算的 1×3×3 卷积，每个空间注意力块之后插入一个跨帧的时间注意力块；同一个网络把时间注意力屏蔽掉就能当图像模型，于是可以图像、视频联合训练。在 BAIR 视频预测上，它的 FVD（视频版的 FID，用视频动作识别网络 I3D 的特征计算，越低越好）为 66.92，对照表中此前最好的 NUWA 为 86.9。文本条件用的是语言模型 BERT-large 的句子嵌入，采样时用无分类器引导（沿条件预测与无条件预测之差的方向多走一步，让样本更符合条件），与文本到图像的做法相同（[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)第 2、5、6 节；[视频与时序领域页](../multimodal/fields/video-temporal/README.md)）。

**留下的问题**：所有扩散模型都用卷积 U-Net 作主干，这种归纳偏置是否必要？LDM 的作者认为扩散模型的生成能力部分来自 U-Net 对图像类数据的归纳偏置。

### 阶段三：主干收敛（2022 年起）

**本阶段的变化与各领域的表现**：

- 图像：DiT（2022）在 LDM 的潜空间里把 U-Net 换成作用于潜变量块的标准 Transformer，最大模型在 ImageNet 256×256 类条件生成上把 FID 从 LDM 的 3.60 降到 2.27，计算量越大 FID 越低（[视觉生成领域页](../multimodal/fields/generation/README.md)的 DiT 节点）。到这里，语言与图像的生成都用 Transformer 主干。
- 视频：本库目前收录的视频生成证据止于 Video Diffusion Models（2022）。视频生成的主干是否也换成了 Transformer、时空 token 怎样组织，列入开放问题。

## 收敛与分化

**走向同一种做法的地方**

- 训练信号：三种模态都用数据本身出题，再做大规模预训练。
- 主干：语言与图像都落在 Transformer 上（decoder-only 语言模型；DiT）。论证见 [CNN 与 Transformer](cnn-vs-transformer.md)。
- 条件与采样技巧跨模态共用：无分类器引导同时用于类条件图像（DiT 的 2.27）、文本到图像和文本到视频；视频模型的文本条件直接取自预训练语言模型 BERT 的嵌入。
- 输入先变成 token：文本分词，图像压到潜空间再切块（LDM、DiT），机器人动作在一些模型里也被编码成离散 token（[VLA 领域页](../robotics-embodied/fields/vla.md)第七节的 FAST）。

**仍然不同的地方**

- **生成过程。** 语言的主流仍是自回归。DFlash（2026）的作者写道，扩散语言模型可以并行生成，但目前通常不如自回归模型；他们只把一个小型块扩散模型用作草稿器，由自回归的目标模型并行验证（[DFlash 文献卡](../llm/papers/arxiv-2602.06036/README.md)）。图像与视频的主流是逐级去噪。视频模型把两者组合起来：一个视频块内部联合去噪，块与块之间自回归地向后延长（[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)第 5 节）。π0.5 在一个模型里同时用两种方式：文字子任务自回归解码，低层连续动作用流匹配（从噪声出发、沿学到的向量场把样本搬到数据分布）生成（[VLA 领域页](../robotics-embodied/fields/vla.md)第六、七节）。[判断] 两类生成过程的分界线是数据形态：离散 token 适合逐个预测，连续信号适合从噪声逐步修正。
- **卷积的位置。** 图像生成的主干长期以卷积为主（DCGAN、DDPM、LDM），换成 Transformer 之后，卷积仍留在入口：DiT 用现成的卷积 VAE 把图像压成潜变量。
- **评测。** 语言用零样本与少样本任务成绩；图像用 FID；视频用 FVD。三者都对实现细节敏感：DiT 统一用 ADM（OpenAI 的像素空间扩散模型）的评测代码重算 FID；Video Diffusion 在 Kinetics-600（约 40 万段、600 类人类动作视频）上只改变真值片段的抽样方式，FVD 就从 16.2 变到 16.9。

## 当前开放问题

- **视频生成的主干是否也转向 Transformer，时空 token 怎样组织？** Video Diffusion 的作者提到，分解的时空注意力在视频 Transformer 里已被证明计算上划算，他们把它放进了卷积 U-Net。之后的大规模视频生成系统本库尚未收录原文。入口：[视频与时序领域页](../multimodal/fields/video-temporal/README.md)、[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)。
- **自回归与扩散会不会统一成一种生成过程？** 入口：[DFlash 文献卡](../llm/papers/arxiv-2602.06036/README.md)、[VLA 领域页](../robotics-embodied/fields/vla.md)（π0.5 的离散与连续两条支路）。
- **生成得像，离能用于控制的世界模型有多远？** Video Diffusion 在 BAIR 上的设置是给首帧预测后续帧，机器人未来的动作没有作为可控输入，也没有测物体永久性和接触动力学。入口：[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)第 7 节、[世界模型领域页](../multimodal/fields/world-models/README.md)。
- **扩散模型有没有像语言那样的规模定律？** DiT 给出的是 12 个模型上计算量与 FID 的相关，没有拟合出随参数、数据、算力变化的幂律。入口：[训练科学页](../cross-domain/fields/training-science/README.md)、[视觉生成领域页](../multimodal/fields/generation/README.md)。

## 批注

**判断的支撑论文与反例**

- **收敛在配方，生成过程按数据形态分两类。** 支撑：GPT-3 Sec.1 与 Sec.5、Wang 等 2022 Sec.4–5（语言收敛到因果 decoder）；DDPM Sec.1、LDM Sec.1、DiT Sec.1（图像收敛到扩散，再到 Transformer 主干）；Video Diffusion Sec.1、Sec.3（视频沿用图像扩散）；DFlash 摘要（扩散语言模型目前通常不如自回归）；π0.5（见 VLA 领域页，离散文字与连续动作分开生成）。反例或边界：视频曾有离散化后自回归生成的路线（VideoGPT，在 BAIR 上不如 Video Diffusion，但这只是一个 benchmark 上的一次比较）；VLA 里也有把动作离散成 token、用自回归生成的模型（RT-2、OpenVLA，见 [OpenVLA 精读](../robotics-embodied/papers/openvla/reading.md)），所以"连续信号用去噪"是主流倾向，不是必然。
- **潜空间加切块起到了分词的作用。** 支撑：LDM Sec.1（为降低像素空间扩散的计算成本而压缩）、DiT Sec.3.1（在卷积 VAE 的潜空间里切块）。反例或边界：Video Diffusion 留在像素空间，用分解注意力而不是潜空间压缩来控制计算量；潜空间方案受自编码器的重建精度限制（LDM Sec.5 自述超分辨率已受此限制）。

**易误读**

- "CNN 不适应生成任务"只对语言成立。图像生成的主干从 DCGAN 到 DDPM、LDM 长期以卷积为主，DiT（2022）之后才转向 Transformer；视频在 Video Diffusion（2022）里仍是卷积 U-Net 加注意力。
- GAN 原文的主实验用多层感知机，只有一个 CIFAR-10 版本用了卷积判别器和"反卷积"生成器；能稳定训练的卷积 GAN 结构来自 DCGAN。
- DDPM 的 3.17 相对训练集计算，相对测试集为 5.24；DiT 的 2.27 用了无分类器引导。Video Diffusion 在 UCF101 上报告的 FID 用的是视频网络 C3D 的特征，不能与图像 FID 横向比较。
- Video Diffusion 的 BAIR 结果 66.92 用 Langevin 采样 256 步，另有等量的校正步；它是在无条件训练的模型上用引导方法做视频预测。
- "下一词预测与扩散都是自监督"指训练信号不需要人工标注；文本到图像、文本到视频模型仍需要配对的图文或视频–文字数据。

**与其他页面的关联**

- [深度学习的规模化](scaling.md) 的阶段三是本页的上层总线；[CNN 与 Transformer](cnn-vs-transformer.md) 讨论主干转向的结构原因。
- [DDPM 精读](../multimodal/papers/ddpm/reading.md) 与[扩散讲义](../foundations/lessons/17-diffusion.md) 讲去噪目标怎么算；[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md) 第 2 节有分解时空注意力的计算量推导。
- [VLA 领域页](../robotics-embodied/fields/vla.md) 是"离散与连续两种生成过程在一个模型里共存"的实例。

**出处（本库没有单篇目录的论文，正文链接到领域页节点）**

- GAN：https://arxiv.org/abs/1406.2661 ；DCGAN：https://arxiv.org/abs/1511.06434 ；LDM：https://arxiv.org/abs/2112.10752 ；DiT：https://arxiv.org/abs/2212.09748 ；Whisper：https://arxiv.org/abs/2212.04356
- Seq2seq：https://arxiv.org/abs/1409.3215 ；BERT：https://arxiv.org/abs/1810.04805 ；T5：https://arxiv.org/abs/1910.10683 ；GPT：https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf ；Wang 等 2022：https://arxiv.org/abs/2204.05832 ；PaLM：https://arxiv.org/abs/2204.02311 ；LLaMA：https://arxiv.org/abs/2302.13971 ；Kaplan 等：https://arxiv.org/abs/2001.08361
- Video Diffusion Models 原文：https://arxiv.org/abs/2204.03458 （v2 PDF 第 3 节、表 2、第 4.3 节与附录 A 本轮逐段核对）
- VideoGPT（只作为 Video Diffusion 表 2 中的对照出现，本轮未打开原文）：https://arxiv.org/abs/2104.10157

**未核实 / 待验证**

- Video Diffusion（2022）之后的视频生成系统，包括采用 Transformer 主干的大规模视频模型，本轮没有打开原文，正文只把它们写成开放问题。
- VideoGPT 的结构只依据它的题名，NUWA 只作为 Video Diffusion 表 2 中此前最好的对照出现；两篇原文都没有打开核对。
- DiT 关于 Gflops 与 FID 的相关只覆盖 ImageNet 256×256 上的 12 个模型；扩散模型的规模定律本库没有收录专门研究。
- Whisper 目前没有对应的领域页节点或单篇目录。
