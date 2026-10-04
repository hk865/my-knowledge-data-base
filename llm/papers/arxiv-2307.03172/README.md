# Lost in the Middle: How Language Models Use Long Contexts

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2307.03172)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言模型已经能接收很长的输入，但它们实际用上了多少长上下文，缺少受控的测量。
- **核心方法**：设计两个受控任务：多文档问答（10、20 或 30 篇检索文档中只有 1 篇含答案，改变它的位置与文档总数）与合成的键值检索（给一串 JSON 键值对，按键取值）。准确率随相关信息的位置呈 U 形：在开头或结尾最高，在中间显著下降，显式加长了上下文的模型也是如此。相关文档放在中间时，GPT-3.5-Turbo 的多文档问答准确率低于完全不给文档的闭卷设置（56.1%）；加长上下文的版本与原版表现几乎相同。encoder-decoder 模型只在训练长度以内对位置较稳健；把问题放在文档前后各一次（query-aware contextualization）能让键值检索接近完美，但对多文档问答影响很小；未经指令微调的基座模型同样呈 U 形。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"注意力不丢失"一节"信息在中间"这一失败场景的证据；"更长更大的注意力"一节用它说明大海捞针只检验检索，位置本身就会改变结果。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2307.03172 · [全文 PDF](https://arxiv.org/pdf/2307.03172) · Stanford University、UC Berkeley、Samaya AI · TACL 2023 接收（arXiv 页面注释）
- 方向：llm/pretraining、llm/long-context、cross-domain/evaluation
