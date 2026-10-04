# Let's Verify Step by Step

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2305.20050)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：训练更可靠的推理模型时，奖励模型应该监督最终结果，还是监督每个中间步骤。
- **核心方法**：固定生成器，只比较奖励模型：在 MATH 上用 best-of-N 重排来评估，过程监督（人对每一步标对错）的奖励模型明显优于结果监督，解出 MATH 代表性子集 78% 的题；主动学习提高了过程标注的效率；公开 80 万条步骤级人工标签 PRM800K。论文刻意不研究用奖励模型去做 RL。
- **为什么在这个库里**：过程奖励模型（PRM，一句话：给推理的每一步打分的奖励模型）的代表，[RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)"奖励来源"一格；DeepSeek-R1 的"失败尝试"把 PRM 难以定义步骤、难以标注、会被钻空子列为放弃理由，DeepSeekMath 提到 PRM800K 仍有约 20% 错标。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2305.20050 · [全文 PDF](https://arxiv.org/pdf/2305.20050) · OpenAI
- 方向：llm/posttraining/rl、llm/posttraining/preferences
