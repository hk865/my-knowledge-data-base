# EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2503.01840
- 类型：论文
- 年份：2025
- [官方入口](https://arxiv.org/abs/2503.01840)

这是文献卡，没有独立 reading.md，不计为全文精读；用户是否已读未知。

## 2026年10月3日核验与阅读线索

- 阅读范围：§2.1–2.2、§3.1；训练细节未全文核验
- 核验版本：恢复 v1 2025-03-03；最新 v3 2025-04-23
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

融合目标低/中/高层特征，经 FC 压缩，与采样 token embedding 一起输入轻量 decoder；直接预测 token，自回归后续步使用 draft 输出替代尚未取得的 target 特征；采用动态 draft tree 和 tree attention 并行验证。

需训练目标专用 drafter 并访问内部特征；不是任意黑箱小模型 API；本轮未重现实验。

分布或质量保证：沿用精确 speculative verification

官方核验来源：
- [https://arxiv.org/abs/2503.01840](https://arxiv.org/abs/2503.01840)
- [https://arxiv.org/html/2503.01840v1](https://arxiv.org/html/2503.01840v1)

未独立复现，不镜像PDF。
