# Instruction-Following Evaluation for Large Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.07911)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：指令遵循能力的评测没有标准：人工评测贵、慢、难以复现；用 LLM 打分可能有偏，受评审模型能力限制（摘要、§1）。
- **核心方法**：只测"可验证指令"：能用程序客观检查是否遵守的约束，例如"写 400 词以上""关键词 AI 至少出现 3 次""全文用 JSON"。定义 25 类可验证指令，构造 541 条提示，每条含一个或多个指令；报告提示级与指令级的严格准确率，以及先去掉 Markdown 加粗、首行、末行等 8 种变换再判的宽松准确率（宽松版减少误判失败，但会引入误判通过）。GPT-4 提示级严格准确率 76.89%，PaLM 2 S 43.07%。作者承认几乎没有指令能 100% 客观验证，例如加粗后的结束语会被朴素字符串匹配判错。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"评测即目标"一节的核心例子：因为能用程序判分，它的 25 类约束被 [Tülu 3](../../../llm/papers/arxiv-2411.15124/README.md) 直接合成为训练数据与 RLVR 奖励；Tülu 3 随后自建约束不重叠的 IFEval-OOD，发现各模型 IFEval 80 分上下、IFEval-OOD 只有 20–30 分。[后训练](../../../llm/fields/posttraining/README.md)各页以它为指令遵循的主要指标。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2311.07911 · [全文 PDF](https://arxiv.org/pdf/2311.07911) · Google、Yale University
- 发表：arXiv 预印本（v1）
- 方向：cross-domain/evaluation、llm/posttraining/sft、llm/posttraining/rl
