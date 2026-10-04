# The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.13208)

- **解决什么**：模型把不可信内容当成同级命令时，如何学会按来源优先级处理冲突指令。
- **核心方法**：显式定义指令优先级，并生成分层指令跟随训练数据，让模型学习忽略低优先级的冲突要求。
- **为什么在这个库里**：与 [CaMeL](../camel/reading.md) 的执行期信息流检查形成互补，连接模型行为训练与工具授权；优先级：必读。

[来源信息](source.json)
