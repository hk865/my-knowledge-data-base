# Fast Inference from Transformers via Speculative Decoding

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2211.17192
- 类型：论文
- 年份：2022
- [官方入口](https://arxiv.org/abs/2211.17192)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：方法 §2.1–2.3、Algorithm 1；未逐行复核附录证明
- 核验版本：v2 2023-05-18; ICML 2023 / PMLR 202:19274–19286, 2023-07-23–29
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

小模型顺序草拟 K 个 token；大模型并行计算 K+1 个条件分布；从左向右按 min(1,target/draft) 接受。首拒绝处丢弃后缀，按归一化 max(target−draft,0) 补一个 token；全接受则从目标末位分布再采一个尾 token。

必须能访问两者分布并使用兼容 token 空间；收益取决于接受率、draft 开销与硬件；相同分布不代表相同随机种子的逐字输出。

分布或质量保证：精确目标分布（理想算术），不是语义判卷

官方核验来源：
- [https://arxiv.org/abs/2211.17192](https://arxiv.org/abs/2211.17192)
- [https://arxiv.org/html/2211.17192v2](https://arxiv.org/html/2211.17192v2)

未独立复现，不镜像PDF。
