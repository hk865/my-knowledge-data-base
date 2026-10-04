# 视觉生成

> 状态：领域入门页 · v2 · 依据 [synthesis.csv](synthesis.csv)（20 篇）
>
> 速览：
> - 视觉生成要从随机噪声（加上文字、类别等条件）造出一张从没存在过、看起来却真实的图或一段视频。主流做法分三大家族：GAN（生成器与判别器对抗）、扩散与流匹配（学会一步步去噪）、自回归（把图切成 token，像写字一样逐个写出来）。
> - 2014–2020 年 GAN 的样本最锐利，但训练不稳、会模式坍缩；2021 年扩散模型在 ImageNet 256×256 上把 FID 从 BigGAN-deep 的 6.95 降到 4.59，代价是 DDPM 生成一张图要调用网络 1000 次。
> - 扩散成为主流靠的是 2021–2022 年的三步：压到潜空间降成本（LDM），接上语言模型做文本条件（DALL·E 2、Imagen），主干换成 Transformer（DiT）；流匹配（2022）与 SD3（2024）再把去噪路径拉直，少走几步。
> - 自回归路线一直并行（DALL·E 2021、Parti 2022、VAR 2024）；GAN 的判别器转入自编码器训练和少步蒸馏，作为"挑错"的损失项继续使用。
> - 每一代都有清楚的失败场景：模式坍缩、采样慢、属性绑定错、数不清物体、分不清左右、写不对字。视频、2022 年后的公司模型与世界模型，见续篇[观点页](../../../perspectives/generative-convergence.md)。
> - 2025–2026 年：多模态大模型成为图像生成器的条件编码器（Qwen-Image）甚至生成器本身（HunyuanImage 3.0、GPT-4o 图像生成），生成与编辑并进同一个模型，扩散模型开始用 GRPO 加奖励模型做强化学习；写字大幅改善，但生僻字、长段小字和左右关系仍在 2026 年官方材料的已知局限里（主线第 10 个节点）。

本页是[多模态总目录](../../README.md)下的一个方向。拆分后的基线见 [Baseline 页](BASELINES.md)，问题路线见[路线图](ROADMAP.md)，收录的全部论文见[论文目录](PAPERS.md)。

## 先看这里：生成在做什么，三大家族各是什么

### 生成要解决什么

给一句"一只戴墨镜的柴犬骑自行车"，生成一张从没存在过、却看起来像照片的图；给一段视频的前几帧，续写后面的画面。两件事都要求模型学到图像（或视频）的整个分布，再从中按条件抽样：抽出来的样本要逼真，不同样本之间要有多样性，还要服从给定的文字、类别或已知帧。

把问题缩到最小：一张 256×256 的彩色图是 196,608 个数，真实照片只占这个巨大空间里极小的一片。生成模型的工作，是把一个容易抽的随机数（例如标准高斯噪声）变成落在这片区域里的一组数。三大家族的区别，就在"怎样从噪声走到一张图"。

### 三大家族

**GAN：一个造、一个验，互相逼着变好。** 生成器 G 把随机数 z 变成一张图；判别器 D 看一张图，打分它像不像真的。D 学着把真图和假图分开，G 学着骗过 D。最简单的例子（示例数值）：真实数据是一维的数，集中在 5 附近；G(z) = z + b，起初 b = 0，造出来的数都在 0 附近，D 很快学会"接近 5 才是真的"；G 顺着 D 的打分把 b 往 5 推，直到 D 分不出来。一次前向就出样本，所以快。它做不好的事也能用同一个例子看到：如果真实数据有两堆，一堆在 2、一堆在 8，G 只要把所有输出都放在 8 附近，每个样本都能骗过 D，2 那一堆却再也不出现。这就是**模式坍缩**（生成器把许多不同的输入映到同一类输出，多样性丢失）。GAN 原文第 6 节把它叫作"Helvetica 情形"，要求 D 与 G 同步训练来避免。

**扩散与流匹配：先学会把图弄脏，再学会一步步擦干净。** 训练时往真实图像上逐级加高斯噪声，让网络看着带噪的图预测加进去的噪声；生成时从纯噪声出发，反复减去预测的噪声，几十到上千步之后得到一张图。答案（加进去的噪声）由我们自己造出来，所以训练目标稳定、能覆盖整个分布。用一个数手算的完整过程见[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 2–5 节。流匹配是同一思路的另一种写法：把噪声点和数据点用直线连起来，让网络学"沿这条线该往哪走、走多快"（速度）；讲义第 6.1 节的例子里，噪声 −0.5、数据 2，速度就是 2 −（−0.5）= 2.5。路径越直，生成时需要的步数越少。

**自回归：把图切成 token，像写字一样逐个预测。** 先训练一个分词器（一种自编码器，把图像压成一格一格的离散编号），例如 DALL·E（2021）把 256×256 的图压成 32×32 = 1024 个 token，每个 token 是 8192 个编号之一。之后的做法和语言模型完全一样：把文字 token 和图像 token 排成一条序列，按"已知前面的，预测下一个"训练，生成时从左上角写到右下角。好处是能直接复用语言模型的结构与规模化经验（见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)）；代价是分词会丢细节，1024 个 token 就要顺序预测 1024 次。

### 它们怎样演变、现在用在哪里

```
2014  GAN ──── DCGAN(2015) ──── 主导样本质量到 2020 ───────────→ 退为部件：自编码器的判别器损失、少步蒸馏
2020        DDPM / Score SDE ── ADM(2021) ── LDM(2021) ── DiT(2022) ── 流匹配 / SD3(2024) ──→ 图像与视频的主流
2021        DALL·E(自回归) ── Parti(2022) ── VAR(2024) ───────────→ 与语言模型统一的路线；视频与世界模型中按帧自回归
2025        多模态大模型作条件编码器(Qwen-Image) / 在语言模型内部扩散(HunyuanImage 3.0) ──→ 生成与编辑合一，扩散 + GRPO
```

