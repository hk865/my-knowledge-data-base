# InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2504.10479)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：主流 MLLM 由纯文本 LLM 经多段流程"事后"改造而来，要靠专门数据和复杂的冻结、多段微调日程才保住语言能力，带来对齐难题和资源开销。
- **核心方法**：原生多模态预训练：把语言预训练与多模态对齐合成一个阶段，在大规模纯文本与多模态数据上用同一个自回归目标训练所有层（为省算力仍从预训练好的 LLM 基座与 InternViT 初始化）。结构沿用 ViT–MLP–LLM 与 448 切块，视觉 token 用更小的位置增量（V2PE）以容纳长上下文；后训练为 SFT 加混合偏好优化 MPO，配合测试时扩展。消融：InternVL2-8B 用原生预训练替换 MLP 预热后，与完整多段训练的基线表现相当；MPO 让 78B 与 38B 的七项推理均分各高 4.1、4.5。InternVL3-78B 的 MMMU 72.2%。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 7 个节点与开放问题"后接会被原生多模态取代吗"的入口；注意它的"原生"指训练日程，不是 [Chameleon](../arxiv-2405.09818/README.md) 式早融合。自述在 MMHal 等个别幻觉 benchmark 上略降。承诺公开训练数据。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2504.10479（Jinguo Zhu 等 51 位作者；当前 v3，2025-04）· [全文 PDF](https://arxiv.org/pdf/2504.10479v3) · 上海人工智能实验室 OpenGVLab 等
- 方向：[视觉语言模型](../../fields/vlm/README.md)
