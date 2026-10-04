# 视觉生成的基线

[回到入门](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 基线是谁、为什么是它

本方向用两条基线：[DDPM](../../papers/ddpm/README.md) 定义"怎样训练、怎样采样"，LDM + DiT（加无分类器引导）定义 2022 年之后图像与视频模型共用的骨架。GAN 与离散 token 自回归是两条对照基线。

**训练与采样的基线：[DDPM](../../papers/ddpm/README.md)（2020，UC Berkeley）。**

- **接口**：标准高斯噪声进去，网络被调用 1000 次、逐级去噪，一张图出来；没有任何条件。
- **训练范式**：抽一张真实图、抽一个噪声等级 t、按闭式一步加噪，让网络回归加进去的那份噪声（Lsimple，一句话：不加权的均方误差）。答案由我们自己造，不需要标注，也不需要判别器。
- **评估方式**：CIFAR10 无条件生成的 FID 3.17（FID：生成样本与真实样本在 Inception 网络特征空间里的分布距离，越低越好）。

此后的扩散与流匹配论文，包括视频生成和机器人的 [Diffusion Policy](../../../robotics-embodied/papers/diffusion-policy/README.md)，都可以读成"保留这个训练形态，换掉其中某个部件"。机制与手算见 [DDPM 精读](../../papers/ddpm/reading.md)。

**现代骨架的基线：[LDM](../../papers/arxiv-2112.10752/README.md)（2021，Munich/Heidelberg 与 Runway）+ [DiT](../../papers/arxiv-2212.09748/README.md)（2022，UC Berkeley 与 NYU）+ [无分类器引导](../../papers/arxiv-2207.12598/README.md)（2021–2022，Google）。**

- **接口**：图像先由自编码器压到潜空间（DiT 中 256×256×3 的图变成 32×32×4），潜变量切成小块作 token，Transformer 去噪；类别或文字作为条件注入，采样时用无分类器引导（同一网络的有条件预测与无条件预测按权重外推）；最后解码器还原成像素。
- **为什么选它**：2024 年后的官方报告几乎都写明落在这个骨架上。Sora 报告引用 DiT 作主干来源；[SD3](../../papers/arxiv-2403.03206/README.md)、[HunyuanVideo](../../papers/arxiv-2412.03603/README.md)、[Wan](../../papers/arxiv-2503.20314/README.md)、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md) 都是"潜空间 + Transformer + 流匹配或整流流"。各家的差别都可以写成"这个骨架的某个部件换成了什么"。
- **评估方式**：ImageNet 256×256 类条件生成的 FID-50K（LDM 3.60 → DiT 2.27，都用了无分类器引导）。

**两条对照基线。** [GAN](../../papers/arxiv-1406.2661/README.md)（2014）一次前向就出样本，代价是训练不稳、模式坍缩；读它是为了理解扩散为什么胜出，以及判别器为什么又以损失项的身份回来。离散 token 自回归（[VQGAN](../../papers/arxiv-2012.09841/README.md) 的分词器 + Transformer，[DALL·E](../../papers/arxiv-2102.12092/README.md)）把图像生成写成语言建模；读它是为了理解"分词器的重建能力就是质量上限"这个一直没有消失的问题，以及 VAR、Genie、Cosmos 为什么仍在用这条路。

## 基线的结构拆分

