# Zephyr: Direct Distillation of LM Alignment

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.16944)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：小模型经蒸馏 SFT 后任务准确率提高，但不能很好地回应自然提示，即没有对齐。
- **核心方法**：以 Mistral-7B 为底座，先用大模型生成的对话做蒸馏 SFT，再用教师模型（GPT-4）给多个回答打分得到的 AI 偏好数据（UltraFeedback）做蒸馏 DPO；不需人工标注，训练中也不需采样，几个小时即可完成；Zephyr-7B 在 MT-Bench 上超过 Llama2-Chat-70B。作者记录：DPO 训练一个 epoch 后训练集准确率就到 100%（强烈过拟合），却没有损害 MT-Bench 与 AlpacaEval；但 SFT 超过一个 epoch 时，DPO 训练越久越退化。作者自述的主要局限是用 GPT-4 当评委，它偏向从自己蒸馏出的模型和冗长但可能错误的回答；数学与代码远弱于闭源模型（§6）。
- **为什么在这个库里**：[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)"偏好来源 = AI + 离线 DPO"一格的开源代表，2023 年社区对齐配方的样板。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2310.16944 · [全文 PDF](https://arxiv.org/pdf/2310.16944) · Hugging Face（H4 团队）
- 方向：llm/posttraining/preferences、llm/posttraining/sft
