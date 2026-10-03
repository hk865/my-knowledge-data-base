# RelayLLM: Efficient Reasoning via Collaborative Decoding

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2601.05167
- 类型：论文
- 年份：2026
- [官方入口](https://arxiv.org/abs/2601.05167)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：§2.1–2.3、训练流程摘要；未全文审训练消融
- 核验版本：无版本 URL 当前解析 v1 2026-01-08
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

小模型输出 `<call>n</call>` 暂停，交给大模型续写 n token（或 EOS 提前结束）；调用标记从大模型上下文删除，小模型保留标记及大模型续写后接回；warm-up+GRPO 学习求助。

大模型在接管时真实生成，不是批量裁决所有小模型 token；训练及数学 benchmark 范围有限；低调用比例不等于通用端到端省时比例。

分布或质量保证：经验准确率—调用成本折中，无精确目标分布保证

官方核验来源：
- [https://arxiv.org/abs/2601.05167](https://arxiv.org/abs/2601.05167)
- [https://arxiv.org/html/2601.05167](https://arxiv.org/html/2601.05167)

未独立复现，不镜像PDF。
