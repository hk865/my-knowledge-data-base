# OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.16038)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自动驾驶需要预测三维场景怎样演化；多数方法只预测物体框的运动，丢掉了可行驶区域、路沿、植被这类细粒度的场景结构。
- **核心方法**：在三维语义占据（occupancy：把周围空间划成体素，每个体素标为空或某个语义类别）空间里建世界模型：先用 VQ-VAE 把每帧占据压成离散的场景 token，再用类 GPT 的时空生成 Transformer 自回归预测下一帧的场景 token 与自车 token，解码出未来占据和自车轨迹；规划不使用物体框和地图监督。在 Occ3D 上做 4D 占据预测，在 nuScenes 上做运动规划。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)批注中"驾驶方向的占据世界模型"对照项：与操作世界模型同样是"分词器 + 自回归 Transformer"，但状态是几何占据而不是像素或特征。做不好的场景写在表里：以真值占据为输入时未来 1–3 秒平均 mIoU 为 17.14%，换成由相机预测的占据（OccWorld-D）降到 8.62%，完全自监督的 OccWorld-S 只有 0.26%（Table 1）；规划 L2 平均 1.17 m，不如用了地图、物体框等辅助监督的 UniAD（1.03 m，Table 2）；新进入视野的车辆预测不出来（Fig.1 说明）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2311.16038 · [全文 PDF](https://arxiv.org/pdf/2311.16038) · 清华大学自动化系、电子工程系
- 方向：multimodal/world-models、robotics/navigation-planning
