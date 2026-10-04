# Defeating Prompt Injections by Design

> 状态：文献卡 · 2025 预印本 / SaTML 2026 · [原文](https://arxiv.org/abs/2503.18813)

- **解决什么**：Agent 读取不可信材料时，防止隐藏指令通过工具调用造成未授权操作或数据外泄。
- **核心方法**：在 Dual-LLM 的规划与解析分离上，增加受限解释器、值级别来源/读者标签和调用前策略检查，同时约束控制流与数据流。
- **为什么在这个库里**：[Agent 基线](../../fields/agents/BASELINES.md)中“动作空间与接口”“环境”的安全增强路线，与[权限、沙箱与协作](../../fields/agents/permissions-isolation-collaboration.md)连读；优先级：必读。

[技术精读：机制、手算与实验边界](reading.md) · [来源信息](source.json)
