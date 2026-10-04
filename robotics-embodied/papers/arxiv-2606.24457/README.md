# Lite Any Stereo V2: Faster and Stronger Efficient Zero-Shot Stereo Matching

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2606.24457)

- **解决什么**：轻量双目模型在跨域精度和边缘设备延迟之间难两全，只减少理论乘加次数也未必更快。
- **核心方法**：以纯 2D 代价聚合替换重 3D 模块，结合合成监督、自蒸馏、过滤后的真实双目伪标签；提供前馈与迭代变体，在 GPU 和 Orin 上实际测时，强反光、透明物体与歧义几何仍会失败。
- **为什么在这个库里**：作为 [Fast-FoundationStereo](../arxiv-2512.11130/README.md) 的部署导向对照，回答[感知](../../fields/perception/README.md)里“泛化能否保留在小模型中”。优先级：选读（边缘算力受限时）。
