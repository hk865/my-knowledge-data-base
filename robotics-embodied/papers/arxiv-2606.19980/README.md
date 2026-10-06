# ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.19980)

- **解决什么**：机器人策略改进需要人反复设计训练、评估和恢复流程，怎样让通用Agent在受限环境中组织这些实验。
- **核心方法**：相对人工迭代策略，先固定经人检查的reset、reward和安全接口，再让代码Agent调整策略程序、BC/RL训练与数据配方，依据真机反馈保留改进。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中的“通用模型组织动作侧学习”主线，连接免训练工具调用与允许低层适配的研究。优先级：必读。
