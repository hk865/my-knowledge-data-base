# 模型训练与多模态

云端来源（可能仅原账户可访问）：https://chatgpt.com/space/page_dc8d589957448191bb8d49223db799e8

本页把大语言模型与多模态训练放在同一研究入口，连接架构、训练阶段、数据和算力约束。以下是基础论文种子集，后续应优先回应聊天中尚未解决的问题，不以追逐新论文替代研究目标。

## 初始兴趣与待验证问题

来自此前讨论的初始画像，优先级待确认：注意力与 KV cache、压缩和效率；数据筛选、合成与课程；预训练、SFT、RL 的目标与衔接。多模态延伸包括视觉表征、跨模态对齐和动作接口。

建议判断标准：改动影响哪一训练阶段？提升来自结构、数据还是计算预算？参数量、token 数、训练 FLOPs 与推理成本是否可比？

## 基础论文

### Attention Is All You Need

2017年首次公开 · [原文](https://arxiv.org/abs/1706.03762) · 去重键 arXiv:1706.03762

问题：如何摆脱序列模型中的循环与卷积瓶颈。方法：基于注意力的 Transformer。原文证据：机器翻译任务及句法分析验证；不能直接据此断言现代 LLM、视觉或机器人任务中的收益。

关联判断：理解注意力与后续缓存、结构改动的共同起点；本文不直接解决 KV cache 压缩。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

### Training Compute Optimal Large Language Models

原题 Training Compute-Optimal Large Language Models · 2022年 · [原文](https://arxiv.org/abs/2203.15556) · 去重键 arXiv:2203.15556

问题：固定训练算力如何分配模型大小与训练 token。方法：训练多组模型拟合计算最优规模关系，再用 Chinchilla 验证。原文证据：在研究覆盖的训练设置中支持模型大小和 token 协同增长。

证据边界：关联判断，不应把其经验规律当作所有数据质量、多模态配比或包含推理成本的通用最优解。关联判断：为数据量与规模选型建立基线。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

### Training language models to follow instructions with human feedback

2022年 · [原文](https://arxiv.org/abs/2203.02155) · 去重键 arXiv:2203.02155

问题：语言预训练目标与用户意图不一致。方法：示范数据监督微调，再用人类输出排序进行强化学习微调。原文证据：作者提示分布上的人工偏好评估及部分 NLP 评测；模型仍会犯错。

关联判断：适合对照预训练、SFT、RL 各自使用的数据与优化目标；偏好改善不等于所有能力提高，也不直接证明机器人闭环可靠。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

## 后续检索队列

按聊天证据确认优先级后补充：KV cache 与压缩、数据选择与合成、多模态对齐与联合训练。每个新条目须说明它回答了哪条具体问题；跨机器人主题保留交叉引用，避免重复记录。

## 从历史聊天提取的论文链接

2026年9月30日更新。以下按研究问题分组，从历史聊天检索摘要恢复具体链接，再核验题名与标识。每条标注用户提供或助手提供及可恢复日期；助手推荐不代表你已采纳。用户阅读状态均待确认，本次不是全文精读或独立复现。跨方向条目可重复展示，但按统一标识只计一次。

原有3篇基础论文卡保留为初始推荐，不冒充聊天中提取的论文；已有手册来源另列。架构和监督方式为交叉标签，无已核实聊天链接的细类保留覆盖缺口。

### 大语言模型

#### 预训练

- [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, preference alignment

- [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, synthetic data, supervised fine-tuning

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised language modeling

- [OLMo: Accelerating the Science of Language Models](https://arxiv.org/abs/2402.00838) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised language modeling

- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) · 2021 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-12；标签：self-supervised pretraining

- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-12；标签：self-supervised pretraining

- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18、2026-09-12；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://arxiv.org/abs/2601.07372) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-26；标签：self-supervised language modeling

- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](https://arxiv.org/abs/2002.10957) · 2020 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：teacher-student attention distillation

- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108) · 2019 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：language modeling, teacher distillation

- [GraphCodeBERT: Pre-training Code Representations with Data Flow](https://arxiv.org/abs/2009.08366) · 2020 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：masked language modeling, structure-aware self-supervision

- [Probing Pretrained Models of Source Code](https://arxiv.org/abs/2202.08975) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

#### 后训练 监督微调

- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](https://arxiv.org/abs/2502.18080) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01、2026-09-10；标签：teacher-generated reasoning, self-training

- [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-10；标签：supervised fine-tuning, synthetic reasoning traces

- [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, preference alignment

- [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, synthetic data, supervised fine-tuning

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-05、2026-09-30；标签：reinforcement learning, verifiable reward, supervised fine-tuning, distillation

- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18、2026-09-12；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://arxiv.org/abs/2407.18219) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：iterative fine-tuning, online imitation, environment feedback

- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](https://arxiv.org/abs/2403.13271) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：teacher-generated plans, multi-task supervised learning

- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://proceedings.mlr.press/v267/chen25bx.html) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01；标签：self-training

#### 后训练 偏好学习

- [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, preference alignment

#### 后训练 强化学习

- [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-05、2026-09-30；标签：reinforcement learning, verifiable reward, supervised fine-tuning, distillation

- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18、2026-09-12；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

#### 架构与效率

- [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, preference alignment

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, synthetic data, supervised fine-tuning

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised language modeling

- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) · 2021 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-12；标签：self-supervised pretraining

- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-12；标签：self-supervised pretraining

- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18、2026-09-12；标签：self-supervised pretraining, supervised fine-tuning, reinforcement learning

- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://arxiv.org/abs/2601.07372) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-26；标签：self-supervised language modeling

- [Tokenizer-Agnostic Engram Module](https://arxiv.org/abs/2607.29065) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-26；标签：language-model training

- [Cross-Model Memory Transfer via Target-Side Reader Adaptation](https://arxiv.org/abs/2608.17050) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-26；标签：reader adaptation

- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](https://arxiv.org/abs/2002.10957) · 2020 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：teacher-student attention distillation

- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108) · 2019 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：language modeling, teacher distillation

- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](https://arxiv.org/abs/2403.03853) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

- [GraphCodeBERT: Pre-training Code Representations with Data Flow](https://arxiv.org/abs/2009.08366) · 2020 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：masked language modeling, structure-aware self-supervision

- [Naturalness of Attention: Revisiting Attention in Code Language Models](https://arxiv.org/abs/2311.13508) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18

#### 推理时计算

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-10；标签：process reward model

- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](https://arxiv.org/abs/2502.18080) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01、2026-09-10；标签：teacher-generated reasoning, self-training

- [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-10；标签：supervised fine-tuning, synthetic reasoning traces

- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](https://arxiv.org/abs/2407.21787) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-10；标签：verifiable outcomes

- [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised pretraining, synthetic data, supervised fine-tuning

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-30；标签：self-supervised language modeling

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-05、2026-09-30；标签：reinforcement learning, verifiable reward, supervised fine-tuning, distillation

- [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://arxiv.org/abs/2412.09078) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://arxiv.org/abs/2407.18219) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：iterative fine-tuning, online imitation, environment feedback

- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](https://arxiv.org/abs/2403.13271) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-18；标签：teacher-generated plans, multi-task supervised learning

- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](https://arxiv.org/abs/2510.01171) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://proceedings.mlr.press/v267/chen25bx.html) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01；标签：self-training

- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](https://aclanthology.org/2024.findings-emnlp.882/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://aclanthology.org/2025.emnlp-main.504/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Reasoning Does Not Necessarily Improve Role-Playing Ability](https://aclanthology.org/2025.findings-acl.537/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-25

- [Self-Discover: Large Language Models Self-Compose Reasoning Structures](https://deepmind.google/research/publications/64816/) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://mlanthology.org/iclr/2023/yao2023iclr-react/) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-01

- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://mlanthology.org/tmlr/2024/wang2024tmlr-voyager/) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23

### 多模态与世界表征

#### 视觉表征

覆盖缺口：本次没有恢复并核验到该细类的历史聊天论文链接；不据此判断你没有兴趣，也不补入通用推荐。

#### 图文对齐

覆盖缺口：本次没有恢复并核验到该细类的历史聊天论文链接；不据此判断你没有兴趣，也不补入通用推荐。

#### 视觉语言模型

覆盖缺口：本次没有恢复并核验到该细类的历史聊天论文链接；不据此判断你没有兴趣，也不补入通用推荐。

#### 视觉生成

覆盖缺口：本次没有恢复并核验到该细类的历史聊天论文链接；不据此判断你没有兴趣，也不补入通用推荐。

#### 世界模型

- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](https://arxiv.org/abs/2210.05861) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：slot transformer, autoregressive dynamics, unsupervised video prediction

- [SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](https://arxiv.org/abs/2206.07764) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：slot-based video encoder, depth prediction, sparse LiDAR supervision, no segmentation labels

- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](https://arxiv.org/abs/2311.16038) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：scene tokenizer, GPT-like spatiotemporal transformer, occupancy reconstruction, future token prediction

- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](https://arxiv.org/abs/2408.14197) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：BEV memory, world decoder, action conditioning, occupancy forecasting, flow forecasting

- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://arxiv.org/abs/2411.04983) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：DINOv2 patch encoder, action-conditioned predictor, offline trajectory future-feature prediction, pretrained visual features

- [Back to the Features: DINO as a Foundation for Video World Models](https://arxiv.org/abs/2507.19468) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：DINOv2 encoder, latent future predictor, uncurated video predictive learning, action-conditioned finetuning

- [FOCUS: Object-Centric World Models for Robotics Manipulation](https://arxiv.org/abs/2307.02427) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：object-centric world model, model-based agent, model-based reinforcement learning, exploration bonus

- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](https://arxiv.org/abs/2505.11528) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：latent diffusion, DINO geometric features, CLIP semantic features, diffusion policy, future latent prediction, pretrained visual feature alignment

- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](https://arxiv.org/abs/2607.04546) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：two-stage mask dynamics, ControlNet, Stable Video Diffusion, simulation pretraining, real-demonstration finetuning, action-conditioned mask prediction

- [A Survey of World Models for Autonomous Driving](https://arxiv.org/abs/2501.11260) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：survey

- [Object-Centric World Model for Language-Guided Manipulation](https://arxiv.org/abs/2503.06170) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：slot attention, language-conditioned latent predictor, latent future-state prediction

- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](https://arxiv.org/abs/2607.13451) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：spring-mass simulator, sliding-window transformer, 3D Gaussian Splatting, physics-guided residual dynamics fitting

- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：3D Gaussian Splatting, semantic fusion, collision geometry, Unity-ROS2-MoveIt, sparse RGB reconstruction

- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](https://arxiv.org/abs/2506.07454) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：3D scene graph, LLM-to-PDDL, multi-robot mapping, not established from abstract

- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：video generative model, inverse dynamics model, reinforcement-learning post-training, inverse-dynamics action rewards

- [Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：action-flow conditioned video model, action head, cross-embodiment action-consequence learning

- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](https://arxiv.org/abs/2505.06111) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：DINO-space latent action model, language conditioning, action decoder, internet-video pretraining, task-centric latent action learning

- [What Do Latent Action Models Actually Learn?](https://arxiv.org/abs/2506.15691) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：linear latent-action analysis, PCA connection, auxiliary action prediction

- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](https://arxiv.org/abs/2604.11689) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-23；标签：benchmark, visual and latent-action representations

- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](https://arxiv.org/abs/2608.26103) · 2026 · 用户提供 · 聊天日期 2026-08-29；标签：causal video-action model, paired human-robot video learning, in-context future chunk prediction

- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://www.roboticsproceedings.org/rss21/p153.html) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：differentiable physics simulator, Gaussian Splatting, digital cousins, visual observational loss, few-shot physical trajectories, physics-aware randomization, model-based reinforcement learning

- [World Models for Robotic Manipulation: A Survey](https://onlinelibrary.wiley.com/doi/10.1002/smb2.70053) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-04；标签：survey

### 待核验线索

以下只恢复名称、截断链接或其他不足信息，暂不作为已核验论文入库：Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving；Self-Refine；PromptAgent；Reflexion；Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting；AgentBench；τ-bench；Relational knowledge in attention (reported arXiv 2409.00617)；Later-layer factual formation (reported arXiv 2606.07978)；https://www.mdpi.com/1424-8220/26/17/5595；PointWorld (historical label)；名称与链接均待核；名称与链接均待核。

## 2026年9月30日问题图更新

证据来自可检索历史摘要，未取得原会话链接；以下是反复关注的学习机制之具体问题，不代表正式选题或训练项目。

- **Q-0930-context：可读取长度与长程任务能力。** 用户02:29:14 UTC讨论线性/稀疏注意力与causal mask复杂度，02:47:21 UTC讨论128K任务、32K/64K RL rollout与信用分配。关联：预训练/长上下文数据 → 后训练/SFT适配 → RL/奖励与信用分配 → 推理/稀疏计算；这些维度需分别核验，不能用支持的窗口长度替代任务成功率。

- **Q-0930-sft：阶段划分与数据使用。** 用户03:10:54和03:11:30 UTC询问SFT损失与示范数据为何不纳入较早训练。关联：预训练/数据配比与课程 ↔ SFT/监督位置与示范格式 ↔ 评估/同口径损失。整理建议：阅读时记录loss定义、数据分布和token掩码；不能从单个数值判断哪一阶段损害能力。

- **Q-0930-evidence：能力来源的证据。** 延续对预训练能力与后训练塑造的追问；优先找同模型、同预算的阶段消融，区分作者声明、基准成绩和跨分布泛化。尚未取得足以分离所有因素的证据。

### 本轮定向阅读（复用已有目录）

- [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383)，arXiv:2501.15383，2025-01-26。来源：历史助手于2026-09-30约02:52 UTC提供；现有记录02:52:50，本轮检索02:52:48，秒级时间有差异，保留原记录并注明，不当作两次讨论。作者摘要描述长数据合成、渐进预训练、多阶段SFT和稀疏推理优化；关联Q-0930-context。边界：摘要未构成长RL信用分配已解决的证据。

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)，arXiv:2203.02155，2022-03-04。来源：原有starter，不冒充本轮聊天提取。示范监督后使用输出排序进行RLHF；关联Q-0930-sft。边界：作者偏好评测不能回答所有数据混合方案的优劣。

核验深度：2026-09-30核对两篇官方摘要与身份；未全文精读或复现，用户阅读状态未知。没有新增已核验论文，不以重复条目填充目录。

## 全文精读与技术路线图

- [Qwen2.5-1M 全文精读](deep-readings/qwen2.5-1m.md)：从训练课程、长指令 SFT、短样本偏好优化，到 DCA 外推、稀疏 prefill 和部署系统，逐项区分原文、实验、分析与未公开细节。覆盖报告正文、公式、算法、图表；不是独立复現。

- [长上下文 LLM 技术路线图](roadmaps/long-context.md)：围绕位置、计算机制、训练信号、推理资源和评测五轴，区分直接采用、机制依赖、互补对照和评测关系。
