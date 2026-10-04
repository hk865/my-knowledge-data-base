# SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2506.01844)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：现有 VLA 动辄数十亿参数，训练和部署都贵；训练数据也集中在学术和工业数据集，没有用上低成本机器人平台上社区采集的数据。
- **核心方法**：沿用 [π0](../arxiv-2410.24164/README.md) 的"视觉语言模型 + 流匹配动作专家输出动作块"结构（流匹配，一句话：学习把噪声连续搬运成动作的速度场，可看作扩散的一种连续形式），缩小到约 4.5 亿参数（SmolVLM-2 底座，动作专家约 1 亿），用社区数据训练；再加一套异步推理，把感知与动作预测从动作执行中解耦，上一段动作块还在执行时就计算下一段。单卡可训，可部署到消费级 GPU 甚至 CPU，摘要称性能与约 10 倍大的 VLA 相当。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向"规模与部署"一侧的参照：在同一动作头路线下把模型做小，并单独处理推理延迟；代码、模型与数据随 LeRobot 开放，是自己上手复现 VLA 成本最低的入口之一。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2506.01844（Shukor 等 14 位作者，Hugging Face；v1，2025-06）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2506.01844) · 代码：[huggingface/lerobot](https://github.com/huggingface/lerobot)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)）
