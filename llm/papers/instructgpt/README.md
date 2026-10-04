# Training language models to follow instructions with human feedback

> 状态：逐步教学版 · 2022 · [原文](https://arxiv.org/abs/2203.02155)

[返回大语言模型目录](../../README.md)

- **解决什么**：模型变大不等于更会遵循用户意图：大模型仍会编造、输出有害内容或答非所问。
- **核心方法**：在 GPT-3 上分三步：用标注者写的示范做 SFT（监督微调）；收集标注者对多个模型输出的排序，训练奖励模型（给回答打分、预测人更偏好哪个的模型）；以奖励模型为信号用 PPO（一种限制每步更新幅度的策略梯度算法）继续优化（加 KL 惩罚，PPO-ptx 版本再混入预训练数据的梯度）。在面向 API 提示分布的人类评估中，1.3B 的 InstructGPT 输出比 175B 的 GPT-3 更受偏好；真实性提高、有害输出减少，在公开 NLP 数据集上的退化很小。
- **为什么在这个库里**：后训练三个方向（[监督微调方向](../../fields/posttraining/sft/README.md)、[偏好学习方向](../../fields/posttraining/preferences/README.md)、[强化学习方向](../../fields/posttraining/rl/README.md)）的共同起点：今天"SFT → 偏好 → RL"的流程从这里分化。[DPO](../dpo/README.md) 简化了其中奖励模型加 PPO 的两步。优先级：必读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

[Language Models are Few-Shot Learners](../gpt3/README.md)（被对齐的底座）→ [Proximal Policy Optimization Algorithms](../ppo/README.md)（第三步用的算法）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2203.02155 · [全文 PDF](https://arxiv.org/pdf/2203.02155v1) · 教学版依据 v1
- 作者：Long Ouyang、Jeff Wu、Xu Jiang、Diogo Almeida、Carroll L. Wainwright 等 20 位（OpenAI）
- 方向：llm/posttraining/sft、llm/posttraining/preferences、llm/posttraining/rl
