# 语言、图像、视频的生成收敛到相近的配方：由数据出题的生成式目标、Transformer 主干、规模化

> 状态：观点 · 草稿 · 2026-10-04
>
> 速览：
> - 三种模态的生成在 2018–2024 年先后收敛到三个共同成分：由数据本身出题的训练目标、Transformer 主干、大规模预训练；生成过程按数据形态分成两类，离散 token 用自回归，连续信号用扩散或流匹配。
> - 视频生成有四种基本做法：时空分解的卷积 U-Net（2022）、在图像潜空间模型上插时间层（2023）、时空 patch 上的 Transformer（2023–2024）、视频 token 上的自回归语言模型（2021–2023）；2024 年之后的大模型几乎都落在"压缩到时空潜空间 + Transformer + 扩散或流匹配"上。
> - 2024–2026 年最强的视频模型多在公司手中（Google 的 Veo、OpenAI 的 Sora、字节跳动的 Seedance、快手的 Kling），官方报告写清了大方向，参数量、数据规模和训练细节大多不公开；腾讯的 HunyuanVideo 与阿里的 Wan 公开了权重和较完整的技术报告。
> - 做视频生成的团队把"世界模拟"写成了目标，世界模型的新主力也多出自视频生成团队（DeepMind 的 Genie 系列）；他们追求的可交互、长时一致、可编辑，正是视频生成做不好的地方。
> - 每个阶段都有清楚的失败场景：早期视频只有几秒、低分辨率；之后是长时不一致、物理不对（玻璃不会碎、吃东西不留痕）、写不对字、数不清物体；世界模型则卡在记忆只有几十秒到一分钟、动作空间窄。

## 一句话

三种模态的生成在 2018–2024 年间先后收敛到三个共同成分：一个由数据本身出题、同时就是生成过程的训练目标，一个可以规模化的主干，以及大规模预训练。[判断] 收敛发生在训练配方上，生成过程本身按数据形态分成两类：离散的 token 序列用自回归逐个生成，连续的信号（图像、视频、机器人动作）用从噪声出发的逐级去噪或流匹配。视频在 2024 年完成主干收敛之后，最前沿的团队把目标从"生成好看的片段"推向"模拟一个能交互的世界"。

## 驱动力

**1. 生成式目标本身就是自监督信号（语言 2018 年起，图像 2020 年起，视频 2022 年起）**

下一词预测不需要标注：文本的下一个词就是答案，训练形式与使用形式一致。扩散模型的训练目标是预测加进图像里的噪声，答案同样由数据和人为加的噪声给出，生成时把这个预测反复用于去噪（[DDPM 精读](../multimodal/papers/ddpm/reading.md)、[扩散讲义](../foundations/lessons/17-diffusion.md)）。Video Diffusion Models（2022，Google）的作者写明，视频生成基本沿用标准的高斯扩散形式，改动只在为适应加速器内存而做的结构调整上（[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md)第 1–3 节）。这一点让生成模型直接接上了[规模化](scaling.md)的总线：训练数据的量只受原始数据限制。

**2. 主干统一带来可共享的训练配方和规模化性质（2022 年起）**

DiT 的作者把"架构统一"列为用 Transformer 替换 U-Net 的理由（[视觉生成领域页](../multimodal/fields/generation/README.md)的 DiT 节点）。同年的 Whisper（OpenAI 的语音识别模型）给出同样的理由。到了视频，Meta 的 Movie Gen（2024）写得最直接：主干"紧密遵循 LLaMa3"的 Transformer 块，有意保持与大语言模型相似，以便放心地扩大规模；OpenAI 的 Sora 技术报告（2024）把"视觉 patch 之于 Sora，就像文本 token 之于大语言模型"作为方法的出发点（[Sora 技术报告卡](../multimodal/papers/sora-tech-report/README.md)）。

**3. 规模化行为可以预测（2020 年起）**

语言模型的损失随参数、数据、算力呈幂律下降（Kaplan 等 2020，见[训练科学页](../cross-domain/fields/training-science/README.md)）；DiT 的 12 个模型中，计算量与 FID（生成样本与真实样本在 Inception 网络特征空间中的分布距离，越低越好）的相关系数为 −0.93；SD3（2024）报告验证损失随模型规模和训练步数平滑下降，图像和视频都未见饱和；Wan（2025）在摘要中称其 14B 模型展示了视频生成随数据和模型规模的规模定律（[Wan 卡](../multimodal/papers/arxiv-2503.20314/README.md)）。可预测的扩展让"把同一配方做大"成为一个可以规划的投入。

**4. 压缩到潜空间，让高维连续信号的生成算得起（2021 年起）**

像素空间的扩散训练常需数百 GPU 天。LDM（2021）先用自编码器把图像压到低维潜空间再做扩散，DiT 又在这个潜空间里把潜变量切块成 token。视频把压缩扩展到时间轴：Sora 训练一个"在时间和空间上都压缩"的网络，再切成时空 patch；Wan 的视频 VAE 把时间压 4 倍、长宽各压 8 倍；Seedance 1.0 的 VAE 压缩比设为时间 4 倍、长宽各 16 倍。[判断] 潜空间加切块，在连续信号上起到了文本分词的作用：把原始数据变成长度可控、可以交给同一个主干的序列。

