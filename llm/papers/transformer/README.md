# Attention Is All You Need

> 状态：技术精读 · 2017 · [原文](https://arxiv.org/abs/1706.03762)

[返回大语言模型目录](../../README.md)

- **解决什么**：循环网络在序列内逐步计算，训练难以并行；卷积要堆多层才能连接远距离位置。
- **核心方法**：相对"RNN 或 CNN 编码器—解码器 + 注意力"的结构，完全去掉循环和卷积，只用多头自注意力（每个位置按 query 与 key 的相似度加权读取其他位置的 value）、前馈层、残差和归一化堆叠成编码器—解码器，位置信息用正弦位置编码加入。WMT 2014 英德翻译 28.4 BLEU，比此前最好结果（含集成）高 2 BLEU 以上；英法翻译在 8 张 GPU 上训练 3.5 天，单模型达到 41.8 BLEU。
- **为什么在这个库里**：[架构与效率方向](../../fields/architecture/README.md)的地基：今天的 decoder-only LLM 都从这里的注意力算子出发，后续的 MLA、稀疏注意力、状态空间模型都在改它的某个部件。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)
- 关系页：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)（两种子层怎样分工）· [递推状态谱系](../../../foundations/relations/recurrent-state.md)第 5 节（注意力改成线性形式后退化为递推）

## 身份信息

- 稳定标识：arxiv:1706.03762 · [全文 PDF](https://arxiv.org/pdf/1706.03762v7) · NIPS 2017 · 精读依据 v7
- 作者：Ashish Vaswani、Noam Shazeer、Niki Parmar、Jakob Uszkoreit、Llion Jones、Aidan N. Gomez、Łukasz Kaiser、Illia Polosukhin（Google Brain、Google Research、多伦多大学）
- 方向：llm/architecture
