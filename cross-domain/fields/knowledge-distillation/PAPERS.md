# 知识蒸馏：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

以下每项链接到唯一的单篇目录。跨方向出现是交叉引用，不重复计算资源。

- [Model Compression](../../papers/url-cornell-compression.kdd06/README.md) · 2006 · 文献卡，暂无独立精读
- [Do Deep Nets Really Need to be Deep?](../../papers/arxiv-1312.6184/README.md) · 2013 · 文献卡，暂无独立精读
- [FitNets: Hints for Thin Deep Nets](../../papers/arxiv-1412.6550/README.md) · 2014 · 文献卡，暂无独立精读
- [Distilling the Knowledge in a Neural Network](../../papers/arxiv-1503.02531/README.md) · 2015 · 文献卡，暂无独立精读

## 跨方向引用（语言模型中的蒸馏）

- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](../../../llm/papers/arxiv-1910.01108/README.md) · 2019 · 文献卡 · 预训练阶段的软标签加隐藏层对齐，层数减半
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](../../../llm/papers/arxiv-2002.10957/README.md) · 2020 · 文献卡 · 只蒸馏最后一层的自注意力分布与值关系
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](../../../llm/papers/arxiv-2403.13271/README.md) · 2024 · 文献卡 · 把大模型的推理过程作为小模型的训练数据
- 后训练里的 on-policy 蒸馏与多教师合并（Qwen3、DeepSeek-V4、Kimi K3）见[后训练总览](../../../llm/fields/posttraining/README.md)。
