# Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2501.19309
- 类型：论文
- 年份：2025
- [官方入口](https://arxiv.org/abs/2501.19309)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：§4.1、§5.1、Table 1
- 核验版本：v1 2025-01-31
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

在冻结目标模型最后 hidden embedding 上训练线性 judge head，预测当前草稿 token 正确性；标准 SD 接受 mask 与 judge 阈值接受 mask 作 OR。δ=1 才退化回标准 SD。

judge 可误接受；论文明确必须测生成质量；8B/405B 的 9.7× 是 HuggingFace 基线，优化 GPT-fast 对照为 3.9×，不可混用。

分布或质量保证：放宽接受规则，经验质量保持，不保目标原分布

官方核验来源：
- [https://arxiv.org/abs/2501.19309](https://arxiv.org/abs/2501.19309)
- [https://arxiv.org/html/2501.19309v1](https://arxiv.org/html/2501.19309v1)

未独立复现，不镜像PDF。
