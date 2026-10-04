# 多模态与世界表征

[回到全库](../README.md) · [基础概念](../foundations/README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文与资源](PAPERS.md)

## 按细分方向学习

六个方向按"图像怎样变成表示 → 怎样接上语言 → 怎样加上时间 → 怎样生成与预测世界"排列。每个方向有入门页、Baseline 页、路线图和论文列表。

| 方向 | 回答什么 | 入门页 |
|---|---|---|
| 视觉表征 | 什么是好的视觉表示，从手工特征、监督预训练到自监督与图文监督，怎样从任务、测量和内部三方面判断 | [入门](fields/visual-representation/README.md) |
| 图文对齐 | 图像和文字怎样进入同一个空间：对比学习、sigmoid 损失、数据筛选，以及组合关系、计数等做不好的地方 | [入门](fields/alignment/README.md) |
| 视觉语言模型（VLM） | 视觉编码器怎样接到 LLM 上并训练：连接器、分辨率、训练流水线，幻觉与"不看图也能答"的评测问题 | [入门](fields/vlm/README.md) |
| 视觉生成 | 扩散、自回归与流匹配三大家族怎样生成图像和视频，配方为什么走向同一套 | [入门](fields/generation/README.md) |
| 视频与时序表征 | 时间怎样进入表示：从双流、3D 卷积到视频 Transformer、视频 LLM，以及 benchmark 有没有测到时间 | [入门](fields/video-temporal/README.md) |
| 世界模型（多模态侧） | 世界模型本身怎么造：潜空间动力学、预测式表征、视频生成当模拟器，以及物理合理性怎样评测 | [入门](fields/world-models/README.md) |

机器人怎样使用世界模型见[机器人侧的世界模型](../robotics-embodied/fields/world-models/README.md)；VLM 作为 VLA 骨干见 [VLA](../robotics-embodied/fields/vla/README.md)；生成为什么走向同一套配方见观点页[生成的收敛](../perspectives/generative-convergence.md)。

## 单篇论文目录

本领域收录 98 项资源，其中 8 篇有讲解；其他方向的相关论文通过索引交叉引用。

- [浏览本领域论文与跨方向引用](PAPERS.md)
- [直接浏览单篇文件夹](papers/README.md)

每篇论文的文件夹含文献卡README与source.json；有讲解的论文另含reading.md。

## 阅读状态标记

- 技术精读：按指定论文版本写的完整讲解
- 逐步教学版：在技术精读基础上补充逐步说明与算例
- 选定章节讲解：只讲论文中明确列出的章节
- 文献卡：论文身份、官方原文入口与定位
