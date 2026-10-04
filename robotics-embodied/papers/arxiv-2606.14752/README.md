# X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.14752)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：现有动作分词器（action tokenizer，一句话：把连续动作序列编码成离散 token 的模块）只为重建而离散化，码本保留了运动几何，却几乎不给 VLA 骨干提供语义监督。
- **核心方法**：相对只做压缩的 [FAST](../arxiv-2501.09747/README.md)，把分词器当作推理与控制之间的语义接口：编码器—语义残差量化（SRQ）—解码器结构中，残差向量量化（一句话：多级码本，每级量化上一级剩下的误差）的第一级用掩码动作建模训练成表达粗粒度运动意图的"动作语言"，更深的级保留细节；再用与预训练基础模型表征的对比对齐、下一帧视觉语言特征预测做语义对齐。在 240 万条轨迹上预训练后冻结，作为混合离散—连续 VLA 的表征监督；摘要报告多模态 grounding 比 FAST 高 13.5%、长时程任务高 8.25。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向"动作表示"一格：[RT-2](../arxiv-2307.15818/README.md)、[OpenVLA](../openvla/README.md) 的逐维分桶 → FAST 的 DCT 压缩 → 本篇带语义的分层量化。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2606.14752（Kang 等 13 位作者；当前 v2，2026-06）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2606.14752)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)
