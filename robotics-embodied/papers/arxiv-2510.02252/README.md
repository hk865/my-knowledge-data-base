# Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.02252)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：人形动作跟踪先要把人体动作重定向（retargeting，一句话：把人体骨架动作映射成机器人关节轨迹）到机器人上；重定向留下的脚滑、自穿透、物理不可行等瑕疵，通常留给 RL 策略靠大量奖励调参和域随机化去弥补。
- **核心方法**：在压住奖励调参的条件下，统一用 [BeyondMimic](../arxiv-2508.08241/README.md) 训练跟踪策略，比较两个开源重定向器（PHC、ProtoMotions）、Unitree 的闭源高质量数据和新提出的 GMR。在 LAFAN1（一个人体动作捕捉数据集）子集上，多数动作都能跟踪，但重定向瑕疵显著降低策略鲁棒性，动态或长序列尤甚；GMR 在跟踪表现和对原动作的忠实度上都优于开源方法，接近闭源基线。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向人形分支"参考动作数据质量"这一部件：说明跟踪效果有一部分取决于数据前处理，而不只取决于策略和奖励。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2510.02252（Araujo、Ze、Xu、Wu、Liu；v1，2025-10）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2510.02252)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
