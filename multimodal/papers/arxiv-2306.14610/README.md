# SugarCrepe: Fixing Hackable Benchmarks for Vision-Language Compositionality

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2306.14610)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Winoground、ARO、CREPE 等组合性考题里，规则生成的负样本句子常常不通顺、不合常理，存在可被利用的偏差。
- **核心方法**：先证明这些考题能被"盲模型"刷分：只看句子是否合理（Vera）或是否通顺（语法模型）、完全不看图，就能胜过最好的 CLIP；再用 ChatGPT 生成通顺、合理的负样本，并通过对抗式筛选去掉剩余偏差，构成 SugarCrepe。在它上面重新评估，发现 NegCLIP 这类"批内加组合难负样本"的方法的提升被大幅高估。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 4 个节点的"做不好"部分：评测考题本身也会被刷分。它修正了 [ARO](../arxiv-2210.01936/README.md) 的结论，提醒读者组合性提升要在去偏后的考题上确认。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2306.14610 · [全文 PDF](https://arxiv.org/pdf/2306.14610) · University of Washington、Allen Institute for AI
- 方向：multimodal/alignment、cross-domain/evaluation
