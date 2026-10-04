# DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.03300)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源模型在竞赛级数学上远落后于闭源模型；同时 PPO 需要一个与策略同样大的价值模型，显存与计算负担重，而且语言模型通常只在最后一个 token 拿到奖励，逐 token 准确的价值函数很难训练（§4.1）。
- **核心方法**：从 Common Crawl 挖出 120B 数学 token，对 7B 模型继续预训练 500B token，数学 SFT 之后用 GRPO（Group Relative Policy Optimization，一句话：对同一题采一组回答，用组内奖励的均值与标准差归一化得到优势，去掉价值模型，KL 项直接加进损失）做 RL：GSM8K 从 82.9% 到 88.2%，MATH 从 46.8% 到 51.7%。这一版的奖励来自训练出来的奖励模型（也试了过程监督）。§5.2.2 发现 RL 提高了 Maj@K（K 次采样多数投票）却没有提高 Pass@K（K 次中至少一次答对），作者解释为 RL 让输出分布更稳健、把 TopK 里的正确答案提上来，而不是增强基础能力。
- **为什么在这个库里**：GRPO 的出处，[RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)"优势估计 = 组内相对"一格的基线；§5.2.2 的观察比 Yue 等（2025）的 pass@k 研究早一年。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2402.03300 · [全文 PDF](https://arxiv.org/pdf/2402.03300) · DeepSeek-AI、清华大学、北京大学
- 方向：llm/posttraining/rl、llm/pretraining
