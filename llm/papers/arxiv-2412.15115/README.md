# Qwen2.5 Technical Report

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.15115)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在 Qwen2 的基础上同时改进预训练与后训练，发布多个尺寸的开放权重模型，以及两个托管的 MoE 模型（Qwen2.5-Turbo、Qwen2.5-Plus）。
- **核心方法**：相对 Qwen2，预训练数据从 7T 扩到 18T token；后训练用 100 万条以上样本做 SFT（监督微调：用示范数据直接训练），再做多阶段强化学习：先离线 DPO（直接偏好优化：直接在偏好对上训练，不单独训练奖励模型），再在线 GRPO（组相对策略优化：用同一提示下一组回答的相对得分估计优势，不需要价值网络）。生成长度从 2K 提高到 8K。开放权重的旗舰 Qwen2.5-72B-Instruct 与约 5 倍大的 Llama-3-405B-Instruct 表现相当。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)中数据规模与配比一线、[强化学习方向](../../fields/posttraining/rl/README.md)与[偏好学习方向](../../fields/posttraining/preferences/README.md)中"DPO 之后接 GRPO"的开源报告。它的模型是 [Qwen2.5-1M](../qwen2.5-1m/README.md)、[s1](../arxiv-2501.19393/README.md)、[TOPS](../arxiv-2502.18080/README.md) 的底座。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2412.15115 · [全文 PDF](https://arxiv.org/pdf/2412.15115)
- 作者：Qwen Team（An Yang、Baosong Yang、Beichen Zhang、Binyuan Hui 等，阿里巴巴）
- 方向：llm/pretraining、llm/posttraining/sft、llm/posttraining/preferences、llm/posttraining/rl
