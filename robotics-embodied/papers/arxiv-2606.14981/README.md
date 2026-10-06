# Inference-time Policy Steering via Vision and Touch

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.14981)

- **解决什么**：仅凭视觉选择动作难以判断细微接触状态，怎样结合长期目标与短时触觉改善执行。
- **核心方法**：相对直接执行Diffusion Policy，学习视觉触觉世界模型，用冻结视觉评分器先选模式，再由触觉潜表示与文本奖励引导局部动作编辑。
- **为什么在这个库里**：[动作模型干预讲义](../../fields/embodied-agents/action-model-intervention.md)中的感知向量与预测工具支线：解释哪些接触证据应交给专门组件。优先级：选读。
