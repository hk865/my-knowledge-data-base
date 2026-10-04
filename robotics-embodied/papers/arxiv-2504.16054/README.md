# π0.5: a Vision-Language-Action Model with Open-World Generalization

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2504.16054)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VLA 在实验室中表现不错，但能否在没见过的真实家庭里泛化、完成长时程任务，仍不清楚。
- **核心方法**：在 [π0](../arxiv-2410.24164/README.md) 基础上用异构数据协同训练：除约 400 小时移动操作机器人在多户真实家庭中采集的数据外，还用其他（非移动）机器人数据、实验室数据、高层子任务预测、人在旁边逐步口头指导的数据和网络视觉语言数据（第一阶段 97.6% 的样本不是家庭中的移动操作数据）。两阶段训练：预训练用 FAST token 表示动作，后训练加上 π0 式流匹配动作专家；推理时先预测语义子任务（如「拿起砧板」），再据此生成低层动作块。在训练中没出现过的新家庭里完成清理厨房、卧室这类长时程灵巧任务。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向「数据」与「层级推理」两个部件：作者的实验显示，来自其他机器人、高层语义预测和网络数据的知识迁移是泛化的关键；后续的 [π0.7](../arxiv-2604.15483/README.md) 在它之后。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2504.16054
- 题名：arXiv 页面题名写作 `$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization`。
- 作者：Physical Intelligence、Kevin Black 等（共 36 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2504.16054)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
