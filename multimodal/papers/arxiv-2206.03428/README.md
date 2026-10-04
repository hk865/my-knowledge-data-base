# Revealing Single Frame Bias for Video-and-Language Learning

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2206.03428)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视频-语言模型直觉上需要多帧输入，但多帧是否真有好处、收益是否值得成倍增加的计算与显存，并不清楚。
- **核心方法**：训练时每段视频只随机取 1 帧（相当于图文模型），推理时把多帧特征拼接后一起送入跨模态编码器（早融合），并在大规模图文与视频文本数据上预训练。这个不看时间的模型在 MSRVTT、DiDeMo、ActivityNet Captions 检索和三个视频问答上达到或超过多帧方法；作者据此指出这些数据集存在"静态外观偏差"，并用 SSv2 的动作模板（例如"把[某物]抛起再接住"）另建两个检索任务：单帧模型在模板检索 R1 上比 4 帧的 Frozen 低 10.9，在 DiDeMo 上却高 16.4。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 6 步与"站在现在看过去"中"单帧就够"批评的代表；[LLaVA-Video](../arxiv-2410.02713/README.md) 的引言把它作为反面引用，用更动态的数据说明帧数确实重要。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2206.03428 · [全文 PDF](https://arxiv.org/pdf/2206.03428) · UNC Chapel Hill
- 方向：multimodal/video-temporal、multimodal/alignment
