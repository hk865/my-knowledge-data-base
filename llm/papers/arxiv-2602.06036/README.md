# DFlash: Block Diffusion for Flash Speculative Decoding

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2602.06036
- 类型：论文
- 年份：2026
- [官方入口](https://arxiv.org/abs/2602.06036)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：§3、§4.1–4.2、Table 1；未审实现级验证代码
- 核验版本：恢复 v1 2026-02-05；最新 v2 2026-05-28（ICML 2026 camera-ready）
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

小型 block diffusion 一次前向并行填整块 mask；融合目标多层 hidden states，并注入每一 draft 层的 K/V、缓存复用；以目标 bonus token 为块起点。

需 target 内部特征与专门训练；不是“无需验证的 diffusion”；加速表随模型/任务/温度变化。

分布或质量保证：论文宣称 lossless；本轮确认草拟方法，未独立审计验证实现

官方核验来源：
- [https://arxiv.org/abs/2602.06036](https://arxiv.org/abs/2602.06036)
- [https://arxiv.org/html/2602.06036v1](https://arxiv.org/html/2602.06036v1)

未独立复现，不镜像PDF。
