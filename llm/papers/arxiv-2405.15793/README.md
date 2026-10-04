# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.15793)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言模型智能体通过为人设计的界面（如 shell）操作软件，在仓库级软件工程任务上表现差；界面设计怎样影响智能体表现尚无系统研究。
- **核心方法**：把语言模型智能体看作有自己需求的新一类用户，为它专门设计智能体—计算机接口（ACI：一组简化的文件查看、搜索、编辑、执行命令及其反馈格式），让模型在整个仓库中导航、创建和编辑代码、运行测试。相对此前非交互式的语言模型方法，SWE-bench 的 pass@1（一次尝试即解决的问题比例）达到 12.5%，HumanEvalFix 达到 87.7%。
- **为什么在这个库里**：[Agent 与上下文系统方向](../../../cross-domain/fields/agents/README.md)中"接口决定智能体能做什么"的代表，也是[评估与监督可靠性方向](../../../cross-domain/fields/evaluation/README.md)里 SWE-bench 这类代码智能体评测的早期系统基线。与 [ReAct](../../../cross-domain/papers/react/README.md) 对照：同是思考—行动循环，本篇改的是行动空间。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2405.15793 · [全文 PDF](https://arxiv.org/pdf/2405.15793) · 代码、数据与演示公开
- 作者：John Yang、Carlos E. Jimenez、Alexander Wettig、Kilian Lieret、Shunyu Yao、Karthik Narasimhan、Ofir Press（普林斯顿大学）
- 方向：cross-domain/agents、llm/inference、cross-domain/evaluation、cross-domain/model-science
