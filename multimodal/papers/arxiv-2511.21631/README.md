# Qwen3-VL Technical Report

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2511.21631)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：扩展多模态能力不能侵蚀底座 LLM 的语言能力；Qwen2.5-VL 的 M-RoPE 把维度切成时间、高、宽三组造成频谱不均、伤害长视频，绝对时间的位置编号在长视频里过大过稀，还要求训练数据均匀覆盖各种帧率。
- **核心方法**：视觉塔改为在 SigLIP-2（SO-400M；2B/4B 用 300M 的 Large）上继续做动态分辨率训练；两层 MLP 把 2×2 特征合成一个 token；交错 M-RoPE 让时间、高、宽均匀分布在高低频段；DeepStack 把 ViT 三个层级的特征经专门的合并模块加到 LLM 前三层；视频改用文字时间戳 token；损失改为按平方根归一化的逐 token 损失。预训练四段：只训合并模块（67B token）→ 全参数（约 1T）→ 32K 长上下文（约 1T）→ 256K（100B）。后训练：长 CoT SFT → 只用文本数据的强到弱蒸馏（含 on-policy 蒸馏）→ 推理 RL（SAPO 算法，约 3 万条可验证查询）与通用 RL。稠密 2B/4B/8B/32B 与 MoE 30B-A3B、235B-A22B，全部 Apache 2.0。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 7 个节点，并写出了前作 [Qwen2.5-VL](../arxiv-2502.13923/README.md) 的坑。后训练中两条失败值得记住：通用 RL 专门纠正 SFT 留下的"强而错的先验"（反直觉计数、复杂表盘读时）；"用图思考"的工具 RL 中模型退化成只调一次工具来骗取奖励。是 [InternVLA-A1](../../../robotics-embodied/papers/arxiv-2601.02456/README.md) 的底座之一；蒸馏做法与 [Qwen3](../../../llm/papers/arxiv-2505.09388/README.md) 一致。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2511.21631（Shuai Bai 等 64 位作者；当前 v2，2025-11）· [全文 PDF](https://arxiv.org/pdf/2511.21631v2) · 阿里巴巴 Qwen 团队
- 方向：[视觉语言模型](../../fields/vlm/README.md)、[视频与时序](../../fields/video-temporal/README.md)、[LLM 强化学习](../../../llm/fields/posttraining/rl/README.md)
