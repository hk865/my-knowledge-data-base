# LIMA: Less Is More for Alignment

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2305.11206)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大模型对齐的两个阶段（预训练、指令微调与 RLHF）各自贡献多少。
- **核心方法**：只用 1,000 条精选的提示与回答（约 75 万 token）对 65B 的 LLaMa 做标准监督微调，不做 RLHF；人评中 43% 的情况下 LIMA 与 GPT-4 持平或更好，对 Bard 为 58%，对经过人类反馈训练的 DaVinci003 为 65%。作者据此提出表层对齐假说（Superficial Alignment Hypothesis，一句话：知识和能力几乎都在预训练中学到，对齐只教模型和用户交互时用哪一种格式）；消融显示只加数量、不加提示多样性时收益迅速递减。作者自述：精选样本费人力、难扩展；不如产品级模型稳健，一次不走运的采样或对抗性提示就可能给出弱回答（§7）。
- **为什么在这个库里**：后训练总览"与预训练的关系"一节最常被引用的证据，[SFT Baseline 表](../../fields/posttraining/sft/BASELINES.md)"数据规模 = 少而精"一格；它的结论来自人评的帮助性，要和 Gekhman 等（新知识与幻觉）、Flan-PaLM（推理数据）一起读。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2305.11206 · [全文 PDF](https://arxiv.org/pdf/2305.11206) · Meta AI、CMU、USC、特拉维夫大学
- 方向：llm/posttraining/sft
