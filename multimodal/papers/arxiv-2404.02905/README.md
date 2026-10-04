# Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.02905)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：把图像 token 展平成一维逐个预测有四个问题：VQ 特征本有双向依赖，却被强加单向假设；不能做"给下半张补上半张"这类要双向推理的任务；展平破坏空间邻近；n×n 个 token 要 n² 步。
- **核心方法**：多尺度 VQ 分词器把一张图编码成从 1×1 到全分辨率的一串 token 图，Transformer 按"下一个尺度"自回归，同一尺度内的 token 并行生成。ImageNet 256×256 类条件生成：自回归基线 FID 18.65 → VAR 1.73（2B 参数），Inception Score 80.4 → 350.2，推理快约 20 倍；作者称 DiT-XL/2 的生成耗时是它的 45 倍，并报告超过 L-DiT-3B/7B。测试损失与规模的线性相关系数接近 −0.998。作者自述：分词器沿用基线未改；还没有做文本到图像和视频，列为后续方向。代码与模型公开。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 9 个节点中自回归一侧的代表，[Baseline 页](../../fields/generation/BASELINES.md)部件 3"由粗到细的自回归"与部件 5 两格；它与 [DiT](../arxiv-2212.09748/README.md) 的比较是"自回归与扩散会不会合成一种生成方式"这一开放问题的入口。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2404.02905 · [全文 PDF](https://arxiv.org/pdf/2404.02905) · 北京大学、字节跳动
- 方向：multimodal/generation