| 家族 | 当时做不好的场景（原文证据） | 后来怎样补 | 现在用在哪里（原文证据） |
|---|---|---|---|
| GAN | 模式坍缩、需要 D 与 G 同步训练（GAN Sec.6）；训练更久时滤波器坍缩到单一振荡模式（DCGAN Sec.7）；LDM Sec.1 概括其结果主要局限于变化较少的数据 | 结构约束（DCGAN）；最终在 ImageNet 上被扩散模型超过（ADM） | LDM 的自编码器用"感知损失 + 局部块判别器"训练（LDM Sec.3.1）；Seedance 1.0 的视频 VAE 也加了类似 PatchGAN 的判别器（Sec.2.1），蒸馏阶段用判别器纠正加速带来的伪影（Sec.5.1）；ADD 用判别器损失把大扩散模型压到 1–4 步 |
| 扩散 / 流匹配 | 采样慢：DDPM 设 1000 步，在 TPU v3-8 上生成 128 张 256×256 图要 300 秒（附录 B）；像素空间训练常需数百 GPU 天（LDM Sec.1） | 潜空间（LDM）、Transformer 主干（DiT）、直线路径（流匹配、SD3）、蒸馏（ADD） | 图像：SD3 用整流流加 MM-DiT；视频：Veo 3、Sora、HunyuanVideo、Wan、Seedance 1.0 都用潜空间扩散或流匹配加 Transformer（见[观点页](../../../perspectives/generative-convergence.md)） |
| 自回归 | dVAE 重建丢失文字、细线等细节（DALL·E Fig.1）；计数超过 7 个基本不准、左右关系近乎随机（Parti Sec.6.3）；展平成一维后破坏空间邻近、需要 O(n²) 步（VAR Sec.3） | 更好的分词器（Parti 的 ViT-VQGAN）、由粗到细逐尺度预测（VAR） | VideoPoet（2023）用 decoder-only 语言模型生成视频 token；世界模型 Genie（2024）按帧自回归生成，Genie 2 被官方称为"自回归的潜空间扩散模型"：用带因果 mask 的 Transformer 逐帧往后生成潜变量（见[观点页](../../../perspectives/generative-convergence.md)） |

[判断] 三个家族的分工今天大致是：扩散与流匹配负责"把一段连续信号画好"，自回归负责"沿时间或沿序列往后接"，GAN 的判别器负责"挑局部细节的错"。2024 年之后的大模型常把三者组合在一个系统里。[判断] 2025 年起分工上多了一层：语言模型（或多模态大模型）负责"理解要画什么"，扩散负责画；在 HunyuanImage 3.0 和 GPT-4o 图像生成里，这两件事已在同一个网络中完成。判别器在蒸馏中仍在用（Seedream 4.0），在自编码器训练中则出现了去掉它的反例（Qwen-Image、Qwen-Image-2.0，见批注）。

## 主线历史

每个节点写三件事：上一个节点留下的问题、这一节点改变了什么、它自己做不好的场景。

