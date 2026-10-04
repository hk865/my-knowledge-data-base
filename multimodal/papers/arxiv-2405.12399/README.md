# Diffusion for World Modeling: Visual Details Matter in Atari

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.12399) · NeurIPS 2024

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：DreamerV2/V3、IRIS 等世界模型把环境压成一串离散潜变量，以减少多步预测的误差累积；作者认为这种压缩会丢掉对决策重要的小细节，例如驾驶时远处的红绿灯或行人。
- **核心方法**（DIAMOND）：不压成离散潜变量，直接用扩散模型以过去几帧（帧堆叠）和动作为条件生成下一帧，智能体完全在这个"梦"里训练。关键设计是采用 EDM 形式的扩散：DDPM 在少步去噪时误差迅速累积、轨迹漂出分布，EDM 一步也稳定，因为动作后果可能多峰而取 3 步。Atari 100k 上平均人类归一化分 1.46，在 Asterix、Breakout、Road Runner 这类小细节重要的游戏上优势明显；对比可视化中 IRIS 的敌人与奖励来回互换、Breakout 的分数前后不一致，DIAMOND 的分数按规则正确加分。同一模型放大到 381M 参数、在 87 小时 CS:GO 录像上训练后可在 RTX 3090 上以 10Hz 交互，但靠近墙壁或视野丢失时会忘记当前状态、凭空换出新武器或新区域，还会错误地允许空中连跳。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)中"潜变量模型忽略任务相关的小物体"这一坑的直接证据，也是从 Dreamer 一线（压缩后在潜空间学）转到像素级扩散世界模型的转折点；与 [GameNGen](../arxiv-2408.14837/README.md)、[Genie 2](../genie-2-blog/README.md) 同期。作者自述记忆只靠帧堆叠，规模也修不好记忆。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2405.12399 · [全文 PDF](https://arxiv.org/pdf/2405.12399v2) · University of Geneva、University of Edinburgh、Microsoft Research
- 方向：multimodal/world-models、multimodal/generation
