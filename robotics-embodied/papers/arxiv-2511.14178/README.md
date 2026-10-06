# Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2511.14178)

- **解决什么**：动作模型在新场景中的零样本部署成功率低，怎样借助视觉语言推理调整候选动作并利用执行反馈。
- **核心方法**：相对直接执行扩散策略，让冻结GPT-4o编写黑盒奖励，以进化式候选选择和加噪—去噪迭代优化动作，再用执行反馈修改奖励。
- **为什么在这个库里**：[动作模型干预讲义](../../fields/embodied-agents/action-model-intervention.md)中“黑盒奖励搜索”的前史，便于与VLS的梯度引导对读；实验基座为DiVLA/RDT-1B。优先级：必读。 [技术精读](reading.md)。