1. **VAE（2013，Amsterdam）与 GAN（2014，Montréal）**。问题：深度生成模型的似然和后验难以计算，训练要靠近似推断或马尔可夫链采样。VAE 把变分下界重参数化，用一个神经网络编码器近似后验，整个模型可以直接用随机梯度训练；GAN 换一条路，让生成器与判别器对抗，只靠反向传播和前向采样，不需要写出似然。**做不好**：VAE 原文只在 MNIST 和 Frey Face 上验证，并自述潜空间维度更高时边缘似然估计变得不可靠（Sec.5）；GAN 原文主实验用多层感知机，作者自述没有显式的分布表示，判别器与生成器必须同步训练，否则生成器会把许多输入映射到同一张图（Sec.6，模式坍缩）。
2. **DCGAN（2015，indico 与 FAIR）**。留下的问题：把 GAN 换成卷积网络、扩大到真实图像的尝试一直不成功，训练常常发散。改变：经大量探索找到一组能稳定训练的全卷积结构（去掉全连接和池化层、使用批归一化等），在 300 多万张 LSUN 卧室图上训练。**做不好**：作者仍自述训练更久时部分滤波器会坍缩到单一振荡模式（Sec.7）。此后几年 GAN 在多数图像生成任务上保持最好的样本质量（ADM 第 1 节的概括），但 ADM 同时指出它多样性不足、训练常坍缩、难以扩展到新领域；LDM 第 1 节的说法是，GAN 的好结果主要局限于变化较少的数据，对抗学习不易扩展到复杂的多峰分布。
3. **DDPM（2020，UC Berkeley）与 Score SDE（2020，Stanford 与 Google Brain）**。留下的问题：GAN 难训练、覆盖不全分布，而似然模型样本质量落后。DDPM 把生成拆成从纯噪声出发的逐级去噪，训练目标是预测加进去的噪声，CIFAR10 无条件生成 FID 3.17；去噪网络是卷积残差块为主、在 16×16 分辨率处加自注意力的 U-Net。Score SDE 把加噪写成连续时间的随机微分方程，证明 DDPM 与多噪声分数匹配是两种 SDE 的离散化，CIFAR-10 FID 降到 2.20，并首次用这类模型生成 1024×1024 的人脸。**做不好**：采样慢。DDPM 固定 1000 步，每步调用一次网络，在 TPU v3-8 上生成一批 128 张 256×256 图像要 300 秒（附录 B）；Score SDE 第 6 节自述采样仍比同一数据集上的 GAN 慢。DDPM 的对数似然也不如其他似然模型（Sec.4.3）；在 ImageNet、LSUN 这类更难的数据上仍不及 BigGAN-deep。
4. **DALL·E（2021 年 2 月，OpenAI）：自回归第一次把文本到图像做到网页规模**。留下的问题：此前的文本到图像（多为 GAN）只在 MS-COCO、CUB 这类小数据集上改模型假设，样本常有物体变形、摆放不合逻辑。改变：用 dVAE 把图像压成 1024 个离散 token，与文本 token 拼成一条序列，在 2.5 亿对网页图文上训练 120 亿参数的自回归 Transformer；在 MS-COCO 零样本人工评测中，按描述匹配有 93% 的多数票偏好它而非 DF-GAN。**做不好**：dVAE 重建会丢失或扭曲毛发纹理、店面文字和细线（Fig.1）；在鸟类细分数据集 CUB 上，FID 比最好的此前方法差近 40 点（Sec.3.1）。
5. **ADM（2021，OpenAI）**。留下的问题：扩散模型只在 CIFAR-10 上领先。作者假设差距来自 GAN 的结构被反复打磨过，以及 GAN 能用多样性换保真度。改变：一轮 U-Net 结构消融，加上分类器引导（采样时用一个在带噪图像上训练的分类器的梯度，把样本推向目标类别）。ImageNet 256×256 类条件生成 FID 从 BigGAN-deep 的 6.95 降到 4.59。benchmark 的主战场随之从 CIFAR-10 迁到 ImageNet 类条件生成。**做不好**：第 7 节自述多步去噪使采样仍比 GAN 慢；分类器引导只适用于有标注的数据集。
6. **LDM（2021，LMU Munich、Heidelberg 与 Runway）**。留下的问题：像素空间扩散训练常需数百 GPU 天，ADM 每次前向约 1120 Gflops（DiT 原文 Fig.2 的统计）。改变：先用自编码器把图像压到低维潜空间，再在潜空间里扩散；U-Net 仍以二维卷积为主，加交叉注意力（以图像特征为查询、以文本编码为键和值）接入条件，ImageNet 类条件 FID 3.60，计算更少，并在 LAION-400M 上训练了文本到图像模型。代码和模型公开，DiT 原文把它作为 Stable Diffusion 的出处引用。**做不好**：第 5 节自述顺序采样仍比 GAN 慢；需要像素级精度时，自编码器的重建能力会成为瓶颈，超分辨率模型已受此限制。
7. **DALL·E 2（OpenAI）、Imagen 与 Parti（Google），2022：目标转向任意文字**。留下的问题：类别标签只能指定 1000 种东西，人想用任意文字描述画面。DALL·E 2 先由一个先验根据文字生成 CLIP 图像嵌入，再由扩散解码器根据嵌入生成图像；Imagen 改用只在文本上预训练的冻结 T5-XXL 作文本编码器，发现加大语言模型比加大图像扩散模型更能提升画质和图文对齐；同年 Google 的另一组作者用 Parti 走自回归路线，把 encoder–decoder Transformer 扩到 200 亿参数。三者在 MS-COCO 零样本 FID 上分别为 10.39、7.27 和 7.23。评测随之从 ImageNet FID 迁到 COCO 零样本 FID 加人工评测，Imagen 建了 DrawBench，Parti 建了 PartiPrompts。同年 Google 的 [Video Diffusion](../../papers/video-diffusion/README.md) 把扩散方法扩到视频：把图像 U-Net 扩成空间与时间分解的 3D U-Net，图像和视频联合训练。**做不好**：这一代的失败集中在"听懂复杂的话"。DALL·E 2 第 7 节自述把颜色分别绑定到两个方块上会弄混，难以生成连贯的文字；Imagen 第 6 节自述生成人物时质量明显下降，第 3 节指出 CLIP 分数不善于计数；Parti 第 6.3 节列得最细：颜色串到未指定颜色的物体上，同类物体最多可靠地画到 7 个，多种物体同时计数几乎完全失败，左右关系基本随机，提示说"盘子里没有香蕉"仍会画出香蕉，而且提示越复杂错误越多。
8. **DiT（2022 年 12 月 arXiv，UC Berkeley 与 NYU）**。留下的问题：从 DDPM 到 LDM，所有扩散模型都用卷积 U-Net 作主干，这种归纳偏置是否必要？改变：在 LDM 的潜空间里，把 U-Net 换成作用于潜变量块的标准 Transformer。12 个模型的计算量与 FID 相关系数为 −0.93，计算量越大样本越好；最大模型在 ImageNet 256×256 类条件生成上把 FID 从 LDM 的 3.60 降到 2.27。作者把"作为 DALL·E 2、Stable Diffusion 这类系统的主干"列为后续工作。**做不好**：论文只在 ImageNet 类条件生成上验证，没有做文本条件；图像编码仍靠现成的卷积 VAE（Sec.3.1），重建上限不变。
9. **流匹配（2022，Meta FAIR 与 Weizmann）到 SD3（2024，Stability AI）：把路径拉直，并把文本条件放进 Transformer**。留下的问题：扩散只能用少数由扩散过程定义的弯曲路径，训练时间长、采样步数多（Flow Matching Sec.1）；用交叉注意力把固定的文本表示接进模型，文字理解有限（SD3 Sec.1）。改变：流匹配直接回归从噪声到数据的速度场，最优传输路径是直线；在 ImageNet 32×32 上达到同样数值误差约只需扩散模型 60% 的函数调用（Fig.7）。SD3 用整流流（同一类直线路径）训练，并提出 MM-DiT：文本与图像两路 token 各用一套权重，在注意力里双向交换信息；8B 模型在 GenEval 上总分 0.74，高于 DALL·E 3 的 0.67，验证损失随规模平滑下降，图像与视频都未见饱和。同一时期，自回归一侧的 VAR（2024，北京大学与字节跳动）把"下一个 token"改成"下一个尺度"，在 ImageNet 256×256 类条件生成上报告 FID 1.73、比同类自回归基线快约 20 倍。**做不好**：SD3 的 GenEval 分项里，位置关系最好也只有 0.33–0.40，是各项最低的（Table 5）；SD3 第 5.2.1 节说明潜空间方案的质量上限仍受自编码器重建限制；VAR 第 8 节自述还没有做文本到图像和视频。
10. **2025–2026：语言模型进入生成器，生成与编辑合一，扩散模型做强化学习**（阿里 Qwen、腾讯混元、字节 Seed、美团、OpenAI、Google）。留下的问题：SD3 一代用固定的文本编码器读提示，写字、位置、计数仍是最弱项，编辑要另训模型。改变有三条。其一，多模态大模型（一句话：能同时读图和文字的语言模型）成为条件编码器，或者干脆就是生成器：[Qwen-Image](../../papers/arxiv-2508.02324/README.md)（2025 年 8 月）用冻结的 Qwen2.5-VL 读提示，接 200 亿参数的 MMDiT；[HunyuanImage 3.0](../../papers/arxiv-2509.23951/README.md)（2025 年 9 月）在一个总参数 800 亿以上、每 token 激活 130 亿的 MoE（混合专家：每个 token 只走一部分子网络）语言模型内部对 VAE 潜变量做扩散，文字自回归、图像去噪，画之前可先写一段思维链；OpenAI 的[系统卡](../../papers/gpt-4o-image-generation-system-card/README.md)写明 GPT-4o 图像生成（2025 年 3 月）是"原生嵌入 ChatGPT 的自回归模型"，Google 的 [Gemini 3.1 Flash Image](../../papers/gemini-3-1-flash-image-model-card/README.md)（Nano Banana 2，2026 年 2 月）模型卡只写"基于 Gemini 3 Flash"。其二，编辑成为同一模型的一等任务：Qwen-Image 把输入图同时送进 Qwen2.5-VL（语义）与 VAE（细节）；[Seedream 4.0](../../papers/arxiv-2509.20427/README.md)（2025 年 9 月）把文生图、单图编辑、多图组合放进一次联合后训练；[Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md)（2026 年 5 月）从预训练起就混入编辑数据（先 1 成，后 3 成）。其三，把多步去噪当作决策过程做强化学习：GRPO（一句话：同一提示采一组图，按组内相对奖励更新）配视觉语言模型打分的奖励模型，Qwen-Image 的 GenEval 从 0.87 升到 0.91，位置一项从 0.76 升到 0.87。写字大幅改善：Qwen-Image 写 3500 个一级常用汉字的单字准确率 97.29%。**做不好**：长尾仍在。Qwen-Image 写 1605 个三级生僻字只对 6.48%（[LongCat-Image](../../papers/arxiv-2512.07584/README.md) 把引号内的文字改为逐字编码后报告 70.3%）；Qwen-Image-2.0 引言列出长文字的字形扭曲与漏字、中英文以外的文字、2K 以上的重复纹理与光照不一致、多实体提示的概念遗漏；Gemini 3.1 Flash Image 模型卡自述小字模糊、长段落、角色不一致、编辑时把输入图原样贴回，以及"偶尔混淆左右"，Parti 2022 年列出的空间关系问题到 2026 年仍在商用模型的已知局限里。强化学习也有坑：[Qwen-Image-2.0-RL](../../papers/arxiv-2606.27608/README.md) 在全部 40 个去噪步上训练，几轮内就出现奖励投机（模型钻奖励模型的空子），无分类器引导在采样和训练中都用会崩溃。评测随之迁移：GenEval 接近饱和，各家改报竞技场 Elo（用户盲选两张图）和自建考题；在 Qwen 团队自己的 Qwen-Image-Bench 上，Qwen-Image-2.0-RL 的 57.84 仍低于 GPT Image 2 的 64.69。

