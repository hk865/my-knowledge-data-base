# Classifier-Free Diffusion Guidance

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2207.12598)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：分类器引导要额外训练一个在带噪数据上的分类器，不能直接用现成分类器；而且沿分类器梯度采样像是对分类器做对抗攻击，FID、IS 这类基于分类器的指标变好，可能只是"骗过了分类器"。
- **核心方法**：训练时以概率 p_uncond 把条件随机换成"空"，让同一个网络同时学条件与无条件的噪声预测；采样时取 ε̃ = (1+w)·ε(z, c) − w·ε(z)，沿"条件减无条件"的方向多走一步。p_uncond 取 0.1 或 0.2 好于 0.5。ImageNet 128×128 上 w = 0.3、256 步时 FID 2.43，优于分类器引导的 ADM-G（2.97）；w 加到 4 时 Inception Score 从约 158 升到约 422、FID 升到约 21.5，强引导的样本颜色饱和。作者自述的代价：每步要算两次网络（条件与无条件），按网络调用次数公平比较应看 128 步的 3.04，反而不如 ADM-G；以多样性换保真度，在部署中可能伤害数据里本就少见的群体。论文未声明代码发布。
- **为什么在这个库里**：[Baseline 页](../../fields/generation/BASELINES.md)部件 6"条件与引导"的默认做法：[LDM](../arxiv-2112.10752/README.md)（引导系数 1.5 得到 3.60）、[DiT](../arxiv-2212.09748/README.md) 的 2.27、[Imagen](../arxiv-2205.11487/README.md)（10% 概率丢弃文本）、[DALL·E 2](../arxiv-2204.06125/README.md)、[Video Diffusion](../video-diffusion/README.md) 都用它，[Genie 2](../genie-2-blog/README.md) 用它增强动作可控性。公式与数值例子见 [Video Diffusion 精读](../video-diffusion/reading.md)机制第 5 节。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2207.12598 · [全文 PDF](https://arxiv.org/pdf/2207.12598) · Google Research, Brain Team · 短版见 NeurIPS 2021 Workshop
- 方向：multimodal/generation
