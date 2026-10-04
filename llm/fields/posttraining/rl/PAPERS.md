# 语言模型强化学习论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [后训练总览](../README.md)

按[入门页](README.md)主线历史的阶段排列；每篇链接到唯一的单篇目录，"格"指它在 [Baseline 表](BASELINES.md)中的位置。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 1 PPO 与 RLHF（2017–2022）

- [Proximal Policy Optimization Algorithms](../../../papers/ppo/reading.md)（PPO） · 2017 · OpenAI · 技术精读 · 格：基线（裁剪目标）
- [Deep reinforcement learning from human preferences](../../../papers/arxiv-1706.03741/README.md) · 2017 · OpenAI、DeepMind · 文献卡（主要归偏好学习） · 格：奖励来源 = 学到的奖励预测器
- [Learning to summarize from human feedback](../../../papers/arxiv-2009.01325/README.md) · 2020 · OpenAI · 文献卡（主要归偏好学习） · 格：奖励模型 + PPO 用于语言
- [Training language models to follow instructions with human feedback](../../../papers/instructgpt/reading.md)（InstructGPT） · 2022 · OpenAI · 逐步教学版 · 格：基线（RLHF 中的 PPO）
- [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](../../../papers/arxiv-2204.05862/README.md) · 2022 · Anthropic · 文献卡（主要归偏好学习） · 格：奖励与 √KL 的线性关系
- [Scaling Laws for Reward Model Overoptimization](../../../papers/arxiv-2210.10760/README.md) · 2022 · OpenAI · 文献卡（主要归偏好学习） · 格：正则 = KL 惩罚的作用
- [Llama 2: Open Foundation and Fine-Tuned Chat Models](../../../papers/arxiv-2307.09288/README.md) · 2023 · Meta · 文献卡（主要归偏好学习） · 格：拒绝采样 + PPO
- [Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study](../../../papers/arxiv-2404.10719/README.md) · 2024 · 清华大学等 · 文献卡（主要归偏好学习） · 格：PPO 的关键配置

## 2 去掉价值模型，奖励换成验证器（2023–2024）

- [Let's Verify Step by Step](../../../papers/arxiv-2305.20050/README.md) · 2023 · OpenAI · 文献卡 · 格：奖励来源 = 过程奖励模型
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](../../../papers/arxiv-2402.03300/README.md) · 2024 · DeepSeek · 文献卡 · 格：基线（GRPO 的出处）
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../../papers/deepseek-v2/reading.md) · 2024 · DeepSeek · 技术精读（主要归预训练） · 格：GRPO 分推理对齐与偏好对齐两阶段
- [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](../../../papers/arxiv-2411.15124/README.md) · 2024 · AI2、华盛顿大学 · 文献卡 · 格：奖励来源 = 规则验证器（RLVR 的命名）
- [Qwen2.5 Technical Report](../../../papers/arxiv-2412.15115/README.md) · 2024 · 阿里巴巴 · 文献卡 · 格：离线 DPO 之后接在线 GRPO（奖励模型打分）
- [DeepSeek-V3 Technical Report](../../../papers/arxiv-2412.19437/README.md) · 2024 · DeepSeek · 文献卡 · 格：规则奖励 + 带理由的奖励模型，GRPO

## 3 大规模 RLVR 与长思维链（2024.9–2025.1）

- [Learning to reason with LLMs](../../../papers/openai-o1/README.md)（o1 博客） · 2024 · OpenAI · 文献卡（主要归推理时计算） · 格：闭源参照
- [OpenAI o1 System Card](../../../papers/arxiv-2412.16720/README.md) · 2024 · OpenAI · 文献卡 · 格：闭源参照
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../../papers/arxiv-2501.12948/README.md) · 2025 · DeepSeek · 文献卡 · 格：基线（GRPO + 规则奖励的规模化）
- [Kimi k1.5: Scaling Reinforcement Learning with LLMs](../../../papers/arxiv-2501.12599/README.md) · 2025 · 月之暗面 · 文献卡 · 格：优势估计 = 镜像下降变体；长度奖励；部分 rollout

## 4 复现与修正（2025）

- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](../../../papers/arxiv-2503.14476/README.md) · 2025 · 字节跳动 Seed、清华 AIR、港大 · 文献卡 · 格：裁剪、动态采样、token 级损失、去 KL
- [Understanding R1-Zero-Like Training: A Critical Perspective](../../../papers/arxiv-2503.20783/README.md)（Dr. GRPO） · 2025 · Sea AI Lab 等 · 文献卡 · 格：优势估计 = 去掉长度与标准差归一化
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](../../../papers/arxiv-2504.13837/README.md) · 2025 · 清华 LeapLab、上海交大 · 文献卡 · 格：评测口径 = 大 k 的 pass@k
- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../../papers/arxiv-2505.22617/README.md) · 2025 · 上海 AI Lab 等 · 文献卡 · 格：裁剪 = 限制高协方差 token
- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](../../../papers/arxiv-2501.17161/README.md) · 2025 · 港大、UC Berkeley、Google DeepMind 等 · 文献卡（主要归 SFT） · 格：对照 = SFT 与 RL 的泛化
- [Qwen3 Technical Report](../../../papers/arxiv-2505.09388/README.md) · 2025 · 阿里巴巴 · 文献卡 · 格：数据 = 少量高难题；多领域 = 分阶段 + 蒸馏

## 5 规模化：多领域、稳定性与长度预算（2025）

- [Kimi K2: Open Agentic Intelligence](../../../papers/arxiv-2507.20534/README.md) · 2025 · 月之暗面 · 文献卡 · 格：token 预算、PTX 损失、自我批评 rubric 奖励
- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](../../../papers/arxiv-2512.02556/README.md) · 2025 · DeepSeek · 文献卡 · 格：稳定性修补；多领域 = 专家蒸馏 + 混合 RL

## 6 RL 造专家，蒸馏做统一模型（2026）

- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](../../../papers/arxiv-2606.19348/README.md) · 2026 · DeepSeek · 文献卡（主要归预训练） · 格：多领域 = 多教师 on-policy 蒸馏（全词表）；三档推理强度
- [Kimi K3: Open Frontier Intelligence](../../../papers/arxiv-2607.24653/README.md) · 2026 · 月之暗面 · 文献卡（主要归预训练） · 格：部分 rollout 与逐 token 正则；多领域 = 多教师 on-policy 蒸馏（逐 token）

## 跨领域的对照

- [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](../../../../robotics-embodied/papers/arxiv-2509.09674/README.md) · 2025 · 文献卡（归机器人与具身） · 把 GRPO 与 DAPO 式的探索技巧搬到 VLA 上
