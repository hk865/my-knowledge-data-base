# Genie 2: A large-scale foundation world model

> 状态：文献卡 · 2024 · [原文（Google DeepMind 官方博客）](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：训练通用的具身智能体缺少足够丰富多样的训练环境；[Genie](../arxiv-2402.15391/README.md)（2024 年 2 月）只能生成 2D 平台游戏，约 1 帧/秒，记忆 16 帧。
- **核心方法**：从一张图（多为 Imagen 3 生成）出发，生成可用键盘鼠标操作的 3D 世界，每一步接收人或智能体的动作、生成下一帧。官方写明的结构是"自回归的潜空间扩散模型"：自编码器得到潜帧，带因果 mask 的大 Transformer 逐帧往后生成，推理时用无分类器引导增强动作可控性。官方展示的能力包括识别该移动的是角色而不是树和云、离开视野的区域回来时正确渲染、同一起点的反事实轨迹、物体交互与水烟光影；一致的世界最长约一分钟，多数示例 10–20 秒。博客样例来自未蒸馏的基础模型，能实时玩的是蒸馏版本，画质下降。参数量与数据未公开。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)主线第 5 个节点：Genie 一线从离散 token（MaskGIT 式）转向潜空间扩散，并把 SIMA 智能体放进生成的世界里执行指令，说明 DeepMind 做世界模型的目的是给智能体造环境。后续见 [Genie 3 博客](../genie-3-blog/README.md)。优先级：选读。

## 身份信息

- 稳定标识：url:https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/ · 2024-12-04 · Google DeepMind（Parker-Holder 主导，署名 32 人）
- 方向：multimodal/world-models、multimodal/generation
