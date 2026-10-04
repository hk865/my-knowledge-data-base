# Understanding R1-Zero-Like Training: A Critical Perspective

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.20783)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：R1-Zero 式训练（不经 SFT、直接从基座做 RL）里，哪些现象来自基座、哪些来自 RL 算法。
- **核心方法**：检查多个基座：包括 DeepSeek-V3-Base 在内，几乎都已出现"顿悟"式的自我反思；Qwen2.5 基座不用提示模板反而高约 60%，作者推测其预训练含问答拼接的文本。指出 GRPO 的两个优化偏差：按回答长度归一化，让错误回答越写越长（长度偏差）；按组内标准差归一化，让太易或太难的题权重过大（难度偏差）；并发现多个流行的开源 PPO 实现也按长度归一化损失。去掉这两项得到 Dr. GRPO，token 效率更高；用它在 7B 基座上训练，8 张 A100 跑 27 小时，AIME 2024 达到 43.3%。
- **为什么在这个库里**：后训练总览"GRPO 的长度偏置"一条的出处，[RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)"损失聚合"一格；它对"顿悟时刻"的复核，是读 DeepSeek-R1 时必须带上的边界。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2503.20783 · [全文 PDF](https://arxiv.org/pdf/2503.20783) · Sea AI Lab、新加坡国立大学、新加坡管理大学 · COLM 2025
- 方向：llm/posttraining/rl
