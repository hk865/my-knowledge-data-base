# Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2006.16236)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自注意力的时间与显存随序列长度 N 平方增长，长序列训练很慢；此前的稀疏分解（Child 等 2019）与 Reformer 降低了训练复杂度，却不能加速自回归推理，Reformer 还要求 Q 与 K 相同，不能用于解码（§1–2）。
- **核心方法**：把 softmax 相似度换成两个特征映射的点积 φ(q)ᵀφ(k)（论文用 φ(x) = elu(x) + 1），利用矩阵乘法的结合律先算 Σφ(k)vᵀ，复杂度降到 O(N)；带因果 mask 的版本可以写成以矩阵为状态的 RNN，生成每个 token 只更新固定大小的状态（§3.2–3.4）。CIFAR-10 逐像素生成的吞吐是 softmax 注意力的 4462 倍，bits/dim 3.40 对 3.47（同样训练 7 天，线性模型多跑了约 3 倍 epoch）；WSJ 语音识别的音素错误率 8.08，好于 Reformer 的 9.33，但差于 softmax 的 5.12（Table 1–3）。
- **为什么在这个库里**：[递推状态谱系](../../../foundations/relations/recurrent-state.md)第 5 节"线性注意力"节点，也是[架构与效率方向](../../fields/architecture/README.md)"线性注意力与状态空间"一线的起点。实验只覆盖图像生成和语音，没有做语言建模；站在现在看，固定大小的状态在"从上下文里精确找回某个 token"上吃亏，[Based](../arxiv-2402.18668/README.md) 与 [Repeat After Me](../arxiv-2402.01032/README.md) 量化了这个缺口，[Kimi Linear](../arxiv-2510.26692/README.md) 用逐通道的遗忘门并保留四分之一的全注意力层来弥补。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2006.16236 · [全文 PDF](https://arxiv.org/pdf/2006.16236) · ICML 2020 · Idiap Research Institute、EPFL（另有 University of Washington、University of Geneva 作者）
- 方向：llm/architecture
