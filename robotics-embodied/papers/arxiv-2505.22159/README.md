# ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2505.22159)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：VLA（视觉语言动作模型，一句话：用预训练视觉语言模型直接输出机器人动作的策略）在插拔、按压这类需要力控的接触密集任务上表现差，视觉被遮挡或接触动力学不确定时尤其如此。
- **核心方法**：以 [π0](../arxiv-2410.24164/README.md) 为基线，把 6 轴力/力矩反馈当作一等模态：在动作解码阶段加入力感知的混合专家融合模块 FVLMoE（混合专家，一句话：由门控按输入把信息路由给不同子网络），把预训练视觉语言特征与实时力信号融合；同时发布含视觉、本体和力信号的 ForceVLA-Data（5 个接触任务）。摘要报告平均任务成功率比 π0 系基线高 23.2%，插头插入最高 80% 成功。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向"观测输入"部件上的改动：在视觉、语言、本体之外加入力觉，对应开放问题"接触密集操作只靠视觉够不够"。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2505.22159（Yu 等 12 位作者；arXiv 注明 NeurIPS 2025）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2505.22159)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)（另见[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)）
