# Large Behavior Models and Atlas Find New Footing

> 状态：文献卡 · 2025 · [原文](https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：Atlas 要做边走边操作的长任务（整理、搬运零件），逐个行为手写或逐任务编程跟不上；要让"能示范出来的事，机器人就能学会"。
- **核心方法**：Boston Dynamics 与 TRI 合作。数据靠 VR 全身遥操作采集：遥操作建在 Boston Dynamics 的 MPC 系统上，Atlas 的站姿、支撑多边形和迈步意图跟随操作者。策略是 450M 参数的扩散 Transformer，用 flow matching 损失训练；输入头部立体相机图像（30 Hz）、本体感知和语言提示，输出夹爪、颈部偏航、躯干位姿、双手位姿和左右脚位姿，每次预测 48 步（1.6 秒）、执行约 24 步；脚的位姿交给下层 MPC 去稳定实现。多任务、多本体训练，数据来自 Atlas（50 自由度）、上半身测试台（29 自由度）和 TRI 的 Ramen 机器人，含仿真数据。推理时不改训练就能把执行速度提高 1.5–2 倍。作者把夹爪力控、更多样的数据来源、对 VLA 做 RL 列为后续工作。
- **为什么在这个库里**：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)方向"大规模真实示范"在人形全身上的公司版本：上层纯模仿、下层仍是 MPC，与 [Figure Helix 02](../figure-helix-02/README.md)（下层是用人体动作加仿真 RL 训出的全身控制器）形成对照；也补全了[运动控制方向](../../fields/control-locomotion/README.md#工业界方案成熟在哪里没公开什么)里 Boston Dynamics 一行"保留已验证的模型控制器"的做法。优先级：选读。

## 身份信息

- 稳定标识：url:https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/（Boston Dynamics 官方博客，与 Toyota Research Institute 合作，2025-08）
- 方向：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)（另见[运动控制与腿足运动](../../fields/control-locomotion/README.md)、[VLA](../../fields/vla/README.md)）
