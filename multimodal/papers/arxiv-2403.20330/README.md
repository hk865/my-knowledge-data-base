# Are We on the Right Way for Evaluating Large Vision-Language Models?

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.20330)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：现有多模态 benchmark 有两个问题：许多题不必看图，答案在题干里或靠 LLM 的世界知识即可答出；LLM 与 LVLM 训练中有无意的数据泄漏，模型不看图也能答出必须看图的题。
- **核心方法**：用 25 个 LLM 和 22 个 LVLM 在 6 个 benchmark 上做不看图测试：ScienceQA 超过 50%、MMMU 约 20% 的题被多数 LLM 直接答对，GeminiPro 不看图 MMMU 42.9%；Sphinx-X-MoE 不看图 MMMU 43.6%，比它的 LLM 底座高 17.9 个百分点。用 8 个 LLM 自动初筛（超过 2 个能答对的题剔除）、16 个 LVLM 分难度、再人工审核，得到 1500 道必须看图的题，覆盖 6 种核心能力、18 个细项，并提出多模态增益 MG 与泄漏 ML 两个指标。最好的高分辨率 GPT-4V 只有 57.1%。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 6 个节点与"用什么衡量进展"中盲答与泄漏的主要证据；与 [Cambrian-1](../arxiv-2406.16860/README.md) 的开图/关图对照互相印证。自述计划扩成在线测试集以防泄漏。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2403.20330（Lin Chen 等 11 位作者；当前 v2，2024-04）· [全文 PDF](https://arxiv.org/pdf/2403.20330v2) · 中国科学技术大学、香港中文大学、上海人工智能实验室
- 方向：[视觉语言模型](../../fields/vlm/README.md)
