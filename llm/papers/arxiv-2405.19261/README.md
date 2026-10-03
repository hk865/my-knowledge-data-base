# Faster Cascades via Speculative Decoding

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2405.19261
- 类型：论文
- 年份：2024
- [官方入口](https://arxiv.org/abs/2405.19261)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：§4.1–4.3、Algorithms 4–5、Lemma 3–5；未逐行审全部证明
- 核验版本：v2 2024-10-21
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

令 π=(1−r)q+r p，用 min(1,π/q) 接受与 max(π−q,0) 残差补采；批量算大模型后应用 deferral。最优规则把质量收益与 TV 距离导致的拒绝成本权衡，实际用概率峰值作 plug-in 估计。

有理论目标与估计误差界，不等于所有任务质量不降；r 选择改变输出分布。

分布或质量保证：精确采样所定义的混合/级联分布 π；不一般等于大模型 p

官方核验来源：
- [https://arxiv.org/abs/2405.19261](https://arxiv.org/abs/2405.19261)
- [https://arxiv.org/html/2405.19261v2](https://arxiv.org/html/2405.19261v2)

未独立复现，不镜像PDF。