**5. 算力与产品集中到公司（2022 年起，视频最明显）**

[判断] 2022 年之后，最强的视频模型由少数公司训练，多数不发布权重，技术报告只写方向。腾讯的 HunyuanVideo 报告（2024）开篇就说，领先的视频生成模型仍是闭源的，开源与闭源之间出现了明显的能力差距，并在图 2 对比两边的训练算力（[HunyuanVideo 卡](../multimodal/papers/arxiv-2412.03603/README.md)）；OpenAI 的 Sora 报告明说"模型与实现细节不包含在本报告中"。这让本页 2024 年之后的证据，只能以官方报告和模型卡为准。

## 先交代基础：视频生成的四种基本做法

结论：视频比图像多出一根时间轴，四种做法的分歧都在"时间怎样处理、算力花在哪"。2024 年之后，第三种（时空 patch 上的 Transformer）与第二种的潜空间压缩合流，成为大模型的默认结构。

| 做法 | 时间怎样处理 | 代表（年份，团队） | 当时做不好的场景（原文证据） |
|---|---|---|---|
| **时空分解的 U-Net**（像素空间，常配级联超分辨率） | 帧内用 1×3×3 卷积和空间注意力，帧间插入时间注意力；整块帧一起去噪 | [Video Diffusion](../multimodal/papers/video-diffusion/README.md)（2022，Google）；[Imagen Video](../multimodal/papers/arxiv-2210.02303/README.md)（2022，Google）：1 个基础模型 + 3 个空间超分 + 3 个时间超分，共 7 个扩散模型、116 亿参数，生成 1280×768、24 帧/秒、128 帧（约 5.3 秒） | Video Diffusion 主要在 64×64 上评测，自述相对更高分辨率的工作可能处于劣势；Imagen Video 一次只能生成约 5.3 秒，最高分辨率的超分模型为省内存和算力改成全卷积、不用注意力（Sec.2.3） |
| **在图像潜空间模型上插时间层** | 冻结预训练的图像 LDM，只训练新插入的时间层，让各帧"对齐"成连贯视频 | Align your Latents（2023，LMU Munich 与 NVIDIA）：把 Stable Diffusion 变成最高 1280×2048 的文本到视频模型 | 引言自述此前的视频扩散模型大多只能生成低分辨率的短视频；附录 B 自述生成结果尚不能与真实视频区分 |
| **时空 patch 上的 Transformer**（视频 DiT） | 把压缩后的视频切成时空 patch，作为 Transformer 的 token；用窗口或分解注意力控制计算 | W.A.L.T（2023，Google 与 Stanford）；[Sora](../multimodal/papers/sora-tech-report/README.md)（2024，OpenAI） | W.A.L.T 引言指出此前所有视频扩散方法都用 U-Net，因为全注意力的内存随序列长度平方增长；它自己生成的是 512×896、8 帧/秒、3.6 秒 |
| **视频 token 上的自回归** | 先用 VQ 类分词器把视频压成离散 token，再像语言模型一样逐个预测 | VideoGPT（2021，UC Berkeley）；VideoPoet（2023，Google）：decoder-only Transformer，用 MAGVIT-v2 分词视频、SoundStream 分词音频，最大 8B | VideoGPT 自述在 UCF-101 上很快过拟合，认为该数据集相对数据复杂度太小（Sec.4.5）；VideoPoet 自述分词的重建质量给画质设了上限，小物体与精细细节在大幅运动时仍难生成（Sec.5.6） |

[判断] VideoPoet 的引言给出了自回归一侧的处境：语言模型在文本到视频上的质量尚未达到视频扩散模型的水平，它的优势在于能直接复用语言模型的基础设施和多任务训练方式。2024 年之后，自回归在视频生成的主模型里退到次要位置，却在世界模型里以"按帧往后生成"的形式回来（见"从视频生成到世界模型"）。

## 阶段

### 阶段一：各模态各用各的生成器（2014–2019）

**上一阶段留下的问题**：深度生成模型的似然难以计算，要靠近似推断或马尔可夫链；语言的序列到序列任务需要专门的结构。

**本阶段的变化与各领域的表现**：

- 语言：Seq2seq（2014）与 Transformer（2017）都是 encoder–decoder，做的是以源句为条件的翻译生成（[Transformer 精读](../llm/papers/transformer/reading.md)）。2018–2019 年三条路线并存：GPT 用 decoder-only 加下一词预测，BERT 用 encoder-only 加遮蔽预测，T5 把所有任务统一成文本到文本，在其微调设定下 encoder–decoder 加去噪最好（[预训练领域页](../llm/fields/pretraining/README.md)）。
- 图像：GAN（2014）让生成器与判别器对抗训练，只靠反向传播；DCGAN（2015）找到能稳定训练的全卷积结构（[视觉生成领域页](../multimodal/fields/generation/README.md)的 GAN 节点）。
- 视频：Video Diffusion 在 BAIR 机器人推物数据集（给 1 帧、预测后 15 帧的视频预测 benchmark）上的对照表里同时列着两类此前的方法：GAN 一类（DVD-GAN、TrIVD-GAN）和"先离散化、再用 Transformer 自回归生成"一类（VideoGPT）。

