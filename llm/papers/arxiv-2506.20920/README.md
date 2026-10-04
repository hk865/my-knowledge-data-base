# FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2506.20920)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：英语网页清洗配方直接搬到其他语言时，过滤、去重与评测标准怎样调整。
- **核心方法**：继承 FineWeb 流水线，用按语言适配的规则与阈值构建语料，并结合重复次数和质量重新加权；用单语言训练消融隔离各步骤的影响。
- **为什么在这个库里**：位于[预训练 Baseline](../../fields/pretraining/BASELINES.md)的数据组成一格，把"数据质量高"拆成可检验的处理步骤。优先级：选读。

## 身份信息

- 作者：Guilherme Penedo、Hynek Kydlíček、Vinko Sabolčec、Bettina Messmer、Negar Foroutan、Amir Hossein Kargaran、Colin Raffel、Martin Jaggi、Leandro Von Werra、Thomas Wolf
- 稳定标识：arxiv:2506.20920 · [全文](https://arxiv.org/pdf/2506.20920)
- 方向：llm/pretraining

## 批注

**易误读**

- 主要消融按语言分别训练模型；语料覆盖范围大于下游验证范围，不能由此推出一个联合多语言模型在所有语言上都同样受益。
