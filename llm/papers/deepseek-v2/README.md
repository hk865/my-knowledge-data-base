# DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

> 状态：技术精读 · 2024 · [原文](https://arxiv.org/abs/2405.04434)

[返回大语言模型目录](../../README.md)

- **解决什么**：同时压低训练成本和推理成本：MoE（混合专家：每个 token 只激活部分前馈子网络）能减少每个 token 的计算，但长上下文生成时，每层、每头保存的 KV 缓存仍是显存与带宽瓶颈。
- **核心方法**：相对 DeepSeek 67B 稠密模型，注意力改用 MLA（多头潜在注意力：各头的 key/value 由一个 512 维潜向量恢复，推理时只缓存潜向量，并把携带 RoPE 位置信息的部分单独解耦），前馈层改用 DeepSeekMoE（细粒度专家加共享专家）。总参数 236B、每 token 激活 21B，预训练 8.1T token，支持 128K 上下文。与 DeepSeek 67B 相比，训练成本省 42.5%，KV 缓存减少 93.3%，最大生成吞吐提高到 5.76 倍。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"KV 缓存压缩"与"稀疏专家"两格的代表系统；上接 [DeepSeekMoE](../arxiv-2401.06066/README.md)，下接 [DeepSeek-V3](../arxiv-2412.19437/README.md)。精读把两种节省的来源拆开并做了手算。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)
- 关系页：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 7 节"MoE"节点（DeepSeekMoE 稀疏化 FFN，MLA 压缩 KV 缓存）

## 阅读顺序

[Attention Is All You Need](../transformer/README.md)（注意力与 KV 的来源）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2405.04434 · [全文 PDF](https://arxiv.org/pdf/2405.04434v5) · 精读依据 v5
- 作者：DeepSeek-AI
- 方向：llm/architecture、llm/pretraining、llm/posttraining/sft、llm/posttraining/rl