**做不好的场景**：GAN 原文与 DCGAN 都自述训练不稳定和模式坍缩（生成器把许多不同输入映射到同一类输出）；LDM 第 1 节概括，GAN 的好结果主要局限于变化较少的数据。视频一侧，VideoGPT 引言把视频生成进展慢归因于时空相关的高维建模与算力需求。

### 阶段二：目标收敛（2019–2022）

**上一阶段留下的问题**：图像生成的对抗训练不稳定；语言里哪种结构和目标最好，结论随评测设定而变。

**本阶段的变化与各领域的表现**：

- 语言收敛到 decoder-only。GPT-3（2020）只靠提示中的几个示例完成任务（in-context learning，不更新权重）。BigScience 的对照实验（Wang 等 2022）解开了 T5 与 GPT-3 看起来矛盾的结论：只做无监督预训练后直接零样本评测，因果 decoder-only 最好；加多任务微调后，encoder–decoder 最好（[预训练领域页](../llm/fields/pretraining/README.md)）。
- 图像收敛到扩散。DDPM（2020）用逐级去噪替代对抗训练，CIFAR10 无条件生成的 FID 为 3.17；去噪网络是 PixelCNN++ 式的 U-Net（对称的编码–解码卷积网络，跨层拼接补回细节）。LDM（2021）在潜空间里保留这种卷积主干，用交叉注意力接入文本等条件。
- 视频沿用图像的配方。Video Diffusion Models（2022）把图像扩散的 U-Net 扩成在空间和时间上分解的 3D U-Net，同一个网络把时间注意力屏蔽掉就能当图像模型，于是可以图像、视频联合训练；在 BAIR 视频预测上，它的 FVD（视频版的 FID，用视频动作识别网络 I3D 的特征计算，越低越好）为 66.92，对照表中此前最好的 NUWA 为 86.9。同年的 Imagen Video 把这一结构做成 7 个模型的级联，用 1400 万对视频–文本加 6000 万对图像–文本的内部数据，再加 LAION-400M 训练（[视频与时序领域页](../multimodal/fields/video-temporal/README.md)）。

**做不好的场景**：采样慢，DDPM 生成一张图要调用网络 1000 次；视频只有几秒、低分辨率（Video Diffusion 以 64×64 为主，Imagen Video 约 5.3 秒）；文本条件下的属性绑定、计数和文字渲染差（DALL·E 2、Imagen、Parti 的自述，见[视觉生成领域页](../multimodal/fields/generation/README.md)第 7 个节点）。LDM 的作者还认为，扩散模型的生成能力部分来自 U-Net 对图像类数据的归纳偏置，留下"卷积主干是否必要"的问题。

### 阶段三：主干收敛（2022–2023）

**上一阶段留下的问题**：所有扩散模型都用卷积 U-Net 作主干；视频若改用 Transformer，全注意力的内存随 token 数平方增长。

**本阶段的变化与各领域的表现**：

- 图像：DiT（2022）在 LDM 的潜空间里把 U-Net 换成作用于潜变量块的标准 Transformer，ImageNet 256×256 类条件 FID 从 LDM 的 3.60 降到 2.27。到这里，语言与图像的生成都用 Transformer 主干。
- 视频：W.A.L.T（2023）给出视频侧的同一步：用因果编码器把图像和视频压进同一个潜空间，再用窗口注意力的 Transformer 去噪，在 UCF-101 与 Kinetics-600 上不用无分类器引导就达到当时最好。Align your Latents（2023）走另一条更省的路：直接复用公开的 Stable Diffusion，只训练时间层。VideoPoet（2023）则证明 decoder-only 语言模型也能生成有竞争力的视频。

**做不好的场景**：分辨率和时长仍受限（W.A.L.T 3.6 秒、8 帧/秒）；自回归一侧受分词器上限约束（VideoPoet Sec.5.6）；评测仍以 UCF-101、Kinetics 上的 FVD 为主，衡量不了文字遵循与物理。

### 阶段四：规模化与产品化，视频生成交到公司手里（2024–2026）

**上一阶段留下的问题**：视频 Transformer 的结构已经可行，剩下的是能否像语言模型那样，靠更大的模型、更多的数据和更长的上下文得到质变。

**本阶段的变化**：2024 年 2 月 OpenAI 的 Sora 技术报告把三件事合在一起：时空压缩网络、时空 patch、扩散 Transformer，在原生长宽比和时长上训练，生成最长一分钟的高清视频。此后各家的官方报告几乎都落在同一套骨架上，差别转到数据、后训练（偏好对齐与强化学习）、音频与多模态条件、加速。下表只列官方报告、官方博客、官方模型卡里明确写出的内容。

