# Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2605.30280)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：操作、导航等具身任务通常各用专门模型，能力割裂，跨任务、环境和机器人本体的泛化有限。
- **核心方法**：把 Qwen 的视觉语言模型从感知、理解、推理扩展到连续动作与轨迹生成：接一个 DiT（扩散 Transformer）动作解码器；用本体描述提示（embodiment-aware prompt，一句话：用文字说明当前是哪种机器人、采用什么控制约定）支持多平台；把操作、导航和轨迹预测统一成"动作与轨迹预测"，在操作轨迹、人类第一视角示范、合成仿真、视觉语言导航和辅助视觉语言数据上联合预训练。Instruct 版报告 LIBERO（一句话：桌面操作仿真基准）成功率 97.9%、[R2R](../r2r/README.md) 导航的 OSR（一句话：轨迹中任一点进入目标范围即算成功的比例）69.0% 等结果。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向"跨本体、跨任务统一"的大模型路线代表，把[导航与规划](../../fields/navigation-planning/README.md)里的视觉语言导航也并进同一个动作模型。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2605.30280（Wang 等 40 位作者；当前 v2，2026-06）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2605.30280)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)（另见[导航与规划](../../fields/navigation-planning/README.md)）