2022 年之后的视频生成、公司模型（Google、OpenAI、字节跳动、快手）与开源视频模型，以及它们怎样走向世界模型，写在续篇[观点页：生成收敛](../../../perspectives/generative-convergence.md)。

**与语言生成的对照**。语言生成走的是另一种生成过程：decoder-only Transformer 在离散 token 上逐个预测下一个词（见 [LLM 预训练方向](../../../llm/fields/pretraining/README.md)）；图像生成收敛到在连续潜空间里逐级去噪。两边的共同点在生成过程之外：训练目标都由数据自己提供（下一词、加进去的噪声），主干在 DiT 之后都是 Transformer，计算量越大样本越好；语言模型还直接进入图像生成，Imagen 用 T5-XXL 作文本编码器，DALL·E 2 的先验就是一个带因果 mask 的 decoder-only Transformer，DALL·E 与 Parti 则直接把图像生成写成语言建模。[判断] 两种模态收敛的是主干、训练信号和规模化方式，生成过程本身仍然不同；完整论证见[观点页：生成为何收敛到同样的配方](../../../perspectives/generative-convergence.md)，规模化的总线见[深度学习的规模化](../../../perspectives/scaling.md)。

### 方法后继：一步生成与语义潜空间（2025–2026）

产品报告里的写字、编辑和偏好优化之外，基线还有两处基本选择仍在变化：模型预测瞬时变化还是整个区间的变化，以及扩散究竟在哪一种潜空间里进行。以下三篇接在流匹配与 LDM/DiT 后阅读。

