# Measuring Massive Multitask Language Understanding

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2009.03300)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：GLUE 发布约一年、SuperGLUE 发布约一年就被做到接近人类水平，作者认为这些 benchmark 测的是语言技能，没有测到模型在预训练中从网上读到的大量专业知识（§1）。
- **核心方法**：57 个学科（初等数学、美国历史、法律、医学等）的四选一考试题，共 15,908 题：每科 5 题作 few-shot 示例，验证集 1,540 题，测试集 14,079 题。只在 zero-shot 与 few-shot 下评测，故意不提供大训练集，假设知识来自预训练（§5"The Internet as a Training Set"）。GPT-3 175B few-shot 平均 43.9%，13B 及以下接近随机的 25%；UnifiedQA 48.9%；未经专门训练的众包工人 34.5%，作者估计专家水平约 89.8%。GPT-3 的平均置信度与实际准确率最多相差 24 个百分点，即不知道自己什么时候错。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"从任务看"中"预训练给了多少知识"一类评测的源头，也是主线历史的第一个节点；它的饱和（GPT-4 在 2023 年 3 月达到 86.4%，此后前沿模型停在 86%–87%，见 [MMLU-Pro](../arxiv-2406.01574/README.md)）引出 MMLU-Pro、[GPQA](../arxiv-2311.12022/README.md)、[HLE](../arxiv-2501.14249/README.md) 这条"加难"链。同一作者在 HLE 中再次测量校准误差。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2009.03300 · [全文 PDF](https://arxiv.org/pdf/2009.03300) · UC Berkeley、Columbia、UChicago、UIUC
- 发表：ICLR 2021
- 方向：cross-domain/evaluation、llm/pretraining
