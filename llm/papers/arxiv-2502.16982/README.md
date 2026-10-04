# Muon is Scalable for LLM Training

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2502.16982)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Muon（对梯度动量矩阵做近似正交化之后再更新参数的优化器）在小型语言模型上效果好，但三件事没有验证：能否扩到数十亿参数、万亿 token；正交化需要完整的梯度矩阵，怎样在分布式训练里实现；预训练与监督微调能否都用它。
- **核心方法**：相对原始 Muon 加两处修改。一是加入 AdamW 式的权重衰减：作者观察到，不加时权重和层输出的 RMS 持续增长，超出 bf16 的高精度范围，长训练中损失反而落后。二是按矩阵形状缩放更新（乘 0.2·√max(A, B)），使不同形状矩阵的更新 RMS 一致，并与 AdamW 通常的 0.2–0.4 对齐，从而直接复用为 AdamW 调好的学习率和权重衰减。在计算最优设定下的规模定律实验中，Muon 达到与 AdamW 相同的损失只需约 52% 的训练 FLOPs。据此训练 Moonlight（摘要称 3B 激活、16B 总参数的 MoE，5.7T token，最后 0.5T token 用数学、代码、推理类最高质量数据冷却），并公开分布式实现与中间检查点。自述局限：AdamW 预训练的模型用 Muon 微调（或反过来）效果欠佳，原因有待研究。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"优化器"一线的起点。[Muon 讲义](../../../foundations/lessons/modules/optimization/muon.md)讲正交化的机制，本篇讲规模化需要的两处修改。后续 [Kimi K2](../arxiv-2507.20534/README.md) 加入 QK-Clip，[Kimi K3](../arxiv-2607.24653/README.md) 改为按注意力头分块正交化，[DeepSeek-V4](../arxiv-2606.19348/README.md) 在 1.6T 模型上采用。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2502.16982 · [全文 PDF](https://arxiv.org/pdf/2502.16982) · Moonshot AI（另有 UCLA 作者）
- 方向：llm/pretraining
