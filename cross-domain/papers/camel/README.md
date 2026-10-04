# Defeating Prompt Injections by Design

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2503.18813
- 类型：论文
- 日期：2025-03-24
- 日期依据：arXiv submission history；方法阅读固定 v2
- [原文入口](https://arxiv.org/abs/2503.18813v2)
- 阅读版本：arXiv:2503.18813v2
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

CaMeL 分离只看可信请求的 P-LLM 与处理不可信数据、无工具权的 Q-LLM；受限 Python 解释器传播数据来源/读者标签，并在工具调用前执行策略。

- 实际阅读范围：v2_full_text_targeted_read_threat_model_method_limitations_sections_3_5_7_9_10
- 证据边界：假设用户 prompt 和 memory 未被攻击；纯文本误导、无外泄的错误摘要/钓鱼非目标（§3.1）。 侧信道、策略覆盖、去密审批疲劳仍是边界（§7、§9）；解释器形式化验证列为未来工作（§10）。 不能外推为所有语义正确性保证，或替代 OS/VM 沙箱。 仅核验论文及作者仓库，不运行代码；不混用 v1/v2 指标。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://arxiv.org/abs/2503.18813v2](https://arxiv.org/abs/2503.18813v2)
- [https://arxiv.org/html/2503.18813v2](https://arxiv.org/html/2503.18813v2)

只保留公开原文链接，不镜像第三方全文。
