# XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2308.01263)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：安全训练让模型拒绝不安全请求，但有的模型连明显安全、只是用词像危险请求的问题也拒绝（夸大的安全行为，即过度拒答），缺少系统的测量。
- **核心方法**：250 条安全提示，分 10 类（同形异义如"kill a Python process"、比喻、安全语境如游戏里的"杀人"、定义、真实或虚构的历史事件、公众人物的隐私等），另配 200 条不安全的对照提示；作者人工把回答标为完全遵从、完全拒绝或部分拒绝。带原系统提示的 Llama2-70b-chat 完全拒绝 38% 的安全提示，另有 21.6% 部分拒绝；去掉系统提示后降为 14% 与 15.6%。Mistral-7B-Instruct 不拒绝安全提示，但也遵从最不安全的提示，加上护栏系统提示后又出现过度拒答。GPT-4 平衡最好，只在隐私类安全提示上有拒绝。作者认为过度拒答来自"词汇过拟合"：模型对某些词过度敏感。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"安全对齐"一节中过度拒答的标准测试，必须与越狱鲁棒性一起测，否则只优化一侧会把另一侧推坏。[Llama 2](../../../llm/papers/arxiv-2307.09288/README.md) 自述加强安全后出现的误拒，正是它测的现象。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2308.01263 · [全文 PDF](https://arxiv.org/pdf/2308.01263) · Bocconi University、University of Oxford、Stanford
- 发表：NAACL 2024（主会）
- 方向：cross-domain/evaluation、llm/posttraining/preferences
