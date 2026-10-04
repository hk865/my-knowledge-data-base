# Generate, Track, Improve: Perceptive Multi-Skill Humanoid Locomotion with RL-Fine-Tuned Motion Generators

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.31577)

- **解决什么**：人形跟踪器会跟参考动作之后，还需要选出与眼前地形兼容的动作，以及应对训练外的技能组合。
- **核心方法**：深度图条件的流匹配生成器给全身参考轨迹，控制引导的 RL 跟踪器执行；用结构化探索收集回合，再以优势加权回归改进生成器。仿真消融测地形穿越和技能选择，G1 真机演示走跑、跳箱与楼梯。
- **为什么在这个库里**：把 [SONIC](../arxiv-2511.07820/README.md) 的“跟踪能力”与[运动控制](../../fields/control-locomotion/README.md)的“地形感知”放在同一问题下比较，也补[模仿与强化](../../fields/imitation-reinforcement-learning/README.md)里“RL 改生成器”的位置。优先级：选读；手工奖励、动作素材选择和纯深度缺少语义仍是边界。
