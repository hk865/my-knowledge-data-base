# Genie 3: A new frontier for world models

> 状态：文献卡 · 2025 · [原文（Google DeepMind 官方博客）](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：[Genie 2](../genie-2-blog/README.md) 的实时版本要靠蒸馏、画质下降，一致的世界多数只有 10–20 秒；要成为智能体的训练环境，世界模型需要实时、长时间一致，并能被更丰富地干预。
- **核心方法**：输入一段文字即生成可实时导航的世界，720p、24 帧/秒，数分钟内基本一致，视觉记忆可回溯约一分钟。官方只写了逐帧自回归：每生成一帧都要参考随时间增长的整条轨迹（回到一分钟前去过的地方，就要取回那时的信息），并在每秒内完成多次；作者明说"自回归地生成环境比一次生成整段视频更难，误差会累积"，而这种一致性是涌现的，没有 NeRF、高斯泼溅那样的显式 3D 表示。新增"可提示的世界事件"：交互过程中用文字改天气、加入物体和角色。官方列出的局限：智能体能直接执行的动作有限；多个独立智能体的交互难以模拟；不能准确还原真实地点；清晰文字通常只在描述里写明时才出现；连续交互只能支撑几分钟。结构、参数量、数据都未公开，以有限研究预览方式提供。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)主线第 6 个节点，以及观点页[《生成收敛》](../../../perspectives/generative-convergence.md#从视频生成到世界模型)"可交互、长时一致、可编辑"三件事的当前状态。两位署名作者分别来自 Genie 与 [GameNGen](../arxiv-2408.14837/README.md)，博客把 Veo 与 Genie 并列为"世界模拟"的不同能力维度。优先级：必读。

## 身份信息

- 稳定标识：url:https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/ · 2025-08-05 · Google DeepMind（Jack Parker-Holder、Shlomi Fruchter）
- 方向：multimodal/world-models、multimodal/generation
