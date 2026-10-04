# SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2210.05861)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：对象中心模型已能把场景拆成物体，但物体之间的交互动力学还建不好，长时预测会变糊、会丢物体。
- **核心方法**：两阶段：先用预训练的槽注意力模型（视频用 SAVi）把每帧编码成一组物体槽并冻结，再训练一个 Transformer 在槽序列上自回归预测未来的槽，解码回图像。相比把图像切成规则网格 token 的视频预测，一个物体始终对应一个向量，长时预测更一致。无监督学到的动力学可以接到 CLEVRER 视觉问答（回答"接下来会发生什么"）、Physion 和 PHYRE 目标条件规划上，在视觉问答上超过使用真值物体标注的对手。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"① 表示"一行中对象中心视频动力学的代表，[语言引导的对象中心世界模型](../arxiv-2503.06170/README.md)沿用了它的结构。做不好的场景是作者自己写的：依赖的预训练对象中心模型还扩展不到真实视频，所以实验全在合成数据上；两阶段训练让前几步预测变差（附录 F）。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2210.05861 · [全文 PDF](https://arxiv.org/pdf/2210.05861) · 多伦多大学、Vector Institute、三星 AI 中心（多伦多）、Google Research · ICLR 2023
- 方向：multimodal/world-models、multimodal/video-temporal
