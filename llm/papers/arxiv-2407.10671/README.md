# Qwen2 Technical Report

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2407.10671)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：发布 0.5B 到 72B 的开放权重稠密模型和一个 MoE 模型（混合专家：每个 token 只激活部分前馈子网络），在语言理解、多语言、代码、数学和推理上超过前代 Qwen1.5 和多数开放权重模型。
- **核心方法**：相对 Qwen1.5：预训练数据扩到 7T 以上 token；注意力改用分组查询注意力（GQA：多个查询头共享一组 KV，减小 KV 缓存），用双块注意力（DCA）加 YARN 把上下文外推到训练长度之外；MoE 版 57B-A14B 从 Qwen2-7B 上扩（upcycle）而来。后训练先用 50 万条以上的指令数据做 SFT，再做离线与在线两阶段的 DPO（直接偏好优化：不训练独立奖励模型，直接在偏好对上优化）。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)中 Qwen 一线（数据从 7T 到 [Qwen2.5](../arxiv-2412.15115/README.md) 的 18T）的起点，也是[偏好学习方向](../../fields/posttraining/preferences/README.md)里"SFT 之后接离线、在线 DPO"的开源样本。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2407.10671 · [全文 PDF](https://arxiv.org/pdf/2407.10671) · 权重发布于 Hugging Face 与 ModelScope
- 作者：An Yang、Baosong Yang、Binyuan Hui、Bo Zheng、Bowen Yu 等 62 位（Qwen Team，阿里巴巴集团）
- 方向：llm/pretraining、llm/architecture、llm/posttraining/sft、llm/posttraining/preferences