| 团队 | 模型与时间 | 官方写明的结构 | 官方写明的数据 | 官方自述做不好的场景 | 官方没写（开放问题） |
|---|---|---|---|---|---|
| OpenAI | [Sora](../multimodal/papers/sora-tech-report/README.md)，2024 年 2 月技术报告 | 时空同时压缩的视频压缩网络；时空潜变量 patch 作 token；扩散 Transformer；图像当作单帧视频联合训练；用 DALL·E 3 的重新标注技术给全部视频生成详细描述，用 GPT 扩写用户提示 | 只写"大量带描述的视频"，并在原生分辨率、时长、长宽比上训练 | 不能准确模拟玻璃破碎等基本交互的物理；吃东西不总能留下正确的状态变化；长视频会逐渐不连贯，物体会凭空出现 | 参数量、数据规模与来源、算力、压缩比、采样步数（报告明说不含模型与实现细节） |
| OpenAI | Sora 2，2025 年 9 月 30 日发布页 | 只写是"旗舰级音视频生成模型"，能遵循跨多个镜头的复杂指令并保持世界状态一致，同步生成对白与音效 | 未写 | 页面自述"远非完美"；以投篮为例说早期模型会扭曲现实去满足指令（没投进的球被"传送"进篮筐），Sora 2 会让球从篮板弹开 | 结构、数据、规模全部未写；同一页面注明 Sora 产品已于 2026 年 4 月 26 日停止提供 |
| Google DeepMind | [Veo 3](../multimodal/papers/veo3-tech-report/README.md)，2025 年 5 月技术报告与模型卡（模型卡 2026 年 1 月更新，覆盖后续版本） | 潜空间扩散，同时对音频的时间潜变量和视频的时空潜变量去噪；去噪网络基于 Transformer | 图像、视频、音频及其标注；用多个 Gemini 模型生成不同详细程度的描述；按安全、合规与质量过滤，跨来源做语义去重；用 TPU、JAX 训练 | 技术报告：文字生成仍差，常有小幻觉，偏爱电影感镜头与频繁切镜；模型卡：复杂场景或复杂运动中保持完整一致仍是挑战；产品页：短语音片段的自然一致仍在改进 | 参数量、数据规模、压缩比、采样步数；Veo 3.1 的结构变化 |
| Meta | Movie Gen，2024 年 10 月 | 30B 参数 Transformer，紧密遵循 LLaMa3 的块设计；流匹配训练；最长上下文 73K 个视频 token，对应 16 秒、16 帧/秒 | 约 O(100)M 段视频与 O(1)B 张图像联合预训练 | 自述现有自动指标在文字对齐、视觉质量与真实感三项上都不可靠，必须靠人工评测 | 是否开放权重（HunyuanVideo 报告称其开源时间尚未确定） |
| 腾讯混元 | [HunyuanVideo](../multimodal/papers/arxiv-2412.03603/README.md)，2024 年 12 月，开源 | 因果 3D VAE；先双流（视频、文本 token 分开处理）再单流（拼接后联合处理）的 Transformer，13B；用 decoder-only 多模态大模型作文本编码器；流匹配 | 数十亿图文对分级过滤；视频分五个阶段逐步提高分辨率（256×256×65 帧到 720×1280×129 帧）；最后用 100 万条人工标注的高质量片段微调 | 自述随意扩大数据、算力、参数"效率不够"，需要专门的缩放策略；60 位评测者、1533 条提示的人工对比中，文字对齐与视觉质量都有对照模型更高（CNTopB、Luma1.6），优势主要在运动质量 | 视频数据总量 |
| 阿里通义万相 | [Wan](../multimodal/papers/arxiv-2503.20314/README.md)（Wan2.1），2025 年 3 月 arXiv，开源 | Wan-VAE（3D 因果 VAE，时间压 4 倍、长宽各压 8 倍）；扩散 Transformer + 流匹配；umT5 文本编码器；14B 与 1.3B 两种规模（1.3B 只需 8.19 GB 显存） | 数十亿张图像与视频 | 大幅运动场景中保持细节仍是难题（也是全领域的问题）；14B 模型在单张高端 GPU 上不加优化生成一段视频约需 30 分钟；教育、医疗等专门场景表现可能不足 | 结构、数据流程、权重均公开；训练总算力本轮未在报告中找到 |
| 字节跳动 Seed | [Seedance 1.0](../multimodal/papers/arxiv-2506.09113/README.md)，2025 年 6 月 | VAE 压缩（时间 4 倍、长宽 16 倍）并用判别器损失训练；空间层与时间层解耦的扩散 Transformer，空间层采用 SD3 的 MMDiT；微调过的 decoder-only 大模型作文本编码器；流匹配；三个奖励模型（基础、运动、美学）做 RLHF；多阶段蒸馏，加速约 10 倍 | 多来源视频，多阶段筛选与均衡，配精确的视频描述 | 引言把当前模型的共同难题写成"提示遵循、运动合理与画质三者难以兼顾"；未单列局限 | 参数量、数据规模 |
| 字节跳动 Seed | [Seedance 2.0](../multimodal/papers/arxiv-2604.14148/README.md)，2026 年 2 月在中国发布，4 月技术报告 | 只写"统一、高效、大规模的音视频联合生成架构"，支持文本、图像、音频、视频四种输入；4–15 秒、480p 与 720p | 未写 | 轻微形变伪影、边缘情形的运动合理性、高频噪声、音频失真、多人说话时口型错位；物理规律类考题对所有被测模型都难；编辑任务共同的失败是没响应编辑或改动了不该改的区域；续写中颜色不一致、主体遗漏或重复 | 结构、参数量、数据全部未写 |
| 快手可灵 | [Kling-Omni](../multimodal/papers/arxiv-2512.16776/README.md)（Kling-O1），2025 年 12 月 | 多模态大模型做提示增强；Omni-Generator 在共享嵌入空间里处理视觉与文本 token；多模态超分辨率；指令预训练、监督微调、强化学习；蒸馏到 10 步采样 | 自建覆盖参考生成、编辑、多图参考等任务的数据体系 | 引言列出现有视频模型的三个短板：任务割裂、只靠文本描述不了精确的空间关系与视觉参照、缺乏对物理与逻辑的理解 | 参数量、数据规模；Kling 3.0 的结构 |

