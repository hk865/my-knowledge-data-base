# 运动控制与腿足运动：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

本方向已经有可独立阅读的领域讲解，按具体问题解释模块职责、方法边界与研究接口。此页把领域讲解、已有baseline、阅读路线和单篇论文目录汇到一起。

## 第二步：沿具体文章拆机制

[Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](../../papers/convex-mpc/README.md) → [RMA Rapid Motor Adaptation for Legged Robots](../../papers/rma/README.md) → [Proximal Policy Optimization Algorithms](../../../llm/papers/ppo/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

先阅读已有领域讲解，再从下面的阅读顺序中选择一篇，与自己的任务输入、输出和评估条件对照。

## 第四步：保留边界

真实机器人中的观察、状态估计、计划与执行各有误差。跨方向的方法关联不表示相同实验环境或直接历史继承。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。

## 2026年10月3日：风险与恢复

[新增文献卡](PAPERS.md)分开对照鲁棒步态、跌倒起身、风险敏感策略和主动恢复。FastRLAP实证为RC车，Recovery RL关注约束安全，不能视为四足持续卡死的现成修复。先明确失败状态、有效进展和退出恢复条件，再提出可证伪的实验。
