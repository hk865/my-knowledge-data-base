# Measuring AI Ability to Complete Long Software Tasks

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.14499)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：benchmark 分数的现实含义不清楚；作者想用"人类要花多久"来度量 AI 智能体能做多长的任务（摘要）。
- **核心方法**：提出 50% 时间跨度（50%-task-completion time horizon，一句话：模型有一半把握做成的任务，人类专家通常要做多久）：先请有相关经验的人完成 RE-Bench、HCAST 与 66 个短任务（SWAA），记录用时；再对每个模型拟合"成功率 ~ 人类用时"的逻辑斯蒂曲线，取 50% 处的用时。原版 170 个任务，Claude 3.7 Sonnet 约 50 分钟，2019 年以来前沿模型的时间跨度约每 7 个月翻一倍（摘要）。任务全部能被代码自动判分，因此偏向格式固定、少开放式判断；环境基本静态、很少"一步错满盘输"、不涉及其他智能体（附录 B.2）。作者按 16 项"凌乱度"给任务打分，凌乱度每高 1 分，成功率比只按长度预测的低约 8.1%，但高、低凌乱度两组随时间的进步速度相近（附录 F.2）。METR 2026 年 1 月发布 [Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)：任务从 170 个增到 228 个，8 小时以上的长任务从 14 个增到 31 个，其中只有 5 个有人类实测用时；删改的任务多因描述含糊、容易被钻空子或判分函数有错。[在线页面](https://metr.org/time-horizons/)（最后更新 2026-05-08）写明：每个模型约 1000 次运行，逐条复核作弊，通常要 1–2 周日历时间；16 小时以上的测量在现有任务集上不可靠。
- **为什么在这个库里**：[观点页](../../../perspectives/eval-shapes-models.md)"长程与长尾"一节的主要证据：它把"任务越长越难测"变成了可读的数字（50% 与 80% 时间跨度相差数倍、长任务缺人类基线、高跨度测量不可靠），也说明可自动判分的长任务本身是被筛选过的"干净"任务。[Agent 方向](../../fields/agents/README.md)的进展度量之一。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2503.14499 · [全文 PDF](https://arxiv.org/pdf/2503.14499)
- 作者：Thomas Kwa、Ben West、Joel Becker、Amy Deng、Katharyn Garcia、Max Hasin、Sami Jawhar、Megan Kinniment、Nate Rush、Sydney Von Arx 等 26 位（METR）
- 题名：v1（2025-03）题为 Measuring AI Ability to Complete Long Tasks，v3 起改为现名；当前为 v4（2026-07-10）。
- 开放情况：分析代码与数据开放（github.com/METR/eval-analysis-public）；部分任务为私有。
- 方向：cross-domain/evaluation、cross-domain/agents
