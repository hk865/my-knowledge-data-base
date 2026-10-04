# InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.12195)

- **解决什么**：长视频任务需要多轮取证，保留更多视频和工具记录又使注意力缓存迅速增长。
- **核心方法**：MCR 将观察、工具结果与记忆组织成迭代推理上下文；M²LA 用低维潜状态压缩 KV 缓存，同时保留输入 token，再经分阶段训练恢复和提升能力。
- **为什么在这个库里**：把 [视频与时序路线](../../fields/video-temporal/ROADMAP.md)从“帧数预算”接到“缓存与反复取证”。优先级：选读。
