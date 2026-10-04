# Continuous Integration

> 状态：资料卡 · 2000 · [原文](https://martinfowler.com/articles/continuousIntegration.html)

- **解决什么**：怎样尽早发现独立开发产生的集成错误。
- **核心方法**：CI要求成员至少每天集成到共同代码线，每次用自动构建与测试尽早发现集成错误；快速提交测试与更慢的真实依赖/端到端验证可以分层；作者明确指出测试不能证明不存在缺陷。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：把集成看作持续交换真实代码和反馈，不把安装CI服务等同CI实践。优先级：必读。
