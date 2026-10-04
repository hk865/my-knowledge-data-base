# A Careful Examination of Large Language Model Performance on Grade School Arithmetic

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.00332)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：数学推理 benchmark 的分数有多少来自数据污染（与测试题相近的数据混进训练集）而不是推理能力（摘要、§1）。
- **核心方法**：仿照 2019 年重建 ImageNet 测试集检查过拟合的做法，完全由人工（不用任何 LLM）重新出 1,205 道小学应用题，命名 GSM1k，在人类解题率、解题步数、答案量级等指标上对齐 GSM8k。最多下降 8 个百分点（v4 摘要；早期版本数字不同）；Phi、Mistral 与部分 Llama 系列几乎在所有尺寸上都表现出系统性过拟合，Gemini、GPT、Claude 等前沿模型几乎没有；模型生成 GSM8k 原题的概率与它在两套题上的落差正相关（Spearman r² = 0.36），作者认为部分模型记住了 GSM8k，但污染不是全部原因（§5.4），过拟合的模型仍能解新题（Phi-2 掉 6 个点仍能解出一半以上）。数据集不公开，承诺在三个不同底座的开源模型达到 95% 或 2025 年 6 月（以先到者为准）时公开，并另留一批题以防经 API 泄漏。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"污染"一节的核心证据：用重新采集的同分布测试集直接量出落差，比在训练语料里查重更可信；"不公开、预先承诺公开条件、另留备用题"也是"为什么要隐藏评测数据"的一个原文范例。同一机构参与了 [HLE](../arxiv-2501.14249/README.md)（同样保留私有集）。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2405.00332 · [全文 PDF](https://arxiv.org/pdf/2405.00332) · Scale AI
- 发表：NeurIPS 2024 Datasets and Benchmarks
- 方向：cross-domain/evaluation
