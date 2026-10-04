# τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.12045)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有 benchmark 不测 agent 与人类用户的交互，也不测是否遵守领域规则；它们把信息一次性全给出，没有人在回路中（摘要、§1）。
- **核心方法**：零售与航空两个领域：JSON 数据库、Python 工具、一份 Markdown 写的业务政策，由语言模型扮演带隐藏指令的用户与 agent 多轮对话。奖励 r = 最终数据库是否与唯一标准结果相同 × 回复是否包含必要信息，取 0 或 1；作者承认 r = 1 只是必要条件，例如未经用户确认就办理退货也可能得 1（§3）。提出 pass^k：同一任务独立跑 k 次全部成功的概率，衡量可靠性而非"至少一次成功"。gpt-4o 函数调用 agent 的 pass^1 零售 61.2%、航空 35.2%（Table 2），零售上 pass^8 降到 25% 以下（§5.1）。失败分析：约 55% 是参数或信息错误，25% 是决策错误（含违反政策），其余是复合请求只完成一部分（§5.2）。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"真实环境 benchmark"阶段对"可靠性"与"守规则"的度量；pass^k 把长程误差累积变成了可读的数字。后续 τ²-bench（arXiv 2506.07982）加入用户也能操作环境的双控制设定。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2406.12045 · [全文 PDF](https://arxiv.org/pdf/2406.12045)
- 作者：Shunyu Yao、Noah Shinn、Pedram Razavi、Karthik Narasimhan（Sierra）
- 开放情况：代码开放：github.com/sierra-research/tau-bench（MIT）；README 说明零售与航空任务已有修正版。
- 方向：cross-domain/agents、cross-domain/evaluation
