# Perception Encoder: The best visual embeddings are not at the output of the network

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2504.13181)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视觉编码器的预训练目标各有偏向：图文对比适合零样本分类与检索，描述生成适合接语言模型，空间自监督适合检测这类定位任务；把几种目标组合起来越来越复杂、难以扩展。能否用一种简单、可扩展的目标得到对所有下游都好的特征？
- **核心方法**：先把纯图文对比的配方做强（渐进分辨率、LAMB 优化器、更大批量、RoPE、注意力池化、数据增强、遮蔽正则等），在 54 亿对公开图文上训练 2B 参数的 PEcore，再用自建的视频数据引擎生成视频描述做微调。逐层冻结特征分析发现：这个对比模型的中间层已有与 AIMv2（描述生成训练）的语言类任务、DINOv2 的空间类任务相当的特征，但越靠近输出层越差，经语言模型做的视觉定位在最后一层表现极差；作者称之为对齐问题。据此做两种对齐：PElang 取第 47 层（共 50 层）接语言模型继续训练；PEspatial 让最后一层向自己的第 41 层特征以及 SAM 2.1 的掩码对齐。零样本 ImageNet 鲁棒性平均 86.6、Kinetics-400 76.9；配 8B 语言模型 DocVQA 94.6；COCO 检测 66.0 box mAP。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"读出接口 = 中间层加对齐微调"一行。标题本身就是对 [LLaVA](../llava/README.md) 取倒数第二层这一做法的系统解释（[CLIP 精读](../clip/reading.md)"局限与后续"第 4 条），也是"图文对比能否兼顾密集任务"的正面证据；文字类任务上它强于 [DINOv3](../arxiv-2508.10104/README.md)，ImageNet 线性评测两者相近。代码、模型与视频数据集均已发布。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2504.13181 · [全文 PDF](https://arxiv.org/pdf/2504.13181) · Meta FAIR（另有 UT Austin、MBZUAI、复旦大学、Meta Reality Labs 作者）
- 方向：multimodal/visual-representation、multimodal/alignment
