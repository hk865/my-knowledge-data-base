# NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.07896)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：到达图像目标与无目标探索通常用两个模型，能否用一个足够有表达力的策略同时做。
- **核心方法**：在 [ViNT](../arxiv-2306.14846/README.md) 的 Transformer 编码上加目标遮罩（训练时以 50% 概率遮住目标），动作由扩散策略直接生成，不再生成子目标图像。探索成功率 98%（子目标扩散 77%），碰撞更少，参数 19M 对 335M。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)Baseline 页"全局决策 + 局部执行"一行；扩散策略的机制见 [Diffusion Policy 精读](../diffusion-policy/reading.md)。优先级：存档。
