# Score-Based Generative Modeling through Stochastic Differential Equations

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2011.13456)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：SMLD（在多个噪声尺度上估计分数、再用 Langevin 动力学采样）与 DDPM 都是"先逐级加噪、再学逆转"，各自只用有限个噪声尺度，缺一个统一框架。
- **核心方法**：把加噪写成连续时间的随机微分方程（SDE）；逆向 SDE 只依赖每个时刻的分数（对数密度对数据的梯度），由此说明 SMLD 与 DDPM 分别是两种 SDE（VE、VP）的离散化。同一个分数模型还给出预测–校正采样器、可以精确计算似然的概率流 ODE，以及不必重训就能做的类条件生成、修复和上色。CIFAR-10 无条件生成 FID 2.20、Inception Score 9.89（DDPM 为 3.17），均匀去量化似然 2.99 bits/dim，并首次用分数模型生成 1024×1024 人脸。作者自述采样仍比同数据集上的 GAN 慢，可选采样器多，带来大量要调的超参数。代码与检查点公开。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 3 个节点（与 [DDPM](../ddpm/README.md) 并列），[Baseline 页](../../fields/generation/BASELINES.md)部件 4 的连续时间写法；概率流 ODE 是 [DDIM](../arxiv-2010.02502/README.md) 与[流匹配](../arxiv-2210.02747/README.md)"确定性少步路径"的理论入口。分数的直觉见[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6 节。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2011.13456 · [全文 PDF](https://arxiv.org/pdf/2011.13456) · Stanford University、Google Brain · ICLR 2021
- 方向：multimodal/generation
