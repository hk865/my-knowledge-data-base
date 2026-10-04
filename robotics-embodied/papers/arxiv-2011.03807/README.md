# Sim-to-Real Transfer for Vision-and-Language Navigation

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2011.03807)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：仿真里训练的 VLN 策略放到真实机器人上会怎样，离散动作怎样接到连续运动上。
- **核心方法**：在 VLN 策略与 TurtleBot2 之间加一个子目标模型，把"去下一个视点"预测成机器人附近的航点，配合域随机化；在 325 m² 办公室、1.3 km 指令上测试。仿真 55.9%，真机有预建地图 46.8%，没有地图 22.5%；子目标落在真值 0.5 m 内的只有 29%，窄缝处最难。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 4 步：本方向少有的同一策略仿真与真机的成对数字，量化了 sim-to-real 与狭窄通道的损失。优先级：必读。
