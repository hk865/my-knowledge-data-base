# RT-1: Robotics Transformer for Real-World Control at Scale

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2212.06817)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视觉和语言领域靠大规模、多样的预训练数据得到能零样本或少样本解决下游任务的模型；机器人领域还没有证明这一点，因为真实机器人数据很难采集。
- **核心方法**：用 13 台机器人在 17 个月里采集 13 万条示范、覆盖 700 多条任务指令，训练 35M 参数的 Robotics Transformer：6 帧历史图像经 FiLM（一句话：用语言嵌入逐通道缩放和平移图像特征）条件化的 EfficientNet 编码，TokenLearner 压缩视觉 token 后送入 Transformer，输出离散化的机械臂与底盘动作，以 3 Hz 闭环控制。训练指令上成功率 97%；对新任务、干扰物、新背景的泛化分别比次优基线高 25%、36%、18%。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向的起点基线：确立「大规模真机示范 + Transformer + 离散动作」的配方；[RT-2](../arxiv-2307.15818/README.md) 换上网络预训练的 VLM 底座，[Open X-Embodiment](../arxiv-2310.08864/README.md) 把数据扩展到多机构、多本体。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2212.06817
- 作者：Anthony Brohan、Noah Brown 等（共 51 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2212.06817)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
