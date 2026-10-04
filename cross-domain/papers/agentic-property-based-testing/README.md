# Finding bugs across the Python ecosystem with Claude and property-based testing

> 状态：文献卡 · 2026 · [原文](https://www.anthropic.com/research/property-based-testing)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：常见的单元测试是基于示例的，只检查几个具体输入的输出；性质测试（property-based testing）检查一条一般性质是否对全部（或大多数）输入成立，但性质要靠人想出来、写成测试。文章问：能否让 agent 从代码里自己推出性质、写成性质测试，在真实的 Python 包里找出 bug。
- **核心方法**：agent 做成一个 Claude Code 自定义命令，输入一个文件、模块或函数，分五步：读代码（类型标注、docstring、函数名、注释）→ 提出应当成立的一般性质 → 用 Hypothesis 写性质测试 → 运行，并反思失败是真 bug 还是测试本身写错 → 把确认的 bug 写成结构化报告；用待办清单维持多步推理，用反思环节压低误报（"Our Property-Based Testing Agent"一节）。第一阶段用 Claude Opus 4.1 跑 100 多个流行 Python 包，得到 984 份 bug 报告（"Searching for bugs in real PyPI packages"一节）；人工抽查 50 份，56% 是真 bug，32% 是真 bug 且值得上报；按 15 分评分细则排序后，得分最高的报告中 86% 有效、81% 有效且值得上报。第二阶段用 Sonnet 4.5 在 10 个重要包上多次运行，另用基于 Sonnet 4.5 的评估 agent 读代码和报告判断正确性与严重程度，并请 3 位专家复核高严重度 bug（"Evaluating the agent"一节）。作者人工上报 5 个 bug：NumPy 的 `numpy.random.wald` 返回负数等 3 个补丁已合并，1 个补丁已提交，python-dateutil 的 `easter()` 被维护者判为有意行为（"Maintainer validation"一节）。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)批注把它与 [MORPHAGENT](../morphagent/README.md) 一起列为"从测试一侧加强验证"的例子，回应"测试只查正确答案在不在"的问题；对应[评估方向](../../fields/evaluation/README.md)"捷径与裁判偏差"一节的"单元测试判错""测试通过不等于代码好"两条：性质测试检查的是对一类输入都该成立的关系，而不是几个示例答案。文章也写出做不好的场景：从语义微妙或复杂的代码里推出性质仍然困难（"Conclusion"一节）；代码带有隐含假设时，只有维护者能决定该测哪条性质（dateutil 一例，"Maintainer validation"一节）。优先级：选读。

## 身份信息

- 稳定标识：url:https://www.anthropic.com/research/property-based-testing · Anthropic 官方研究博客（2026-01-14） · 作者 Muhammad Maaz（MATS、Anthropic）、Liam DeVoe（Northeastern University）、Zac Hatfield-Dodds、Nicholas Carlini（Anthropic）
- 关联论文：[Agentic Property-Based Testing: Finding Bugs Across the Python Ecosystem](https://arxiv.org/abs/2510.09907)（arXiv:2510.09907，同一组作者，NeurIPS 2025 第 4 届 Deep Learning for Code Workshop）
- 方向：cross-domain/agents、cross-domain/evaluation
