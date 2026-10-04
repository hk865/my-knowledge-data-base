# 知识蒸馏：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [综合表](synthesis.csv)

以下每项链接到唯一的单篇目录。跨方向出现是交叉引用，不重复计算资源。按入门页的阶段排列。

## 本方向的单篇目录

- [Model Compression](../../papers/url-cornell-compression.kdd06/README.md) · 2006 · 文献卡 · 集成给伪数据打标签，压成小网络（阶段 1）
- [Do Deep Nets Really Need to be Deep?](../../papers/arxiv-1312.6184/README.md) · 2013 · 文献卡 · 浅网络回归深网络的 logit（阶段 2）
- [FitNets: Hints for Thin Deep Nets](../../papers/arxiv-1412.6550/README.md) · 2014 · 文献卡 · 中间层提示，学生比教师更深更窄（阶段 3）
- [Distilling the Knowledge in a Neural Network](../../papers/arxiv-1503.02531/README.md) · 2015 · 文献卡 · 温度软目标，本方向的经典基线（阶段 2）

## 跨方向引用

语言模型：
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](../../../llm/papers/arxiv-1810.04805/README.md) · 2018 · 文献卡 · BERT 时代压缩的教师
- [TinyBERT: Distilling BERT for Natural Language Understanding](../../../llm/papers/arxiv-1909.10351/README.md) · 2019 · 文献卡 · 逐层蒸馏，预训练与微调两段（阶段 4）
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](../../../llm/papers/arxiv-1910.01108/README.md) · 2019 · 文献卡 · 预训练阶段的软标签加隐藏层对齐，层数减半（阶段 4）
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](../../../llm/papers/arxiv-2002.10957/README.md) · 2020 · 文献卡 · 只蒸馏最后一层的自注意力分布与值关系（阶段 4）
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](../../../llm/papers/arxiv-2403.13271/README.md) · 2024 · 文献卡 · 把大模型的推理过程作为小模型的训练数据（阶段 5）
- [Gemma 2: Improving Open Language Models at a Practical Size](../../../llm/papers/arxiv-2408.00118/README.md) · 2024 · 文献卡 · logit 蒸馏作为小模型的预训练目标（阶段 5）
- [Gemma 3 Technical Report](../../../llm/papers/arxiv-2503.19786/README.md) · 2025 · 文献卡 · 按教师概率采 256 个 logit；大小教师之争（阶段 5）
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../../llm/papers/arxiv-2501.12948/README.md) · 2025 · 文献卡 · 80 万条推理数据蒸给开放小模型；蒸馏与 RL 对照（阶段 6）
- [Qwen3 Technical Report](../../../llm/papers/arxiv-2505.09388/README.md) · 2025 · 文献卡 · 强到弱蒸馏：离线 + on-policy（阶段 6）
- [On-Policy Distillation](../../../llm/papers/thinking-machines-on-policy-distillation/README.md) · 2025 · 文献卡（官方博客）· on-policy 蒸馏的公开说明与复现（阶段 6）
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../../llm/papers/arxiv-2504.13837/README.md) · 2025 · 文献卡 · 蒸馏能引入新推理模式，RL 主要重新分配概率（阶段 6）
- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](../../../llm/papers/arxiv-2512.02556/README.md) · 2025 · 技术精读 · 领域专家蒸馏后再做混合 RL（阶段 7 的前一形态）
- [GLM-5: from Vibe Coding to Agentic Engineering](../../../llm/papers/arxiv-2602.15763/README.md) · 2026 · 文献卡 · 跨阶段 on-policy 蒸馏防遗忘（阶段 7）
- [Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](../../../llm/papers/arxiv-2604.13016/README.md) · 2026 · 文献卡 · on-policy 蒸馏的成功条件与长轨迹上的信号衰减（阶段 7）
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](../../../llm/papers/arxiv-2606.19348/README.md) · 2026 · 技术精读 · 十多个教师的全词表 on-policy 蒸馏取代混合 RL（阶段 7）
- [Kimi K3: Open Frontier Intelligence](../../../llm/papers/arxiv-2607.24653/README.md) · 2026 · 文献卡 · 9 个领域 × 推理强度专家的多教师 on-policy 蒸馏（阶段 7）

视觉与生成：
- [Training data-efficient image transformers & distillation through attention](../../../multimodal/papers/arxiv-2012.12877/README.md) · 2020 · 文献卡 · 蒸馏 token，CNN 教师
- [DINOv2: Learning Robust Visual Features without Supervision](../../../multimodal/papers/arxiv-2304.07193/README.md) · 2023 · 文献卡 · 先训最大模型再蒸馏出一族
- [AM-RADIO: Agglomerative Vision Foundation Model -- Reduce All Domains Into One](../../../multimodal/papers/arxiv-2312.06709/README.md) · 2023 · 文献卡 · 无标签多教师特征蒸馏
- [DINOv3](../../../multimodal/papers/arxiv-2508.10104/README.md) · 2025 · 文献卡 · 蒸馏出 ViT 与 ConvNeXt 一族
- [C-RADIOv4 (Tech Report)](../../../multimodal/papers/arxiv-2601.17237/README.md) · 2026 · 文献卡 · 教师换成 SigLIP 2、DINOv3、SAM 3
- [Qwen-Image-2.0-RL Technical Report](../../../multimodal/papers/arxiv-2606.27608/README.md) · 2026 · 文献卡 · 在策略蒸馏合并文生图与编辑两个 RL 教师
- [RADIO1D: Elastic Representations for Condensed Vision Modeling](../../../multimodal/papers/arxiv-2607.03624/README.md) · 2026 · 文献卡 · 多教师蒸馏到长度可变的 1D token

机器人（特权教师与 DAgger）：
- [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../../../robotics-embodied/papers/arxiv-1011.0686/README.md) · 2011 · 文献卡 · DAgger
- [Vision-and-Language Navigation（R2R）](../../../robotics-embodied/papers/r2r/README.md) · 2017 · 技术精读 · student-forcing 即在线 DAgger
- [Learning Quadrupedal Locomotion over Challenging Terrain](../../../robotics-embodied/papers/arxiv-2010.11251/README.md) · 2020 · 文献卡 · 特权教师 → 本体感知学生
- [RMA: Rapid Motor Adaptation for Legged Robots](../../../robotics-embodied/papers/rma/README.md) · 2021 · 技术精读 · 从历史回归环境隐变量
- [Extreme Parkour with Legged Robots](../../../robotics-embodied/papers/arxiv-2309.14341/README.md) · 2023 · 文献卡 · DAgger 蒸馏出深度输入策略

后训练里的 on-policy 蒸馏与多教师合并的整体脉络见[后训练总览](../../../llm/fields/posttraining/README.md)。

## 正文引用、尚无文献卡的论文

这些论文只核对了入门页所引的段落，仓库里还没有单篇目录。前两篇在 [synthesis.csv](synthesis.csv) 中。

- [MiniLLM: On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) · 2023 · 尚无文献卡
- [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes（GKD）](https://arxiv.org/abs/2306.13649) · 2023 · 尚无文献卡
- [Distillation Scaling Laws](https://arxiv.org/abs/2502.08606) · 2025 · 尚无文献卡
- [MiMo-V2-Flash Technical Report](https://arxiv.org/abs/2601.02780) · 2026 · 尚无文献卡
- [Gemma 4 Technical Report](https://arxiv.org/abs/2607.02770) · 2026 · 尚无文献卡
- [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626) · 2026 · 尚无文献卡（只读了摘要）

早期文献的来源记录见 [history.md](history.md)。
