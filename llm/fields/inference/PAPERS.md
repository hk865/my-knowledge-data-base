# 推理时计算论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [草稿—验证导读](draft-verification-guide.md)

按[入门页](README.md)主线历史的阶段排列。每篇链接到唯一的单篇目录，"格"指它在 [Baseline 表](BASELINES.md)中的位置。跨方向的论文只列与本方向相关的一面，不重复计数。

## 1 思维链与自洽投票（2022）

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](../../papers/arxiv-2201.11903/README.md) · 2022 · Google · 文献卡 · 格：生成器 = 提示中写出推理（基线）
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](../../papers/arxiv-2203.11171/README.md) · 2022 · Google · 文献卡 · 格：选择与验证 = 多数投票（基线）
- [Self-Discover: Large Language Models Self-Compose Reasoning Structures](../../papers/arxiv-2402.03620/README.md) · 2024 · 南加州大学、Google DeepMind · 文献卡 · 格：生成器 = 提示层面的推理结构

## 2 验证器、搜索与重复采样（2024）

- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](../../papers/arxiv-2407.21787/README.md) · 2024 · Stanford、Oxford、Google DeepMind · 文献卡 · 格：预算分配 = 重复采样；选择与验证 = 规则或测试
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](../../papers/test-time-compute/README.md) · 2024 · UC Berkeley、Google DeepMind · 技术精读 · 格：预算分配 = 按难度分配；选择与验证 = PRM 搜索
- [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](../../papers/arxiv-2412.09078/README.md) · 2024 · 华为诺亚方舟实验室 · 文献卡 · 格：预算分配 = 多棵推理树
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](../../papers/arxiv-2407.18219/README.md) · 2024 · CMU、UC Berkeley · 文献卡 · 格：生成器 = 训练修订能力

## 3 推理模型（2024-09 – 2025-01）

- [Learning to reason with LLMs](../../papers/openai-o1/README.md)（OpenAI o1） · 2024 · OpenAI · 官方博客 · 格：生成器 = RL 训练长思维链
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../papers/arxiv-2501.12948/README.md) · 2025 · DeepSeek · 文献卡 · 格：生成器 = RL 训练长思维链、蒸馏；选择与验证 = 规则奖励
- [Kimi k1.5: Scaling Reinforcement Learning with LLMs](../../papers/arxiv-2501.12599/README.md) · 2025 · Kimi（Moonshot AI） · 文献卡 · 格：生成器 = RL 训练长思维链；停止与长度 = 长度奖励与 long2short
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](../../papers/arxiv-2403.13271/README.md) · 2024 · 山东师范大学、北京大学等 · 文献卡 · 格：生成器 = 蒸馏推理

## 4 控制思考长度（2025）

- [s1: Simple test-time scaling](../../papers/arxiv-2501.19393/README.md) · 2025 · Stanford 等 · 文献卡 · 格：停止与长度 = 预算强制；生成器 = 小数据蒸馏
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](../../papers/url-https-proceedings.mlr.press-v267-chen25bx.html/README.md) · 2024–2025 · Tencent AI Lab、上海交大 · 文献卡 · 格：停止与长度 = 偏好优化压缩
- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](../../papers/arxiv-2502.18080/README.md) · 2025 · 人民大学、Microsoft Research · 文献卡 · 格：停止与长度 = 最短正确回答
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](../../papers/arxiv-2510.01171/README.md) · 2025 · 东北大学、Stanford 等 · 文献卡 · 格：选择与验证 = 增加候选多样性

## 5 解码与服务效率（2022–2026）

- [Fast Inference from Transformers via Speculative Decoding](../../papers/arxiv-2211.17192/README.md) · 2022 · Google · 文献卡 · 格：解码执行 = 精确投机解码（基线）
- [Accelerating Large Language Model Decoding with Speculative Sampling](../../papers/arxiv-2302.01318/README.md) · 2023 · DeepMind · 文献卡 · 格：解码执行 = 精确投机解码（基线）
- [Speculative Decoding with Big Little Decoder](../../papers/arxiv-2302.07863/README.md) · 2023 · 文献卡 · 格：解码执行 = 放宽验证
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](../../papers/arxiv-2309.06180/README.md)（vLLM） · 2023 · UC Berkeley 等 · 文献卡 · 格：显存与批处理 = 分页 KV 缓存
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](../../papers/arxiv-2305.13245/README.md) · 2023 · Google · 文献卡 · 格：显存与批处理 = 减少 KV 头数
- [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](../../papers/arxiv-2402.02750/README.md) · 2024 · Rice、Texas A&M、CMU 等 · 文献卡 · 格：显存与批处理 = KV 量化
- [Faster Cascades via Speculative Decoding](../../papers/arxiv-2405.19261/README.md) · 2024 · 文献卡 · 格：解码执行 = 放宽验证（精确采样混合分布）
- [Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment](../../papers/arxiv-2501.19309/README.md) · 2025 · 文献卡 · 格：解码执行 = 放宽验证
- [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](../../papers/arxiv-2503.01840/README.md) · 2025 · 北京大学、Microsoft Research 等 · 文献卡 · 格：解码执行 = 读目标特征的草稿器
- [RelayLLM: Efficient Reasoning via Collaborative Decoding](../../papers/arxiv-2601.05167/README.md) · 2026 · 文献卡 · 格：解码执行 = 关键片段接管
- [DFlash: Block Diffusion for Flash Speculative Decoding](../../papers/arxiv-2602.06036/README.md) · 2026 · 文献卡 · 格：解码执行 = 块扩散草稿器
- [DFlash 2: Keep Drafting Parallel](../../papers/dflash-2/README.md) · 2026 · 官方博客 · 格：解码执行 = 块扩散草稿器

