# DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression

> 状态：技术精读 · 2026 · [原文](https://arxiv.org/abs/2609.19969)

[返回大语言模型目录](../../README.md)

- **解决什么**：长程智能体让模型的工作负载以输入为主：预填充（prefill，一次性处理整段输入）仍然昂贵，KV 缓存占满 HBM 与 SSD 的容量和传输带宽，成为进一步降低部署成本的主要瓶颈。
- **核心方法**：相对 DeepSeek-V4-Flash，主要改动有四处。结构改为因果编码器-解码器（CED，受 YOCO 启发）：20 层因果编码器接 20 层解码器，解码器的全局 KV 由编码器最后一层的隐藏状态投影得到，大部分提示 token 不必走完解码器，预填充时每 token 激活 8B 参数、解码时 16B。注意力改为 CSA2，在层间复用全局 KV 与索引，全局 KV 缓存用 FP4 存储，降到每 token 约 890 字节，约为 V4-Flash 的 1/4。接入 196B 参数的 [Engram](../arxiv-2601.07372/README.md) 查表记忆。骨干预训练去掉 MTP（多 token 预测）模块，改用单独训练的 DSpark 草稿器做投机解码。模型有 552B 骨干参数，在 45T token 的多模态语料上预训练；稀疏注意力在 64K 长度上从头训练，不再有稠密预热。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"更长更大的注意力"一节训练时稀疏一路当前的末端（[NSA](../arxiv-2502.11089/README.md) → [V3.2](../arxiv-2512.02556/README.md) → [V4](../arxiv-2606.19348/README.md) → 本篇），也是"知识能否从 FFN 里再拆出去"这一开放问题的证据：Engram 进入了正式发布的模型。它在结论中写明做不好的场景：新结构的鲁棒性边界尚未完全刻画，CSA2 的选择误差与 SWA 状态的近似重建可能在未测试的边界情形下损害能力。优先级：选读。精读把 890 字节拆成"每 token 2.5 条全局 KV × 每条 356 字节"，并列出原文只用文字交代、没有数值消融的几项压缩代价。

## 阅读入口

- [技术精读](reading.md)
- [证据档案](evidence.json)
- [原文版本与阅读记录](source.json)

## 阅读顺序

[DeepSeek-V4 精读](../arxiv-2606.19348/reading.md)（CSA/HCA 与三代 KV 字节对比）→ 本篇；Engram 的机制见 [Engram](../arxiv-2601.07372/README.md)。

## 身份信息

- 稳定标识：arxiv:2609.19969 · [全文 PDF](https://arxiv.org/pdf/2609.19969) · DeepSeek-AI · 摘要称模型检查点已在 Hugging Face 发布
- 方向：llm/pretraining、llm/architecture、llm/long-context
