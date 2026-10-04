# FinanceBench: A New Benchmark for Financial Question Answering

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.11944)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：缺少面向上市公司财报的开卷金融问答测试，用来给企业部署设一个最低标准。
- **核心方法**：10,231 个关于上市公司公开文件（年报等）的问题，附答案与证据段落；从中抽 150 例，人工复核 16 种模型配置的回答（共 2,400 条）。主表 8 种配置中，GPT-4-Turbo 闭卷只答对 9%；所有文件共用一个向量库检索时 19%（68% 拒答）；每份文件单独一个向量库 50%；把整份文件放进长上下文 79%；直接给证据页（oracle）85%。失败方式不同：Llama 2 多为答错（幻觉），GPT-4-Turbo 在检索设置下多为拒答。作者自述：长上下文做法在企业场景下延迟高，也放不下更大的文件；拿到正确信息后，模型仍会在推理上出错。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"金融"一节：同一个模型从 19% 到 79%，差别全在检索与上下文的组织方式，说明这类任务的成绩首先受系统与长上下文限制；"拒答还是编造"也是金融、法律这类高风险领域共有的取舍。长上下文本身的评测见[长上下文方向](../../../llm/fields/long-context/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2311.11944 · [全文 PDF](https://arxiv.org/pdf/2311.11944) · Patronus AI、Contextual AI、Stanford
- 发表：arXiv 预印本；数据集在 Hugging Face（PatronusAI/financebench）
- 方向：cross-domain/evaluation、llm/long-context
