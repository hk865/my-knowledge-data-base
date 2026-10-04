# How we built our multi-agent research system

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://www.anthropic.com/engineering/multi-agent-research-system
- 类型：官方博客，非论文
- 日期：2025-06-13
- 日期依据：Published Jun 13, 2025
- [原文入口](https://www.anthropic.com/engineering/multi-agent-research-system)
- 阅读版本：Published Jun 13, 2025
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

主研究Agent分解问题，独立子Agent搜索并压缩证据，再由主Agent综合和补查；有效分派包含目标、输出格式、工具/来源建议和明确边界；持久状态与检查点支持失败恢复；评估同时检查事实、引文、完整性、来源质量和工具效率，并保留人工测试

- 实际阅读范围：架构、分派合同、评估、可靠性及同步瓶颈；内部评估未复现
- 证据边界：结果针对其研究系统与内部评估，不能外推到任意编码任务 文中指出紧耦合和大量共享上下文不利于多Agent；发布时同步调度存在瓶颈

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)

只保留公开原文链接，不镜像第三方全文。