| 部件 | DDPM 的选择 | LDM + DiT 的选择 | 这个部件决定什么 |
|---|---|---|---|
| 1 数据与描述 | CIFAR10、LSUN、CelebA-HQ 的无标注图像 | ImageNet 类别标签；LDM 的文本模型用 LAION-400M 网页图文 | 能听懂什么样的提示；偏见、版权与不当内容从这里进入 |
| 2 表示空间 | 像素空间，中间状态与图像同维 | 自编码器潜空间，下采样 8 倍、4 通道 | 计算量；质量上限（自编码器的重建能力） |
| 3 主干与生成过程 | 卷积 U-Net，16×16 处加自注意力；整张图一起去噪 | 潜变量块上的 Transformer，adaLN-Zero 注入条件 | 能否随算力规模化；能否和文本 token 放在一个网络里 |
| 4 训练目标与噪声路径 | 预测噪声 ε，Lsimple，线性日程，1000 级 | 同为 1000 级线性日程，沿用 ADM 的"学习反向方差" | 训练效率；少步采样时误差多大 |
| 5 采样器与步数 | 祖先采样 1000 步 | 250 步（DiT 用 DDPM 采样，LDM 用 DDIM） | 生成一张图要调用网络多少次 |
| 6 条件接入与引导 | 无条件 | 类别嵌入（DiT）或交叉注意力接文本（LDM）；无分类器引导 | 能否按文字作图；保真度与多样性怎样取舍 |
| 7 规模化与后训练 | 35.7M–256M 参数，没有后训练 | DiT 的 12 个模型：计算量与 FID 相关系数 −0.93；没有后训练 | 加算力是否稳定变好；能否按人的偏好调 |
| 8 时间轴与动作 | 只有扩散时间，没有帧时间 | 同 | 能否生成视频；能否逐帧响应动作，成为世界模型 |
| 9 评测 | CIFAR10 的 FID、IS、似然 | ImageNet 的 FID-50K（ADM 的评测代码） | FID 测分布距离，测不出是否听懂文字、是否符合物理 |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 1 数据 | 网页规模的图文对 | [DALL·E](../../papers/arxiv-2102.12092/README.md)（2.5 亿对）、[Imagen](../../papers/arxiv-2205.11487/README.md)（约 4.6 亿内部 + 4 亿 LAION） | 零样本文本到图像成立；Imagen 以数据含不当内容、存在刻板印象为由不发布 |
| 1 数据 | 用 CLIP 打分过滤并公开 | [LAION-5B](../../papers/arxiv-2210.08402/README.md) | 让 LDM / Stable Diffusion 一类可复现；继承过滤模型的偏差，后来删除不安全链接重新发布 |
| 1 数据 | 用模型重写描述 | [SD3](../../papers/arxiv-2403.03206/README.md)（一半换成合成描述）、[Sora](../../papers/sora-tech-report/README.md)、[Veo 3](../../papers/veo3-tech-report/README.md)（Gemini 生成多粒度描述） | 提示遵循提升；描述模型的偏好随之进入生成模型 |
| 1 数据 | 视频分阶段筛选 + 少量高质量微调 | [HunyuanVideo](../../papers/arxiv-2412.03603/README.md)（最后用约 100 万条人工挑选片段）、[Wan](../../papers/arxiv-2503.20314/README.md)、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)、[Cosmos](../../papers/arxiv-2501.03575/README.md)（约 2000 万小时筛出约 1 亿段） | 画质与运动提升；公司报告多不公开数据规模 |
| 1 数据 | 无动作标注的游戏或自有车队视频 | [Genie](../../papers/arxiv-2402.15391/README.md)（3 万小时平台游戏）、[GameNGen](../../papers/arxiv-2408.14837/README.md)（PPO 智能体的录像）、[GAIA-1](../../papers/arxiv-2309.17080/README.md)（4700 小时自有驾驶数据） | 能学动作条件的动力学；只覆盖单一游戏或单一车队 |
| 2 表示 | 学一个带 KL 正则的潜空间，编码器近似后验 | [VAE](../../papers/arxiv-1312.6114/README.md) | 潜变量模型可以端到端随机梯度训练，LDM 的 KL 正则自编码器沿用这一写法；原文只在 MNIST、Frey Face 上验证 |
| 2 表示 | 像素空间 + 级联超分辨率 | [ADM](../../papers/arxiv-2105.05233/README.md)、[DALL·E 2](../../papers/arxiv-2204.06125/README.md)（64→256→1024）、[Imagen](../../papers/arxiv-2205.11487/README.md)、[Video Diffusion](../../papers/video-diffusion/README.md)、[Imagen Video](../../papers/arxiv-2210.02303/README.md)（7 个子模型） | 没有自编码器的重建上限；算力大，DALL·E 2 自述 64×64 起步使复杂场景缺细节，Imagen Video 最高分辨率的超分模型为省内存改成全卷积 |
| 2 表示 | 连续潜空间（感知损失 + 局部块判别器训练自编码器） | [LDM](../../papers/arxiv-2112.10752/README.md)（同样 200 万步，像素扩散与 8 倍下采样差 FID 38）、[SD3](../../papers/arxiv-2403.03206/README.md)（通道数 4 → 16） | 训练与采样都省；LDM、SD3 都自述重建能力是质量上限 |
| 2 表示 | 冻结视频 VAE 的编码器，只用文字密集图像微调图像解码器，去掉对抗损失 | [Qwen-Image](../../papers/arxiv-2508.02324/README.md)（2025 年 8 月） | 小字与细节的重建提升，为写字打底；作者称重建变好后判别器给不出有效指导 |
| 2 表示 | 高压缩自编码器 + 语义对齐损失，追求"好重建"之外的"好扩散" | [Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md)（2026 年 5 月，Qwen 团队，16 倍下采样） | 训练更省、原生高分辨率；作者写明压缩比、重建保真与可扩散性三者互相牵制，并认为大规模训练中对抗损失多余、把它去掉了 |
| 2 表示 | 离散 token（dVAE、VQGAN） | [DALL·E](../../papers/arxiv-2102.12092/README.md)（1024 个 token）、[VQGAN](../../papers/arxiv-2012.09841/README.md)（16 倍下采样，256 个 token）、[Chameleon](../../papers/arxiv-2405.09818/README.md) | 能直接套语言模型；DALL·E 丢细线与文字，VQGAN 下采样超过 16 倍重建崩坏，Chameleon 多文字图像重建差 |
| 2 表示 | 时空同时压缩的视频 VAE | [Sora](../../papers/sora-tech-report/README.md)、[HunyuanVideo](../../papers/arxiv-2412.03603/README.md)（因果 3D VAE）、[Wan](../../papers/arxiv-2503.20314/README.md)（时间 4×、长宽各 8×）、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)（时间 4×、长宽各 16×，加判别器损失） | 长视频算得起；大幅运动中保持细节仍难（Wan 自述），压缩比各家取舍不同 |
| 3 主干 | U-Net 结构消融 | [ADM](../../papers/arxiv-2105.05233/README.md)（更多注意力、BigGAN 残差块、AdaGN）、[Imagen](../../papers/arxiv-2205.11487/README.md)（Efficient U-Net） | ImageNet 上超过 BigGAN-deep；像素 ADM 每次前向约 1120 Gflops |
| 3 主干 | 时空分解 3D U-Net | [Video Diffusion](../../papers/video-diffusion/README.md)、[Imagen Video](../../papers/arxiv-2210.02303/README.md) | 注意力计算约省到 1/16；斜向运动靠层间交替传递 |
| 3 主干 | 潜变量块上的 Transformer | [DiT](../../papers/arxiv-2212.09748/README.md) | 计算量越大 FID 越低（−0.93），FID 2.27；切块越小 token 越多，计算量按 4 倍增长 |
| 3 主干 | 文本与图像两路权重、双向注意力（MM-DiT、双流转单流） | [SD3](../../papers/arxiv-2403.03206/README.md)、[HunyuanVideo](../../papers/arxiv-2412.03603/README.md)、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)（空间层用 MM-DiT） | 文字理解与排版提升；文本一路也要一套完整权重，参数增加 |
| 3 主干 | 视频全时空注意力 vs 空间、时间解耦 | 全注意力：[HunyuanVideo](../../papers/arxiv-2412.03603/README.md)；解耦：[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)；结构未公开：[Veo 3](../../papers/veo3-tech-report/README.md)、[Seedance 2.0](../../papers/arxiv-2604.14148/README.md)、[Kling-Omni](../../papers/arxiv-2512.16776/README.md) | 表达力与效率的取舍，团队之间仍有分歧 |
| 3 生成过程 | 下一 token 自回归 | [DALL·E](../../papers/arxiv-2102.12092/README.md)、[VQGAN](../../papers/arxiv-2012.09841/README.md)、[Chameleon](../../papers/arxiv-2405.09818/README.md)、[GAIA-1](../../papers/arxiv-2309.17080/README.md)、[Cosmos](../../papers/arxiv-2501.03575/README.md)（自回归一支） | 与语言模型同构；n×n 个 token 要 n² 步，GAIA-1 自述 argmax 采样会陷入重复 |
| 3 生成过程 | 下一尺度自回归 | [VAR](../../papers/arxiv-2404.02905/README.md) | 自回归基线 FID 18.65 → 1.73、约快 20 倍；分词器未改，没有做文本到图像 |
| 3 生成过程 | 在 MoE 语言模型内部对 VAE 特征做扩散，理解与生成共用一个模型 | [HunyuanImage 3.0](../../papers/arxiv-2509.23951/README.md)（2025 年 9 月，腾讯混元，总参数 800 亿以上、每 token 激活 130 亿） | 能在生成前做思维链推理；开放的只有图像生成模块 |
| 3 生成过程 | 原生嵌入多模态大模型（官方只给措辞，结构未公开） | [GPT-4o 图像生成](../../papers/gpt-4o-image-generation-system-card/README.md)（官方称"原生嵌入 ChatGPT 的自回归模型"）、[Gemini 3.1 Flash Image](../../papers/gemini-3-1-flash-image-model-card/README.md)（"基于 Gemini 3 Flash"） | 可调用语言模型的知识、联网搜索后再画；无法从官方材料判断用了哪种生成过程 |
| 4 目标 | 学习反向方差、余弦日程 | [Improved DDPM](../../papers/arxiv-2102.09672/README.md) | 似然 2.94 bits/dim、100 步接近最优；最好的似然那一行 FID 变差，余弦日程在 256×256 上不如线性 |
| 4 目标 | 连续时间 SDE 与分数 | [Score SDE](../../papers/arxiv-2011.13456/README.md) | 统一 DDPM 与分数匹配，FID 2.20，可精确算似然；采样器选项多、超参多 |
| 4 目标 | v 预测 | [Video Diffusion](../../papers/video-diffusion/README.md)、[Imagen Video](../../papers/arxiv-2210.02303/README.md) | 避免 ε 预测在高分辨率上的颜色漂移 |
| 4 目标 | 流匹配：回归直线路径的速度 | [Flow Matching](../../papers/arxiv-2210.02747/README.md)、[HunyuanVideo](../../papers/arxiv-2412.03603/README.md)、[Wan](../../papers/arxiv-2503.20314/README.md)、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md) | 同样误差约省 40% 网络调用、训练步数少得多；CIFAR-10 上 FID 不如以往 |
| 4 目标 | 整流流 + reflow 拉直 | [Rectified Flow](../../papers/arxiv-2209.03003/README.md) | 一步生成 FID 4.85；多步结果反而变差（2.58 → 3.36） |
| 4 目标 | 整流流 + 偏向中段的时间采样 | [SD3](../../papers/arxiv-2403.03206/README.md) | 61 种组合中只有它胜过 LDM 的旧设定；均匀时间采样的整流流并不更好 |
| 4 目标 | 带判别器的对抗目标 | [GAN](../../papers/arxiv-1406.2661/README.md)、[DCGAN](https://arxiv.org/abs/1511.06434) | 一步出样本；模式坍缩、训练不稳 |
| 5 采样 | 确定性非马尔可夫路径，免重训 | [DDIM](../../papers/arxiv-2010.02502/README.md) | 20–100 步接近 1000 步质量，快 10–50 倍；10 步 FID 13.36 仍明显变差 |
| 5 采样 | 预测–校正 | [Score SDE](../../papers/arxiv-2011.13456/README.md)、[Video Diffusion](../../papers/video-diffusion/README.md) | 同样调用次数下略好；校正一步也算一次网络调用 |
| 5 采样 | 渐进蒸馏、多阶段蒸馏 | [Imagen Video](../../papers/arxiv-2210.02303/README.md)（每级 8 步）、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)（约 10 倍）、[Kling-Omni](../../papers/arxiv-2512.16776/README.md)（10 步） | 可用于产品；Genie 2 的实时蒸馏版画质下降 |
| 5 采样 | 对抗蒸馏 | [ADD](../../papers/arxiv-2311.17042/README.md) | 1–4 步，4 步多数比较胜过 50 步 SDXL；多样性略降 |
| 5 采样 | 对抗蒸馏 + 对抗分布匹配；分布匹配蒸馏（DMD） | [Seedream 4.0](../../papers/arxiv-2509.20427/README.md)（混合判别器、基于扩散的判别器，2K 图最快 1.4 秒）、[Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md)（DMD，4 次网络调用） | 可用于产品；判别器在这里仍是主力，Qwen-Image-2.0 自述在多场景、极少步数下保住全部能力仍很难 |
| 5 采样 | 拉直路径后一步 Euler | [Rectified Flow](../../papers/arxiv-2209.03003/README.md)、[SD3](../../papers/arxiv-2403.03206/README.md)（大模型少步掉分更少） | 不需要单独的蒸馏器；reflow 次数多会累积误差 |
| 6 条件 | 类别嵌入加到时间步嵌入 | [Improved DDPM](../../papers/arxiv-2102.09672/README.md)、[ADM](../../papers/arxiv-2105.05233/README.md) | 类条件生成；只有 1000 个类 |
| 6 引导 | 分类器引导 | [ADM](../../papers/arxiv-2105.05233/README.md) | FID 4.59 超过 BigGAN-deep；要单独训练带噪分类器，只适用于有标注的数据 |
| 6 引导 | 无分类器引导 | [CFG](../../papers/arxiv-2207.12598/README.md)；[LDM](../../papers/arxiv-2112.10752/README.md)、[DiT](../../papers/arxiv-2212.09748/README.md)、[Imagen](../../papers/arxiv-2205.11487/README.md)、[Genie 2](../../papers/genie-2-blog/README.md) 都在用 | 一行代码换掉分类器；每步两次前向，引导强了颜色饱和、多样性下降 |
| 6 条件 | 交叉注意力接入文本编码 | [LDM](../../papers/arxiv-2112.10752/README.md) | 任意条件都能接；SD3 认为固定文本表示的单向注入对理解有限 |
| 6 条件 | CLIP 图像嵌入作中间表示 | [DALL·E 2](../../papers/arxiv-2204.06125/README.md) | 多样性更好；属性绑定和写字更差 |
| 6 条件 | 冻结的纯文本语言模型作编码器 | [Imagen](../../papers/arxiv-2205.11487/README.md)（T5-XXL）、[Imagen Video](../../papers/arxiv-2210.02303/README.md)、[SD3](../../papers/arxiv-2403.03206/README.md)（CLIP×2 + T5） | 扩大文本编码器比扩大 U-Net 更有效；SD3 去掉 T5 后写字的胜率只剩 38% |
| 6 条件 | decoder-only 多模态大模型作编码器或改写提示 | [HunyuanVideo](../../papers/arxiv-2412.03603/README.md)、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)、[Kling-Omni](../../papers/arxiv-2512.16776/README.md)、[Qwen-Image](../../papers/arxiv-2508.02324/README.md)（冻结的 Qwen2.5-VL）、[Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md)（冻结的 Qwen3-VL）、[LongCat-Image](../../papers/arxiv-2512.07584/README.md)（引号内文字逐字编码）、[Sora](../../papers/sora-tech-report/README.md)（用 GPT 扩写提示） | 长提示与参考图、参考视频都能接；改写器本身可能替模型"答题" |
| 6 条件 | 动作或潜在动作 | [Genie](../../papers/arxiv-2402.15391/README.md)（8 个潜在动作）、[GameNGen](../../papers/arxiv-2408.14837/README.md)、[DIAMOND](../../papers/arxiv-2405.12399/README.md)、[GAIA-1](../../papers/arxiv-2309.17080/README.md)、[Cosmos](../../papers/arxiv-2501.03575/README.md) | 可交互；动作空间窄 |
| 7 规模化 | 计算量与样本质量的平滑关系 | [Improved DDPM](../../papers/arxiv-2102.09672/README.md)（FID 随算力近似幂律）、[DiT](../../papers/arxiv-2212.09748/README.md)（−0.93）、[VAR](../../papers/arxiv-2404.02905/README.md)（−0.998）、[SD3](../../papers/arxiv-2403.03206/README.md)（未见饱和）、[Wan](../../papers/arxiv-2503.20314/README.md) | 投入可规划；[HunyuanVideo](../../papers/arxiv-2412.03603/README.md) 自述随意扩大效率不够，[Cosmos](../../papers/arxiv-2501.03575/README.md) 发现更大不更符合物理 |
| 7 后训练 | DPO、奖励模型 RLHF、强化学习 | [SD3](../../papers/arxiv-2403.03206/README.md)（512² 上 GenEval 0.68 → 0.71）、[Seedance 1.0](../../papers/arxiv-2506.09113/README.md)（三个奖励模型）、[Kling-Omni](../../papers/arxiv-2512.16776/README.md)、[Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md)（五类奖励模型 + 基于 GRPO 的扩散强化学习） | 偏好与提示遵循提升；改进只覆盖奖励模型测得到的维度（Seedance 1.0 分基础、运动、美学三类） |
| 7 后训练 | 扩散 GRPO：去噪轨迹当决策过程，视觉语言模型打分的奖励模型 | [Qwen-Image](../../papers/arxiv-2508.02324/README.md)（DPO 后 GRPO，GenEval 0.87 → 0.91）、[Qwen-Image-2.0-RL](../../papers/arxiv-2606.27608/README.md)（逐点打分奖励、只用 CFG 采样、只训高噪声步、在策略蒸馏合并任务专家）、[HunyuanImage 3.0](../../papers/arxiv-2509.23951/README.md)（DPO → MixGRPO → SRPO）、[LongCat-Image](../../papers/arxiv-2512.07584/README.md)（AIGC 检测器作奖励） | 位置、写字、质感显著提升；全部去噪步都训会迅速奖励投机，改进只到奖励模型测得到的维度 |
| 7 多任务 | 文生图与编辑联合训练，编辑成为一等任务 | [Qwen-Image](../../papers/arxiv-2508.02324/README.md)（输入图同时进 VL 与 VAE）、[Seedream 4.0](../../papers/arxiv-2509.20427/README.md)（单图、多图编辑与多图输出）、[Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md)（预训练即混入编辑数据）、[Gemini 3.1 Flash Image](../../papers/gemini-3-1-flash-image-model-card/README.md) | 一个模型覆盖创作流程；遵循指令与保持原图互相牵制（Seedream 4.0 人评：GPT-Image-1 遵循最好、一致性最差，Gemini 2.5 相反） |
| 7 多任务 | 参考生成、编辑、续写、音频放进一个模型 | [Veo 3](../../papers/veo3-tech-report/README.md)（音视频联合去噪）、[Seedance 2.0](../../papers/arxiv-2604.14148/README.md)、[Kling-Omni](../../papers/arxiv-2512.16776/README.md) | 一个模型覆盖创作流程；编辑时不响应或改错区域是共同失败 |
| 8 时间轴 | 整块视频联合去噪 + 分块延长 | [Video Diffusion](../../papers/video-diffusion/README.md)（重建引导）、[Imagen Video](../../papers/arxiv-2210.02303/README.md) | 块内连贯；Imagen Video 单次约 5.3 秒 |
| 8 时间轴 | 原生时长与长宽比，图像当单帧视频 | [Sora](../../papers/sora-tech-report/README.md)、[HunyuanVideo](../../papers/arxiv-2412.03603/README.md)、[Wan](../../papers/arxiv-2503.20314/README.md) | 最长一分钟；长视频会逐渐不连贯 |
| 8 时间轴 | 逐帧自回归 + 动作条件 | [Genie](../../papers/arxiv-2402.15391/README.md)（16 帧记忆、约 1 帧/秒）、[Genie 2](../../papers/genie-2-blog/README.md)、[Genie 3](../../papers/genie-3-blog/README.md)（约一分钟视觉记忆）、[GameNGen](../../papers/arxiv-2408.14837/README.md)（给上下文帧加噪抗漂移）、[DIAMOND](../../papers/arxiv-2405.12399/README.md) | 实时可玩；误差累积，记忆只有几秒到一分钟 |
| 9 评测 | 精度与召回分开测保真与覆盖 | [Improved DDPM](../../papers/arxiv-2102.09672/README.md)、[ADM](../../papers/arxiv-2105.05233/README.md) | 暴露 GAN 召回低；仍依赖 Inception 特征 |
| 9 评测 | 人评 + 分项考题 | [Imagen](../../papers/arxiv-2205.11487/README.md)（DrawBench）、[Parti](https://arxiv.org/abs/2206.10789)（PartiPrompts）、[SD3](../../papers/arxiv-2403.03206/README.md)（GenEval） | 位置、计数、绑定这类弱项被单独测出；提示集与评审各家不同，不能跨报告比较 |
| 9 评测 | 竞技场 Elo（用户盲选）+ 各家自建考题 | [Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md)（LMArena）、[Qwen-Image-2.0-RL](../../papers/arxiv-2606.27608/README.md)（Qwen-Image-Bench）、[Seedream 4.0](../../papers/arxiv-2509.20427/README.md)（MagicBench、DreamEval）、[Gemini 3.1 Flash Image](../../papers/gemini-3-1-flash-image-model-card/README.md)（GenAI-Bench Elo） | GenEval 接近饱和后的替代；榜单随时间变，自建考题互不可比 |
| 9 评测 | 视频的物理常识与物理规律 | [VideoPhy](../../papers/arxiv-2406.03520/README.md)（最好 39.6%）、[Physics-IQ](../../papers/arxiv-2501.09038/README.md)（最好 29.5%）、[PhyWorld](../../papers/arxiv-2411.02385/README.md)（分布外误差不随规模下降） | 逼真与物理正确分开测；场景数有限 |

[判断] 读完这张表，DDPM 的九个部件里，从 2020 年留到 2026 年的只有部件 4 的训练形态（"答案由我们自己加的噪声或路径给出，网络回归它"）。表示空间、主干、路径形状、采样器、条件接入在 2021–2024 年全部换过；2024 年之后的竞争集中到部件 1（数据与描述）、部件 7（规模化与后训练）和部件 8（时间轴与动作）。2025–2026 年的图像报告也是这样：[Qwen-Image-2.0](../../papers/arxiv-2605.10730/README.md) 的引言把超长文字、多语言排版、2K 以上的高分辨率写实、复杂指令遵循列为仍未解决的问题，改动集中在数据、条件编码器（多模态大模型）和强化学习上；部件 3 上的新动向是把自回归与扩散放进同一个语言模型（[HunyuanImage 3.0](../../papers/arxiv-2509.23951/README.md)）。

## 方法后继：重新选择预测对象与潜空间

| 部件 | 改法 | 代表 | 为什么值得对照 |
|---|---|---|---|
| 4 目标 / 5 采样 | 从瞬时速度改为区间平均速度，直接训练一步生成 | [MeanFlow](../../papers/arxiv-2505.13447/README.md) | 与"多步教师再蒸馏"区别在目标；主要证据为类条件图像 |
| 2 表示 | 冻结语义编码器，训练解码器组成RAE；在高维特征中扩散 | [RAE](../../papers/arxiv-2510.11690/README.md) | 把理解表征接到生成；需处理高维噪声与容量 |
| 2 表示 / 4 目标 | 将RAE扩到自由文本，重测小规模配方 | [Scaling T2I RAE](../../papers/arxiv-2601.16208/README.md) | 部分网络补丁可简化；保留噪声调度，结论限于所选编码器/VAE对照 |

## 批注

**易误读**

- LDM 的 3.60 与 DiT 的 2.27 都用了无分类器引导（LDM 引导系数 1.5，LDM Table 3；DiT Table 2）；ADM-G 的 4.59 用的是分类器引导，三者都是 250 步采样。
- 表中"约省 40% 网络调用"指 Flow Matching 在 ImageNet 32×32 上达到同样数值误差约需扩散路径 60% 的调用（Fig.7），不是同 FID 下的步数。
- Rectified Flow 的 4.85 是 2-整流流再蒸馏后的一步结果；不蒸馏的一步为 12.21（Table 1）。
- CFG 的 2.43 是 256 步、每步两次前向；按网络调用次数对齐 ADM-G 应看 128 步的 3.04（CFG Sec.4.3）。
- SD3 的 GenEval 0.68 → 0.71 是 8B 模型在 512² 上加 DPO 前后；0.74 是 1024² 加 DPO（SD3 Table 5）。
- VQGAN 的 5.20 是按分类器打分只留 5% 样本的结果，不用拒绝采样为 15.78（VQGAN Table 4）。
- 视频行里的数字都来自各家自己的报告，评测提示集与评审不同，不能互相比较。

**与其他论文的关联**

- 部件 4 与 5 的推导链（预测噪声 = 估计分数，概率流 ODE，直线路径）见[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6 节与 [DDPM 精读](../../papers/ddpm/reading.md)"局限与后续"；部件 6 的引导公式见 [Video Diffusion 精读](../../papers/video-diffusion/reading.md)机制第 5 节。
- 部件 3 的卷积到 Transformer 的转换，跨领域论证见[观点页：CNN 与 Transformer](../../../perspectives/cnn-vs-transformer.md)；视频一侧各家结构对照见[观点页：生成收敛](../../../perspectives/generative-convergence.md)阶段四的表。
- 部件 8 的"逐帧自回归 + 动作条件"在[世界模型方向](../world-models/BASELINES.md)有自己的 Baseline 表；同一套训练形态用于机器人动作，见 [Diffusion Policy](../../../robotics-embodied/papers/diffusion-policy/README.md) 与 [π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md)（流匹配动作头）。
- 部件 6 的 CLIP 来自[图文对齐方向](../alignment/README.md)；部件 6 的 decoder-only 文本编码器与[视觉语言模型方向](../vlm/README.md)的模型同源。

**判断的支撑与边界**

- "只有训练形态留了下来"：支撑是本表各行（LDM、DiT、Flow Matching、DDIM、CFG、SD3 各换一个部件）与[观点页](../../../perspectives/generative-convergence.md)"驱动力 1"。边界：流匹配回归的是速度而不是噪声，两者可以互相换算（[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6.1 节），所以"形态留下"指"答案由人为构造的路径给出"这一点；VAR 与 Genie 一类自回归模型的训练形态是下一 token 或下一尺度预测，不在这条线上。
- "2024 年之后竞争集中到数据、后训练、时间轴"：支撑是 Seedance 1.0（RLHF、蒸馏）、Kling-Omni（强化学习）、SD3（合成描述、DPO）、Genie 2/3，以及 Qwen-Image-2.0 第 1 节（数据飞轮、Qwen3-VL 条件编码器、GRPO 强化学习）。边界：Seedance 2.0、Veo 3、Kling-Omni 没有公开结构，结构上是否仍在变化无法从官方材料判断。
- "判别器以损失项留在自编码器里"（入门页"三个家族的分工"）的反例：Qwen-Image 第 2.3 节（重建变好后判别器给不出有效指导）与 Qwen-Image-2.0 第 3.1 节认为大规模 VAE 训练中对抗损失多余，去掉它以求训练稳定，改用语义对齐损失。判别器在蒸馏（ADD、Seedance 1.0、Seedream 4.0）中的作用不受这条影响；LongCat-Image 把 AIGC 检测器当奖励模型，判别信号换到了后训练。

**未核实 / 待验证**

- 2025–2026 年各行的事实取自对应文献卡（本轮打开了 Qwen-Image、Qwen-Image-2.0、Qwen-Image-2.0-RL、HunyuanImage 3.0、Seedream 3.0/4.0、LongCat-Image、ERNIE-Image 的 PDF 与 OpenAI、Google 的官方系统卡和模型卡）。GPT-4o 图像生成、Gemini 图像模型与 Seedream 4.0 的结构未公开，表中只写官方措辞；Seedream 5.0 Lite、FLUX.2、Z-Image、GLM-Image 的官方材料没有打开。
- DCGAN、Parti 本轮没有建卡，表中链接到 arXiv，相关数字以[入门页](README.md)与 [synthesis.csv](synthesis.csv) 为准。
- 视频与世界模型各行（Imagen Video 至 Genie 3、DIAMOND、GAIA-1、Cosmos、VideoPhy、PhyWorld、Physics-IQ、Chameleon、LAION-5B）的事实取自对应文献卡与观点页，本页没有重新打开原文。
- "改写器本身可能替模型答题"的依据是 Veo 3 零样本论文的作者自述（见[观点页](../../../perspectives/generative-convergence.md)批注），在图像模型上没有找到同类实验。
