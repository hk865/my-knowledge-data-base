# s1: Simple test-time scaling

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.19393)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：OpenAI o1 展示了测试时扩展（推理时多花计算换更好结果），但没有公开方法；本篇寻找达到测试时扩展和强推理表现的最简做法。
- **核心方法**：只用 1000 条带推理轨迹的问题（s1K，按难度、多样性、质量三条标准筛选，三条都做了消融）对 Qwen2.5-32B-Instruct 做 SFT（监督微调）；推理时用预算强制控制思考长度：要提前结束就强行截断，要延长就在模型想结束时追加 "Wait"，模型常因此复查并修正答案。s1-32B 在竞赛数学（MATH、AIME24）上比 o1-preview 最多高 27%；用预算强制继续加长思考，AIME24 从 50% 升到 57%。
- **为什么在这个库里**：[监督微调方向](../../fields/posttraining/sft/README.md)"少量高质量推理数据够不够"和[推理时计算方向](../../fields/inference/README.md)"思考长度能否控制"两问的最小基线；与 [DeepSeek-R1](../arxiv-2501.12948/README.md) 的大规模 RL 路线对照。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2501.19393 · [全文 PDF](https://arxiv.org/pdf/2501.19393) · 模型、数据与代码公开
- 作者：Niklas Muennighoff、Zitong Yang、Weijia Shi、Xiang Lisa Li、Li Fei-Fei、Hannaneh Hajishirzi、Luke Zettlemoyer、Percy Liang、Emmanuel Candès、Tatsunori Hashimoto（斯坦福、华盛顿大学、AI2、Contextual AI）
- 方向：llm/posttraining/sft、llm/inference
