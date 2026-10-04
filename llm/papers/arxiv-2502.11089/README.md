# Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention

> 状态：技术精读 · 2025 · [原文](https://arxiv.org/abs/2502.11089) · [ACL 2025 正式版](https://aclanthology.org/2025.acl-long.1126/)

[返回大语言模型目录](../../README.md)

- **解决什么**：长上下文下标准注意力计算昂贵。已有的稀疏注意力多数只在推理时稀疏化，理论上的加速难以兑现，也不能端到端训练；事后稀疏化还会偏离预训练形成的注意力结构（作者引用的研究：top 20% 的注意力只覆盖约 70% 的注意力分数，检索头容易在推理时被剪掉）。
- **核心方法**：每个查询并行走三条分支，再用门控加权合并：压缩分支把连续的 KV 块压成一个粗粒度 token，读全局概况；选择分支借压缩分支的注意力分数挑出最重要的若干个 KV 块，读细节；滑动窗口分支读局部。块的选择在同一个 GQA 组（共享一份 KV 的一组查询头）内保持一致，以配合硬件的访存方式；整个机制从预训练开始就参与训练（选块这一步本身不可微，梯度经压缩分支和被选中的 KV 传回）。在 27B 总参数、3B 激活的 GQA+MoE 模型上用 8K 长度的文本预训练 270B token（实验设置一节的数字；引言写作 260B），LongBench（长文本理解评测集）平均 0.469，比全注意力高 0.032；64K 大海捞针所有位置都找回；64K 长度上前向、反向的内核分别比全注意力快 9.0、6.0 倍，解码按访存量估计快 11.6 倍。为了训练稳定，第一层的 MoE 换成 SwiGLU 形式的普通 MLP。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"注意力不丢失"与"更长更大的注意力"两节里"训练时就稀疏"一路的起点，后续依次是 DSA（[DeepSeek-V3.2](../arxiv-2512.02556/README.md)）、CSA/HCA（[DeepSeek-V4](../arxiv-2606.19348/README.md)）与 CSA2（[DeepSeek-V4.1-Flash](../arxiv-2609.19969/README.md)）。第一层换回 MLP 也是入门页"层的位置成为设计变量"的证据之一。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：三路读取的机制、64K 下读多少 KV 的手算，以及它的部件在 V3.2、V4、V4.1-Flash 中怎样被拆开重用
- [图解与说明](figures/README.md)
- [证据档案](evidence.json)与[原文版本与阅读记录](source.json)
- 下一篇：[DeepSeek-V3.2 精读](../arxiv-2512.02556/reading.md)（DSA 与本篇的逐项对照）

## 阅读顺序

[DeepSeek-V2 精读](../deepseek-v2/reading.md)（MLA：压缩每个位置的缓存）→ 本篇（压缩每次读取的位置数）→ [DeepSeek-V3.2 精读](../arxiv-2512.02556/reading.md)。

## 身份信息

- 稳定标识：arxiv:2502.11089 · [全文 PDF](https://arxiv.org/pdf/2502.11089) · DeepSeek-AI、北京大学、华盛顿大学
- 方向：llm/pretraining、llm/architecture、llm/long-context
