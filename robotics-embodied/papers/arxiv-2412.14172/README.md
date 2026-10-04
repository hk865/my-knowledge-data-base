# Learning from Massive Human Videos for Universal Humanoid Pose Control

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.14172)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：人形全身控制主要靠 RL 或遥操作，受限于仿真环境的多样性和示范采集成本；网络上的人类视频量大，却不能直接用于机器人。
- **核心方法**：从网络和学术数据集收集 16 万多段以人为中心的视频，依次做视频描述生成文本、3D 人体动作重建、重定向到人形机器人关键点、再用 RL 学出可在实机执行的关节目标，得到 Humanoid-X 数据集（163,800 个动作样本，超过 2000 万个带文本描述的人形姿态）；在其上训练 Transformer 模型 UH-1，把动作离散成 token，由文本指令自回归生成人形动作。在 Unitree H1-2 上实机测试。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向人形「数据来源」部件：把动捕换成网络视频，并把语言接口引入全身控制。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2412.14172
- 作者：Jiageng Mao、Siheng Zhao 等（共 10 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2412.14172)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
