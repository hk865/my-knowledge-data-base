# BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2508.08241)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：从人类动作数据学人形技能时，已有方法要么动作不自然，要么要为每段动作单独调参；而且只会模仿特定动作或特定目标，难以组合技能去解没见过的任务。
- **核心方法**：两层：先用一套紧凑的动作跟踪设定（motion tracking，一句话：训练策略让机器人逐帧复现参考动作，路线起点见 [DeepMimic](../arxiv-1804.02717/README.md)），用同一组超参学会侧空翻、旋踢、冲刺等高动态动作；再训练一个统一的潜空间扩散模型，借分类器引导（classifier guidance，一句话：采样时用目标函数的梯度把扩散生成推向新目标）在测试时完成训练中没见过的任务，包括动作补全、摇杆遥操作和避障，并零样本迁移到实机。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向人形分支"从动作跟踪到通用控制"一格的代表，也是 [GMR](../arxiv-2510.02252/README.md) 用来训练策略的跟踪器。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2508.08241（Liao、Truong、Huang、Gao、Tevet、Sreenath、Liu；当前 v4，2025-11）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2508.08241) · 项目页：[beyondmimic.github.io](https://beyondmimic.github.io/)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
