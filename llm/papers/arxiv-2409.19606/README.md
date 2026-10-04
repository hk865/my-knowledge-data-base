# Hyper-Connections

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2409.19606)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：残差连接的两种常用放法各有代价：Pre-Norm（先归一化再进子层）缓解梯度消失，却让深层特征彼此高度相似、新增的层贡献越来越小，作者称为表示坍缩；Post-Norm 缓解坍缩，却重新带来梯度消失。作者把这叫作跷跷板，根源是两者都把层的输入与输出之间的连接强度写死了（§1）。
- **核心方法**：把残差流扩成 n 份（n > 1），用可学习的深度连接（每层从前面哪几份读、写回哪几份）与宽度连接（同层各份之间交换信息）替代固定的残差相加，动态版本（DHC）的连接权重随输入变化。OLMoE-1B-7B 上 DHC×4 收敛快 1.8 倍，训练 500B token 后 ARC-Challenge 高 6 分；n = 1 时跷跷板仍在，效果反而变差（Fig.1、附录 F）。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"归一化与残差"一线中 [Pre-LN](../arxiv-2002.04745/README.md) 之后的节点。站在现在看，它的混合矩阵没有约束，在更大规模上暴露了问题：DeepSeek 的 [mHC](../arxiv-2512.24880/README.md) 报告 27B 模型约第 12k 步损失突升、复合映射的最大增益峰值约 3000，改用双随机矩阵约束；Kimi 的 [Attention Residuals](../arxiv-2603.15031/README.md) 换成跨层注意力。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2409.19606 · [全文 PDF](https://arxiv.org/pdf/2409.19606) · ICLR 2025 · ByteDance Seed-Foundation-Model Team
- 方向：llm/architecture
