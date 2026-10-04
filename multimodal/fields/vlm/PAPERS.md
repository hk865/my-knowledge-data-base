# 视觉语言模型：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

每项链接到唯一的单篇目录；"Baseline 格"指 [Baseline 页](BASELINES.md)"后续工作在改哪个部件"表中的部件编号。跨方向出现是交叉引用，不重复计数。

## 基线与对照基线

- [Visual Instruction Tuning](../../papers/llava/README.md)（LLaVA）· 2023 · 技术精读 · 主基线（原版）
- [Improved Baselines with Visual Instruction Tuning](../../papers/arxiv-2310.03744/README.md)（LLaVA-1.5）· 2023 · 文献卡 · 主基线
- [Flamingo: a Visual Language Model for Few-Shot Learning](../../papers/arxiv-2204.14198/README.md) · 2022 · 文献卡 · 对照基线；Baseline 格 3、5
- [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](../../papers/arxiv-2301.12597/README.md) · 2023 · 文献卡 · 对照基线；Baseline 格 3

## 模型

- [PaLI: A Jointly-Scaled Multilingual Language-Image Model](../../papers/arxiv-2209.06794/README.md) · 2022 · 文献卡 · Baseline 格 4、6
- [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](../../papers/arxiv-2308.12966/README.md) · 2023 · 文献卡 · Baseline 格 1、3、5、6
- [InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks](../../papers/arxiv-2312.14238/README.md) · 2023 · 文献卡 · Baseline 格 1
- [Gemini: A Family of Highly Capable Multimodal Models](../../papers/arxiv-2312.11805/README.md) · 2023 · 文献卡 · Baseline 格 4
- [DeepSeek-VL: Towards Real-World Vision-Language Understanding](../../papers/arxiv-2403.05525/README.md) · 2024 · 文献卡 · Baseline 格 1、5
- [How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites](../../papers/arxiv-2404.16821/README.md)（InternVL 1.5）· 2024 · 文献卡 · Baseline 格 1、2、3
- [Chameleon: Mixed-Modal Early-Fusion Foundation Models](../../papers/arxiv-2405.09818/README.md) · 2024 · 文献卡 · Baseline 格 4
- [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](../../papers/arxiv-2409.12191/README.md) · 2024 · 文献卡 · Baseline 格 1、2、3、5
- [Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models](../../papers/arxiv-2409.17146/README.md) · 2024 · 文献卡 · Baseline 格 2、5、6、8
- [Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling](../../papers/arxiv-2412.05271/README.md)（InternVL 2.5）· 2024 · 文献卡 · Baseline 格 1、6
- [DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding](../../papers/arxiv-2412.10302/README.md) · 2024 · 文献卡 · Baseline 格 1、2、4
- [Qwen2.5-VL Technical Report](../../papers/arxiv-2502.13923/README.md) · 2025 · 文献卡 · Baseline 格 1、2、5、7
- [Kimi-VL Technical Report](../../papers/arxiv-2504.07491/README.md) · 2025 · 文献卡 · Baseline 格 2、3、4、5、7
- [InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models](../../papers/arxiv-2504.10479/README.md) · 2025 · 文献卡 · Baseline 格 5、7
- [Qwen3-VL Technical Report](../../papers/arxiv-2511.21631/README.md) · 2025 · 文献卡 · Baseline 格 2、3、4、7

## 评测与诊断

- [Evaluating Object Hallucination in Large Vision-Language Models](../../papers/arxiv-2305.10355/README.md)（POPE）· 2023 · 文献卡 · Baseline 格 8
- [Are We on the Right Way for Evaluating Large Vision-Language Models?](../../papers/arxiv-2403.20330/README.md)（MMStar）· 2024 · 文献卡 · Baseline 格 8
- [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](../../papers/arxiv-2406.16860/README.md) · 2024 · 文献卡 · Baseline 格 1、3、5、8

## 交叉引用（目录在其他方向）

- [Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md)（CLIP）· 2021 · VLM 最常用的视觉塔来源，见[图文对齐](../alignment/README.md)
- [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](../../../llm/papers/arxiv-2403.05530/README.md) · 2024 · 长上下文方向的卡片
- [OpenVLA: An Open-Source Vision-Language-Action Model](../../../robotics-embodied/papers/openvla/README.md) · 2024 · VLM 骨干用于机器人，见 [VLA 方向](../../../robotics-embodied/fields/vla/README.md)
- [RT-2](../../../robotics-embodied/papers/arxiv-2307.15818/README.md)、[π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md)、[InternVLA-A1](../../../robotics-embodied/papers/arxiv-2601.02456/README.md)、[Qwen-VLA](../../../robotics-embodied/papers/arxiv-2605.30280/README.md) · 以 PaLI-X / PaLM-E、PaliGemma、InternVL3 与 Qwen3-VL、Qwen VLM 为底座的 VLA

## 联合训练、视觉初始化与音视频智能体（2026）

- [Kimi K2.5](../../../llm/papers/arxiv-2602.02276/README.md)：必读固定预算下的视觉注入时机对照
- [Qwen3.5](../../../llm/papers/qwen3.5/README.md)：选读另一团队的早融合与混合注意力配方
- [Kimi K3](../../../llm/papers/arxiv-2607.24653/README.md)：必读从零视觉塔与预训练视觉塔的稳定性对照
- [Qwen3.8-Omni](../../papers/arxiv-2609.25611/README.md)：选读从音视频理解到工具闭环的接口变化

## 检索、视频取证与世界模型的交叉接口

- [Qwen3-VL-Embedding and Qwen3-VL-Reranker](../../papers/arxiv-2601.04720/README.md) · 2026 · 文献卡 · VLM 用于独立召回与逐对重排；主归属[图文对齐](../alignment/README.md)
- [InternVideo3](../../papers/arxiv-2606.12195/README.md) · 2026 · 文献卡 · 长视频上下文、缓存压缩与多轮取证；主归属[视频与时序](../video-temporal/README.md)
- [Cosmos 3](../../papers/arxiv-2606.02800/README.md) · 2026 · 文献卡 · VLM 推理流与视频、动作生成流连接；主归属[世界模型](../world-models/README.md)
