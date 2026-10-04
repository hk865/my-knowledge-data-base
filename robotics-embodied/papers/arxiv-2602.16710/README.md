# EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2602.16710)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：灵巧手的遥操作数据贵而少；人类第一视角视频多，但此前的利用规模小，也不清楚人类数据的规模能否可预测地换来机器人上的表现。
- **核心方法**：用 SLAM 估计相机运动、用手部姿态估计取 21 个手部关键点，把 20,854 小时第一视角人类视频标成动作（腕部相对位姿，加上经优化重定向到灵巧手关节空间的手指动作），规模比此前的工作大 20 倍以上；另加 829 小时 Apple Vision Pro 采集的高精度数据。模型是 VLM 骨干加 DiT 流匹配动作专家，不同机械手只换输入输出的适配层。训练分三段：人类数据预训练，约 50 小时人-机对齐数据的中期训练，按任务的机器人后训练。人类动作预测的验证损失随数据小时数呈对数线性下降（R² = 0.9983），并且能预测真机表现；在 22 自由度的灵巧手上，平均成功率比不做人类预训练高 54%；没见过的叠衬衫只给 1 条机器人示范即达 88%。
- **为什么在这个库里**：[VLA 方向](../../fields/vla/README.md)开放问题"真机数据之外的数据能顶多少"的直接证据，也是 NVIDIA 数据金字塔路线（[GR00T N1](../arxiv-2503.14734/README.md)）的延续：GR00T N1.7 的官方说明写明把这 2 万小时放进了预训练。从[模仿学习](../../fields/imitation-reinforcement-learning/README.md)的角度看，它模仿的是人手而不是机器人。作者写明尺度律不外推到测量范围以外，在测到的范围内还没有饱和。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2602.16710（Zheng、Niu 等 15 位作者，NVIDIA、UC Berkeley、University of Maryland 等；v1，2026-02-18）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2602.16710)
- 方向：[视觉-语言-动作模型](../../fields/vla/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)）
