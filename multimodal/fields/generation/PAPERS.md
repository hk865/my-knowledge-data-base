# 视觉生成：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

按[入门页](README.md)"主线历史"的节点分组，节点之后是续篇（视频与公司模型、世界模型）和交叉引用。每项链接到唯一的单篇目录；"Baseline 格"指 [Baseline 页](BASELINES.md)"后续工作在改哪个部件"表中的部件编号（1 数据、2 表示、3 主干与生成过程、4 目标与路径、5 采样、6 条件与引导、7 规模化与后训练、8 时间轴与动作、9 评测）。跨方向出现是交叉引用，不重复计数。

## 基线

- [Denoising Diffusion Probabilistic Models](../../papers/ddpm/README.md)（DDPM）· 2020 · 技术精读 · 训练与采样的基线（主线节点 3）
- [High-Resolution Image Synthesis with Latent Diffusion Models](../../papers/arxiv-2112.10752/README.md)（LDM）· 2021 · 文献卡 · 现代骨架基线之一（主线节点 6）；Baseline 格 2、6
- [Scalable Diffusion Models with Transformers](../../papers/arxiv-2212.09748/README.md)（DiT）· 2022 · 文献卡 · 现代骨架基线之一（主线节点 8）；Baseline 格 3、7
- [Classifier-Free Diffusion Guidance](../../papers/arxiv-2207.12598/README.md) · 2022 · 文献卡 · 现代骨架的引导部件；Baseline 格 6

## 节点 1–2：潜变量模型与对抗训练（2013–2015）

