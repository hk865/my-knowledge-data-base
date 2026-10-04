# RoFormer: Enhanced Transformer with Rotary Position Embedding

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2104.09864)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自注意力本身不区分位置（打乱 token 顺序，注意力分数不变），需要一种把位置写进 Q、K 匹配里的编码；原文认为已有的绝对、相对位置编码各有不足。
- **核心方法**：RoPE（旋转位置编码）：把 Q、K 的每两维看成一个平面向量，按 token 的绝对位置旋转一个角度，不同维度对用不同频率；旋转后 q·k 只依赖两个 token 的相对位置 m−n（§3.2.2），且随相对距离增大内积有长期衰减（§3.4.3），并能与线性注意力兼容（§3.3）。实验规模较小：WMT14 英德 27.5 BLEU（Transformer-base 27.3），中文长文本 CAIL2019-SCM 上 1024 长度的 RoFormer 为 69.79%（BERT-512 为 67.77%）。作者在 §4.5.5 写明说不清它为什么收敛更快、为什么长文本上更好。
- **为什么在这个库里**：[长上下文方向](../../fields/long-context/README.md)"位置"一环的起点：Llama 与 Qwen 系列的位置编码都是 RoPE，后来的 [PI](../arxiv-2306.15595/README.md)、[YaRN](../arxiv-2309.00071/README.md)、[ABF](../arxiv-2309.16039/README.md) 都在改它的频率或位置索引。机制见 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 8.3 节。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2104.09864 · [全文](https://arxiv.org/pdf/2104.09864) · 追一科技（Zhuiyi Technology）
- 方向：llm/long-context、llm/architecture