**做不好的场景**：三类问题贯穿各家自述。其一，物理与状态变化（Sora 的玻璃与汉堡、Seedance 2.0 的物理规律考题、Wan 的大幅运动）。其二，长时一致性（Sora 的长视频不连贯、Veo 3 模型卡的复杂场景一致性、Seedance 2.0 续写中的主体遗漏或重复）。其三，文字与符号（Veo 3 报告"文字生成仍差"；Wan 把"首个能同时生成中英文画面文字的模型"列为四个主要特点之一）。评测本身也成了问题：Movie Gen 与 Seedance 2.0 都改以人工评测和分项考题为主，FVD 不再是主要指标。

## 从视频生成到世界模型

结论：[判断] 2024–2026 年，世界模型的新主力多出自视频生成团队。他们把视频生成器改造成"给一个动作、生成下一帧"的模拟器，关心的是视频生成做不好的三件事：可交互（实时响应动作）、长时一致（离开视野的物体回来时还在、关键符号不变）、可编辑（用文字改变正在运行的世界）。

**谁在做，从哪里来。** 证据来自官方材料里的自我定位和作者名单：

- OpenAI 把 Sora 技术报告直接命名为"视频生成模型作为世界模拟器"，结论是继续扩大视频模型是通向物理世界与数字世界通用模拟器的可行路径。报告作者 Bill Peebles 是 DiT 的第一作者，报告也引用 DiT 作为 Sora 的主干来源。`[历史]`
- Google DeepMind 的 Genie 3 博客把 Veo 2、Veo 3 与 Genie 1、Genie 2 并列为"世界模拟"的不同能力维度。博客两位署名作者中，Jack Parker-Holder 是 Genie 原文的共同第一作者，Shlomi Fruchter 是 GameNGen（用扩散模型实时模拟游戏 DOOM）的作者之一；Genie 3 的主要贡献者名单里有 W.A.L.T 第一作者 Agrim Gupta，以及 Genie 原文引用的视频模型 Phenaki 的第一作者 Villegas。`[历史]`
- NVIDIA 的 [Cosmos](../multimodal/papers/arxiv-2501.03575/README.md)（2025）把"世界基础模型"直接做成视频生成模型：同时提供扩散和自回归两类 Transformer，从约 2000 万小时原始视频中筛出约 1 亿段片段训练，开放权重。
- 快手 Kling-Omni 自称是通向"多模态世界模拟器"的关键一步；Seedance 2.0 把后续方向写成"生成模型与物理世界的深度对齐"。

**三件事各做到哪里、卡在哪里。**

| 能力 | 代表与官方做到的 | 官方自述做不好的场景 |
|---|---|---|
| **可交互**（每一步接收动作，生成下一帧） | [Genie](../multimodal/papers/arxiv-2402.15391/README.md)（2024 年 2 月）：11B 参数，从 20 万小时网络游戏视频中筛出 3 万小时 2D 平台游戏，不用任何动作标注，无监督学出 8 个"潜在动作"，逐帧可控。Genie 2（2024 年 12 月）：3D 世界，键盘鼠标操作，结构是"自回归的潜空间扩散模型"，用带因果 mask 的 Transformer 逐帧生成，并用无分类器引导增强动作可控性。Genie 3（2025 年 8 月）：输入文字即生成世界，720p、24 帧/秒实时交互。GameNGen（2024）：单张 TPU 上以 20 帧/秒运行 DOOM | Genie：约 1 帧/秒，离实时很远；Genie 2：实时版本是蒸馏模型，画质下降；Genie 3：智能体能直接执行的动作范围仍然有限，多个独立智能体之间的复杂交互仍难模拟 |
| **长时一致**（物体离开视野再回来仍在，屏幕上的数字与文字不乱） | Sora 报告：物体被遮挡或出画后常能保持（"并不总是"）；Genie 2：一致的世界最长约一分钟，多数示例 10–20 秒；Genie 3：数分钟内基本一致，视觉记忆可回溯约一分钟，且这种一致性是涌现的，没有 NeRF、高斯泼溅那样的显式 3D 表示 | Genie：只有 16 帧记忆，长时一致很难，会"幻想"出不现实的未来；GameNGen：只能看到 3 秒多的历史，部分游戏状态靠屏幕上的弹药、血量数字保留，容易构造出记忆不够的情形；Genie 3：清晰的文字通常只在输入描述里写明时才会出现，连续交互只能支撑几分钟；Cosmos：缺乏物体永久性 |
| **可编辑**（用文字改变正在运行的世界，或改一段已有视频） | Genie 3 的"可提示的世界事件"：在交互中用文字改变天气、加入新物体和角色；Sora 支持视频续写、循环与 SDEdit 式改风格；Seedance 2.0、Kling-Omni 把参考生成与编辑做进同一个模型 | Seedance 2.0 报告：所有被测模型共同的失败是没响应编辑，或改动了不该改的区域；Genie 3：世界事件不一定由智能体自己执行 |
| **物理合理** | Veo 3 被用作通用视觉模型：Google DeepMind（2025）用 18,384 段生成视频测了 62 个定性任务和 7 个定量任务，Veo 3 能零样本做分割、边缘检测、走迷宫等，从 Veo 2 到 Veo 3 提升明显 | 同一论文的失败案例：深度图只能分出前景背景，不会按给定的力或轨迹箭头运动，打绳结时出现不可能的绳子运动，不认识字母网格里的单词；Cosmos：接触丰富的动力学不准，更大的模型画质更好，在物理对齐测试上却没有更好 |

