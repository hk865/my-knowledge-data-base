# In-Context Imitation Learning via Next-Token Prediction

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2408.15980)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：机器人策略遇到新任务通常要微调；能否像大语言模型那样，在输入中给几条示范就执行新任务、不更新参数？
- **核心方法**：ICRT（In-Context Robot Transformer）是一个按 Llama2 结构搭建的因果 Transformer（默认是随机初始化的 12 层 Base 版），在由图像观测、本体状态和动作组成的感知运动轨迹上做自回归预测，不用语言和奖励；推理时把新任务的遥操作示范轨迹作为提示放在前面，模型据此执行。先在 DROID 上预训练，再在作者采集的多任务数据上微调。在 Franka 机械臂上，对未见任务的泛化显著优于微调后的 Octo 和加了动作块的 OpenVLA。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向「任务怎样指定」这一部件的一种答案：用示范轨迹而不是语言作提示，与 [Behavior Prompting Policy](../arxiv-2606.30457/README.md) 同属「示范即提示」。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2408.15980
- 作者：Letian Fu、Huang Huang 等（共 8 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2408.15980)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
