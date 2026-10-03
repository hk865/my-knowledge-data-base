# Accelerating Large Language Model Decoding with Speculative Sampling

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2302.01318
- 类型：论文
- 年份：2023
- [官方入口](https://arxiv.org/abs/2302.01318)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：Algorithm 2、§4.1–4.2、§5、§6.1；未逐行复核证明
- 核验版本：v1 2023-02-02
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

与 Leviathan 独立同期提出同一核心拒绝采样机制；明确 K+1 logits 并行验草稿、首拒绝残差重采样、全接受 bonus token。分布先应用 temperature/top-k/nucleus 再验证。

论文 p=draft、q=target，与 Leviathan 符号相反；低 batch、memory-bound 是批验接近单步成本的条件；benchmark 提升不是通用常数。

分布或质量保证：精确目标分布，论文限定 hardware numerics

官方核验来源：
- [https://arxiv.org/abs/2302.01318](https://arxiv.org/abs/2302.01318)
- [https://arxiv.org/html/2302.01318v1](https://arxiv.org/html/2302.01318v1)

未独立复现，不镜像PDF。
