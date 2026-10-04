# Evaluating Large Language Models Trained on Code

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2107.03374)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：怎样衡量代码模型"写出能运行的正确程序"，以及在 GitHub 代码上微调的 GPT 能写到什么程度。
- **核心方法**：发布 HumanEval：164 道手写的 Python 函数题，每题含函数签名、docstring 和平均 7.7 个单元测试；手写是为了避开 GitHub 上已有的答案。指标用 pass@k（每题采 k 个样本、至少一个通过全部测试的概率，文中给出无偏估计），不用 BLEU，因为作者发现正确解与错误解的 BLEU 分布大量重叠。Codex 是在 5,400 万个公开仓库、过滤后 159GB 的 Python 文件上微调的 GPT 系列模型：12B 版本 pass@1 为 28.8%（GPT-3 为 0%，GPT-J 为 11.4%），每题采 100 个样本时 70.2% 的题至少有一个通过；再在正确实现的独立函数上做监督微调得到的 Codex-S 为 37.7%。作者自述的局限：docstring 描述长操作链、把操作绑定到变量时容易出错；§7.2 的"失配"：提示中的代码含细微 bug 时，Codex 会写出比自己能力更差的代码，加上"写正确代码"的指令也不能消除，且差距随模型增大而扩大。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"代码：函数级正确性"一节的起点。它确立了"执行单元测试即评分"的口径，这一口径后来直接成为可验证奖励（[DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 用编译与测试用例做奖励）。§7.2 的"失配"是"为过测试而写代码"一节的前史：模型倾向于模仿训练分布，而不是做用户实际想要的事。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2107.03374 · [全文 PDF](https://arxiv.org/pdf/2107.03374) · OpenAI
- 发表：arXiv 预印本
- 方向：cross-domain/evaluation、llm/pretraining
