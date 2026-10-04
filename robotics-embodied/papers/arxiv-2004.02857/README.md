# Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2004.02857)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：导航图版本的 VLN 隐含已知拓扑、节点间瞬移、完美定位三个不现实的假设，成绩可能虚高。
- **核心方法**：把 R2R 搬到 Habitat 的连续环境里，智能体用前进、转向这类低层动作而不是在视点间跳转来执行同样的指令（VLN-CE）。77% 的 R2R 轨迹能转换，平均每条 55.88 个动作；最好模型测试 SPL 0.21，导航图上的 RCM 为 0.38。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 4 步与 [Baseline 页](../../fields/navigation-planning/BASELINES.md)"环境表示 + 局部执行"一行：此后 VLN 默认报告连续环境结果。优先级：必读。
