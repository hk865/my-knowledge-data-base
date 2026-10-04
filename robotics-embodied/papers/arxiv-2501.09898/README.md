# FoundationStereo: Zero-Shot Stereo Matching

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.09898)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：学习式双目匹配要在目标域上微调才好用，零样本泛化差；机器人常用的双目深度在无纹理、反光处本来就给不出可靠深度（[感知方向](../../fields/perception/README.md)"传感器深度"一行的失效）。
- **核心方法**：NVIDIA 用 Omniverse 路径追踪渲染 100 万对合成双目图像，覆盖室内外、驾驶、操作、导航场景，并对基线、焦距、光照随机化，再用自动筛选剔除含糊样本；网络用侧调（side-tuning）适配器把冻结的 Depth Anything V2 单目先验接进来，与 CNN 特征拼接，并在代价体上做长程上下文推理。在 Middlebury、ETH3D、KITTI 上零样本的误差低于作者对照的此前方法。A100 上 375×1242 的图约 0.7 秒；作者写明还没为效率优化（建议蒸馏与剪枝），训练集里透明物体很少。
- **为什么在这个库里**：[Depth Anything V2](../arxiv-2406.09414/README.md)"用合成标注修真实标注的失效"在双目上的对应；NVIDIA 在 GR00T N1.6 的仿真到真机流程里把它列为深度模块，与 [cuVSLAM](../arxiv-2506.04359/README.md)、nvblox 一起组成定位与感知栈。CVPR 2025。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2501.09898（NVIDIA，Wen、Trepte、Aribido、Kautz、Gallo、Birchfield；当前 v4，2025-04-04；CVPR 2025）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2501.09898)
- 方向：[感知](../../fields/perception/README.md)
