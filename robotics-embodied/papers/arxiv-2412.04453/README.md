# NaVILA: Legged Robot Vision-Language-Action Model for Navigation

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.04453)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让足式机器人听自然语言导航，同时能在复杂地形上稳定行走；从语言直接到关节动作很难。
- **核心方法**：两层：微调 VILA 视觉语言模型输出"向前 75 cm""右转 30 度"这类中层语言动作，再由带视觉的 RL 运动策略执行；训练数据加入 YouTube 第一人称游览视频。R2R-CE 成功率 54%，真机 25 条指令 88%；失败来自偏离后无法纠错。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 5 步：VLA 与足式 RL 运动策略的接口写成语言，底层与[运动控制](../../fields/control-locomotion/README.md)的四足策略同类。优先级：必读。
