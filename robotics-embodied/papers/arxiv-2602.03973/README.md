# VLS: Steering Pretrained Robot Policies via Vision-Language Models

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2602.03973)

- **解决什么**：预训练动作策略遇到新物体、位置或任务要求时，怎样在部署期间用语言条件引导动作，而不重新训练整个策略。
- **核心方法**：相对直接执行 π0.5 的动作块，让视觉语言模型生成可微奖励程序，在扩散或流匹配采样中用奖励梯度调整候选，并加入多粒子搜索。
- **为什么在这个库里**：[具身 Agent 基线表](../../fields/embodied-agents/BASELINES.md)中“动作生成时引导”的直接 π0.5 案例，与候选筛选、环境整理形成可比较的干预位置。优先级：必读。 [技术精读](reading.md)。
