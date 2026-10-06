# Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2510.16281)

- **解决什么**：视觉语言动作模型说出的子计划与实际动作可能不一致，怎样在执行前筛掉无法兑现计划的候选。
- **核心方法**：对已训练的推理型π0采样动作候选并在仿真中预测结果，由GPT-4o比较预期末态与语言子计划的一致性后选择执行。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中“预测后果再筛选”的前史，与VLS、VLA-Pilot的动作生成优化区别开。优先级：选读。
