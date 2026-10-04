# Toolformer: Language Models Can Teach Themselves to Use Tools

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2302.04761)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言模型在算术、事实查询这类小工具就能做好的事上反而出错：拿不到新信息、编造事实、算不准、不知道今天的日期（§1）。
- **核心方法**：只给每个 API 几条人写的示例，让 GPT-J（6B）在 CCNet 子集上自己插入候选 API 调用，执行后只保留"让后面 token 的损失至少下降一个阈值"的调用，再用这些数据微调（§2）。工具有问答（Atlas）、计算器、维基百科检索（BM25）、翻译（600M 的 NLLB）、日历（§3）。零样本下它在数学应用题上超过大得多的 OPT-66B 与 GPT-3 175B（ASDiv 40.4，GPT-3 为 14.0，Table 4）；开放问答上仍输给 GPT-3（TriviaQA 48.8 对 65.9，Table 5），作者归因于检索接口太简单、模型不能改写查询。自述局限（§7）：不能链式调用工具、不能交互式使用、是否调用对输入措辞敏感、样本效率低（处理一百多万篇文档只得到几千条有用的计算器调用）、不考虑调用成本。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"提示时代"里少见的训练路线：用自监督损失判断"这次工具调用有没有用"，是后来把 agent 行为训进权重的早期形态；它自述的"不能链式、不能交互"正是 ReAct 式多轮循环与后来的多轮 agent RL 要补的。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2302.04761 · [全文 PDF](https://arxiv.org/pdf/2302.04761)
- 作者：Timo Schick、Jane Dwivedi-Yu、Roberto Dessì、Roberta Raileanu、Maria Lomeli、Luke Zettlemoyer、Nicola Cancedda、Thomas Scialom（Meta AI Research、Universitat Pompeu Fabra（NeurIPS 2023 正式版另加 Eric Hambro，共 9 位））
- 开放情况：论文未写代码或数据的发布声明（未核实是否有官方仓库）。
- 方向：cross-domain/agents、llm/posttraining/sft
