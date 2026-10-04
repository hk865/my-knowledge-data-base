# OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.08858)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用运动学姿态作为统一接口，让人通过 VR 头显、RGB 相机或语言指令控制带灵巧手的全尺寸人形（Unitree H1），并能从遥操作示范或 GPT-4o 得到自主行为。可部署的策略只能拿到稀疏输入（头和手的位姿），作者写明这让 RL 优化变得困难。
- **核心方法**：相对 [H2O](../arxiv-2403.04436/README.md) 加入教师-学生：先用 RL 训练看全身特权信息的教师，再按 DAgger 框架（一句话：让学生自己走，由教师在学生到达的状态上给动作标签）把它蒸馏成只看稀疏输入和本体历史的学生，损失是学生与教师动作之差的平方。消融（表 1a）：同样带长历史的学生，用 DAgger 模仿教师成功率 94.10%，直接用 RL 训练只有 47.11%，作者写道没有 DAgger 时策略在长历史输入下难以学成；不带历史时两者是 93.80% 与 90.62%；教师为 94.77%。另发布了含六项日常任务的全身示范数据集 OmniH2O-6。作者自述依赖根部里程计，对分布外目标没有安全保证（§5）。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)「为什么绕不开模仿学习」一节中「教师-学生蒸馏本身就是模仿」的最直接证据：同一个学生，模仿教师比自己做 RL 高出约 47 个百分点；对照 [模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)中的 [DAgger](../arxiv-1011.0686/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2406.08858
- 作者：Tairan He、Zhengyi Luo、Xialin He、Wenli Xiao、Chong Zhang、Weinan Zhang、Kris Kitani、Changliu Liu、Guanya Shi（CMU 与上海交通大学）
- 发表：arXiv 页面未写会议；正式发表信息未核实
- 全文：[arXiv PDF](https://arxiv.org/pdf/2406.08858)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
