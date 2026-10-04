# SFT 论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [后训练总览](../README.md)

按[入门页](README.md)主线历史的阶段排列；每篇链接到唯一的单篇目录，"格"指它在 [Baseline 表](BASELINES.md)中的位置。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 1 多任务指令微调（2021–2022）

- [Finetuned Language Models Are Zero-Shot Learners](../../../papers/arxiv-2109.01652/README.md)（FLAN） · 2021 · Google · 文献卡 · 格：示范来源 = 公开任务改写
- [Scaling Instruction-Finetuned Language Models](../../../papers/arxiv-2210.11416/README.md)（Flan-PaLM） · 2022 · Google · 文献卡 · 格：数据配比 = 加入思维链

## 2 人写示范进入 RLHF 流水线（2022）

- [Training language models to follow instructions with human feedback](../../../papers/instructgpt/reading.md)（InstructGPT） · 2022 · OpenAI · 逐步教学版 · 格：基线（人写示范）

## 3 少而精，或让模型自己写（2022–2023）

- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](../../../papers/arxiv-2212.10560/README.md) · 2022 · 华盛顿大学等 · 文献卡 · 格：示范来源 = 模型自生成
- [LIMA: Less Is More for Alignment](../../../papers/arxiv-2305.11206/README.md) · 2023 · Meta AI 等 · 文献卡 · 格：数据规模 = 少而精
- [Llama 2: Open Foundation and Fine-Tuned Chat Models](../../../papers/arxiv-2307.09288/README.md) · 2023 · Meta · 文献卡 · 格：数据规模 = 少而精（27,540 条）
- [Zephyr: Direct Distillation of LM Alignment](../../../papers/arxiv-2310.16944/README.md) · 2023 · Hugging Face · 文献卡（主要归偏好学习） · 格：示范来源 = 蒸馏 SFT

## 4 知识边界与筛选（2024）

- [DeepSeek LLM: Scaling Open-Source Language Models with Longtermism](../../../papers/arxiv-2401.02954/README.md) · 2024 · DeepSeek · 文献卡（主要归预训练） · 格：训练过程 = 两阶段降重复
- [Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?](../../../papers/arxiv-2405.05904/README.md) · 2024 · Technion、Google Research · 文献卡 · 格：筛选 = 去掉未知事实
- [The Llama 3 Herd of Models](../../../papers/arxiv-2407.21783/README.md) · 2024 · Meta · 文献卡 · 格：筛选 = 拒绝采样与知识探针
- [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](../../../papers/arxiv-2411.15124/README.md) · 2024 · AI2、华盛顿大学 · 文献卡 · 格：评测 = 开发集与未见集分离
- [Qwen2 Technical Report](../../../papers/arxiv-2407.10671/README.md) · 2024 · 阿里巴巴 · 文献卡 · 格：数据规模 = 50 万条以上指令数据，之后接离线与在线 DPO
- [Qwen2.5 Technical Report](../../../papers/arxiv-2412.15115/README.md) · 2024 · 阿里巴巴 · 文献卡 · 格：数据规模 = 100 万条以上 SFT 样本
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../../papers/deepseek-v2/reading.md) · 2024 · DeepSeek · 技术精读（主要归预训练） · 格：150 万条 SFT 后接 GRPO
- [Qwen2.5-1M Technical Report](../../../papers/qwen2.5-1m/reading.md) · 2025 · 阿里巴巴 · 技术精读（主要归预训练） · 格：长上下文的 SFT 数据

## 5 长思维链：冷启动与蒸馏（2024–2025）

- [DeepSeek-V3 Technical Report](../../../papers/arxiv-2412.19437/README.md) · 2024 · DeepSeek · 文献卡 · 格：示范来源 = 推理模型（从 R1 蒸馏）
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../../papers/arxiv-2501.12948/README.md) · 2025 · DeepSeek · 文献卡 · 格：基线（蒸馏）；位置 = 冷启动
- [s1: Simple test-time scaling](../../../papers/arxiv-2501.19393/README.md) · 2025 · Stanford 等 · 文献卡 · 格：数据规模 = 1,000 条推理数据
- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](../../../papers/arxiv-2502.18080/README.md) · 2025 · 文献卡（主要归推理时计算） · 格：示范的思维链长度（摘要称过长的思维链在部分领域损害推理，各领域存在不同的最优长度分布）
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](../../../papers/arxiv-2403.13271/README.md) · 2024 · 文献卡 · 格：示范来源 = 推理模型（CodePLAN：把大模型写代码前的解题计划蒸馏给小模型）
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](../../../papers/url-https-proceedings.mlr.press-v267-chen25bx.html/README.md) · 2025 · 文献卡（主要归推理时计算） · 格：长思维链模型的过度思考

## 6 on-policy 蒸馏与 SFT、RL 的分工（2025–2026）

- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](../../../papers/arxiv-2501.17161/README.md) · 2025 · 港大、UC Berkeley、Google DeepMind 等 · 文献卡 · 格：对照 = SFT 与 RL
- [Qwen3 Technical Report](../../../papers/arxiv-2505.09388/README.md) · 2025 · 阿里巴巴 · 文献卡 · 格：损失 = on-policy 蒸馏；位置 = 冷启动与 RL 后融合
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](../../../papers/arxiv-2606.19348/README.md) · 2026 · DeepSeek · 文献卡（主要归预训练） · 格：损失 = 多教师 on-policy 蒸馏
- [Kimi K3: Open Frontier Intelligence](../../../papers/arxiv-2607.24653/README.md) · 2026 · 月之暗面 · 文献卡（主要归预训练） · 格：位置 = 冷启动；损失 = 多教师 on-policy 蒸馏

## 相关但不在主线

- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](../../../papers/arxiv-2407.18219/README.md) · 2024 · 文献卡 · RISE：迭代微调，教模型在失败尝试之后修改回答，与智能体方向交叉
