# GraphCodeBERT: Pre-training Code Representations with Data Flow

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2009.08366)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有的代码预训练模型把代码当作 token 序列，忽略了代码本身的结构，而结构携带关键的语义。
- **核心方法**：以 CodeBERT（Feng 等 2020，在代码与自然语言上做掩码语言建模的模型）的参数初始化，在输入中加入数据流（变量之间"值从哪里来"的语义关系，比抽象语法树层次浅），用图引导的掩码注意力把数据流的边编码进 Transformer。预训练任务在掩码语言建模之外新增两项：预测数据流的边，对齐代码 token 与数据流节点的表示。在代码搜索、克隆检测、代码翻译、代码修复四项任务上评测。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)里"把领域结构写进预训练输入与目标"的早期例子。代码模型探针工作 [INSPECT](../../../cross-domain/papers/arxiv-2312.05092/README.md) 用它作被测模型，发现融入结构信息的模型对代码特征表示得更好。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2009.08366 · [全文 PDF](https://arxiv.org/pdf/2009.08366) · ICLR 2021
- 作者：Daya Guo、Shuo Ren、Shuai Lu、Zhangyin Feng、Duyu Tang 等 18 位（中山大学、北航、北大、哈工大、Microsoft Research Asia 等）
- 方向：llm/pretraining、llm/architecture
