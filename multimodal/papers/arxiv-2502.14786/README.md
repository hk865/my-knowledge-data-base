# SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2502.14786)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源的对比图文编码器大多贴近 CLIP 原配方，在定位和密集（逐块）特征上落后，也没有把已有的改进合进一个模型；而它们正被大量用作 VLM 的视觉塔。
- **核心方法**：在 [SigLIP](../arxiv-2303.15343/README.md) 的 sigmoid 损失上加带解码器的描述、密集描述与指代表达预测（LocCa），训练最后 20% 加自蒸馏与遮蔽预测，小模型再用主动数据筛选蒸馏；数据 90% 英文、10% 非英文并做去偏过滤；另有保留长宽比、可变序列长度的 NaFlex 变体。So400m/14 在 384 像素下 ImageNet 零样本 83.2%→84.1%，36 种语言的 XM3600 图到文 R@1 26.6%→57.5%，并按 PaliGemma 2 式配方作为 VLM 视觉塔评测。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md)主线第 7 个节点，对齐编码器交给 [VLM](../../fields/vlm/README.md) 的接口；它把描述生成、自监督与数据筛选合并，是对 CLIP 式模型定位、密集特征和多语言短板的直接回应。自述 NaFlex 外推不好，不同收入与地区之间的差距几乎没缩小。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2502.14786 · [全文 PDF](https://arxiv.org/pdf/2502.14786) · Google DeepMind
- 方向：multimodal/alignment、multimodal/vlm、multimodal/visual-representation
