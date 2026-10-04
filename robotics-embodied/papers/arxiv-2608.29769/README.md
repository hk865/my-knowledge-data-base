# Learning Agile Perceptive Traversal of Sparse 3D Structures for Humanoids

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2608.29769)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：[AME-2](../arxiv-2601.08485/README.md) 只用 2.5D 高程图，作者自述不处理完全三维的运动；人形要跳上单杠、悬吊攀爬（brachiation）、再落地，或者钻过头顶只有 2 cm 粗的横杆，这些稀疏的三维结构在高程图里表示不出来，而且杆在头顶时传感器常常看不全。
- **核心方法**：ETH RSL（Hutter 组，第二作者 Chong Zhang 是 AME-1/AME-2 的第一作者）在 PM-01 人形上装头戴固态激光雷达，不建高程图，把原始激光回波按 2D 扫描网格保留（每格存相对传感器的命中位置与距离），用改编自 AME-2 的注意力编码器加 GRU 记忆处理，并加一个预测杆中心线的辅助损失。训练是分相位的教师-学生：起跳、攀爬、落地三个特权教师（看杆端点、接触状态、机身速度、电池与温度）用 RL 分别训出，学生先 DAgger 行为克隆、再预热 critic、最后做带衰减行为锚定的正则化 PPO；不用人体动作数据。真机三种杆配置下"起跳→攀爬→落地"15 次成功 14 次，攀爬速度 0.5 m/s；另一个策略钻过 2 cm 横截面的横杆，10 次试验。
- **为什么在这个库里**：[运动控制方向](../../fields/control-locomotion/README.md#从本体状态到环境状态)"从本体状态到环境状态"一线（Lee 2020 → Miki 2022 → AME-1/AME-2）的最新节点：环境状态从高程图换成带记忆的原始三维回波；训练又是"先模仿教师、再用 RL 补"的组合。作者自述只有几个分开训练的任务策略，对更多样几何的鲁棒性还没有证明，需要长程空间记忆的部分可观测结构留作后续。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2608.29769（Ongan、Zhang、Sun、Cramariuc、Cadena、Hutter；ETH Zurich Robotic Systems Lab、ETH AI Center、Computer Vision and Geometry Group；v1，2026-08-30）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2608.29769)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)（另见[感知](../../fields/perception/README.md)）
