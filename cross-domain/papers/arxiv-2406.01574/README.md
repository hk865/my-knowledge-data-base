# MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.01574)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：MMLU 饱和：GPT-4 在 2023 年 3 月达到 86.4% 后，2024 年上半年的前沿模型都停在 86%–87%，GPT-4o 在 MATH 与 Chatbot Arena 上大幅提升却在 MMLU 上只多 1 个百分点；分数对提示与打分函数敏感。作者归因于三点：只有 3 个干扰项、可以走捷径；题目偏知识少推理；有不可答或错标的题（§1）。
- **核心方法**：14 个领域 12,000 多题；选项从 4 个扩到 10 个，加入大学难度的推理题，两轮复核（先专家验证，再用当时最强的 LLM 找可疑题、由标注员定向复核）。准确率比 MMLU 下降 16%–33%；24 种提示风格下的分数波动从 4%–5% 降到 2%；思维链（CoT）让 GPT-4o 提高 19%，而在 MMLU 上 CoT 反而有害；GPT-4o 72.6%。对 GPT-4o 的 120 个错例：推理错误 39%，缺领域知识 35%，计算错误 12%。自述局限：仍是选择题，测不到开放式生成；只测文本。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"从测量看"中"饱和之后加难"的代表：同一类知识题，增加选项与推理比例后，区分度与提示稳定性都改善了；也说明"选择题分数"受选项数和提示影响。前作 [MMLU](../arxiv-2009.03300/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2406.01574 · [全文 PDF](https://arxiv.org/pdf/2406.01574) · University of Waterloo、University of Toronto、CMU
- 发表：NeurIPS 2024 Datasets and Benchmarks（Spotlight）
- 方向：cross-domain/evaluation
