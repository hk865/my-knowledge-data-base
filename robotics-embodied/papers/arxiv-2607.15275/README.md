# RoboTTT: Context Scaling for Robot Policies

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.15275)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：现有机器人基础模型只看单步或很短的历史，长时程多阶段任务、从示范中即时模仿、执行中自我改进都受限。
- **核心方法**：在 [GR00T N1](../arxiv-2503.14734/README.md) 系列的 N1.7 上，给 16 层 DiT 各加一层测试时训练层（TTT，一句话：循环状态是一组"快权重"，训练和推理时都用梯度下降更新，把历史压进权重里），把视觉运动上下文扩到 8K 步而不增加推理延迟；训练时用序列动作强制和截断的随时间反向传播来拉长上下文。真机操作任务上整体比单步上下文的 N1.7 基线高 87%，并完成一个 5 分钟、10 阶段的装配任务；8K 上下文比 1K 预训练高 62%。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向"观测历史长度"这一部件，回答开放问题"VLA 要不要记忆、怎样记"；对照 [OpenVLA](../openvla/README.md) 的单帧输入读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2607.15275（Jiang 等 11 位作者，NVIDIA GEAR；v1，2026-07）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2607.15275)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)）
