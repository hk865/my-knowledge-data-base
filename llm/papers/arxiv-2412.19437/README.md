# DeepSeek-V3 Technical Report

> 状态：技术精读 · 2024 · [原文](https://arxiv.org/abs/2412.19437)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：以可控的成本训练一个与领先闭源模型可比的开源 MoE 模型（混合专家：每个 token 只激活部分前馈子网络）。
- **核心方法**：沿用 [DeepSeek-V2](../deepseek-v2/README.md) 的 MLA（多头潜在注意力：把 KV 缓存压成低维潜向量）与 DeepSeekMoE，新增三处：无辅助损失的负载均衡（用每个专家的偏置项调整路由，而不是加一项均衡损失）；多 token 预测（MTP：每个位置额外预测更远的 token 以增强训练，推理时可丢弃这些模块，或拿来做投机解码的草拟）；FP8 混合精度训练。总参数 671B、每 token 激活 37B，预训练 14.8T token，全部训练用 2.788M H800 GPU 小时，过程中没有出现不可恢复的损失尖峰，也没有回滚。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"稀疏化"与"数值精度"两线、[架构与效率方向](../../fields/architecture/README.md) MoE 一线的核心报告。上接 [DeepSeekMoE](../arxiv-2401.06066/README.md) 与 [无辅助损失负载均衡](../arxiv-2408.15664/README.md)，下接以 V3-Base 为底座的 [DeepSeek-R1](../arxiv-2501.12948/README.md) 和 [DeepSeek-V4](../arxiv-2606.19348/README.md)。MTP 一节也是[推理时计算方向](../../fields/inference/README.md)"MTP 与并行验证"的来源。精读手算了 671B / 37B 的参数账与每 token 计算，并用 V3.2、V4、V4.1-Flash 与 Kimi、Qwen、Llama 4 的后续改动反推 V3 路由与部署的隐藏成本。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [证据档案](evidence.json) · [原文版本与阅读记录](source.json)
- 前作：[DeepSeekMoE 精读](../arxiv-2401.06066/reading.md)、[DeepSeek-V2 精读](../deepseek-v2/reading.md)

## 批注

**易误读**
- MTP 模块按深度顺序串联，共享嵌入层与输出头，保留因果链；它不是给任意大模型做草拟的独立小模型，也不是多个并行的独立预测头（§2.2）。
- 第二个 token 85%–90% 的接受率和约 1.8 倍的每秒 token 数，是报告中特定配置的结果（§5.4.3），MTP 本身不提供精确分布保证，要与标准投机验证结合才有。

## 身份信息

- 稳定标识：arxiv:2412.19437 · [全文 PDF](https://arxiv.org/pdf/2412.19437v2) · 精读依据 v2 · 检查点发布于 deepseek-ai/DeepSeek-V3
- 作者：DeepSeek-AI
- 方向：llm/pretraining、llm/architecture、llm/posttraining/sft、llm/posttraining/rl、llm/inference
