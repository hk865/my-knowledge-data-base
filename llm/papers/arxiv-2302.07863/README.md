# Speculative Decoding with Big Little Decoder

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2302.07863
- 类型：论文
- 年份：2023
- [官方入口](https://arxiv.org/abs/2302.07863)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：§3.2–3.4、§2.3 对比与实验摘要
- 核验版本：v4 2023-10-12; NeurIPS 2023
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

fallback：小模型最大预测概率低于阈值才调用大模型；大模型并行回看已有草稿；rollback：找到分布距离超阈值的最早位置，删除该处及后缀并由大模型替换。

小模型过度自信仍可能出错；rollback 有重算成本；阈值需要任务权衡。

分布或质量保证：阈值质量—延迟折中，不保大模型原分布

官方核验来源：
- [https://arxiv.org/abs/2302.07863](https://arxiv.org/abs/2302.07863)
- [https://arxiv.org/html/2302.07863v4](https://arxiv.org/html/2302.07863v4)

未独立复现，不镜像PDF。
