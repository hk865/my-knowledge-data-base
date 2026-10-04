# Acceptance-Aware Draft Model Training for Speculative Decoding

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.24150)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：常见蒸馏损失逐位置拟合目标概率，却没有直接优化"首个拒绝前连续通过多长"，贪心与随机采样的接受机制又不同。
- **核心方法**：相对逐 token 的 KL 损失，EAL 围绕目标 top-1 的连续一致构造窗口代理目标，WTV 围绕温度缩放后两分布的重叠构造窗口目标；另探索用模拟接受长度作奖励的 GRPO 阶段。
- **为什么在这个库里**：[推理基线](../../fields/inference/BASELINES.md)的"草稿训练"一格，把[导读](../../fields/inference/draft-verification-guide.md)中可手算的接受质量接到训练损失。优先级：选读。

## 身份信息
- 作者：Tianhua Xia、Mugilan Ganesan、Yifei Feng、Haiyu Wang、Maximilian Egger、Sai Qian Zhang
- 稳定标识：arxiv:2609.24150 · [全文](https://arxiv.org/html/2609.24150v1)
- 方向：llm/inference

## 批注

**易误读**
- 窗口目标在固定训练前缀上计算，§3.1 使用条件独立假设；它是训练代理目标，不能直接解释为任意自由生成轨迹的无条件精确期望。
- 实验主要报告 batch 1 的接受长度；接受更长不自动等于端到端更快。训练损失也不替代推理时的正确验证与残差补样。

**未核实 / 待验证**
- 当前按 2026-09-21 预印本 v1 解释；跨服务引擎和大批量的时延收益待验证。
