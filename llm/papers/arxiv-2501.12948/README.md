# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.12948)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LLM 的推理能力依赖大量人工标注的推理示范，复杂问题上仍然不够；能否不靠人工推理轨迹，只用强化学习激发推理。
- **核心方法**：DeepSeek-R1-Zero 以 DeepSeek-V3-Base 为起点，跳过 RL 前通常的 SFT（监督微调：用人工示范直接训练），直接用 GRPO（组相对策略优化，不需要价值网络）做强化学习，奖励只看最终答案是否与标准答案一致（基于规则）。模型自发出现更长的回答、自我反思、验证和换路。针对 R1-Zero 可读性差、中英混杂、只擅长推理任务的问题，DeepSeek-R1 用拒绝采样、强化学习与 SFT 交替的多阶段流程补上通用能力与人类偏好对齐，并把推理能力蒸馏到多个小模型。
- **为什么在这个库里**：[强化学习方向](../../fields/posttraining/rl/README.md)中"可验证奖励的推理 RL"的起点报告，回答"RL 在后训练里新增了什么"；它的长思维链模型也是[推理时计算方向](../../fields/inference/README.md)里过度思考研究（如 [Do NOT Think That Much for 2+3=?](../url-https-proceedings.mlr.press-v267-chen25bx.html/README.md)）的分析对象。上接 [DeepSeek-V3](../arxiv-2412.19437/README.md)，算法上可对照 [PPO](../ppo/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2501.12948 · [全文 PDF](https://arxiv.org/pdf/2501.12948) · 正式版 Nature 645: 633–638（2025）；arXiv v2（2026-01-04）
- 作者：DeepSeek-AI
- 方向：llm/posttraining/rl、llm/posttraining/sft、llm/inference
