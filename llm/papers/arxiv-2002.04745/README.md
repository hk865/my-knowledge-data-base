# On Layer Normalization in the Transformer Architecture

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2002.04745)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：原始 Transformer 把层归一化（LayerNorm，把一个位置的特征向量按均值和方差标准化）放在残差相加之后（Post-LN），训练必须先用极小的学习率预热、再逐步升到最大值。预热拖慢训练，最终效果又对最大学习率和预热步数很敏感：IWSLT14 德→英上，不预热时 Adam 训练的 BLEU 只有 8.45，预热后约 34（§3.2）。
- **核心方法**：用平均场理论分析初始化时的梯度：Post-LN 中靠近输出层的参数梯度期望很大，直接用大学习率就会不稳定。把归一化移进每个子层的输入、残差通路保持恒等（Pre-LN，Baevski 与 Auli 2018 等已经在用）后，初始化时的梯度表现良好，于是可以去掉预热。机器翻译与 BERT 预训练上，Pre-LN 不预热就达到与 Post-LN 相当的结果、收敛更快；Post-LN 的 BERT 改用 3e-4 的学习率会发散（§4）。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"归一化与残差"一线的起点：今天的大模型几乎都用 Pre-LN（多换成 RMSNorm，一种只按均方根缩放的简化归一化）。站在现在看，Pre-LN 用训练容易换来了深层效率的损失：[ShortGPT](../arxiv-2403.03853/README.md) 把 pre-norm 模型深层"输入输出高度相似"归因于这种结构，删掉 LLaMA 2-13B 的 25% 层后 MMLU 只从 55.0 降到 52.2；[Hyper-Connections](../arxiv-2409.19606/README.md) 称之为表示坍缩；[Attention Residuals](../arxiv-2603.15031/README.md) 指出隐藏状态幅度随层数增长、每层贡献被稀释。"预热为什么必要"在训练科学中的位置见[训练科学](../../../cross-domain/fields/training-science/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2002.04745 · [全文 PDF](https://arxiv.org/pdf/2002.04745) · ICML 2020 · 作者在 Microsoft Research Asia 实习期间完成（中科院计算所、北京大学、Microsoft Research、南开大学）
- 方向：llm/architecture、cross-domain/training-science
