# Denoising Diffusion Probabilistic Models

> 状态：技术精读 · 2020 · [原文](https://arxiv.org/abs/2006.11239) · [NeurIPS 2020 正式版](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：2020 年 GAN 样本最锐利，但训练不稳、会模式坍缩；能算似然的模型样本质量落后。扩散模型（一句话：先用固定的加噪链把图像逐步变成纯噪声，再训练网络沿相反方向一步步去噪）已由 Sohl-Dickstein 等（2015）提出，却还没有人展示过高质量样本。
- **核心方法**：框架沿用 Sohl-Dickstein 等，改了三处参数化与训练选择：网络预测加进去的那份高斯噪声 ε，而不是反向均值；丢掉变分下界里随噪声等级变化的权重，直接用不加权的均方误差回归噪声（Lsimple）；固定反向方差，用线性噪声日程和带自注意力的 U-Net。预测 ε 让训练目标等价于多噪声尺度的去噪 score matching，把扩散模型与 NCSN 连成一件事；表 2 显示前两处必须一起用，只换参数化时 FID 为 13.51，加上 Lsimple 才到 3.17（FID 一句话：生成样本与真实样本在 Inception 特征空间里的分布距离，越低越好）。无条件 CIFAR10 上 FID 3.17，样本质量与 GAN 相当（表 1），代价是生成一张图要调用网络 1000 次，似然也不占优。
- **为什么在这个库里**：[视觉生成方向 Baseline 页](../../fields/generation/BASELINES.md)的"训练与采样的基线"，也是[入门页](../../fields/generation/README.md)主线第 3 个节点：此后的扩散与流匹配，包括视频生成和机器人的 [Diffusion Policy](../../../robotics-embodied/papers/diffusion-policy/README.md)，都可以读成"保留这个训练形态，换掉其中某个部件"。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：把生成拆成 1000 级去噪；"局限与后续"补了 DDIM、Improved DDPM、LDM、DiT、Flow Matching
- [本篇图解与说明](figures/README.md)

## 身份信息

- 稳定标识：arxiv:2006.11239 · UC Berkeley · NeurIPS 2020
- 年份：2020
- [官方原文页面](https://arxiv.org/abs/2006.11239)
- [官方全文入口](https://arxiv.org/pdf/2006.11239v2)
- 阅读版本：v2
- 方向：multimodal/generation、robotics/embodied-policies
