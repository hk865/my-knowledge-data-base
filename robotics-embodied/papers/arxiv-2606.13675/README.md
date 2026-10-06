# Improving Robotic Generalist Policies via Flow Reversal Steering

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.13675)

- **解决什么**：现成通用动作策略在新任务上的采样先验不合适，怎样把VLM或人的粗粒度方向转成更可靠的连续动作。
- **核心方法**：相对直接采样π0.5，把参考动作经反向流映射成噪声，再正向去噪生成动作；还可由成功轨迹训练辅助噪声策略。
- **为什么在这个库里**：[动作模型干预讲义](../../fields/embodied-agents/action-model-intervention.md)中“参考动作—噪声接口”的近期代表，与VLS奖励梯度及PPS向量场残差对读。优先级：必读。
