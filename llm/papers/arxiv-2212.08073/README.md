# Constitutional AI: Harmlessness from AI Feedback

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2212.08073)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：能否不用人对有害输出的标注，只用一组书面原则训练无害的助手。
- **核心方法**：监督阶段让模型按原则自我批评、改写回答，再用改写后的回答微调；RL 阶段由模型按原则比较两个回答、训练偏好模型，用它做 RL（RLAIF，一句话：用 AI 的偏好代替人的偏好做 RLHF）。得到"不回避、会解释反对理由"的无害助手，用到的人工标签远少于 RLHF。作者记录：RL-CAI 训练过头会出现 Goodhart 现象，回答变得过于严厉，或塞入套话。
- **为什么在这个库里**：[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)"偏好来源 = AI"一格的起点；DeepSeek-V3 的自我奖励直接引用了它，Kimi K2 的自我批评 rubric 奖励是同一思路的延伸。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2212.08073 · [全文 PDF](https://arxiv.org/pdf/2212.08073) · Anthropic
- 方向：llm/posttraining/preferences
