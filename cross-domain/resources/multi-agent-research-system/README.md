# How we built our multi-agent research system

> 状态：资料卡 · 2025 · [原文](https://www.anthropic.com/engineering/multi-agent-research-system)

- **解决什么**：开放式研究任务怎样分解、汇总证据并从执行失败中恢复。
- **核心方法**：主研究Agent分解问题，独立子Agent搜索并压缩证据，再由主Agent综合和补查；有效分派包含目标、输出格式、工具/来源建议和明确边界；持久状态与检查点支持失败恢复；评估同时检查事实、引文、完整性、来源质量和工具效率，并保留人工测试。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：重点看任务合同、证据汇总、可恢复执行三个接口如何协同。优先级：选读。
