# HunyuanImage 3.0 Technical Report

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2509.23951)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：引言写道，Seedream 4.0、Nano Banana、GPT-Image 这些领先的图像生成系统多为闭源，透明度与可复现性受限。
- **核心方法**：以总参数 800 亿以上、每 token 激活 130 亿（64 个专家中选 8 个）的 MoE 语言模型 Hunyuan-A13B 为底座，接一个视觉编码器和一个 16 倍下采样、32 维潜空间的 VAE。文字 token 按下一 token 自回归预测，图像 token 在同一个网络内对 VAE 潜变量做扩散（沿用 Transfusion、JanusFlow 的做法）；"广义因果注意力"让文字只看前文，同一张图内的图像 token 互相全看。作条件的图像同时取 VAE 与视觉编码器特征，理解、生成、编辑在同一条序列里完成。生成前可先写一段思维链，把用户意图改写成详细描述。后训练依次用 DPO、MixGRPO、SRPO 和自研的 ReDA。训练集约 50 亿张图。1000 条提示的人评 GSB 中，相对 Seedream 4.0、Nano Banana、GPT-Image 的相对胜率为 1.17%、2.64%、5.00%。分析发现层越深，专家越按模态分工。
- **为什么在这个库里**：[Baseline 页](../../fields/generation/BASELINES.md)部件 3"理解与生成共用一个语言模型"的开放代表，也是[视觉语言模型方向](../../fields/vlm/README.md)与[生成方向](../../fields/generation/README.md)交汇的一点。目前开放的只有图像生成模块，微调与后训练只针对图像生成。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2509.23951 · [全文 PDF](https://arxiv.org/pdf/2509.23951v3) · 腾讯混元 · arXiv v1 2025-09，v3 2026-06 · 公开代码与图像生成模块权重
- 方向：multimodal/generation、multimodal/vlm
