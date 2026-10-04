# Cosmos World Foundation Model Platform for Physical AI

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.03575)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：物理 AI（带传感器和执行器的系统）缺少"观测与动作交错"的大规模数据，在真实世界里试错又危险；需要一个可以安全交互的世界数字孪生。
- **核心方法**：先用视频生成的方法做一个通用的预训练世界模型（同时提供基于连续潜变量的扩散 Transformer 和基于离散 token 的自回归 Transformer），再用特定环境的数据后训练成专用世界模型；配套视频筛选流水线与视频分词器，权重以宽松许可开放。
- **为什么在这个库里**：[观点页：生成收敛](../../../perspectives/generative-convergence.md)"从视频生成到世界模型"一节的开源证据：世界模型直接建在视频生成之上；它的物理对齐实验（更大不等于更符合物理）是"像素逼真能否换来物理正确"这一开放问题的关键反例。与 [世界模型方向](../../fields/world-models/README.md)相连。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2501.03575 · [全文 PDF](https://arxiv.org/pdf/2501.03575) · NVIDIA · 开放权重
- 方向：multimodal/world-models、multimodal/generation