1. **[MeanFlow](../../papers/arxiv-2505.13447/README.md)，必读。** Flow Matching 学瞬时速度，再由采样器做多步积分；MeanFlow 改学区间平均速度，利用它与瞬时速度的恒等式训练，目标就是一次跨完整区间。它改变的是预测目标，和先训多步教师再蒸馏成少步模型是两种路线。
2. **[RAE](../../papers/arxiv-2510.11690/README.md)，必读。** LDM 的潜空间为重建而学；表示自编码器 RAE 冻结已经学到视觉特征的编码器：DINOv2（用图像不同视图之间的自蒸馏学习）、SigLIP 2（以图文匹配学习语义）或 MAE（遮住图块、从其余图块重建像素），只训练对应解码器，再让 DiT 在这些高维特征里生成。新难点变成高维潜空间的噪声尺度与网络容量，而不只是压缩率。
3. **[Scaling T2I RAE](../../papers/arxiv-2601.16208/README.md)，选读。** 原 RAE 主要在 ImageNet 类条件生成上验证，后继把解码器与扩散模型扩到自由文本生成。结果保留维度相关噪声调度，却重新检验宽扩散头等补丁：在更大规模下，部分复杂设计收益减弱。

`[判断]` 这两条线让"潜空间 + Transformer + 流匹配"从固定配方重新变成可检验的选择：一步方法检验目标是否直接适合部署，RAE 检验用于理解的特征是否也适合生成。它们与公司报告的文字、编辑、强化学习改进是不同层面的增量。

## 技术地基

- **潜变量模型与变分下界**：VAE 的 ELBO 是理解 DDPM 训练目标的起点（DDPM 可以读成编码器固定为加噪链、只学解码方向的多层 VAE），LDM 的自编码器也带 KL 正则。见 [VAE 讲义](../../../foundations/lessons/16-vae.md)第 4 节。
- **扩散：加噪、预测噪声、逐步采样**：训练时一步造出任意噪声等级的样本，生成时从纯噪声顺序去噪；预测噪声与估计分数只差一个缩放，这是 DDPM 与 Score SDE 能统一的原因。流匹配回归速度场，与预测噪声可以互相换算。见[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 2–6 节。
- **离散分词与自回归**：分词器把图像变成离散 token，Transformer 用下一 token 预测建模；分词的重建质量是这条路线的上限。下一 token 预测见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)。
- **去噪主干：U-Net 与 Transformer**："怎样生成"和"用什么网络计算"是两层选择。U-Net 的收缩–扩张结构与跨层拼接见 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节；DiT 的切块与自注意力、LDM 的交叉注意力见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 13 节。
- **引导**：分类器引导用外部分类器的梯度推动采样；无分类器引导把同一模型的条件预测与无条件预测按权重组合，沿两者之差多走一步。两者都以多样性换保真度和条件遵循，类条件与文本条件的最好结果几乎都用了它。公式与一个视频上的例子见 [Video Diffusion 精读](../../papers/video-diffusion/reading.md)第 5 节。

## 主要路线与团队偏好

- **对抗训练**（Montréal 的 GAN，indico 与 FAIR 的 DCGAN）。押注：一次前向就出样本，样本锐利。代价：训练不稳定、模式坍缩；ADM 第 1 节指出 GAN 覆盖的多样性少于似然模型，难以扩展到新领域。2023 年起它以部件的身份回到主流系统：Stability AI 的 ADD 用判别器把扩散模型蒸馏到 1–4 步，字节跳动的 Seedance 1.0 在视频 VAE 和蒸馏中都用了判别器。
- **像素空间扩散加级联超分辨率**（UC Berkeley 的 DDPM，OpenAI 的 ADM，Google 的 Imagen 与 Video Diffusion）。押注：直接在像素上去噪，用多级超分辨率模型提高分辨率。代价：计算量大，采样慢。[判断] Imagen 与 Video Diffusion 出自同一批 Google 作者（Ho、Salimans、Chan、Norouzi、Fleet 同时署名两篇），在潜空间方案 LDM 已发表之后，两篇仍都留在像素空间，并都以滥用和偏见风险为由不发布模型或代码。
- **潜空间扩散与流匹配**（LMU Munich、Heidelberg 与 Runway 的 LDM；UC Berkeley 与 NYU 的 DiT 沿用它的潜空间；Stability AI 的 SD3 与 ADD）。押注：先压缩，把大部分计算放在低维潜空间里，降低训练和采样成本。代价：LDM 与 SD3 都自述自编码器的重建能力是质量上限。[判断] Rombach 与 Blattmann 同时署名 LDM、SD3 与 ADD，Esser 同时署名 LDM 与 SD3：这一批作者从 Heidelberg/Munich 到 Stability AI，连续三篇都押注"潜空间 + 公开权重"。
- **离散 token 自回归**（OpenAI 的 DALL·E，Google 的 Parti，北京大学与字节跳动的 VAR）。押注：把图像生成写成语言建模，直接复用语言模型的结构、训练配方与规模化经验。代价：分词丢细节、顺序生成慢（VAR Sec.3 的四条问题）。这条路线的三篇来自三个团队，按"同一团队两篇以上"的标准不算团队偏好；同一团队反而会换路线：Ramesh 是 DALL·E 第一作者，一年后的 DALL·E 2 改用扩散解码器。
- **借判别模型的表示来控制生成**（OpenAI 的 ADM 与 DALL·E 2）。押注：用一个现成的判别模型（分类器、CLIP）提供条件和方向。代价：ADM 的分类器引导只适用于有标注的数据；DALL·E 2 自述 CLIP 嵌入不显式绑定属性与物体，在要把两种颜色分别绑定到两个方块的提示上会弄混（Sec.7、Fig.14）。[判断] Dhariwal 与 Nichol 同时署名两篇：ADM 在第 7 节提出用带噪 CLIP 以文字引导生成，DALL·E 2 则直接以 CLIP 图像嵌入为条件，同一团队在两篇中重复了"让判别模型的表示驱动生成"这一选择。

## 用什么衡量进展

benchmark 的替换就是这个领域目标的迁移：

