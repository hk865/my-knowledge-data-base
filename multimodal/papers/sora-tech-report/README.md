# Video generation models as world simulators

> 状态：文献卡 · 2024 · [原文](https://openai.com/index/video-generation-models-as-world-simulators/)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：此前的视频生成大多只针对窄类数据、短视频或固定尺寸；OpenAI 想把大语言模型"在互联网规模数据上训练出通用能力"的路子搬到视觉数据上。
- **核心方法**：先用视频压缩网络把视频在时间和空间上同时压缩，再切成时空 patch（一句话：压缩后视频里的一小块时空立方体）当作 Transformer 的 token，用扩散 Transformer（沿用 DiT）在原生分辨率、时长和长宽比上训练，图像当作单帧视频一起训练；用 DALL·E 3 的重新标注技术给全部视频生成详细描述。最长生成一分钟高清视频。报告只给方法方向与定性结果，明说不含模型与实现细节。
- **为什么在这个库里**：[观点页：生成收敛](../../../perspectives/generative-convergence.md)阶段四的起点，也是"从视频生成到世界模型"一节的第一条证据：标题即"视频生成模型作为世界模拟器"，并列出物理与长时一致的失败案例。作者 Bill Peebles 是 DiT 第一作者，连接 [视觉生成领域页](../../fields/generation/README.md)的 DiT 节点。优先级：必读。

## 身份信息

- 稳定标识：url:https://openai.com/index/video-generation-models-as-world-simulators/ · OpenAI · 官方技术报告页面，2024-02-15
- 方向：multimodal/generation、multimodal/video-temporal、multimodal/world-models
