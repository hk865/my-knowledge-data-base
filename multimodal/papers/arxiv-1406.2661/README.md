# Generative Adversarial Networks

> 状态：文献卡 · 2014 · [原文](https://arxiv.org/abs/1406.2661)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：深度生成模型靠最大似然训练，而似然里的概率计算难以处理，要靠近似推断或马尔可夫链采样。能否只用反向传播和前向采样训练一个生成模型？
- **核心方法**：生成器 G 把噪声 z 映成样本，判别器 D 判断样本来自数据还是 G，两者做极小极大博弈；在 D 最优时，G 的目标等于 −log4 加上数据分布与生成分布之间 Jensen–Shannon 散度的两倍，所以全局最优是生成分布等于数据分布。训练初期 D 很容易拒绝假样本、梯度饱和，作者改让 G 最大化 log D(G(z))。主实验的 G、D 都是多层感知机，在 MNIST、TFD、CIFAR-10 上用 Parzen 窗估计对数似然（作者说明这种估计方差大、高维下不好）。作者自述两个缺点：没有生成分布的显式表示；D 必须与 G 同步训练，否则 G 会把太多 z 映到同一个 x（"Helvetica 情形"，即后来所说的模式坍缩）。代码与超参数公开。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 1 个节点，[Baseline 页](../../fields/generation/BASELINES.md)中"一次前向出样本"的对照基线。判别器后来以损失项的身份回到主流：[VQGAN](../arxiv-2012.09841/README.md) 与 [LDM](../arxiv-2112.10752/README.md) 的自编码器、[ADD](../arxiv-2311.17042/README.md) 的少步蒸馏、[Seedance 1.0](../arxiv-2506.09113/README.md) 的视频 VAE 与蒸馏。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1406.2661 · [全文 PDF](https://arxiv.org/pdf/1406.2661) · Université de Montréal
- 名称：arXiv 页面题名为 Generative Adversarial Networks，PDF 首页印的是 Generative Adversarial Nets
- 方向：multimodal/generation
