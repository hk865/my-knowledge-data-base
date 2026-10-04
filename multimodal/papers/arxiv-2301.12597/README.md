# BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2301.12597)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：端到端视觉语言预训练越来越贵；冻结的 LLM 没见过图像，作者认为 Frozen、Flamingo 只用图生文损失不足以弥合模态差距。
- **核心方法**：在冻结的图像编码器与冻结的 LLM 之间放一个轻量 Q-Former（188M 参数，BERT-base 初始化），用 32 个 768 维的可学查询从 ViT-L 的 257×1024 特征中抽取信息，形成信息瓶颈。分两段预训练：先只接图像编码器，用图文对比、图文匹配、图生文三个目标学表征；再接 LLM 做生成学习。零样本 VQAv2 65.0%，比 Flamingo-80B 的 56.3% 高 8.7 个百分点，可训练参数少 54 倍；去掉第一段表征学习，零样本 VQA 明显变差。
- **为什么在这个库里**：[Baseline 页](../../fields/vlm/BASELINES.md)的对照基线（查询瓶颈一格）。自述给 LLM 加上下文示例不提升 VQA（训练数据每条只有一对图文），OK-VQA 不如 Flamingo-80B。[判断] 这类重采样器后来被 MLP 取代，依据见 [LLaVA-1.5](../arxiv-2310.03744/README.md) 附录 C 与[方向页](../../fields/vlm/README.md)主线第 2 节。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2301.12597（Junnan Li 等 4 位作者；当前 v3，2023-06）· [全文 PDF](https://arxiv.org/pdf/2301.12597v3) · Salesforce Research
- 方向：[视觉语言模型](../../fields/vlm/README.md)
