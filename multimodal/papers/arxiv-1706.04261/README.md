# The "something something" video database for learning and evaluating visual common sense

> 状态：文献卡 · 2017 · [原文](https://arxiv.org/abs/1706.04261)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：静态图像上训练的网络看不到物体的变化，缺少物理常识；已有视频数据集的标签是高层概念，网络可以从一两帧认出物体，再凭手的位置、整体速度、相机抖动等间接线索猜出动作（作者称为"作弊"）。
- **核心方法**：请众包演员按"把[某物]放进[某物]""假装把[某物]放到[某物]后面"这类带占位符的模板录制 2–6 秒短视频，同一物体做一组只差细节的动作（包括假装的动作），迫使模型看物体本身的变化；当时 108,499 段、174 个模板类。3D-CNN 在全部 174 类上 top-1 错误率 88.5%。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 2 步里与 Kinetics 对照的"反外观捷径"benchmark。之后 TimeSformer、ViViT、VideoMAE、V-JEPA 都用它的扩充版 Something-Something v2（SSv2）检验时间建模，[Revealing Single Frame Bias](../arxiv-2206.03428/README.md) 用它的模板另建时间密集的检索任务。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1706.04261 · [全文 PDF](https://arxiv.org/pdf/1706.04261) · TwentyBN 等
- 方向：multimodal/video-temporal
- 本文描述的是数据集初版；后续工作常用的 Something-Something v2 约 22 万段（ViViT Sec.4.1 的数字），v2 本身没有单独的论文目录。
