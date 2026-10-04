# A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.03200)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：闭环运动规划与可靠的真机执行需要高保真、可交互的数字孪生，但已有方法重建慢、画质有限，也难以把逼真的视觉模型转成规划可用的碰撞几何。
- **核心方法**：用 3D 高斯泼溅（3DGS：用大量带颜色和透明度的三维高斯椭球表示场景，可快速优化并实时渲染）从 10–20 张稀疏 RGB 图像重建场景；把 Grounded SAM 的二维掩码按多视角一致性提升到三维做语义标注；再滤掉漂浮的伪影，用 alpha shapes 生成贴合的碰撞网格，导入 Unity–ROS2–MoveIt 做运动规划。平均重建 229 秒，约为 NeRF 基线的 5 倍速度；在 Franka Panda 上做抓放与长程重排验证。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"⑤ 数据 / ④ 仿真"一行：它不学动力学，而是显式重建几何，交给物理引擎和规划器，是"学到的世界模型"的对照物。做不好的场景：只适用于刚性、不透明、漫反射或轻微高光的物体；透明玻璃、强反光金属、直径小于 5 mm 的细线会重建不全或碰撞几何不准，作者认为这是多视角 RGB 重建的根本局限（结论前的局限段）。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2601.03200 · [全文 PDF](https://arxiv.org/pdf/2601.03200) · 伦敦大学学院（UCL）计算机系 · Journal of Robot Learning（arXiv 注明已接收）
- 方向：multimodal/world-models、robotics/perception
