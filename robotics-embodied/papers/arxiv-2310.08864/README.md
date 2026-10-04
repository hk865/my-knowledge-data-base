# Open X-Embodiment: Robotic Learning Datasets and RT-X Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.08864)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：机器人学习通常每个应用、每台机器人、甚至每个环境单独训练一个模型；问题是能否像 NLP 和视觉那样，用多种机器人的数据训练出可迁移的通用策略。
- **核心方法**：21 家机构合作，把 22 种机器人本体的 60 个已有数据集统一成标准格式，得到 100 万条以上真机轨迹的 Open X-Embodiment 数据集；在其中 9 种机械臂的混合数据上训练 RT-1-X（RT-1 架构）和 RT-2-X（RT-2 架构，最大 55B）。在 5 个数据量较小的机构任务上，RT-1-X 的平均成功率比各机构原方法和单独训练的 RT-1 高 50%（同一架构，提升来自混合数据）；在 Google 机器人上评测只出现在 WidowX 数据中的技能，RT-2-X 约为 RT-2 的 3 倍。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向「数据」部件的基线：跨本体数据集，此后 [Octo](../arxiv-2405.12213/README.md)、[OpenVLA](../openvla/README.md) 都在它上面预训练。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2310.08864
- 作者：Open X-Embodiment Collaboration、Abby O'Neill 等（共 294 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2310.08864)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
