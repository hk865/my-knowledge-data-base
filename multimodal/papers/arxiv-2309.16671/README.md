# Demystifying CLIP Data

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.16671)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CLIP 成功的主因是数据，但 CLIP 只用一段话描述数据整理；LAION 等用 CLIP 模型做黑盒过滤来复现，等于在蒸馏 WIT 的信息。
- **核心方法**：重建 CLIP 的 50 万个元数据条目（WordNet 同义词集、维基高频词、高互信息二元组、维基条目名），用子串匹配建倒排索引，再按每个条目最多 t = 2 万对平衡：头部条目被截断，尾部全部保留；全程不用任何模型过滤。固定结构与训练步数只比数据，ViT-B/16 在 4 亿对上 ImageNet 零样本 70.8%，高于 CLIP 的 68.3%；只匹配不平衡明显更差；25 亿对时 ViT-L 79.2%、ViT-bigG 82.1%。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md) Baseline 表"数据：元数据加平衡"一格；它代表 Meta 的选择（透明、不依赖过滤模型），与 [DataComp](../arxiv-2304.14108/README.md) 的模型打分过滤形成对照。它统计到 50 万个条目中 11.4 万个无匹配，是长尾概念缺数据的直接证据。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2309.16671 · [全文 PDF](https://arxiv.org/pdf/2309.16671) · FAIR, Meta AI；New York University；University of Washington
- 方向：multimodal/alignment
