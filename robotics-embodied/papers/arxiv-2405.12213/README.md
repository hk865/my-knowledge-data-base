# Octo: An Open-Source Generalist Robot Policy

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.12213)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：通用机器人策略要真正好用，需要能接入不同的传感器和动作空间、适配多种平台，并能高效微调到新环境；开放且能灵活改输入输出的通用策略此前还很少。
- **核心方法**：在 Open X-Embodiment 的 80 万条轨迹上训练 Transformer 策略（27M 与 93M 两个尺寸），任务可用语言或目标图像指定；采用块状注意力掩码并插入读出 token（作用类似 BERT 的 [CLS]，汇总到当前为止的观测序列），读出 token 后接一个小的扩散动作头，预测动作块（一句话：一次预测未来连续若干步的动作）。微调时可以新增或移除观测与任务输入，在消费级 GPU 上几小时适配新的传感器和动作空间；在 9 个机器人平台上验证。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向中「不用 VLM 底座的开放通用策略」代表，与 [OpenVLA](../openvla/README.md)（7B VLM + 离散 token）对照：小模型 + 扩散动作头 + 灵活输入输出。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2405.12213
- 作者：Octo Model Team、Dibya Ghosh 等（共 19 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2405.12213)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
