# Auto-Encoding Variational Bayes

> 状态：文献卡 · 2013 · [原文](https://arxiv.org/abs/1312.6114)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：有向概率模型含连续潜变量、后验难以计算、数据集又很大时，怎样高效地做推断和学习；常用的平均场变分方法要对近似后验求解析期望，一般情况下同样算不出。
- **核心方法**：把变分下界里对潜变量的采样改写成 z = μ + σ·ε（重参数化，ε 取自标准高斯），得到可以直接用随机梯度优化的下界估计量（SGVB）；再用一个神经网络编码器近似每个数据点的后验，与解码器一起训练，这就是变分自编码器。实验只在 MNIST 和 Frey Face 上：与 wake-sleep 比较下界，收敛更快、解更好；边缘似然只在 3 维潜空间的小模型上估计，作者写明潜空间维度更高时估计变得不可靠。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 1 个节点，[Baseline 页](../../fields/generation/BASELINES.md)部件 2"表示空间"的源头：LDM 的自编码器带 KL 正则，DDPM 可以读成编码器固定为加噪链的多层 VAE。重建项与 KL 项的手算见 [VAE 讲义](../../../foundations/lessons/16-vae.md)第 4 节。优先级：必读（先读讲义）。

## 身份信息

- 稳定标识：arxiv:1312.6114 · [全文 PDF](https://arxiv.org/pdf/1312.6114) · Universiteit van Amsterdam
- 方向：multimodal/generation
