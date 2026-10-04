# Scaling Laws for Autoregressive Generative Modeling

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2010.14701)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：[Kaplan 等](../arxiv-2001.08361/README.md)的规模定律只在语言上测过；换成图像、视频、图文、数学这些模态，自回归 Transformer 是否也有同样的规律，最优配比是否相同。
- **核心方法**：沿用 Kaplan 等的方法，在生成式图像建模、视频建模、图文双向生成、数学解题四个领域训练不同规模的自回归 Transformer，发现交叉熵都服从"幂律加常数"：常数项（不可约损失）估计数据分布本身的熵，幂律项（可约损失）估计真实分布与模型分布之间的 KL。最优模型大小也随算力按幂律增长，指数约 0.7，在各领域几乎相同（Fig.2）。按此解释，十亿参数的 Transformer 已几乎完美地建模了降采样到 8×8 的 YFCC100M 图像分布。
- **为什么在这个库里**：[训练科学方向](../../fields/training-science/README.md)"不同模态的差异"一节的主要证据：生成式模型在各模态上拟合交叉熵、最优配比相近；与之对照的是 [Zhai 等](../arxiv-2106.04560/README.md)在判别式视觉上拟合错误率得到的双饱和曲线。边界：它的配比沿用 Kaplan 的方法，其他模态是否也需要 [Chinchilla](../arxiv-2203.15556/README.md) 式修正，原文没有检验。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2010.14701 · [全文 PDF](https://arxiv.org/pdf/2010.14701) · OpenAI · arXiv 预印本
- 作者：Tom Henighan、Jared Kaplan、Mor Katz、Mark Chen、Christopher Hesse、Jacob Jackson、Heewoo Jun、Tom B. Brown、Prafulla Dhariwal、Scott Gray、Chris Hallacy、Benjamin Mann、Alec Radford、Aditya Ramesh、Nick Ryder、Daniel M. Ziegler、John Schulman、Dario Amodei、Sam McCandlish
- 方向：cross-domain/training-science
