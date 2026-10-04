# Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.13271)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大模型借助思维链先推出"解题计划"再写代码，小模型做不到，代码生成能力落后；而出于部署成本和数据安全，很多团队只能部署小模型。
- **核心方法**：相对只用代码答案做常规微调，提出 CodePLAN，把大模型的推理能力蒸馏给小模型：多任务学习，同时训练代码生成与解题计划生成；用反向推理和计划采样保证计划质量。在 APPS 上，小模型的 pass@1（只生成一次即通过测试的题目比例）比常规微调提高 130% 以上。
- **为什么在这个库里**：[监督微调方向](../../fields/posttraining/sft/README.md)中"用大模型的推理轨迹监督小模型"的早期代码例子，也属于[知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)。[DeepSeek-R1](../arxiv-2501.12948/README.md) 后来把推理蒸馏用到长思维链上。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2403.13271 · [全文 PDF](https://arxiv.org/pdf/2403.13271) · LREC-COLING 2024
- 作者：Zhihong Sun、Chen Lyu、Bolun Li、Yao Wan、Hongyu Zhang、Ge Li、Zhi Jin（山东师范大学、华中科技大学、重庆大学、北京大学）
- 方向：llm/posttraining/sft、cross-domain/knowledge-distillation、llm/inference
