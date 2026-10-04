# Reflexion: Language Agents with Verbal Reinforcement Learning

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2303.11366)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言 agent 很难从试错中快速学习：传统强化学习需要大量样本和昂贵的微调（摘要、§1）。
- **核心方法**：不更新权重。每次失败后，让模型把稀疏的反馈（成败、测试结果）写成一段文字反思，存进有容量上限的情景记忆（滑动窗口），下一次尝试时放进提示，相当于"用语言做策略优化"。ALFWorld 上 ReAct + Reflexion 完成 134 个任务中的 130 个；HumanEval（Python）pass@1 91%，同期 GPT-4 为 80%。编程任务的反馈来自模型自己写的单元测试，测试本身会错：自测全部通过而实现错误（假阳性）的比例，MBPP Python 为 16.3%，HumanEval Python 为 1.4%（§4.3、Table 2），于是 MBPP Python 上 Reflexion 低于 GPT-4 基线（77.1 对 80.1，Table 1）。自述局限（§5）：可能陷入局部最优；长期记忆只是滑动窗口；测试驱动在非确定、有副作用、依赖硬件或并发的函数上难以写准输入输出。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"提示时代"中"自我修正"一支的代表。它的自测假阳性是"验证器出错，agent 照样停下来交差"的最早实例之一，后来 RL 训练中的测试特例化是同一个问题在训练时的版本。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2303.11366 · [全文 PDF](https://arxiv.org/pdf/2303.11366)
- 作者：Noah Shinn、Federico Cassano、Edward Berman、Ashwin Gopinath、Karthik Narasimhan、Shunyu Yao（Northeastern University、MIT、Princeton University；官方仓库标注 NeurIPS 2023）
- 开放情况：代码开放：github.com/noahshinn/reflexion（MIT）。
- 方向：cross-domain/agents、llm/inference
