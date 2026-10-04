# Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.04436)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：只用一个 RGB 相机，让人实时遥操作全尺寸人形机器人（Unitree H1）做全身动作。难点之一是人体动作数据里有大量人形做不到的动作，例如侧手翻、步幅比腿还宽的跨步（§I）。
- **核心方法**：提出「sim-to-data」筛数据：先在仿真里训练一个看特权信息、不做域随机化的动作模仿器去模仿全部重定向数据，它模仿不了的片段视为不可行；AMASS 的约 1 万段重定向动作中保留 8.5k 段（§IV-B）。再用清洗后的数据训练可部署的实时模仿策略，零样本上真机。在全部 1 万段上评估，不做筛选的版本成功率 67.9%，H2O 为 72.5%；特权模仿器为 85.5%（表 III）。清洗后数据只用 0.1%、1%、10% 时成功率为 52.0%、58.8%、61.3%（表 IV）。作者自述在不可行或损坏的动作上训练会大幅损害性能，而动作是否可行因机器人而异，目前还没有系统判断可行性的算法（§VII）；实机实验中机身线速度由动作捕捉系统提供，作者说可以换成机载里程计（§VI）。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)「为什么绕不开模仿学习」一节中，人形「从人体动作重定向」一支的代表：模仿要的不只是数据，还要先筛掉机器人做不到的数据。同组的 [OmniH2O](../arxiv-2406.08858/README.md) 在它之上加入教师-学生蒸馏。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2403.04436
- 作者：Tairan He、Zhengyi Luo、Wenli Xiao、Chong Zhang、Kris Kitani、Changliu Liu、Guanya Shi（CMU）
- 发表：arXiv 页面未写会议；正式发表信息未核实
- 全文：[arXiv PDF](https://arxiv.org/pdf/2403.04436)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
