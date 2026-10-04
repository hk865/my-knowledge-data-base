# TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2304.01433)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大语言模型把 Google 的 ML 超级计算机从 256 块 TPU v2 推到 4096 块 TPU v4，规模、可靠性和互连拓扑成为障碍；推荐模型的嵌入查表又带来 all-to-all 通信，它比反向传播中的 all-reduce 更吃网络的二分带宽。
- **核心方法**：用光路交换机（OCS）动态重配片间互连，组成 4096 芯片的 3D 环面（可选扭曲环面）；每块芯片加入加速嵌入查表的 SparseCore；工艺从 TPU v3 的 16 nm 换到 7 nm。相对 TPU v3，性能 2.1 倍、每瓦性能 2.7 倍，作者写明每瓦提升中约 40% 来自工艺、其余来自设计。PaLM 540B 在 TPU v4 上 50 天持续达到峰值浮点性能的 57.8%。
- **为什么在这个库里**：[观点：深度学习的规模化](../../../perspectives/scaling.md)中算力线“通信”一步的证据，也是“工艺与设计各贡献多少”的少数直接拆分。原文还写明 TPU v3 固定的 2D 拓扑阻碍了大语言模型需要的模型切分（§7）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2304.01433 · [全文 PDF](https://arxiv.org/pdf/2304.01433)
- 方向：cross-domain/training-science
