# FOCUS: Object-Centric World Models for Robotics Manipulation

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2307.02427)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：操作任务大多需要机器人与物体交互，而从整幅图像学到的世界模型不区分物体，强化学习探索时容易只学会挥动手臂、很少碰物体。
- **核心方法**：在 DreamerV2 式的模型化强化学习智能体（在世界模型"想象"出的轨迹上训练策略）里，把潜状态拆成按物体的表示，并为每个物体解码分割掩码；再用"最大化物体潜表示的熵"作为探索奖励，鼓励改变物体的状态。在 ManiSkill2 与 robosuite 的稠密奖励任务上比 DreamerV2 学得更快，探索阶段与物体的交互更多，之后适配稀疏奖励任务更容易；在 Franka 机械臂上做了真机演示。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"① 表示"一行：对象中心表示接入 [DreamerV3](../dreamerv3/README.md) 这条"在想象中学策略"路线的例子。做不好的场景：训练需要被关注物体的分割掩码（仿真由模拟器提供，真机靠 SAM 流水线补）；每个物体用独热向量标识，要事先知道物体的数量和身份（Sec.6）。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2307.02427 · [全文 PDF](https://arxiv.org/pdf/2307.02427) · 根特大学（Ghent University）
- 方向：multimodal/world-models、robotics/embodied-policies
