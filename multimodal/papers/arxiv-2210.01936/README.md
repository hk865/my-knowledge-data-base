# When and why vision-language models behave like bags-of-words, and what to do about it?

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2210.01936)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：不清楚视觉–语言模型能否编码物体、属性与关系的组合；已有组合性考题规模小、手工构造，而常用的大规模检索评测也没有暴露这一缺陷。
- **核心方法**：提出 ARO（5 万多题，覆盖 Visual Genome 属性、关系与 COCO、Flickr30k 词序），发现模型像词袋；把检索集的词序或图块顺序打乱后成绩几乎不掉，说明检索既作为评测、也作为训练目标时都不需要组合信息。补救是 NegCLIP：在对比训练的批里加入打乱词序的句子和最近邻图片作难负样本，COCO 词序题从 46% 升到 86%、VG 关系从 63% 升到 81%，下游分类与检索基本不掉。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 4 个节点与 Baseline 表"训练目标：难负样本"一格；它给出"对比目标为什么学不到组合"的机制解释。注意 [SugarCrepe](../arxiv-2306.14610/README.md) 指出它的规则负样本可被不看图的模型识破、NegCLIP 的提升被高估。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2210.01936 · [全文 PDF](https://arxiv.org/pdf/2210.01936) · Stanford University · ICLR 2023
- 方向：multimodal/alignment
