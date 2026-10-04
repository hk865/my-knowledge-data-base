# π0: A Vision-Language-Action Flow Model for General Robot Control

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2410.24164)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：通用机器人策略要做叠衣服、收拾桌面、装箱这类高灵巧任务，需要连续、高频的动作输出；RT-2、OpenVLA 一类自回归离散 token 的 VLA 在这类任务上很吃力。
- **核心方法**：底座是 PaliGemma（Google 的 3B 开放视觉语言模型），另加一组约 300M 参数、从零初始化的「动作专家」权重，专门处理机器人状态和动作，用条件流匹配（一句话：学习把噪声连续变换成动作的速度场，与扩散同类）生成连续动作块，控制频率最高 50 Hz。预训练用约 1 万小时数据，来自 7 种机器人构型、68 个任务，再加 Open X-Embodiment；之后可直接按语言执行、接受高层 VLM 给的子指令，或微调到复杂下游任务。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向「动作表示 = 连续动作块（流匹配）」一格的代表，与 [OpenVLA](../openvla/README.md) 的离散 token 构成本方向的主要对照；[π0.5](../arxiv-2504.16054/README.md) 的后训练沿用这一动作专家，[GR00T N1](../arxiv-2503.14734/README.md) 同样用流匹配生成动作。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2410.24164
- 题名：arXiv 页面题名写作 `$π_0$: A Vision-Language-Action Flow Model for General Robot Control`。
- 作者：Kevin Black、Noah Brown 等（共 24 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2410.24164)
- 发表：RSS 2025（arXiv 注释）
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
