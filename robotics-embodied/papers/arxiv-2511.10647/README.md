# Depth Anything 3: Recovering the Visual Space from Any Views

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2511.10647)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：单目深度（[Depth Anything V2](../arxiv-2406.09414/README.md)）、多视图几何（[VGGT](../arxiv-2503.11651/README.md)）、相机位姿估计各要一种模型；机器人上相机数量、是否已知位姿随场景而变。
- **核心方法**：任意数量的图像进（已知或未知相机位姿都可以），输出空间一致的几何。两点"最简"设计：骨干就是一个普通的 DINO 编码器，不做结构特化；只预测"深度 + 射线"这一个目标，代替复杂的多任务头。用教师-学生方式训练，只用公开学术数据。作者新建的视觉几何基准上，相机位姿精度平均比 VGGT 高 44.3%、几何精度高 25.1%（摘要数字），单目深度超过 DA2；另有按 Metric3Dv2 方式训练的度量深度版本 DA3-Metric，以及前馈 3D 高斯渲染的版本。模型从 0.03B 到 1.1B 共四档。原文没有局限一节，只把动态场景列为未来工作。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)深度一支的延续（Depth Anything → V2 → 本篇，从单目相对深度走到多视图几何与度量深度），同时进入[定位与建图方向](../../fields/localization-mapping/README.md)阶段 5：[AMB3R-SLAM](../arxiv-2609.19518/README.md) 用 80M 参数的 DA3-Small 做前端。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2511.10647（ByteDance Seed，Lin、Chen 等 8 位作者；v1，2025-11-13）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2511.10647) · [项目页](https://depth-anything-3.github.io/)
- 方向：[感知](../../fields/perception/README.md)（另见[定位与建图](../../fields/localization-mapping/README.md)）
