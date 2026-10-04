# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> 状态：逐步教学版 · 2023 · [原文](https://arxiv.org/abs/2303.04137)

[返回机器人与具身目录](../../README.md)

- **解决什么**：从人类示范学视觉运动策略时，同一画面下示范常有几种都正确的做法（多峰）；回归会把它们平均成一个错误动作，逐步独立采样又会在两种做法之间来回跳。
- **核心方法**：把策略写成以观测为条件的去噪扩散过程：从噪声出发逐步去噪，生成一整段未来动作，再滚动执行（预测一段、只执行前几步、然后重新预测）。相对显式的多峰策略 LSTM-GMM（输出高斯混合）、BET（离散行为类别加修正量）和隐式能量策略 IBC（给观测—动作对打能量分，再搜索低能量动作），在 4 个操作基准的 12 个任务上平均提升 46.9%。
- **为什么在这个库里**：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)方向的生成式策略基线，也是[视觉语言动作模型](../../fields/vla/README.md)方向"动作头 = 扩散 / 流匹配"一格的源头，[π0](../arxiv-2410.24164/README.md) 的流匹配动作专家沿这条路线。优先级：必读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 阅读顺序

教学顺序：[DDPM](../../../multimodal/papers/ddpm/README.md)（扩散模型怎样从噪声生成数据）→ 本篇。

## 身份信息

- 稳定标识：arxiv:2303.04137（Chi、Xu、Feng、Cousineau、Du、Burchfiel、Tedrake、Song；RSS 2023，v5 为期刊扩展版，2024-03）
- 全文：[arXiv PDF v5](https://arxiv.org/pdf/2303.04137v5)
- 方向：[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)（另见[视觉语言动作模型](../../fields/vla/README.md)）