[判断] 视频生成团队转向世界模型，延续的是同一套技术，换掉的是目标与评价标准。技术上，Genie 2、GameNGen 都直接沿用视频扩散或潜空间扩散，再把"动作"作为条件按帧自回归；目标上，从"一段片段看起来真"变成"任意动作序列下都前后一致"，于是长时记忆、动作空间和实时速度成了新的瓶颈。机器人一侧的世界模型（预测"执行这个动作之后会发生什么"以便规划）关心的是同一件事，只是动作换成了机械臂的控制量，见[多模态世界模型方向](../multimodal/fields/world-models/README.md)与[机器人世界模型讲义](../robotics-embodied/fields/world-models.md)；在冻结视觉特征上做规划的 [DINO-WM](../multimodal/papers/arxiv-2411.04983/README.md)、用潜空间扩散预测操作结果的 [LaDi-WM](../multimodal/papers/arxiv-2505.11528/README.md)、把视频世界模型与可执行动作对齐的 [EVA](../multimodal/papers/arxiv-2603.17808/README.md) 是那条线上的入口。

## 收敛与分化

**走向同一种做法的地方**

- 训练信号：三种模态都用数据本身出题，再做大规模预训练；视频之后再加偏好对齐与强化学习（Seedance 1.0 的三类奖励模型、Kling-Omni 的强化学习阶段）。
- 主干：语言与图像在 2022 年、视频在 2024 年落到 Transformer 上（decoder-only 语言模型；DiT；Sora、Movie Gen、Veo 3、HunyuanVideo、Wan、Seedance）。论证见 [CNN 与 Transformer](cnn-vs-transformer.md)。
- 训练目标的细节：2024 年后的开源与半开源视频报告（Movie Gen、HunyuanVideo、Wan、Seedance 1.0）都写明用流匹配；Movie Gen 自述流匹配对噪声日程的选择更稳健，并优于扩散损失。
- 条件接入：文本编码器从 CLIP、T5 转向 decoder-only 大语言模型或多模态大模型（HunyuanVideo、Seedance 1.0、Kling-Omni），短提示由语言模型扩写（Sora、Kling-Omni 的提示增强）。
- 输入先变成 token：文本分词，图像与视频压到潜空间再切块，机器人动作在一些模型里也被编码成离散 token（[VLA 领域页](../robotics-embodied/fields/vla.md)第七节的 FAST）。

**仍然不同的地方**

- **生成过程。** 语言的主流仍是自回归。DFlash（2026）的作者写道，扩散语言模型可以并行生成，但目前通常不如自回归模型（[DFlash 文献卡](../llm/papers/arxiv-2602.06036/README.md)）。视频的主模型一次对一整段做去噪，世界模型则按帧自回归、每步去噪（Genie 2），π0.5 在一个模型里同时用两种方式（[VLA 领域页](../robotics-embodied/fields/vla.md)第六、七节）。[判断] 分界线是数据形态与使用方式：离散 token 适合逐个预测，连续信号适合从噪声逐步修正，需要实时响应动作时再沿时间轴自回归。
- **开放程度。** 腾讯、阿里、NVIDIA 公开权重与较完整的报告；Google、OpenAI、字节跳动、快手通过产品或 API 提供模型，报告不给参数量与数据规模；Imagen Video、Genie 都明确选择不发布模型。
- **评测。** 语言用零样本与少样本任务成绩；图像用 FID 加分项考题；视频从 FVD 转向人工评测、竞技场排名和分项考题（Seedance 1.0 引用 Artificial Analysis 排行榜，Veo 3 用 Meta 发布的 MovieGenBench 做人工对比）。各家用的提示集和评测者不同，数字不能跨报告比较。

## 当前开放问题

