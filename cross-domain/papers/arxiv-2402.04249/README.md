# HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.04249)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自动红队（用算法生成越狱提示）各论文评测口径不一、无法比较，先前评测缺少广度、可比性与稳健的指标。
- **核心方法**：510 种有害行为，分为标准、版权、上下文（附带一段具体背景文本）、多模态四类；指标是攻击成功率（ASR），由微调的 Llama 2 13B 分类器判定，并统一目标模型的生成长度（作者发现生成 token 数能让 ASR 变化多达 30%，此前各论文不统一）。比较 18 种红队方法与 33 个目标模型和防御：没有一种攻击或防御普遍有效；在 6 个模型家族、7B 到 70B 的范围内，同一家族里鲁棒性与参数量无关，不同家族之间差别很大，作者据此认为训练流程与数据比规模更重要（版权类行为是例外）。另提出对抗训练方法 R2D2，Zephyr 7B + R2D2 在 GCG 类攻击上的 ASR 比次优的 Llama 2 13B 低 4 倍。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"安全对齐"一节中"越狱鲁棒性主要来自哪一段训练"的直接证据；生成长度改变 ASR 也是"评测口径决定结论"的例子。与测过度拒答的 [XSTest](../arxiv-2308.01263/README.md) 成对使用。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2402.04249 · [全文 PDF](https://arxiv.org/pdf/2402.04249) · UIUC、Center for AI Safety、CMU、UC Berkeley、Microsoft
- 发表：arXiv v2；正式发表信息未核实
- 方向：cross-domain/evaluation、llm/posttraining/preferences