- [Auto-Encoding Variational Bayes](../../papers/arxiv-1312.6114/README.md)（VAE）· 2013 · 文献卡 · Baseline 格 2 的源头
- [Generative Adversarial Networks](../../papers/arxiv-1406.2661/README.md)（GAN）· 2014 · 文献卡 · 对照基线；Baseline 格 4
- DCGAN（[arXiv:1511.06434](https://arxiv.org/abs/1511.06434)）· 2015 · 本库无单篇目录，见入门页节点 2；Baseline 格 4

## 节点 3：扩散成形，以及同期的采样与目标改进（2020–2021）

- [Score-Based Generative Modeling through Stochastic Differential Equations](../../papers/arxiv-2011.13456/README.md)（Score SDE）· 2020 · 文献卡 · Baseline 格 4、5
- [Denoising Diffusion Implicit Models](../../papers/arxiv-2010.02502/README.md)（DDIM）· 2020 · 文献卡 · Baseline 格 5
- [Improved Denoising Diffusion Probabilistic Models](../../papers/arxiv-2102.09672/README.md) · 2021 · 文献卡 · Baseline 格 4、6、7、9

## 节点 4：离散 token 与自回归（2020–2021）

- [Taming Transformers for High-Resolution Image Synthesis](../../papers/arxiv-2012.09841/README.md)（VQGAN）· 2020 · 文献卡 · 对照基线的分词器；Baseline 格 2、3
- [Zero-Shot Text-to-Image Generation](../../papers/arxiv-2102.12092/README.md)（DALL·E）· 2021 · 文献卡 · Baseline 格 1、2、3

## 节点 5：扩散超过 GAN，引导出现（2021）

- [Diffusion Models Beat GANs on Image Synthesis](../../papers/arxiv-2105.05233/README.md)（ADM）· 2021 · 文献卡 · Baseline 格 2、3、6、9
- 无分类器引导见"基线"一组

## 节点 6：潜空间扩散（2021）

- LDM 见"基线"一组
- [LAION-5B: An open large-scale dataset for training next generation image-text models](../../papers/arxiv-2210.08402/README.md) · 2022 · 文献卡 · 目录在[图文对齐方向](../alignment/README.md)；Baseline 格 1

## 节点 7：任意文字作条件，扩到视频（2022）

- [Hierarchical Text-Conditional Image Generation with CLIP Latents](../../papers/arxiv-2204.06125/README.md)（DALL·E 2 / unCLIP）· 2022 · 文献卡 · Baseline 格 2、6
- [Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding](../../papers/arxiv-2205.11487/README.md)（Imagen）· 2022 · 文献卡 · Baseline 格 1、2、3、6、9
- Parti（[arXiv:2206.10789](https://arxiv.org/abs/2206.10789)）· 2022 · 本库无单篇目录，见入门页节点 7；Baseline 格 9
- [Video Diffusion Models](../../papers/video-diffusion/README.md) · 2022 · 技术精读 · Baseline 格 2、3、4、5、8

## 节点 8：Transformer 主干（2022）

- DiT 见"基线"一组

## 节点 9：直线路径、规模化与少步（2022–2024）

- [Flow Matching for Generative Modeling](../../papers/arxiv-2210.02747/README.md) · 2022 · 文献卡 · Baseline 格 4
- [Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow](../../papers/arxiv-2209.03003/README.md) · 2022 · 文献卡 · Baseline 格 4、5
- [Adversarial Diffusion Distillation](../../papers/arxiv-2311.17042/README.md)（ADD）· 2023 · 文献卡 · Baseline 格 5
- [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](../../papers/arxiv-2403.03206/README.md)（SD3）· 2024 · 文献卡 · Baseline 格 1、2、3、4、5、6、7、9
- [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](../../papers/arxiv-2404.02905/README.md)（VAR）· 2024 · 文献卡 · Baseline 格 3、7

## 节点 10：语言模型进入生成器，生成与编辑合一，扩散强化学习（2025–2026）

- [Addendum to GPT-4o System Card: Native image generation](../../papers/gpt-4o-image-generation-system-card/README.md)（GPT-4o 图像生成）· 2025 · 文献卡（官方系统卡）· Baseline 格 3
- [Qwen-Image Technical Report](../../papers/arxiv-2508.02324/README.md) · 2025 · 文献卡 · Baseline 格 2、6、7
- [Seedream 4.0: Toward Next-generation Multimodal Image Generation](../../papers/arxiv-2509.20427/README.md) · 2025 · 文献卡 · Baseline 格 5、7、9
- [HunyuanImage 3.0 Technical Report](../../papers/arxiv-2509.23951/README.md) · 2025 · 文献卡 · Baseline 格 3、7；交叉引用[视觉语言模型方向](../vlm/README.md)
- [LongCat-Image Technical Report](../../papers/arxiv-2512.07584/README.md) · 2025 · 文献卡 · Baseline 格 6、7
- [Gemini 3.1 Flash Image Model Card](../../papers/gemini-3-1-flash-image-model-card/README.md)（Nano Banana 2）· 2026 · 文献卡（官方模型卡）· Baseline 格 3、7、9
- [Qwen-Image-2.0 Technical Report](../../papers/arxiv-2605.10730/README.md) · 2026 · 文献卡 · Baseline 格 2、5、6、7、9
- [Qwen-Image-2.0-RL Technical Report](../../papers/arxiv-2606.27608/README.md) · 2026 · 文献卡 · Baseline 格 7、9
- 本库无单篇目录、只在入门页批注引用：Seedream 3.0（[arXiv:2504.11346](https://arxiv.org/abs/2504.11346)）、ERNIE-Image（[arXiv:2605.25347](https://arxiv.org/abs/2605.25347)）、[ChatGPT Images 2.0 系统卡](https://deploymentsafety.openai.com/chatgpt-images-2-0)（2026）、[Gemini 3 Pro Image 模型卡](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Image-Model-Card.pdf)（2025）

## 续篇：视频生成与公司模型（2022–2026）

论证见[观点页：生成收敛](../../../perspectives/generative-convergence.md)阶段四。

- [Imagen Video: High Definition Video Generation with Diffusion Models](../../papers/arxiv-2210.02303/README.md) · 2022 · 文献卡 · Baseline 格 2、3、4、5、6、8
- [Video generation models as world simulators](../../papers/sora-tech-report/README.md)（Sora 技术报告）· 2024 · 文献卡 · Baseline 格 1、2、6、8
- [HunyuanVideo: A Systematic Framework For Large Video Generative Models](../../papers/arxiv-2412.03603/README.md) · 2024 · 文献卡 · Baseline 格 1、2、3、4、6、7、8
- [Veo: a text-to-video generation system](../../papers/veo3-tech-report/README.md)（Veo 3）· 2025 · 文献卡 · Baseline 格 1、3、7
- [Wan: Open and Advanced Large-Scale Video Generative Models](../../papers/arxiv-2503.20314/README.md) · 2025 · 文献卡 · Baseline 格 1、2、4、7、8
- [Seedance 1.0: Exploring the Boundaries of Video Generation Models](../../papers/arxiv-2506.09113/README.md) · 2025 · 文献卡 · Baseline 格 1、2、3、4、5、6、7
- [Kling-Omni Technical Report](../../papers/arxiv-2512.16776/README.md) · 2025 · 文献卡 · Baseline 格 3、5、6、7
- [Seedance 2.0: Advancing Video Generation for World Complexity](../../papers/arxiv-2604.14148/README.md) · 2026 · 文献卡 · Baseline 格 3、7

## 续篇：世界模型与物理评测（目录主要在[世界模型方向](../world-models/PAPERS.md)）

- [Genie: Generative Interactive Environments](../../papers/arxiv-2402.15391/README.md) · 2024 · 文献卡 · Baseline 格 1、6、8
- [Genie 2: A large-scale foundation world model](../../papers/genie-2-blog/README.md) · 2024 · 文献卡（官方博客）· Baseline 格 5、6、8
- [Genie 3: A new frontier for world models](../../papers/genie-3-blog/README.md) · 2025 · 文献卡（官方博客）· Baseline 格 8
- [Diffusion Models Are Real-Time Game Engines](../../papers/arxiv-2408.14837/README.md)（GameNGen）· 2024 · 文献卡 · Baseline 格 1、6、8
- [Diffusion for World Modeling: Visual Details Matter in Atari](../../papers/arxiv-2405.12399/README.md)（DIAMOND）· 2024 · 文献卡 · Baseline 格 6、8
- [GAIA-1: A Generative World Model for Autonomous Driving](../../papers/arxiv-2309.17080/README.md) · 2023 · 文献卡 · Baseline 格 1、3、6
- [Cosmos World Foundation Model Platform for Physical AI](../../papers/arxiv-2501.03575/README.md) · 2025 · 文献卡 · Baseline 格 1、3、6、7
- [VideoPhy: Evaluating Physical Commonsense for Video Generation](../../papers/arxiv-2406.03520/README.md) · 2024 · 文献卡 · Baseline 格 9
- [How Far is Video Generation from World Model: A Physical Law Perspective](../../papers/arxiv-2411.02385/README.md)（PhyWorld）· 2024 · 文献卡 · Baseline 格 9
- [Do generative video models understand physical principles?](../../papers/arxiv-2501.09038/README.md)（Physics-IQ）· 2025 · 文献卡 · Baseline 格 9

## 交叉引用（目录在其他方向）

- [Chameleon: Mixed-Modal Early-Fusion Foundation Models](../../papers/arxiv-2405.09818/README.md) · 2024 · [视觉语言模型方向](../vlm/README.md)的早融合代表，图像 token 也用于生成；Baseline 格 2、3
- [Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md)（CLIP）· 2021 · DALL·E 2 的条件来源，见[图文对齐方向](../alignment/README.md)
- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../../../robotics-embodied/papers/diffusion-policy/README.md) · 2023 · DDPM 的训练与采样用于动作序列
- [π0: A Vision-Language-Action Flow Model for General Robot Control](../../../robotics-embodied/papers/arxiv-2410.24164/README.md) · 2024 · 流匹配动作头
- [Evaluating Gemini Robotics Policies in a Veo World Simulator](../../../robotics-embodied/papers/arxiv-2512.10675/README.md) · 2025 · 视频生成模型用作机器人策略的评估器

## 预测目标与潜空间的方法后继（2025–2026）

- [MeanFlow](../../papers/arxiv-2505.13447/README.md)：学区间平均速度，必读
- [RAE](../../papers/arxiv-2510.11690/README.md)：冻结语义编码器配生成解码器，必读
- [Scaling T2I RAE](../../papers/arxiv-2601.16208/README.md)：从类条件实验扩到自由文本生成，选读

## 世界模型的条件生成接口

- [World Simulation with Video Foundation Models for Physical AI](../../papers/arxiv-2511.00062/README.md)（Cosmos-Predict2.5 / Transfer2.5） · 2025 · 文献卡 · 多条件视频生成、奖励后训练与空间控制；主归属[世界模型](../world-models/README.md)
- [Cosmos 3: Omnimodal World Models for Physical AI](../../papers/arxiv-2606.02800/README.md) · 2026 · 文献卡 · 自回归推理与扩散生成的双流接口；主归属[世界模型](../world-models/README.md)
