# DataComp: In search of the next generation of multimodal datasets

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2304.14108)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多模态数据集的设计很少被系统研究：许多数据集私有，公开数据集里数据源与过滤方式怎样影响模型并不清楚。
- **核心方法**：反转 benchmark 的惯例：固定 CLIP 训练代码、结构与算力，参赛者只改训练集，在 38 个零样本分类与检索任务上评分；提供 128 亿对的公开候选池和四个算力档。用 CLIP ViT-L/14 分数保留约 30% 并与 ImageNet 图像聚类过滤取交集，得到 DataComp-1B：ViT-L/14 看 130 亿样本，ImageNet 零样本 79.2%，比同条件的 OpenAI CLIP 高 3.7 个百分点；更小但筛得更严的数据集泛化更好。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 6 个节点、Baseline 表"数据：固定训练、只比数据"一格；它把"数据是主要杠杆"变成可比较的实验，也暴露了"以考题为锚做筛选"的风险（最好的过滤以 ImageNet 聚类为锚）。与 [MetaCLIP](../arxiv-2309.16671/README.md) 对照阅读。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2304.14108 · [全文 PDF](https://arxiv.org/pdf/2304.14108) · University of Washington、Columbia、Tel Aviv University、Apple、UT Austin、LAION、AI2 等 · NeurIPS 2023 数据集与 benchmark 赛道
- 方向：multimodal/alignment、cross-domain/evaluation