- **视频有没有像语言那样可外推的规模定律？** Wan 摘要称展示了随数据和模型规模的规律，HunyuanVideo 自述随意扩大不够高效、要专门的缩放策略，Cosmos 发现更大的模型画质更好、物理却没有更好。入口：[训练科学页](../cross-domain/fields/training-science/README.md)、[Wan 卡](../multimodal/papers/arxiv-2503.20314/README.md)、[Cosmos 卡](../multimodal/papers/arxiv-2501.03575/README.md)。
- **像素上的逼真能否换来物理上的正确？** Sora、Veo 3、Cosmos、Seedance 2.0 都把物理列为短板，Veo 3 的零样本论文给出了具体失败任务。入口：[Veo 3 卡](../multimodal/papers/veo3-tech-report/README.md)、[世界模型领域页](../multimodal/fields/world-models/README.md)。
- **长时记忆靠什么？** Genie 从 16 帧到 Genie 3 的约一分钟视觉记忆，GameNGen 只有 3 秒；官方都没有说明记忆机制。入口：[Genie 卡](../multimodal/papers/arxiv-2402.15391/README.md)、[机器人世界模型讲义](../robotics-embodied/fields/world-models.md)。
- **公司模型的哪些细节决定了差距？** Sora、Sora 2、Veo 3、Seedance 2.0、Kling 的参数量、数据规模与训练算力都未公开，开源报告（HunyuanVideo、Wan）是目前唯一能逐项对照的证据。入口：本页阶段四的表。
- **自回归与扩散会不会统一成一种生成过程？** 入口：[DFlash 文献卡](../llm/papers/arxiv-2602.06036/README.md)、[视觉生成领域页](../multimodal/fields/generation/README.md)的 VAR 节点。

## 批注

**判断的支撑与反例**

- **收敛在配方，生成过程按数据形态分两类。** 支撑：GPT-3 Sec.1 与 Sec.5、Wang 等 2022 Sec.4–5（语言收敛到因果 decoder）；DDPM Sec.1、LDM Sec.1、DiT Sec.1（图像收敛到扩散与 Transformer）；Sora 报告、Movie Gen Sec.1、Veo 3 技术报告（视频收敛到潜空间 + Transformer + 扩散或流匹配）；DFlash 摘要。反例或边界：VideoPoet 用纯自回归生成视频并报告有竞争力的结果；VAR 在 ImageNet 类条件生成上用自回归报告了最好的 FID；VLA 里也有离散动作 token 的自回归模型（[OpenVLA 精读](../robotics-embodied/papers/openvla/reading.md)）。所以"连续信号用去噪"是主流倾向，不是必然。
- **潜空间加切块起到了分词的作用。** 支撑：LDM Sec.1、DiT Sec.3.1、Sora 报告"Turning visual data into patches"一节（明确类比文本 token）、Wan 与 Seedance 1.0 的 VAE 一节。反例或边界：Video Diffusion、Imagen Video 留在像素空间，用分解注意力和级联超分控制计算量；潜空间方案受自编码器的重建精度限制（LDM Sec.5、SD3 Sec.5.2.1）。
- **最强视频模型集中在公司手中。** 支撑：HunyuanVideo 摘要与 Sec.1、Fig.2（闭源领先、算力差距）；Sora 报告不含实现细节；Imagen Video Sec.4、Genie Sec.5 选择不发布模型。反例或边界：Wan 报告称 14B 模型在内部与外部评测上超过当时的开源与商业模型，HunyuanVideo 的人工评测中排名第一（对照模型匿名），开源与闭源的差距在 2025 年明显缩小；"最热门"本身没有统一口径。
- **世界模型的新主力出自视频生成团队，关心可交互、一致、可编辑。** 支撑：Sora 报告标题与结论；Genie 3 博客把 Veo 与 Genie 并列，作者与贡献者名单（Parker-Holder、Fruchter、Gupta、Villegas）；GameNGen 作者名单；Cosmos 摘要与 Fig.1；Kling-Omni 摘要；Seedance 2.0 Sec.1。反例或边界：DreamerV3 一类基于强化学习的世界模型（[DreamerV3](../multimodal/papers/dreamerv3/README.md)）和 DINO-WM 一类在冻结表征上学动力学的工作，出发点是控制与规划；Genie 1 的动机写的是强化学习缺少丰富多样的训练环境（Sec.5），关键词含开放式学习（Open-Endedness），它同时借用了视频生成的结构（Sec.1 自述建立在当时的视频生成模型之上）。"主力"是就 2024–2026 年受关注的大模型而言，不是全部世界模型研究。
- **视频生成团队转向世界模型，延续技术、换掉目标。** 支撑：Genie 2 博客"Diffusion world model"一节、GameNGen 摘要（扩散模型以过去帧和动作为条件生成下一帧）、Genie 3 博客"Environmental consistency over a long horizon"一节（自回归逐帧生成比一次生成整段更难，误差会累积）。反例或边界：Genie 1 用的是 MaskGIT 式的离散 token 预测，不是扩散。

**易误读**