- **FID**（生成样本与真实样本在 Inception 网络特征空间中的分布距离，越低越好）是贯穿全线的指标，测试对象却一路在变：CIFAR-10 无条件生成（DDPM 3.17、Score SDE 2.20）→ ImageNet 256×256 类条件生成（BigGAN-deep 6.95 → ADM-G 4.59 → LDM 3.60 → DiT 2.27；自回归的 VAR 报告 1.73）→ MS-COCO 零样本文本到图像（DALL·E 2 10.39、Imagen 7.27、Parti 7.23）。
- **文本条件之后的人工评测与分项考题**：Imagen 指出 FID 与人的感知不完全一致，CLIP 分数（用 CLIP 衡量图文相似度）不善于计数，于是加入人工评测，并新建 DrawBench，按组合、计数、空间关系、长文本、罕见词等类别出题；Parti 的 PartiPrompts 有 1600 多条提示，按类别和难度两个维度拆开。SD3 用 GenEval（一组自动评分的考题，分单个物体、两个物体、计数、颜色、位置、属性绑定六项），分项分数正好暴露了"位置"最难。DALL·E 2 与 GLIDE 的人工对比也分写实度、描述匹配、多样性三项。
- **视频**：Video Diffusion 在 UCF101 无条件生成、BAIR 机器人推动与 Kinetics-600 视频预测上报告 FVD（FID 在视频上的对应：在视频动作识别网络的特征空间里比较分布）与 Inception Score。2023 年后的视频评测转向人工评测和分项考题，见[观点页](../../../perspectives/generative-convergence.md)。
- **口径问题**：FID 对参考集和实现细节敏感，DDPM 的 3.17 相对训练集计算，相对测试集为 5.24，DiT 统一用 ADM 的评测代码重算；类条件和文本条件的最好结果都用了引导，引导强度改变的是保真度与多样性之间的取舍；ADD 发现 SDXL 的 FID 更差，人工评的画质和对齐却更好（Sec.4）；Video Diffusion 自述各论文的数据预处理不总一致。生成质量、条件遵循和物理一致性是三种能力，各需单独的评测。

## 当前开放问题

