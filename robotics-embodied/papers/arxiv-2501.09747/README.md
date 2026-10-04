# FAST: Efficient Action Tokenization for Vision-Language-Action Models

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.09747)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自回归 VLA 需要把连续动作变成离散 token；RT-2、OpenVLA 使用的逐维、逐时间步分桶在高频数据上会让相邻 token 高度相关，学灵巧技能时效果很差，甚至完全失败。
- **核心方法**：对一整段动作块的每个维度做离散余弦变换（DCT，一句话：把信号分解为不同频率余弦分量的系数，JPEG 压缩用的就是它），量化系数后按先低频的顺序交错展平，再用字节对编码（BPE，一句话：反复合并高频共现符号对的压缩式分词）压成稠密 token；只有缩放系数和词表大小两个超参。另在 100 万条真机轨迹上训练出通用分词器 FAST+。与 π0 结合后可扩展到 1 万小时机器人数据，性能与扩散式 VLA 相当，训练时间最多缩短到五分之一。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向「动作表示」部件上的改进：保留离散 token 和自回归，只换分桶方式；它也是 [π0.5](../arxiv-2504.16054/README.md) 预训练阶段的动作表示。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2501.09747
- 作者：Karl Pertsch、Kyle Stachowicz 等（共 9 位作者）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2501.09747)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
