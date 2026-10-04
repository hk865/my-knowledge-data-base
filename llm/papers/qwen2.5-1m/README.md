# Qwen2.5-1M Technical Report

> 状态：技术精读 · 2025 · [原文](https://arxiv.org/abs/2501.15383)

[返回大语言模型目录](../../README.md)

- **解决什么**：把上下文从 128K 扩到 100 万 token，不损失短上下文能力，并把百万 token 输入的推理成本降到可用。
- **核心方法**：相对 128K 版 Qwen2.5：训练侧用长数据合成、渐进式长上下文预训练（最长 256K）和多阶段 SFT；推理侧用无需训练的长度外推（DCA 重写位置距离，配合 YaRN 这种调整 RoPE 频率的外推方法）把可用长度扩大至少 4 倍，再用稀疏注意力加分块预填充（prefill：一次性处理整段输入的阶段）和稀疏度修正降低成本。百万 token 场景下预填充加速 3–7 倍；Qwen2.5-14B-Instruct-1M 在长上下文任务上明显超过 GPT-4o-mini，支持的长度是它的 8 倍。
- **为什么在这个库里**：[长上下文与记忆方向](../../fields/long-context/README.md)和[预训练方向](../../fields/pretraining/README.md)"长注意力放到预训练末段分级加长"一线的开源证据。精读把训练长度、外推长度、输出长度三者拆开。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

[Qwen2.5 Technical Report](../arxiv-2412.15115/README.md)（被扩展的底座）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2501.15383 · [全文 PDF](https://arxiv.org/pdf/2501.15383v1) · 精读依据 v1
- 作者：An Yang、Bowen Yu、Chengyuan Li、Dayiheng Liu、Fei Huang 等 28 位（Qwen Team，阿里巴巴）
- 方向：llm/pretraining、llm/architecture、llm/inference、llm/posttraining/sft、llm/posttraining/preferences
