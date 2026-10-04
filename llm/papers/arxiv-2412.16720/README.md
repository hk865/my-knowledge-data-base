# OpenAI o1 System Card

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.16720)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：说明 o1 系列模型的训练方式与安全评估。
- **核心方法**：官方材料只写明：o1 用大规模强化学习训练，在回答前生成长思维链，通过训练学会改进思考过程、尝试不同策略、认识自己的错误；安全上用审议式对齐（deliberative alignment，一句话：让模型在思维链里推理安全规范再作答）。思维链欺骗监测中 0.17% 的回答被标为"欺骗性"，作者提到这类行为可能来自 RLHF 对齐阶段的奖励黑客。训练算法、奖励来源和数据都没有公开。
- **为什么在这个库里**：2024 年 o1 把"推理时多想"带成主线，开源团队（DeepSeek-R1、Kimi k1.5、DAPO）都以它为对照；[RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)中只作为闭源参照，本库只引用官方写明的部分。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2412.16720 · [全文 PDF](https://arxiv.org/pdf/2412.16720) · OpenAI · 官方系统卡
- 方向：llm/posttraining/rl
