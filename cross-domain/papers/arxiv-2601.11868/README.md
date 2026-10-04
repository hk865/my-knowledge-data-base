# Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.11868)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：现有 benchmark 要么不测真实任务，要么不够难，无法有意义地区分前沿模型（摘要）。
- **核心方法**：每个任务由四部分组成：容器化环境、一段指令、检验完成情况的测试、人工写的参考解；测试只检查最终容器状态，不检查 agent 敲了什么命令（§1、§2.1）。Terminal-Bench 2.0 从 93 位贡献者的 229 个任务中选出 89 个，每个经三位人工审查，约三个审查人时；审查流程包括"参考解能过、空解不能过"的 CI 检查、LLM 审查、专家审查，以及一个被提示去"作弊"的对抗 agent，它找到的漏洞包括给测试环境打补丁、猜答案、把所有可能答案都输出（测试只查正确答案在不在、不查错误答案有没有）（§2.3、附录 B.4）。最好成绩 GPT-5.2 + Codex CLI 62.9%，最好的开放权重 Kimi K2 Thinking 35.7%；作者认为模型的选择通常比框架更重要（Table 2、§4）。自述局限（§5）：任务依赖外网、硬件与运行时会有差异、只有金丝雀字符串防污染、仍可能有任务不满足验证标准。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"命令行 agent"的主要评测，也是本库少见的把"防作弊"写进任务构建流程的 benchmark：测试即奖励，测试写得松就会被 agent 钻空子。1.0 版因任务随外部网站变化而不稳定，2.0 才加强人工验证。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2601.11868 · [全文 PDF](https://arxiv.org/pdf/2601.11868)
- 作者：Mike A. Merrill、Alexander G. Shaw、Nicholas Carlini、Boxuan Li、Harsh Raj、Ivan Bercovich、Lin Shi、Jeong Yeon Shin、Thomas Walshe、E. Kelly Buchanan、等 85 位作者（Stanford University、Laude Institute 等 44 家机构）
- 开放情况：任务与框架开放：github.com/laude-institute/terminal-bench（Apache-2.0）、Harbor 框架；Table 1 与 Table 2 标题写作 74 个任务，与正文 89 个不一致。
- 方向：cross-domain/agents、cross-domain/evaluation
