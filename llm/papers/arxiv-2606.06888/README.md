# Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.06888)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：独立语料有限、算力充足时，怎样反复训练而不过度记忆原文。
- **核心方法**：在强权重衰减的自回归基线上加入掩码输入的辅助下一词损失 MIR，并用耦合参数量与数据量的 SoftQ 拟合重复数据区间。
- **为什么在这个库里**：接续[预训练](../../fields/pretraining/README.md)的"高质量 token 不够怎么办"，为合成改写之外提供正则化对照。优先级：选读。

## 身份信息

- 作者：Zhiwei Xu、Shihao Wu、Hanseul Cho、Wei Hu、Yixin Wang
- 稳定标识：arxiv:2606.06888 · [全文](https://arxiv.org/pdf/2606.06888)
- 方向：llm/pretraining

## 批注

**易误读**

- MIR 每批需要两次前向，改进的是有限独立数据下的利用率；实验到 1.4B 参数、400M 独立 token，且依赖逐配置调参。
