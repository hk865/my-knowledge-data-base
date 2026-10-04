# LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.07974)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：HumanEval、MBPP 等代码评测只测自然语言到代码，并且可能已被训练数据污染或被过拟合（摘要、§1）。
- **核心方法**：持续从 LeetCode、AtCoder、Codeforces 的周赛收集新题并标注发布日期，评测时只用模型训练截止日期之后发布的题；除代码生成外还测自我修复、代码执行、测试输出预测。初版收录 2023 年 5 月到 2024 年 5 月的 500 多题，评测 18 个基座与 34 个指令模型。DeepSeek-Instruct 与 GPT-4o 在各自截止日期之后发布的 LeetCode 题上表现明显下降，作者据此认为它们训练过较早的题；在 HumanEval 上强、在 LiveCodeBench 上弱的主要是微调过的开放模型，可能过拟合了 HumanEval。自述局限：按截止日期切分后题量少（代码生成只剩 349 题，估计 1%–1.5% 的波动），越新的模型可用题越少，计划补充不公开的私有测试集；只测 Python。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"滚动更新、按时间切分"路线的代表，DeepSeek-R1、Qwen3 等推理模型报告都用它（见 [RL 方向](../../../llm/fields/posttraining/rl/README.md)）；"截止日期前后的落差"本身就是一种污染检测方法。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2403.07974 · [全文 PDF](https://arxiv.org/pdf/2403.07974) · UC Berkeley、MIT、Cornell
- 发表：arXiv 预印本（v2）
- 方向：cross-domain/evaluation
