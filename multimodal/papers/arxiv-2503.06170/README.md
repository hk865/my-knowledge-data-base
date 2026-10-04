# Object-Centric World Model for Language-Guided Manipulation

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.06170)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用视频扩散模型当世界模型做预测与规划，算力和数据开销都很大。
- **核心方法**：在对象中心的槽表示空间里建世界模型：用 SAVi 提取物体槽，以 SlotFormer 式的 Transformer 在语言指令条件下预测未来的槽，再由动作解码器从预测的槽解出动作（论文比较了几种从槽预测动作的方式）。在模拟的 Language Table 环境（四块积木，把一块推到另一块旁边）上，成功阈值 0.05 时成功率 50.0%；以视频扩散模型 Susie 作世界模型的基线为 12.0–13.0%，Seer 系列不超过 0.5%（Table 1）。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"① 表示"一行：对象中心表示与语言条件结合的例子，和 [FOCUS](../arxiv-2307.02427/README.md) 一样押注"按物体建模"。做不好的场景：只在模拟环境验证；槽注意力对物体数量的变化不鲁棒；SAVi 与 SlotFormer 都是确定性的，世界模型不建模随机性（附录 A.1）。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2503.06170 · [全文 PDF](https://arxiv.org/pdf/2503.06170) · 首尔国立大学
- 方向：multimodal/world-models、robotics/embodied-policies
