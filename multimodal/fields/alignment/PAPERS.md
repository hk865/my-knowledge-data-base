# 图文对齐：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

以下每项链接到唯一的单篇目录，方括号里是它在 [Baseline 页](BASELINES.md)"后续工作在改哪个部件"表中的格。跨方向出现是交叉引用，不重复计算资源。各篇的问题、对照、局限与出处见 [synthesis.csv](synthesis.csv)。

## 基线

- [Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md)（CLIP）· 2021 · 逐步教学版 · [基线]
- [Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision](../../papers/arxiv-2102.05918/README.md)（ALIGN）· 2021 · 文献卡 · [基线：同一接口的另一种数据选择]

## 改数据

- [LAION-5B: An open large-scale dataset for training next generation image-text models](../../papers/arxiv-2210.08402/README.md) · 2022 · 文献卡 · [数据：CLIP 打分过滤并公开]
- [Reproducible scaling laws for contrastive language-image learning](../../papers/arxiv-2212.07143/README.md)（OpenCLIP 缩放定律）· 2022 · 文献卡 · [数据：规模测量]
- [DataComp: In search of the next generation of multimodal datasets](../../papers/arxiv-2304.14108/README.md) · 2023 · 文献卡 · [数据：固定训练、只比数据]
- [Demystifying CLIP Data](../../papers/arxiv-2309.16671/README.md)（MetaCLIP）· 2023 · 文献卡 · [数据：元数据加平衡]

## 改训练目标

- [Sigmoid Loss for Language Image Pre-Training](../../papers/arxiv-2303.15343/README.md)（SigLIP）· 2023 · 文献卡 · [训练目标：sigmoid]
- [CoCa: Contrastive Captioners are Image-Text Foundation Models](../../papers/arxiv-2205.01917/README.md) · 2022 · 文献卡 · [训练目标：对比加描述生成]
- [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](../../papers/arxiv-2201.12086/README.md) · 2022 · 文献卡 · [训练目标：三目标共享参数；数据：CapFilt]
- [SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](../../papers/arxiv-2502.14786/README.md) · 2025 · 文献卡 · [训练目标、文本侧接口、输出与用法]

## 改图像塔

- [LiT: Zero-Shot Transfer with Locked-image text Tuning](../../papers/arxiv-2111.07991/README.md) · 2021 · 文献卡 · [图像塔：冻结预训练]
- [EVA-CLIP: Improved Training Techniques for CLIP at Scale](../../papers/arxiv-2303.15389/README.md) · 2023 · 文献卡 · [图像塔：遮蔽建模初始化]
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../../papers/vit/README.md)（ViT）· 2020 · 逐步教学版 · [跨方向：主流图像塔的结构，主属[视觉表征](../visual-representation/README.md)]

## 评测与失败诊断

- [Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](../../papers/arxiv-2204.03162/README.md) · 2022 · 文献卡 · [评测]
- [When and why vision-language models behave like bags-of-words, and what to do about it?](../../papers/arxiv-2210.01936/README.md)（ARO、NegCLIP）· 2022 · 文献卡 · [训练目标：难负样本；评测]
- [SugarCrepe: Fixing Hackable Benchmarks for Vision-Language Compositionality](../../papers/arxiv-2306.14610/README.md) · 2023 · 文献卡 · [评测：修补可被刷分的考题]
- [Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs](../../papers/arxiv-2401.06209/README.md)（MMVP）· 2024 · 文献卡 · [输出与用法：交给 VLM 的接口]

## 交叉引用

- [Visual Instruction Tuning](../../papers/llava/README.md)（LLaVA）· 2023 · 技术精读 · 以 CLIP ViT-L/14 为视觉塔的 VLM，主属[视觉语言模型方向](../vlm/README.md)

## 全球覆盖、特征读出与 VLM 检索（2025–2026）

- [Meta CLIP 2](../../papers/arxiv-2507.22062/README.md)：MetaCLIP 英文数据配方的直接后继，必读
- [Perception Encoder](../../papers/arxiv-2504.13181/README.md)：与 SigLIP 2 对照目标和读出的作用，必读
- [Qwen3-VL-Embedding / Reranker](../../papers/arxiv-2601.04720/README.md)：独立编码与联合编码的两阶段检索，选读
