# 视频与时序表征论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

本目录按[入门页](README.md)主线历史的阶段排列。每篇链接到唯一的单篇目录；"格"指它在 [Baseline 表](BASELINES.md)中的位置。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 1 双流与光流（2014）

- [Two-Stream Convolutional Networks for Action Recognition in Videos](../../papers/arxiv-1406.2199/README.md) · 2014 · University of Oxford · 文献卡 · 格：时间算子 = 预计算光流

## 2 大规模动作数据与反外观 benchmark（2017）

- [Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset](../../papers/arxiv-1705.07750/README.md) · 2017 · DeepMind、University of Oxford · 文献卡 · 格：时间算子 = 膨胀 3D 卷积 + 光流（基线）
- [The "something something" video database for learning and evaluating visual common sense](../../papers/arxiv-1706.04261/README.md) · 2017 · TwentyBN · 文献卡 · 格：评测协议 = 模板与假装动作

## 3 双速率（2018）

- [SlowFast Networks for Video Recognition](../../papers/arxiv-1812.03982/README.md) · 2018 · FAIR · 文献卡 · 格：时间算子 = 双速率

## 4 视频 Transformer（2021）

- [Is Space-Time Attention All You Need for Video Understanding?](../../papers/arxiv-2102.05095/README.md) · 2021 · Facebook AI、Dartmouth College · 文献卡 · 格：时间算子 = 分开的时空注意力
- [ViViT: A Video Vision Transformer](../../papers/arxiv-2103.15691/README.md) · 2021 · Google Research · 文献卡 · 格：时间算子 / 帧采样 = 时空管道与分解编码器

## 5 视频自监督（2022–2024）

- [VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](../../papers/arxiv-2203.12602/README.md) · 2022 · 南京大学、腾讯 AI Lab、上海人工智能实验室 · 文献卡 · 格：预训练信号 = 管道遮蔽重建像素
- [Revisiting Feature Prediction for Learning Visual Representations from Video](../../papers/arxiv-2404.08471/README.md)（V-JEPA） · 2024 · Meta FAIR 等 · 文献卡 · 格：预训练信号 = 特征预测；评测协议 = 冻结 + 注意力探针

## 6 视频-语言与长视频评测（2022–2023）

- [Revealing Single Frame Bias for Video-and-Language Learning](../../papers/arxiv-2206.03428/README.md) · 2022 · UNC Chapel Hill · 文献卡 · 格：时间算子（反向检验）= 单帧训练
- [EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](../../papers/arxiv-2308.09126/README.md) · 2023 · UC Berkeley · 文献卡 · 格：评测协议 = 时间证书长度

## 7 视频大模型（2023–2025）

- [Video-LLaVA: Learning United Visual Representation by Alignment Before Projection](../../papers/arxiv-2311.10122/README.md) · 2023 · 北京大学等 · 文献卡 · 格：每帧表示 = 预对齐编码器 + 共享投影（基线）
- [InternVideo2: Scaling Foundation Models for Multimodal Video Understanding](../../papers/arxiv-2403.15377/README.md) · 2024 · 上海人工智能实验室等 · 文献卡 · 格：预训练信号 / 数据 = 三阶段
- [Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](../../papers/arxiv-2405.21075/README.md) · 2024 · 南京大学等 · 文献卡 · 格：评测协议 = 分时长档 + 字幕与音频
- [LLaVA-Video: Video Instruction Tuning With Synthetic Data](../../papers/arxiv-2410.02713/README.md) · 2024 · ByteDance、南洋理工大学 · 文献卡 · 格：数据 / 每帧表示 = 合成指令数据 + 慢快帧 token 分配（基线）
- [Qwen2.5-VL Technical Report](../../papers/arxiv-2502.13923/README.md) · 2025 · 阿里巴巴 Qwen 团队 · 暂无单篇目录 · 格：帧采样 / 时间位置 = 动态帧率 + 绝对时间 MRoPE

## 交叉引用（主归属在其他方向）

视频生成（机制见[视觉生成方向](../generation/README.md)，本方向只引用其时间建模的做法）：

- [Video Diffusion Models](../../papers/video-diffusion/README.md) · 2022 · Google · 技术精读 · 空间与时间分解的 3D U-Net
- [Imagen Video: High Definition Video Generation with Diffusion Models](../../papers/arxiv-2210.02303/README.md) · 2022 · Google · 文献卡 · 时间超分辨率级联
- [Video generation models as world simulators](../../papers/sora-tech-report/README.md)（Sora） · 2024 · OpenAI · 文献卡 · 时空压缩与时空 patch
- [HunyuanVideo: A Systematic Framework For Large Video Generative Models](../../papers/arxiv-2412.03603/README.md) · 2024 · 腾讯混元 · 文献卡 · 因果 3D VAE
- [Wan: Open and Advanced Large-Scale Video Generative Models](../../papers/arxiv-2503.20314/README.md) · 2025 · 阿里通义万相 · 文献卡 · 时间 4 倍压缩的 3D 因果 VAE
- [Seedance 1.0: Exploring the Boundaries of Video Generation Models](../../papers/arxiv-2506.09113/README.md) · 2025 · 字节跳动 Seed · 文献卡 · 空间层与时间层解耦
- [Veo: a text-to-video generation system](../../papers/veo3-tech-report/README.md) · 2025 · Google DeepMind · 文献卡 · 时空潜变量扩散
- [Kling-Omni Technical Report](../../papers/arxiv-2512.16776/README.md) · 2025 · 快手 · 文献卡
- [Seedance 2.0: Advancing Video Generation for World Complexity](../../papers/arxiv-2604.14148/README.md) · 2026 · 字节跳动 Seed · 文献卡 · 续写中的主体遗漏或重复

世界模型与机器人：

- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) · 2025 · Meta FAIR 等 · 文献卡 · V-JEPA 的后续，加动作条件预测器
- [SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](../../papers/arxiv-2206.07764/README.md) · 2022 · 文献卡 · 主归属[世界模型方向](../world-models/README.md)
- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](../../papers/arxiv-2210.05861/README.md) · 2022 · 文献卡 · 主归属世界模型方向
- [Back to the Features: DINO as a Foundation for Video World Models](../../papers/arxiv-2507.19468/README.md) · 2025 · 文献卡 · 主归属世界模型方向
