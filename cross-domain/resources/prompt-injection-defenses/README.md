# Mitigating the risk of prompt injections in browser use

> 状态：资料卡 · 2025 · [原文](https://www.anthropic.com/research/prompt-injection-defenses)

- **解决什么**：浏览器 Agent 怎样应对来自网页内容的提示注入。
- **核心方法**：浏览器读取的外部内容可影响动作；文章将模型训练、内容分类器、人类红队结合，并明确提示注入尚未解决。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
