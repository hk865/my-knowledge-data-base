# DD-PPO: Learning Near-Perfect PointGoal Navigators from 2.5 Billion Frames

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1911.00357)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：仿真强化学习的资源消耗大，需要可扩展的分布式训练来学习无地图的点目标导航。
- **核心方法**：去中心化、同步的分布式 PPO（DD-PPO），128 块 GPU 上比串行快 107 倍；在 Habitat 中训练 25 亿步，RGB-D 加 GPS+Compass 时测试集 SPL 0.948、成功率 0.980；去掉 GPS+Compass 后 SPL 只有 0.15。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 4 步：仿真规模化的代表，同时说明"近乎完美"依赖完美定位。优先级：选读。
