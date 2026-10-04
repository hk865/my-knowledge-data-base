# LiveBench: A Challenging, Contamination-Limited LLM Benchmark

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.19314)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：测试集污染会让 benchmark 很快过时；用人或 LLM 出题、判分的众包评测又会引入偏差，并在难题上判不准（摘要、§1）。
- **核心方法**：同时满足三点：题目来自近期信息源并每月更新（新数学竞赛、arXiv 论文、新闻、Kaggle 数据集），全部有客观标准答案、不用 LLM 裁判，覆盖数学、代码、推理、语言、指令遵循、数据分析六类 18 个任务（包括 Big-Bench Hard、AMPS、IFEval 的加难版本）。新题延后一个月才公开，使公开榜单上始终约有 1/6 的题是私有的。顶尖模型低于 70%；与 Chatbot Arena、Arena-Hard 的相关为 0.91、0.88，GPT-4 系列在用 GPT-4 当裁判的 Arena-Hard 上明显更高。附录中让 GPT-4-Turbo 给 AMC、AIME、SMC 与 Zebra 谜题判对错，错判率 10%–46%。自述局限：只有英文；开放式写作这类任务无法定义标准答案；不同模型家族偏好不同的提示格式。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"滚动更新"路线的通用版（[LiveCodeBench](../arxiv-2403.07974/README.md) 只测代码），也给出了"LLM 裁判在难的数学推理上判不准"的直接数字，说明为什么推理 RL 坚持用规则验证器。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2406.19314 · [全文 PDF](https://arxiv.org/pdf/2406.19314) · Abacus.AI、NYU、NVIDIA、UMD、USC、Columbia
- 发表：ICLR 2025（Spotlight）
- 方向：cross-domain/evaluation
