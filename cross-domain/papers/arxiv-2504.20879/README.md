# The Leaderboard Illusion

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2504.20879)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Chatbot Arena 已成为排名生成式模型的事实标准，但作者认为它存在系统性问题，使比赛场地失衡（摘要、§1，引言以 Goodhart 定律开篇）。
- **核心方法**：综合 200 万场对战，审计 2024 年 1 月到 2025 年 4 月间 42 家提供方、243 个模型。发现：少数提供方可以在公开发布前私下测试多个变体、只公布最好的那个（Llama 4 发布前 Meta 测了 27 个私有变体）；这种"best-of-N 再公布"违背 Bradley–Terry 排名模型的无偏抽样假设，模拟中测 10 个变体可让最高分提高约 100 分；闭源模型被抽中对战的比例更高、被下架更少，Google 与 OpenAI 估计各拿到约 19.2% 与 20.4% 的对战数据，83 个开放权重模型合计约 29.7%；243 个公开模型中 205 个被静默下架。受控实验：微调数据中 Arena 数据占比从 0 提到 70%，在 ArenaHard 上对 Llama-3.1-8B-Instruct 的胜率从 23.5% 升到 49.9%（相对提升 112%），在其他任务上收益有限。自述局限：拿不到原始数据；只覆盖 2025 年 1–3 月的抓取快照；按模型自报身份归属私有变体；部分作者曾向 Arena 提交模型。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"排行榜动态"一节的主要证据：成对人评（[MT-Bench 与 Chatbot Arena 精读](../llm-judge/README.md)）在规模化、成为营销目标之后，出现了与静态 benchmark 不同的失效方式——不是题目泄漏，而是选择性公布与训练分布贴近。正文只用原文结论；Arena 方面的回应未核实。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2504.20879 · [全文 PDF](https://arxiv.org/pdf/2504.20879) · Cohere Labs、Cohere、Princeton、Stanford、Waterloo、MIT、AI2、UW
- 发表：arXiv 预印本（v2）
- 方向：cross-domain/evaluation、llm/posttraining/preferences