- **采样能否少走几步？** 每一篇扩散论文都自述采样比 GAN 慢。三条路在并行推进：直线路径（流匹配、SD3 的整流流；SD3 Table 6 显示大模型在少步采样时掉分更少）、蒸馏（ADD 单步出图）、换生成方式（VAR 自述比自回归基线快约 20 倍）。入口：[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6.1 节、[Flow Matching 原文](../../papers/arxiv-2210.02747/README.md)、[ADD 原文](../../papers/arxiv-2311.17042/README.md)、[VLA 讲义](../../../robotics-embodied/fields/vla.md)第六节（π0.5 用流匹配生成连续动作）。
- **怎样让模型听懂复杂的话，并且自动地测出来？** 属性绑定、计数、空间位置和文字渲染从 DALL·E 2、Parti 到 SD3 一直是最弱的几项；FID 衡量分布距离，衡量不了是否听懂了文字，于是评测转向 DrawBench、PartiPrompts、GenEval 这类分项考题。入口：[Parti 原文](https://arxiv.org/abs/2206.10789)第 6.3 节、[SD3 原文](../../papers/arxiv-2403.03206/README.md) Table 5、[Imagen 原文](../../papers/arxiv-2205.11487/README.md)、[DALL·E 2 原文](../../papers/arxiv-2204.06125/README.md)。
- **自回归与扩散会不会合成一种生成方式？** VAR 在 ImageNet 上报告超过 DiT；Genie 2 已经是官方所说的"自回归的潜空间扩散模型"。入口：[VAR 原文](../../papers/arxiv-2404.02905/README.md)、[观点页](../../../perspectives/generative-convergence.md)。
- **视频生成能否成为可以规划的世界模型？** 好看的视频不等于符合物理、能跟随动作；世界模型要建模"执行某个动作之后会发生什么"。入口：[观点页的"从视频生成到世界模型"](../../../perspectives/generative-convergence.md)、[Video Diffusion 精读](../../papers/video-diffusion/reading.md)"局限与后续"第 7 条、[世界模型方向](../world-models/README.md)、[LaDi-WM](../../papers/arxiv-2505.11528/README.md)、[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](../../papers/arxiv-2603.17808/README.md)。

## 阅读顺序

1. [VAE 讲义](../../../foundations/lessons/16-vae.md)：先弄清变分下界里的重建项和 KL 项，DDPM 的训练目标从这里来。
2. [扩散讲义](../../../foundations/lessons/17-diffusion.md)：用一个数字走一遍加噪、预测噪声和逐步采样，再读第 6 节的分数与 flow matching。
3. [DDPM 精读](../../papers/ddpm/README.md)：主线第 3 个节点的原文。读完可以做一个检验：用单个带噪样本说明 DDPM 要预测什么，再说明条件输入会怎样改变采样过程。
4. [Video Diffusion 精读](../../papers/video-diffusion/README.md)：同一套方法扩到视频，并把分类器无关引导和重建引导讲清楚；它也接到[视频与时序方向](../video-temporal/README.md)。
5. [观点页：生成收敛](../../../perspectives/generative-convergence.md)：本页的续篇，从视频生成的几种基本做法讲到 2026 年的公司模型和世界模型。
6. [Diffusion Policy 精读](../../../robotics-embodied/papers/diffusion-policy/README.md)：被去噪的对象从图像换成机器人动作序列，看同一个生成机制在控制中要额外处理什么。

## 批注

**易误读**

- "先看这里"一节的 GAN 一维例子与"两堆数据"的坍缩例子是教学构造，不出自任何论文的实验；流匹配的数字取自[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6.1 节。
- DDPM 的 FID 3.17 相对训练集计算，相对测试集为 5.24（DDPM Table 1、Sec.4.1）。
- ADM-G 的 4.59 是 250 步采样的结果；与上采样扩散模型结合后为 3.94（ADM Table 5、Abstract）。DiT 的 2.27 用了无分类器引导（DiT Table 2）。VAR 的 1.73 是 2B 模型在 ImageNet 256×256 类条件生成上的结果，评测设置以 VAR 原文为准，与 DiT 的数字来自不同论文。
- Imagen 的 7.27、Parti 的 7.23 与 DALL·E 2 的 10.39 都是 MS-COCO 零样本 FID，但 Imagen 是 FID-30K、引导权重按 Imagen Table 1 的设置，Parti 每条提示采样 16 张再重排（Parti Table 5 说明）；各篇的人工评测协议不同，不能直接合并比较。
- SD3 的 GenEval 0.74 是 1024² 分辨率加 DPO 偏好对齐后的结果，未对齐的同规模模型在 512² 上为 0.68（SD3 Table 5）。
- SD3 位置一项的 0.33–0.40（depth 24 以上各设置）是它自己各项里最低的一项，不是领先：同表 DALL·E 3 的位置为 0.43；SD3 总分高于 DALL·E 3，靠的是两物体、计数、颜色与属性绑定（SD3 Table 5）。
- 2025–2026 年报告里的 GenEval、ChineseWord、竞技场 Elo 多为各家自测或自建考题。同一指标的复测量级一致（Qwen-Image 三级汉字：Qwen 自测 6.48%，LongCat-Image 复测 6.1%），竞技场排名则随时间变（Qwen-Image-2.0 的第 9 名取自 2026-04-22）。
- GAN 原文的主实验用多层感知机，只有一个 CIFAR-10 版本用了卷积判别器和"反卷积"生成器（GAN Fig.2）；能稳定训练的卷积 GAN 结构来自 DCGAN。
- DDPM 中的中间状态 xₜ 与图像同维，不是 LDM 那样压缩后的潜变量；"潜空间扩散"专指 LDM 一类先压缩再扩散的做法。
- 扩散时间与视频帧时间是两根不同的时间轴（Video Diffusion 精读开头的图）。

**方法后继的边界**

- MeanFlow 的 ImageNet 256×256 实验是类条件生成，CIFAR-10 实验是无条件生成（[NeurIPS 2025 正式版 §5.2、Table 2–3](https://papers.nips.cc/paper_files/paper/2025/file/6d13e085b79d454da5910e4ca82a3d9d-Paper-Conference.pdf)）；这些图像实验不支持任意文本或视频任务均可一步完成的推论。
- RAE 的冻结编码器与可训练解码器见论文方法部分；Scaling T2I RAE 的主对照是 SigLIP 2 RAE 与 FLUX VAE（FLUX 文生图模型使用的变分自编码器，把像素压缩为生成用潜变量），同 token 预算包含不同输入分辨率，不能据此推出所有 VAE 被替代。

**判断的支撑论文与反例**（各行见 [synthesis.csv](synthesis.csv)）

- "一步预测目标与语义潜空间是两个可检验的选择"：MeanFlow §4.1 的平均速度恒等式及正式版 §5.2；RAE §3–4 的冻结表征编码器、高维噪声和网络设计；Scaling T2I RAE §3–4 的规模化对照。边界：MeanFlow 只验证了指定图像设置；RAE 原作主要研究 ImageNet；Scaling T2I RAE 仍用多步采样，且其 Table 2 中 FLUX VAE 的重建优于所测 RAE。因此这些证据支持分开比较目标与潜空间，不支持一种配方全面取代另一种。
- "三个家族今天的分工"：支撑——SD3、Veo 3、Wan 等用扩散或流匹配生成连续信号；Genie 2 是"自回归的潜空间扩散模型"，逐帧生成（官方博客"Diffusion world model"一节）；LDM Sec.3.1、Seedance 1.0 Sec.2.1 与 Sec.5.1、ADD 都把判别器用作损失项。反例：VAR 在 ImageNet 类条件生成上用纯自回归报告了最好的 FID；VideoPoet 用纯自回归生成视频。所以这是 2024 年前后大系统的常见组合，不是唯一可行的组合。
- "判别器以损失项留在自编码器里"（速览第 4 条与"三个家族的分工"）的反例：Qwen-Image Sec.2.3 报告重建变好后判别器给不出有效指导，只留重建与感知损失；Qwen-Image-2.0 Sec.3.1 认为大规模 VAE 训练中对抗损失基本多余，去掉以求稳定，改加语义对齐损失。边界：两例都出自 Qwen 团队；Seedream 4.0 的蒸馏仍用混合判别器与基于扩散的判别器（Sec.2.3），LongCat-Image 把 AIGC 检测器当奖励模型，"挑错"的判别信号换了位置继续存在。原判断保留，它描述的是 2024 年前后的常见做法。
- "语言模型负责理解、扩散负责画"：支撑——Qwen-Image Sec.2.2（选 Qwen2.5-VL 的三条理由）、Qwen-Image-2.0 Sec.1（近期框架普遍以视觉语言模型作条件编码器）、HunyuanImage 3.0 Sec.3.1（同一 MoE 语言模型里自回归文字、扩散图像）、GPT-4o 系统卡 Sec.2.1（原生嵌入的自回归模型）。边界：GPT-4o 与 Gemini 图像模型的结构没有公开，"在同一网络中"只能按官方措辞理解；ERNIE-Image 只用 30 亿参数的 Ministral-3 作文本编码器，报告称足以支撑长提示。
- Google 一批作者留在像素空间并不发布模型：Imagen Sec.1、Sec.4.1、Sec.6；Video Diffusion Sec.1、Sec.6（首页作者均为 google.com 邮箱）。边界：DDPM 的 Ho 当时在 UC Berkeley，DDPM 公开了代码，所以"不发布"是这批作者 2022 年的选择，不是同一个人一贯的做法；同在 Google 的 Parti 走自回归，说明 Google 内部并非只押一条路线。
- Rombach、Blattmann 一批作者押注潜空间并公开权重：LDM 首页（预训练模型链接）、SD3 Abstract（承诺公开权重）、ADD 首页（代码与权重链接）。边界：三篇中 LDM 出自大学，后两篇出自 Stability AI，单位变化可能本身就改变了发布策略。
- OpenAI 借判别模型表示驱动生成：ADM Sec.4、Sec.7；DALL·E 2 Abstract、Sec.2、Sec.7。反例：同属 OpenAI 的 CLIP 本身公开了权重，而 DALL·E 2 未声明发布，开放程度并不一致。
- "与语言生成收敛在主干与规模化"：DiT Sec.1 与 Fig.8（Transformer 主干、计算量与 FID 相关 −0.93）、Imagen Sec.1（语言模型规模比扩散模型规模更重要）、DALL·E 2 Sec.2.2（decoder-only Transformer 先验）、SD3 Fig.8（验证损失随规模平滑下降）、VAR Abstract（缩放实验相关系数约 −0.998）。边界：LDM、Imagen、Video Diffusion 仍是卷积 U-Net 主干，收敛发生在 2022 年末之后。

**与其他论文的关联**

- U-Net 本是为几十张图的医学分割设计的编码–解码结构，见[视觉表征方向](../visual-representation/README.md)与 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节；DDPM、LDM、Imagen、Video Diffusion 都沿用它作去噪主干，DiT 才换成 Transformer。
- DALL·E 2 以 [CLIP](../../papers/clip/README.md) 的图像嵌入为条件，视觉表征方向的图文弱监督由此进入生成。
- [Diffusion Policy](../../../robotics-embodied/papers/diffusion-policy/README.md) 把 DDPM 的去噪机制用于动作序列；[VLA 讲义](../../../robotics-embodied/fields/vla.md)第六节讲 π0.5 的 flow matching 动作头。
- [DDPM 精读](../../papers/ddpm/reading.md)第 3 节写出了噪声预测与分数的缩放关系，是主线第 3 个节点"两篇可以统一"的推导。
- 视频与世界模型方向的新卡：[Imagen Video](../../papers/arxiv-2210.02303/README.md)、[Sora 技术报告](../../papers/sora-tech-report/README.md)、[Veo 3](../../papers/veo3-tech-report/README.md)、[HunyuanVideo](../../papers/arxiv-2412.03603/README.md)、[Wan](../../papers/arxiv-2503.20314/README.md)、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)、[Seedance 2.0](../../papers/arxiv-2604.14148/README.md)、[Kling-Omni](../../papers/arxiv-2512.16776/README.md)、[Genie](../../papers/arxiv-2402.15391/README.md)、[Cosmos](../../papers/arxiv-2501.03575/README.md)，论证见观点页。
- HunyuanImage 3.0 延续了[视觉语言模型方向](../vlm/README.md)的早融合路线（[Chameleon](../../papers/arxiv-2405.09818/README.md)），把离散图像 token 换成连续潜变量加扩散。


**未核实 / 待验证**

- Stable Diffusion 1.x 本身的发布材料（模型卡、训练数据）没有打开；本页只按 DiT 原文的引用，把 LDM 视为它的出处。SD3 原文承诺公开权重，实际发布的版本与许可没有另查。
- DCGAN 论文正文未声明代码发布，实际发布情况没有另查。DALL·E 2 论文未声明代码或权重发布；DALL·E 原文只给出 dVAE 代码链接。Parti 论文未声明发布。
- DiT 的正式发表会议没有核实，本页只写 arXiv 时间 2022 年 12 月。
- Video Diffusion 首页没有印出单位，本页按作者邮箱写作 Google。
- GLIDE、DDIM、无分类器引导原文（Ho 与 Salimans）、DALL·E 3 技术报告本轮没有打开，本页只引用其他论文对它们的描述（DALL·E 3 的 GenEval 0.67 来自 SD3 Table 5）。
- VAR"超过 DiT"是 VAR 作者在 ImageNet 类条件生成上的自述，本页没有找到第三方在同一设置下的复现。
- GPT-4o 图像生成、ChatGPT Images 2.0（GPT Image 2）、Gemini 3 Pro Image、Gemini 3.1 Flash Image、Seedream 4.0/4.5 的结构、参数与数据均未公开；Qwen-Image-2.0 未写参数量。Seedream 5.0 Lite、Gemini 3.1 Flash-Lite Image（2026 年 6 月）、FLUX.2、Z-Image、GLM-Image 的官方材料没有打开；竞技场榜单只按各报告的引用。

**参考文献**

- DALL·E：https://arxiv.org/abs/2102.12092 ；Parti：https://arxiv.org/abs/2206.10789 ；Flow Matching：https://arxiv.org/abs/2210.02747 ；SD3：https://arxiv.org/abs/2403.03206 ；VAR：https://arxiv.org/abs/2404.02905 ；ADD：https://arxiv.org/abs/2311.17042
- Seedream 3.0：https://arxiv.org/abs/2504.11346 ；ERNIE-Image：https://arxiv.org/abs/2605.25347 ；ChatGPT Images 2.0 系统卡（2026-04-21）：https://deploymentsafety.openai.com/chatgpt-images-2-0 ；Gemini 3 Pro Image 模型卡（2025-11）：https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Image-Model-Card.pdf
- GAN：https://arxiv.org/abs/1406.2661 ；DCGAN：https://arxiv.org/abs/1511.06434 ；LDM：https://arxiv.org/abs/2112.10752 ；DiT：https://arxiv.org/abs/2212.09748 ；Imagen：https://arxiv.org/abs/2205.11487 ；DALL·E 2：https://arxiv.org/abs/2204.06125
