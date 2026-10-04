# Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization

> 状态：逐步教学版 · 2026 · [原文](https://arxiv.org/abs/2608.26103)

[返回机器人与具身目录](../../README.md)

- **解决什么**：零样本跨任务泛化：策略要执行训练中从未见过的操作任务。
- **核心方法**：借鉴大语言模型的上下文学习，把一段人类视频当作任务说明：因果视频—动作模型 Zero-WAM 依据上下文里的人类视频执行新任务。为解决成对数据稀缺，自动把按任务采样的机器人轨迹转成语义对应的人类视频，得到 HumanGen（8.6K 个任务、7.42 万对）；训练加入上下文未来块预测（IFP）目标，抑制从已见任务学到的捷径，迫使策略从视频提示里取任务信息。RoboTwin 2.0（一句话：双臂操作仿真基准）的 7 个未见任务平均成功率 47.0%，比最强的视频—动作基线高 29.5 个百分点。
- **为什么在这个库里**：[世界模型与行动预测](../../fields/world-models/README.md)方向"视频—动作模型"一格；与 [BPP](../arxiv-2606.30457/README.md)、[ICRT](../arxiv-2408.15980/README.md) 同属"用示范做提示"。优先级：选读。

## 阅读入口

- [逐步教学版](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json) · [作者归属与许可](ATTRIBUTION.md)

## 身份信息

- 稳定标识：arxiv:2608.26103（Zhou 等 12 位作者；当前 v2，2026-08）
- 全文：[arXiv PDF v2](https://arxiv.org/pdf/2608.26103v2) · 项目页：[Zero-WAM](https://robbyant-research.github.io/Zero-WAM/)
- 方向：[世界模型与行动预测](../../fields/world-models/README.md)（另见[视觉语言动作模型](../../fields/vla/README.md)、[具身 Agents](../../fields/embodied-agents/README.md)）
