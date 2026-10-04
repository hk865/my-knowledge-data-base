# Chameleon: Mixed-Modal Early-Fusion Foundation Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.09818)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多模态模型通常为各模态单独建编码器或解码器，限制了跨模态的信息整合，也难以按任意顺序生成图文交错的文档。
- **核心方法**：早融合：训练图像分词器把 512×512 的图量化成 1024 个离散 token（码本 8192），与文字共用 65,536 的词表，用同一个 Transformer 从零在约 10T token 的图文混合数据上训练（最大 34B）。共享全部权重时各模态"竞争"使范数缓慢增长，训练后期在 bf16 下发散（不做图像生成的消融不发散），靠 QK-Norm、调整层归一化位置与 dropout 稳定。34B 模型在描述与 VQA 上超过 Flamingo、IDEFICS，混合模态开放问答的人评中对 Gemini-Pro、GPT-4V 的偏好率为 60.4%、51.6%。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)"早融合"一支公开细节最完整的代表，也连接[视觉生成方向](../../fields/generation/README.md)中的自回归路线。自述图像分词器重建多文字图像很差，给重 OCR 任务设了上限；VQAv2 上 LLaVA-1.5 仍更高；人评提示来自众包，排除了 OCR 与信息图。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2405.09818（Chameleon Team；当前 v2，2025-03）· [全文 PDF](https://arxiv.org/pdf/2405.09818v2) · Meta（Chameleon Team）
- 方向：[视觉语言模型](../../fields/vlm/README.md)、[视觉生成](../../fields/generation/README.md)
