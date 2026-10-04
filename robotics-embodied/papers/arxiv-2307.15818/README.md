# RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2307.15818)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让在网络规模数据上训练的视觉语言模型（VLM）的语义知识直接进入端到端机器人控制，使策略能泛化到机器人数据中没有的物体、指令和简单推理。
- **核心方法**：相对 [RT-1](../arxiv-2212.06817/README.md) 从头训练的专用网络，改用 PaLI-X、PaLM-E 两种预训练 VLM（最大 55B 参数）：每个连续动作维度均匀分成 256 个桶，用整数 token 像文本一样输出；用机器人轨迹和原有网络视觉语言数据混合微调（co-fine-tuning），而不是只用机器人数据。约 6000 次真机评测中，在未见物体、背景、环境上的平均表现约为 RT-1 和 MOO 的 2 倍；在需要语义理解的新指令上（如把物体放到某个数字或图标上、挑最小的物体），成功率是 RT-1 的 2–3 倍。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向的命名之作，「动作表示 = 离散 token」一格的起点：[OpenVLA](../openvla/README.md) 用 7B 开放底座复现这条路线，[FAST](../arxiv-2501.09747/README.md) 改进逐维分桶，[π0](../arxiv-2410.24164/README.md) 改用连续动作头。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2307.15818
- 作者：Anthony Brohan、Noah Brown 等（共 54 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2307.15818)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
