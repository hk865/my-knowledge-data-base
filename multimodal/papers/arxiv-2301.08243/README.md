# Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2301.08243)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：不变性方法（对比学习、自蒸馏）靠人选的视图增强得到语义层次高的表征，但这些增强带来的偏置可能伤害某些下游任务，也难推广到其他模态；像素重建方法不需要增强，表征的语义层次却偏低，线性评测弱，要端到端微调才能发挥。
- **核心方法**：I-JEPA：从一张图中取一个大的上下文块，用一个预测器在表示空间里预测同一张图中几个目标块的表示，目标由参数取滑动平均的目标编码器给出；不重建像素，不做视图增强。关键设计是目标块要足够大（语义级），上下文块要足够分散。ViT-H/14 只用 ImageNet-1K、16 块 A100 不到 72 小时训完，线性评测 79.3%（MAE 的 ViT-H/14 为 77.2%）；448 分辨率的 ViT-H/16 为 81.1%，与用增强的 iBOT ViT-L（81.0%）相当。Clevr 上的线性探针，距离预测 72.4，远高于 DINO ViT-B/8 的 53.4，计数 86.7，低于 MAE 的 90.5。每次迭代比 MAE 慢约 7%，但收敛所需迭代约少 5 倍。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 表示空间预测"一行，JEPA 一支在图像上的起点；视频上的 [V-JEPA](../arxiv-2404.08471/README.md) 与机器人上的 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) 沿用同一目标。它把"不变性由人选的增强决定"写成引言里的问题，是 DINO 系的对照面（[DINO 精读](../dino/reading.md)"局限与后续"第 5 条），也把 MAE 微调依赖的原因归到像素目标上（[MAE 精读](../mae/reading.md)"局限与后续"第 1 条）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2301.08243 · [全文 PDF](https://arxiv.org/pdf/2301.08243) · Meta AI（FAIR）、McGill University、Mila、New York University · ICCV 2023
- 方向：multimodal/visual-representation
