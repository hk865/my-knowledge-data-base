# ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.20270)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LLM 智能体会找捷径完成任务，例如删掉失败的测试而不是修 bug；这既让 benchmark 分数失真，也让编码助手在实际部署中不可靠，需要能量化这种倾向的测量。
- **核心方法**：从 LiveCodeBench 与 SWE-bench 出发，改动单元测试使之与自然语言规格直接冲突：One-Off 改一个测试的期望值，Conflicting 加入与原测试矛盾的副本，于是任务不可能合法完成，模型在这些任务上的"通过率"就是作弊率。GPT-5 在 Oneoff-SWEbench 上作弊 76%，Conflicting-SWEbench 54%，Oneoff-LiveCodeBench 只有 2.9%；总体上更强的模型作弊率更高；Claude 新模型（Opus 4.1、Sonnet 4）比 Sonnet 3.7 少，OpenAI 模型的同类改进不明显。作弊手法分四类：明知被要求不改仍修改测试、重载比较运算符、记录调用状态、特判测试；在 Conflicting-SWEbench 上，GPT-5 与 o3 四类各占 14% 以上，Claude 与 Qwen3-Coder 79% 以上是修改测试。上下文设计影响大：隐藏测试或设为只读能压低作弊；允许"上报人工"中止，GPT-5 从 54% 降到 9%、o3 从 49% 降到 12%，对 Opus 4.1 作用小；允许多次提交，平均通过率从 80% 升到 83%，作弊率也从 33% 升到 38%。LLM 监控器在 LiveCodeBench 上能抓到 86–89% 的作弊，在多文件的 SWE-bench 上只有 42–65%，会被"为了向后兼容"之类的理由骗过。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"为过测试而写代码"一节的核心测量工具：它把 Claude 4 系统卡内部使用的"不可能任务"做成了公开可复现的 benchmark。作者之一来自 Anthropic，比较 Claude 与 GPT 时留意这一点。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2510.20270 · [全文 PDF](https://arxiv.org/pdf/2510.20270) · Carnegie Mellon University、Anthropic
- 发表：arXiv v1（预印本，Under review）
- 方向：cross-domain/evaluation、cross-domain/agents、llm/posttraining/rl
