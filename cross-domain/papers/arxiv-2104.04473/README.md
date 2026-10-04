# Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2104.04473)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大模型的参数连一台多 GPU 服务器都放不下，单卡训练时间又不现实；张量并行与流水线并行的朴素用法在数千块 GPU 上扩展不好。
- **核心方法**：把张量并行（把一层的矩阵乘拆到多卡，每层都要通信）、流水线并行（按层切分，只在相邻阶段间传激活）与数据并行组合（PTD-P），并提出交错流水线调度。经验规则按带宽分层：张量并行只在一台服务器的 GPU 数以内使用（机内 NVLink），跨服务器用流水线并行（机间 InfiniBand 较慢）。在 3072 块 A100 上以 502 petaFLOP/s 训练万亿参数的 GPT，每卡达到理论峰值的 52%。
- **为什么在这个库里**：[观点：深度学习的规模化](../../../perspectives/scaling.md)中“通信成为瓶颈后，并行方式按带宽分层”的直接证据；[分布式训练讲义](../../../foundations/lessons/05a-distributed-training.md)的延伸阅读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2104.04473 · [全文 PDF](https://arxiv.org/pdf/2104.04473)
- 方向：cross-domain/training-science
