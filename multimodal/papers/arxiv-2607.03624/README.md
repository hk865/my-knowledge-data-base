# RADIO1D: Elastic Representations for Condensed Vision Modeling

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.03624)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VLM 普遍把视觉特征当作固定的 2D 块网格送进语言模型，token 数由分辨率决定、相邻块冗余大；而 VLM 训练本身会改变视觉特征：作者测到 C-RADIOv4 经 VLM 微调后特征变得分散，相邻块的相关性（CKA 矩阵的非对角项）从 0.281 降到 0.035（§2.2）。
- **核心方法**：以 SigLIP2、DINOv3、SAM3 为教师做多教师蒸馏，加一个只在训练时使用的解码器，把图像压成长度可变的 1D token 序列；训练时随机截断长度（嵌套 dropout），让靠前的 token 承载全局信息，推理时由用户指定长度。接 9B Nemotron 语言模型、在 10 项 VLM benchmark 上的平均分：1 个 token 51.5，128 个 71.6，256 个 73.3；固定 256 个 token 的 C-RADIOv4-H 为 73.1（Table 1）。同样的 token 预算下，它胜过推理时合并或剪枝 token 的方法。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"读出接口 = 可变长 1D token"一行；[入门页](../../fields/visual-representation/README.md)主线第 8 个节点"VLM 训练会抹掉空间结构"的证据，与 [Perception Encoder](../arxiv-2504.13181/README.md)"最好的特征不在输出层"对照阅读。自述失败模式：OCR 类任务（DocVQA、InfoVQA、OCRBench）在 token 少于 128 个时急剧下降，DocVQA 从 256 个 token 的 93.2 跌到 1 个 token 的 51.1；作者声明受雇于 RADIO 的开发方 NVIDIA。模型已发布。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2607.03624 · [全文 PDF](https://arxiv.org/pdf/2607.03624) · NVIDIA · ICML 2026
- 方向：multimodal/visual-representation、multimodal/vlm
