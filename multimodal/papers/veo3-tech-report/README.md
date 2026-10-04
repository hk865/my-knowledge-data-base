# Veo: a text-to-video generation system

> 状态：文献卡 · 2025 · [原文](https://storage.googleapis.com/deepmind-media/veo/Veo-3-Tech-Report.pdf)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Google DeepMind 的文本（及图像）到音视频生成系统，目标是高分辨率视频并同步生成音频。
- **核心方法**：潜空间扩散：视频与音频分别由自编码器压缩，基于 Transformer 的去噪网络在音频的时间潜变量和视频的时空潜变量上联合去噪；训练数据是图像、视频、音频及其标注，描述由多个 Gemini 模型按不同详细程度生成，并做安全、质量过滤与跨来源语义去重。相对 [Imagen Video](../arxiv-2210.02303/README.md) 的像素空间级联，主干与空间都换了。参数量与数据规模未公开。
- **为什么在这个库里**：[观点页：生成收敛](../../../perspectives/generative-convergence.md)阶段四表中 Google 一行的依据，报告少见地自述了"文字生成仍差、偏爱频繁切镜"等失败；同一模型被 Google DeepMind 用来测试视频模型的零样本视觉能力（arXiv 2509.20328），接到"从视频生成到世界模型"一节。优先级：选读。