## 6 档位化的思考、自我验证与并行思考（2025-08 – 2026）

- [DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning](../../papers/arxiv-2511.22570/README.md) · 2025 · DeepSeek · 文献卡 · 格：选择与验证 = 训练出的验证器 + 元验证器
- [Kimi K2.5: Visual Agentic Intelligence](../../papers/arxiv-2602.02276/README.md) · 2026 · 月之暗面 · 文献卡 · 格：预算分配 = 并行子智能体（PARL）；停止与长度 = Toggle
- [The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence](../../papers/arxiv-2605.26494/README.md) · 2026 · MiniMax · 文献卡（主要归强化学习） · 格：生成器（多轮）= 跨轮保留思考；解码执行 = MTP
- [NVIDIA Nemotron 3: Efficient and Open Intelligence](../../papers/arxiv-2512.20856/README.md) · 2025 · NVIDIA · 文献卡（主要归架构） · 格：停止与长度 = 推理预算控制；解码执行 = MTP
- [GLM-5: from Vibe Coding to Agentic Engineering](../../papers/arxiv-2602.15763/README.md) · 2026 · 智谱、清华 · 文献卡（主要归强化学习） · 格：解码执行 = 共享参数的 MTP
- [Qwen3.5-397B-A17B（官方模型卡）](../../papers/qwen3.5/README.md) · 2026 · 阿里巴巴 · 文献卡（主要归架构） · 格：生成器（多轮）= Qwen3.6 的思考保留
- [Recursive Language Models](../../papers/arxiv-2512.24601/README.md) · 2025 · MIT · 文献卡（主要归长上下文） · 格：预算分配 = 递归调用自己处理长输入

只读了官方页面、未建卡：[gpt-oss-120b & gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925)（2025-08，推理强度档位）；[Gemini 3 Deep Think](https://blog.google/products/gemini/gemini-3-deep-think/)（2025-12，并行推理）；[Introducing Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/)（2026-04，Contemplating 模式与思考压缩）。

## 交叉引用（主归属在其他方向）

- [DeepSeek-V3 Technical Report](../../papers/arxiv-2412.19437/README.md) · 2024 · 预训练方向 · 格：解码执行 = MTP 草稿
- [DeepSeek-V2](../../papers/deepseek-v2/reading.md) · 2024 · 预训练方向 · 技术精读 · 格：显存与批处理 = MLA
- [Qwen2.5-1M Technical Report](../../papers/qwen2.5-1m/reading.md) · 2025 · 长上下文方向 · 技术精读 · 格：显存与批处理 = 稀疏 prefill
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](../../papers/mamba/reading.md) · 2023 · 架构方向 · 技术精读 · 格：显存与批处理 = 换序列算子
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](../../papers/url-https-aclanthology.org-2024.findings-emnlp.882/README.md) · 2024 · EPFL · 模型科学方向 · 思维链忠实性
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](../../papers/url-https-aclanthology.org-2025.emnlp-main.504/README.md) · 2025 · 以色列理工学院、犹他大学 · 模型科学方向 · 思维链忠实性
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](../../papers/url-https-aclanthology.org-2025.findings-acl.537/README.md) · 2025 · 香港大学、Sea AI Lab · 评估方向 · 推理增益的边界
- [ReAct: Synergizing Reasoning and Acting in Language Models](../../../cross-domain/papers/react/README.md) · 2022 · 智能体方向 · 技术精读 · 推理与工具调用交替
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](../../papers/arxiv-2405.15793/README.md) · 2024 · 普林斯顿 · 智能体方向 · 代码智能体
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](../../papers/arxiv-2305.16291/README.md) · 2023 · NVIDIA 等 · 智能体方向 · 技能库与迭代提示

## 2026年10月4日补充

- [Speculative Speculative Decoding](../../papers/arxiv-2603.03251/README.md) · 2026 · 文献卡
- [Acceptance-Aware Draft Model Training for Speculative Decoding](../../papers/arxiv-2609.24150/README.md) · 2026 · 文献卡

## 运行时经验选择

- [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](../../../cross-domain/papers/arxiv-2601.03192/README.md) · 2026 · 文献卡
