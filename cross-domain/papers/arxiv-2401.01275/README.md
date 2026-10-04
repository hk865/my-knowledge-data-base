# CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2401.01275)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：角色扮演对话智能体缺少综合评测；已有数据集或由 LLM 生成，或抽取噪声大，评测结果不可靠。
- **核心方法**：从中文小说与剧本中，先用 GPT-4 抽取对话场景，再经人工筛选，得到 1,785 段多轮对话、77 个主要角色，并配上百度百科的人物资料。13 项指标分四个维度：对话能力（流畅、连贯、一致）、角色一致性（知识暴露、知识准确、知识幻觉、行为与话语一致）、角色吸引力（拟人、沟通技巧、表达多样、共情）、性格回测（让模型以角色身份做 MBTI 问卷，与收集到的角色 MBTI 比对）。12 位标注员对主观指标按 5 分制打分，作者据此训练奖励模型 CharacterRM，它与人工评分的总体 Pearson 相关为 0.631，GPT-4 作裁判（1–3 个示例）只有 0.36–0.39。结论之一：在中文角色扮演上，GPT 系列并不占优，部分中文模型更好。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"角色扮演"一节：主观领域里通用强模型当裁判并不可靠，作者改用人类标注训练的专用奖励模型，评测器与奖励模型在这里是同一个东西。与 [PersonaEval](../arxiv-2508.10014/README.md)（裁判模型能否认出谁在说话）、[推理不一定提升角色扮演](../../../llm/papers/url-https-aclanthology.org-2025.findings-acl.537/README.md) 一起读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2401.01275 · [全文 PDF](https://arxiv.org/pdf/2401.01275) · 中国人民大学高瓴人工智能学院、北京邮电大学
- 发表：arXiv v2；正式发表信息未核实
- 方向：cross-domain/evaluation、llm/posttraining/preferences
