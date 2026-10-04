# On-Policy Distillation

> 状态：文献卡 · 2025 · [原文](https://thinkingmachines.ai/blog/on-policy-distillation/)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：离线蒸馏（学生学教师写好的回答）只教学生在教师走过的前缀上怎么做，学生自己写偏后没人纠正；RL 能在学生自己的轨迹上学，但每条轨迹只有末尾一个奖励，信号稀疏、成本高。
- **核心方法**：学生自己采样回答，教师对学生写出的每个 token 给出自己的对数概率，以逐 token 的反向 KL（学生分布相对教师分布）作为每一步的负奖励，折扣因子取 0，只优化"下一个 token"。博客把它和 RL 的差别概括为：RL 每条轨迹只教 O(1) 比特，蒸馏教 O(N) 比特（N 为 token 数）。实验：Qwen3-8B-Base 先在 40 万条题上做 SFT，AIME'24 为 60%；接着做 on-policy 蒸馏（教师 Qwen3-32B），约 150 步到 70%，作者估计比继续扩大离线 SFT 到同样分数便宜约 9 倍（数据集已有时），算上教师生成数据的成本约 30 倍。博客也复述了 Qwen3 报告的对照：RL 用 17,920 GPU 小时到 67.6%，on-policy 蒸馏用约十分之一的算力到 74.4%。另一个实验用它做持续学习：模型在内部文档上中段训练后指令遵循下降，再用原模型作教师做 on-policy 蒸馏，IF-eval 恢复到 83%（原为 85%），内部知识问答从 18% 提到 41%。
- **为什么在这个库里**：[SFT 方向](../../fields/posttraining/sft/README.md)第 6 节"on-policy 蒸馏"在 Qwen3 报告之外最清楚的公开说明，也是 DeepSeek-V4、Kimi K3、GLM-5 用它合并专家或恢复能力之前的方法说明。它的形式与机器人中的 DAgger 相同（见[后训练总览](../../fields/posttraining/README.md)"与机器人强化学习的共性"）。官方博客，未经同行评议。优先级：必读。

## 批注

**易误读**
- 67.6% 与 74.4% 两个数字是博客引用的 Qwen3 报告结果，不是 Thinking Machines 自己的实验；自己的实验是"60% → 约 150 步到 70%"。
- 方法要求能拿到教师的逐 token 对数概率，并且师生分词兼容。

## 身份信息

- 稳定标识：url:https://thinkingmachines.ai/blog/on-policy-distillation · 官方博客，2025-10-27
- 作者：Kevin Lu 与 Thinking Machines Lab 的合作者
- 方向：llm/posttraining/sft、llm/posttraining/rl