- "CNN 不适应生成任务"只对语言成立。图像生成的主干从 DCGAN 到 DDPM、LDM 长期以卷积为主，DiT（2022）之后才转向 Transformer；视频在 Imagen Video（2022）里仍是卷积 U-Net 加注意力，高分辨率阶段甚至是全卷积。
- 阶段四表中的分辨率、时长和数据描述都来自各家自己的报告，各家的评测提示集、评测者与对照模型不同，排名不能跨报告比较。HunyuanVideo 的对照模型以 CNTopA/B/C 匿名，Wan 的图表也有 CN-TopA/B/C。
- Genie 的"11B"是最终模型的参数量，缩放实验覆盖 4000 万到 27 亿参数；"3 万小时"是从 20 万小时游戏视频中筛出的 2D 平台游戏子集。
- Veo 3 零样本论文中 Veo 3 生成的视频要先经过一个提示改写器（由大语言模型完成），作者自述部分任务的答案可能来自语言模型而不是视频模型，他们为此另测了 Gemini 2.5 Pro 单独能否解题。
- DDPM 的 3.17 相对训练集计算，相对测试集为 5.24；DiT 的 2.27 用了无分类器引导。Video Diffusion 在 BAIR 上的 66.92 用 Langevin 采样 256 步，另有等量的校正步。
- "下一词预测与扩散都是自监督"指训练信号不需要人工标注；文本到图像、文本到视频模型仍需要配对的图文或视频–文字数据，近年还大量依赖模型生成的描述（Sora 的重新标注、Veo 3 用 Gemini 标注）。

**与其他页面的关联**

- [深度学习的规模化](scaling.md) 的阶段三是本页的上层总线；[CNN 与 Transformer](cnn-vs-transformer.md) 讨论主干转向的结构原因。
- [视觉生成领域页](../multimodal/fields/generation/README.md) 是本页图像部分的证据来源，"先看这里"一节解释三大家族；[视频与时序领域页](../multimodal/fields/video-temporal/README.md) 接视频理解一侧。
- [DDPM 精读](../multimodal/papers/ddpm/reading.md) 与[扩散讲义](../foundations/lessons/17-diffusion.md) 讲去噪目标怎么算；[Video Diffusion 精读](../multimodal/papers/video-diffusion/reading.md) 第 2 节有分解时空注意力的计算量推导，是"四种基本做法"第一种的细节。
- [多模态世界模型方向](../multimodal/fields/world-models/README.md)、[机器人世界模型讲义](../robotics-embodied/fields/world-models.md) 与 [DreamerV3](../multimodal/papers/dreamerv3/README.md) 是"从视频生成到世界模型"一节的另一端。
- [VLA 领域页](../robotics-embodied/fields/vla.md) 是"离散与连续两种生成过程在一个模型里共存"的实例。

**出处（本库没有单篇目录的材料，正文链接到领域页节点或卡片）**

- GAN：https://arxiv.org/abs/1406.2661 ；DCGAN：https://arxiv.org/abs/1511.06434 ；LDM：https://arxiv.org/abs/2112.10752 ；DiT：https://arxiv.org/abs/2212.09748 ；SD3：https://arxiv.org/abs/2403.03206 ；Whisper：https://arxiv.org/abs/2212.04356
- Seq2seq：https://arxiv.org/abs/1409.3215 ；BERT：https://arxiv.org/abs/1810.04805 ；T5：https://arxiv.org/abs/1910.10683 ；Wang 等 2022：https://arxiv.org/abs/2204.05832 ；Kaplan 等：https://arxiv.org/abs/2001.08361
- Video Diffusion Models：https://arxiv.org/abs/2204.03458 ；Align your Latents：https://arxiv.org/abs/2304.08818 ；W.A.L.T：https://arxiv.org/abs/2312.06662 ；VideoGPT：https://arxiv.org/abs/2104.10157 ；VideoPoet：https://arxiv.org/abs/2312.14125 ；Movie Gen：https://arxiv.org/abs/2410.13720
- Sora 2 发布页：https://openai.com/index/sora-2/ ；Veo 产品页：https://deepmind.google/models/veo/ ；Veo 3 模型卡：https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf
- Genie 2 博客：https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/ ；Genie 3 博客：https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/ ；GameNGen：https://arxiv.org/abs/2408.14837 ；Video models are zero-shot learners and reasoners：https://arxiv.org/abs/2509.20328

**未核实 / 待验证**

- Kling 3.0、Veo 3.1、Seedance 1.5 的官方技术细节本轮没有找到或没有打开；Kling 3.0 与 Veo 3.1 只作为 Seedance 2.0 报告与 Veo 产品页中的名字出现。
- Seedance 2.0 报告没有写架构；"基于扩散 Transformer"等说法只见于第三方页面，本页不写。
- Sora 2 系统卡（OpenAI 发布页链接的"Sora 2 System Card"）本轮没有打开。
- Genie 3 的结构、参数量与数据，官方博客只说明逐帧自回归生成，其余未写。
- Movie Gen 的权重是否已发布，本页只依据 HunyuanVideo 报告（2024 年 12 月）的说法，之后的情况没有另查。
- Whisper 目前没有对应的领域页节点或单篇目录。
