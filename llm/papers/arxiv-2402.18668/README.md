# Simple linear attention language models balance the recall-throughput tradeoff

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.18668)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：注意力擅长召回（生成时准确用上前文出现过的 token），代价是随长度增长的 KV 缓存；H3、Mamba、RWKV 这类推理时状态大小固定的架构在困惑度上追平了注意力，召回却明显落后：在信息抽取与阅读问答这类召回密集的任务上，注意力比 Mamba 高 32.2 个百分点（§1、Table 1）。
- **核心方法**：先在合成的多查询联想召回任务（MQAR：先给出若干键值对，再按键提问）上测出，召回准确率随推理时状态大小单调上升，并证明任何递推模型要解 MQAR 都需要随序列长度线性增长的状态（Theorem 3.1）。据此提出 Based：用泰勒展开近似 softmax 的线性注意力负责长程，用 64–128 宽的小滑动窗口 softmax 注意力负责精确的局部比较，调节特征维度和窗口宽度即可沿召回–内存曲线移动。1.3B 参数、50B token 上，召回密集任务平均比 Mamba 高 10.36 个百分点；配合 IO 感知的内核，生成吞吐是 FlashAttention-2 的 24 倍（§6）。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)"线性注意力的召回问题"的核心证据：用一个合成任务和一条下界讲清"固定状态能装多少"。后来的混合架构（[Jamba](../arxiv-2403.19887/README.md)、[Kimi Linear](../arxiv-2510.26692/README.md)）都保留一部分精确注意力，与它的结论一致。前作是[线性注意力](../arxiv-2006.16236/README.md)，同类证据见 [Repeat After Me](../arxiv-2402.01032/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2402.18668 · [全文 PDF](https://arxiv.org/pdf/2402.18668) · Stanford University（另有 University at Buffalo 作者） · arXiv v2 页脚标注 ICML 2024 Efficient Systems for Foundation Models 研讨会
- 方向：llm/architecture
