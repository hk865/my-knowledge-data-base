# Kimi K2: Open Agentic Intelligence

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2507.20534)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：高质量人类数据越来越有限，作者把"token 效率"（每个训练 token 带来的性能提升）看作规模化的关键系数；而 token 效率高的 Muon 优化器在放大时会出现注意力 logit 爆炸，引发损失尖峰甚至发散。
- **核心方法**：优化器侧提出 MuonClip，即 Muon 加权重衰减、更新 RMS 匹配，再加 QK-Clip：每步更新后，若某个注意力头在这一批里的最大 logit 超过阈值（K2 取 100），就按比例缩小这个头的 Q、K 投影权重。选择这种做法，是因为 MLA（多头潜在注意力）在推理时不显式构造 Key 矩阵，无法使用 QK-Norm；而 logit soft-cap 只截断结果，Q 与 K 的点积在截断前仍可能过度增长。中等规模实验（9B 激活、53B 总参数）中，原版 Muon 的最大 logit 很快超过 1000；K2（1.04T 总参数、32B 激活，结构仿 DeepSeek-V3，专家数从 256 增到 384，注意力头从 128 减到 64）在 15.5T token 上没有出现一次损失尖峰，前 7 万步内有 12.7% 的头触发过 QK-Clip，之后全部自行回到阈值以下。数据侧用改写提高知识 token 的效用：同一份 wiki 文本原样重复 10 遍，SimpleQA 为 23.76；改写一次再重复 10 遍为 27.39；改写 10 次、每份只训一遍为 28.94。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"损失稳定"与"更多知识"两个问题的交点；它的稀疏度规模定律（固定激活参数时，专家总数越多损失越低）也是"更大网络"一节的证据。前一篇是 [Moonlight](../arxiv-2502.16982/README.md)，下一代是 [Kimi K3](../arxiv-2607.24653/README.md)；结构基础见 [DeepSeek-V3](../arxiv-2412.19437/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2507.20534 · [全文 PDF](https://arxiv.org/pdf/2507.20534) · Kimi Team（Moonshot AI）
- 方向：llm/pretraining、llm/posttraining/rl
