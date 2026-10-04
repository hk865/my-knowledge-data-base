# SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2206.07764)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：槽式对象中心模型（为每个物体分配一个"槽"向量，不需要分割标注）在合成视频里已能无监督地分割、跟踪物体，但遇到相机运动、真实背景、物体繁多的真实视频就失效；原来的 SAVi 以光流为预测目标，只能分出运动物体，分不出静止物体与背景。
- **核心方法**：在同组的 SAVi 上把预测目标从光流换成深度，并按扩大模型规模的经验改结构、加数据增强；仍用第一帧的物体框初始化各个槽。在合成的 MOVi 系列基准上能同时处理静止与运动物体、固定与运动相机；用 LiDAR 得到的稀疏深度作目标，在 Waymo Open 真实驾驶视频上涌现出物体分割与跟踪。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"① 表示"一行中对象中心表示的来源之一：[SlotFormer](../arxiv-2210.05861/README.md) 和[语言引导的对象中心世界模型](../arxiv-2503.06170/README.md)都在 SAVi 系的槽表示上训练动力学。作者自述的两个做不好的场景，也解释了这条线为什么没有走进大规模机器人系统：要靠第一帧物体框作提示；训练要用真值深度（或光流）作目标（Sec.4.4）。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2206.07764 · [全文 PDF](https://arxiv.org/pdf/2206.07764) · Google Research · NeurIPS 2022
- 方向：multimodal/world-models、multimodal/video-temporal
