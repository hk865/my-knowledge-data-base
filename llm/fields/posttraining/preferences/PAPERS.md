# 偏好学习论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [后训练总览](../README.md)

按[入门页](README.md)主线历史的阶段排列；每篇链接到唯一的单篇目录，"格"指它在 [Baseline 表](BASELINES.md)中的位置。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 1 从比较中学奖励（2017–2020）

- [Deep reinforcement learning from human preferences](../../../papers/arxiv-1706.03741/README.md) · 2017 · OpenAI、DeepMind · 文献卡 · 格：前史（偏好 → 奖励预测器 → RL）
- [Learning to summarize from human feedback](../../../papers/arxiv-2009.01325/README.md) · 2020 · OpenAI · 文献卡 · 格：前史（奖励模型 + PPO 用于语言）

## 2 RLHF 三段式与"有帮助、无害"（2022）

- [Training language models to follow instructions with human feedback](../../../papers/instructgpt/reading.md)（InstructGPT） · 2022 · OpenAI · 逐步教学版 · 格：基线（奖励模型 + PPO）
- [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](../../../papers/arxiv-2204.05862/README.md) · 2022 · Anthropic · 文献卡 · 格：偏好来源 = 帮助性与无害性分开
- [Scaling Laws for Reward Model Overoptimization](../../../papers/arxiv-2210.10760/README.md) · 2022 · OpenAI · 文献卡 · 格：评测与分析 = 过度优化规律
- [Constitutional AI: Harmlessness from AI Feedback](../../../papers/arxiv-2212.08073/README.md) · 2022 · Anthropic · 文献卡 · 格：偏好来源 = 书面原则 + AI 比较

## 3 开放模型上的 RLHF（2023）

- [Llama 2: Open Foundation and Fine-Tuned Chat Models](../../../papers/arxiv-2307.09288/README.md) · 2023 · Meta · 文献卡 · 格：优化方式 = 拒绝采样 + PPO；数据 = 每轮重采

## 4 去掉奖励模型：直接偏好优化（2023–2024）

- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](../../../papers/dpo/reading.md)（DPO） · 2023 · Stanford · 逐步教学版 · 格：基线（直接偏好优化）
- [A General Theoretical Paradigm to Understand Learning from Human Preferences](../../../papers/arxiv-2310.12036/README.md)（IPO） · 2023 · Google DeepMind · 文献卡 · 格：损失形式 = 恒等映射
- [A Long Way to Go: Investigating Length Correlations in RLHF](../../../papers/arxiv-2310.03716/README.md) · 2023 · UT Austin、Princeton、Salesforce · 文献卡 · 格：评测与分析 = 长度偏置
- [Zephyr: Direct Distillation of LM Alignment](../../../papers/arxiv-2310.16944/README.md) · 2023 · Hugging Face · 文献卡 · 格：偏好来源 = AI 打分；优化方式 = DPO
- [Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study](../../../papers/arxiv-2404.10719/README.md) · 2024 · 清华大学等 · 文献卡 · 格：优化方式 = 调好的 PPO
- [SimPO: Simple Preference Optimization with a Reference-Free Reward](../../../papers/arxiv-2405.14734/README.md) · 2024 · 弗吉尼亚大学、Princeton · 文献卡 · 格：损失形式 = 长度归一化、无参考模型
- [The Llama 3 Herd of Models](../../../papers/arxiv-2407.21783/README.md) · 2024 · Meta · 文献卡 · 格：优化方式 = DPO；正则 = NLL 与屏蔽格式 token
- [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](../../../papers/arxiv-2411.15124/README.md) · 2024 · AI2、华盛顿大学 · 文献卡 · 格：数据 = on-policy 偏好；损失 = 长度归一化 DPO
- [Qwen2 Technical Report](../../../papers/arxiv-2407.10671/README.md) · 2024 · 阿里巴巴 · 文献卡 · 格：数据与策略的关系 = SFT 之后接离线与在线两阶段 DPO
- [Qwen2.5-1M Technical Report](../../../papers/qwen2.5-1m/reading.md) · 2025 · 阿里巴巴 · 技术精读（主要归预训练与长上下文） · 格：8K 以内短样本的离线偏好优化迁移到长文对话

## 5 评委变成会推理的模型（2024–2026）

- [DeepSeek-V3 Technical Report](../../../papers/arxiv-2412.19437/README.md) · 2024 · DeepSeek · 文献卡 · 格：奖励形式 = 带理由的奖励模型、自我奖励
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../../papers/arxiv-2501.12948/README.md) · 2025 · DeepSeek · 文献卡 · 格：正则 = 长度相当的偏好对、限制偏好奖励的步数
- [Kimi K2: Open Agentic Intelligence](../../../papers/arxiv-2507.20534/README.md) · 2025 · 月之暗面 · 文献卡 · 格：偏好来源 = 自我批评 rubric
- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](../../../papers/arxiv-2512.02556/README.md) · 2025 · DeepSeek · 文献卡 · 格：奖励形式 = 逐题 rubric 的生成式奖励模型
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](../../../papers/arxiv-2606.19348/README.md) · 2026 · DeepSeek · 文献卡（主要归预训练） · 格：奖励形式 = 策略兼任生成式奖励模型

## 相关的评测研究

- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../../../../cross-domain/papers/llm-judge/README.md) · 2023 · 技术精读（归评估方向） · LLM 评委与人类偏好的一致性及位置、冗长等偏差
- [Let's Verify Step by Step](../../../papers/arxiv-2305.20050/README.md) · 2023 · OpenAI · 文献卡（主要归强化学习） · 过程奖励模型：按步骤收集人类标签

## 跨方向引用（归推理时计算，方法属于偏好优化）

- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](../../../papers/url-https-proceedings.mlr.press-v267-chen25bx.html/README.md) · 2025 · 文献卡 · 用 DPO/RPO/SimPO 让推理模型在简单题上少写
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](../../../papers/arxiv-2510.01171/README.md) · 2025 · 文献卡 · 把对齐后多样性下降归因于偏好数据的典型性偏置，并用提示缓解
