# Mitigating the risk of prompt injections in browser use

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://www.anthropic.com/research/prompt-injection-defenses
- 类型：官方博客，非论文
- 日期：2025-11-24
- 日期依据：页面可见 Nov 24, 2025
- [原文入口](https://www.anthropic.com/research/prompt-injection-defenses)
- 阅读版本：2026-10-04所见动态官方页面；未固定不可变版本
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

浏览器读取的外部内容可影响动作；文章将模型训练、内容分类器、人类红队结合，并明确提示注入尚未解决。

- 实际阅读范围：article_body_and_metadata
- 证据边界：研究/产品博文，不是独立学术论文。 该文评估的是当时的 Claude 浏览器配置，不可把其中攻击率推广到任意 Agent 或今天的模型。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://www.anthropic.com/research/prompt-injection-defenses](https://www.anthropic.com/research/prompt-injection-defenses)

只保留公开原文链接，不镜像第三方全文。
