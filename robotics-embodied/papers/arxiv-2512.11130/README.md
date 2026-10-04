# Fast-FoundationStereo: Real-Time Zero-Shot Stereo Matching

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.11130)

- **解决什么**：[FoundationStereo](../arxiv-2501.09898/README.md) 的零样本深度质量好，但重骨干、代价体和迭代更新使机器人难以实时使用。
- **核心方法**：分别用特征蒸馏、按延迟预算搜索代价过滤模块、结构化剪枝压缩三个瓶颈；再用真实双目伪标签补训练分布。与教师和轻量模型比较速度–精度曲线，半透明表面的误差仍会继承。
- **为什么在这个库里**：把[感知方向](../../fields/perception/README.md)的“深度准确”接到“能按时交给控制器”；与 [LAS2](../arxiv-2606.24457/README.md) 对照压缩与重设计两条路线。优先级：必读（准备部署双目时）。
