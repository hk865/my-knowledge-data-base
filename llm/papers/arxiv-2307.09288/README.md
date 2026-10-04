# Llama 2: Open Foundation and Fine-Tuned Chat Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2307.09288)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开放权重的对话模型怎样做到接近闭源产品的帮助性与安全性，并公开微调方法。
- **核心方法**：SFT 只用 27,540 条供应商标注的高质量数据（放弃数百万条第三方数据后效果明显变好）；分别训练帮助性与安全性两个奖励模型，因为两者此消彼长、一个模型难以兼顾；RLHF 前几轮只用拒绝采样微调（rejection sampling，一句话：每个提示采 K 个回答，取奖励最高的拿来做 SFT），V4 起在拒绝采样之后再接 PPO；每轮都用最新模型收集新偏好数据，因为奖励模型在新的输出分布上准确率会很快下降。作者记录的坑：只从上一轮样本中挑答案的 RLHF V3 在写押韵诗上退化；加强安全后对看似敏感、实则无害的提示过度拒绝；SFT 的上限是最好的标注员，作者认为模型写作超过标注员要归功于 RLHF（§5.1）。
- **为什么在这个库里**：[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)中"奖励模型 + 拒绝采样 + PPO"的开放实现，也是 [SFT 方向](../../fields/posttraining/sft/BASELINES.md)"少而精"的工业证据；与 Llama 3 改用 DPO 对照着读。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2307.09288 · [全文 PDF](https://arxiv.org/pdf/2307.09288) · Meta（GenAI）
- 方向：llm/posttraining/sft、llm/posttraining/preferences、llm/posttraining/rl
