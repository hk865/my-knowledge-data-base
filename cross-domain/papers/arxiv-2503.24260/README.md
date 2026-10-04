# MaintainCoder: Maintainable Code Generation Under Dynamic Requirements

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.24260)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：代码生成研究关注功能正确与执行效率，忽略了真实软件开发中的可维护性：需求变化时要返工多少。
- **核心方法**：评测侧 MaintainBench：从 HumanEval、MBPP、APPS、CodeContests、xCodeEval 选题，按四类模式（功能扩展、接口修改、数据结构变换、错误处理增强）系统生成需求变更，配专家审核的测试；用动态指标衡量维护代价：修改后的通过率、代码改动量（改动行数）、修改前后语法树的相似度。方法侧 MaintainCoder 用瀑布式流程、设计模式与多智能体分工（需求分析、模块分解、应用设计模式）追求高内聚、低耦合。发现：已有方法（包括 AgentCoder、MapCoder 等多智能体系统）在需求变化下通过率低、改动量大；MaintainCoder 把动态维护指标提升 60% 以上，初始代码的正确性也更高；可维护性指数、圈复杂度等静态指标反映不了维护代价，彼此之间还相互矛盾。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"代码质量"一节：本库收录的评测中，唯一把"架构是否便于扩展"操作化为"需求变了要改多少"的一篇；它对静态指标的否定，也提醒 [RACE](../arxiv-2407.11470/README.md) 一类用 MI 打分的做法只测到代码表面。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2503.24260 · [全文 PDF](https://arxiv.org/pdf/2503.24260) · 北京大学、McGill University、上海算法创新研究院
- 发表：NeurIPS 2025
- 方向：cross-domain/evaluation、cross-domain/agents
