# CoCa: Contrastive Captioners are Image-Text Foundation Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2205.01917)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：单编码器分类模型不懂自由语言，双塔对比模型做不了 VQA 这类联合理解，编码器–解码器生成模型又没有与图像对齐的文本向量、不便于检索。
- **核心方法**：在 CLIP 式对比目标上加描述生成：文本解码器前半不看图，输出的句子向量与图像向量做对比；后半用交叉注意力看图，逐词生成描述；JFT-3B 的类名与 ALIGN 的 alt-text 都当作文字。小规模消融中只用对比时零样本 ImageNet 70.7%、VQA 59.2%，两个目标一起为 71.6%、69.0%，成本只多 18%；完整模型零样本 ImageNet 86.3%。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md) Baseline 表"训练目标：对比加描述生成"一格；它实现了 [CLIP](../clip/README.md) §6 建议的"联合训练对比与生成目标"，SigLIP 2 的描述损失延续这一思路。论文未声明发布。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2205.01917 · [全文 PDF](https://arxiv.org/pdf/2205.01917) · Google Research
- 方向：multimodal/alignment、multimodal/vlm
