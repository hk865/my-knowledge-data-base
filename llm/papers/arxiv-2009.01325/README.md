# Learning to summarize from human feedback

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2009.01325)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：摘要模型用参考摘要训练、用 ROUGE 评测，两者都只是"摘要质量"的粗糙代理。
- **核心方法**：收集大量人对两份摘要的比较，训练奖励模型，再用 PPO 优化摘要策略（奖励中减去相对监督模型的 KL 惩罚）；在 Reddit TL;DR 上超过人写的参考摘要和大得多的纯监督模型，并能迁移到 CNN/DM 新闻。作者测量了过度优化：轻度优化时人评变好，继续优化后真实偏好下降，奖励模型最终与人的偏好负相关；原文同时指出机器人领域学到的奖励函数也有类似现象（图 5）。作者自述成本高：6.7B 模型的 RL 微调约需 320 GPU 天，标注用了数千小时。
- **为什么在这个库里**：InstructGPT 三段式（SFT → 奖励模型 → PPO）的直接前身，[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)的前史；"奖励过度优化"在语言模型上的第一份测量。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2009.01325 · [全文 PDF](https://arxiv.org/pdf/2009.01325) · OpenAI
- 方向：llm/posttraining/preferences、llm/posttraining/rl
