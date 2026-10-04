# DAPO: An Open-Source LLM Reinforcement Learning System at Scale

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.14476)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：o1 博客与 R1 报告都没有公开大规模 RL 的关键细节，社区难以复现：在 Qwen2.5-32B 基座上直接跑 GRPO，AIME 2024 只有 30 分，低于 DeepSeek 报告的 47 分。
- **核心方法**：找出朴素 GRPO 的熵坍缩（一句话：策略熵在训练早期迅速降低，同组采样几乎一样，探索停止）、奖励噪声与训练不稳，提出四处修改：Clip-Higher（把裁剪上下界解耦，上界放宽到 0.28，让低概率的"探索"token 能被提起来）、动态采样（丢掉全对或全错、优势为 0 的题组）、token 级损失（按 token 而不是按样本平均，避免长回答中的乱码与重复得不到惩罚）、超长回答的软惩罚；并去掉 KL 项，理由是长思维链模型本来就要远离初始模型。在 Qwen2.5-32B 上逐项累加从 30 分到 50 分（表 1）。开源基于 verl 的代码与数据。
- **为什么在这个库里**：[RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)中"裁剪""采样与筛选""损失聚合"三格的代表；它列出的四个坑是 GRPO 在长思维链上的标准故障清单，机器人 VLA 的 [SimpleVLA-RL](../../../robotics-embodied/papers/arxiv-2509.09674/README.md) 借用了其中的 Clip-Higher 与动态采样，并同样去掉 KL。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2503.14476 · [全文 PDF](https://arxiv.org/pdf/2503.14476) · 字节跳动 Seed、清华 AIR、港大
- 方向：llm/posttraining/rl
