# ShortGPT: Layers in Large Language Models are More Redundant Than You Expect

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.03853)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LLM 参数已到数十亿乃至万亿，部署代价高；作者观察到很多层的输入与输出高度相似，对网络功能贡献很小。
- **核心方法**：定义块影响度（Block Influence，BI：用一层输入与输出隐状态的相似度衡量该层的重要性，越相似越不重要），按 BI 直接删去冗余的整层。相对此前更复杂的剪枝方法，只做层删除；作者报告效果优于此前的 SOTA 剪枝方法，并能与量化（降低权重的数值精度）叠加。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)与[模型科学方向](../../../cross-domain/fields/model-science/README.md)共用：既是一种压缩方法，也是"LLM 的深度有多少被真正用到"这一问的观察证据。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2403.03853 · [全文 PDF](https://arxiv.org/pdf/2403.03853)
- 作者：Xin Men、Mingyu Xu、Qingyu Zhang、Bingning Wang、Hongyu Lin、Yaojie Lu、Xianpei Han、Weipeng Chen（百川智能、中科院软件所）
- 方向：llm/architecture、cross-domain/model-science
