# Two-Stream Convolutional Networks for Action Recognition in Videos

> 状态：文献卡 · 2014 · [原文](https://arxiv.org/abs/1406.2199)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：把卷积网络用于视频动作识别时，直接堆叠原始帧的网络学不到运动：作者引述 Karpathy 等（2014）在 Sports-1M 上发现单帧网络与多帧网络表现相近，微调到 UCF-101 后比手工的稠密轨迹特征差约 20%。
- **核心方法**：把视频拆成两路：空间流对单帧 RGB 做识别（可用 ImageNet 预训练），时间流对堆叠的 10 对稠密光流（一句话：相邻两帧之间每个像素的位移向量场，用传统的能量最小化算法预先算好）做识别，两路 softmax 分数晚融合。UCF-101 三个划分平均：只看单帧的空间流 73.0%，光流时间流 83.7%，融合 88.0%，与手工特征 IDT（85.9%–87.9%）相当。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 1 步、[Baseline 表](../../fields/video-temporal/BASELINES.md)中"时间信号 = 预计算光流"一格。只看单帧就有 73.0%，是"动作数据集可以靠外观解"的最早证据之一；最差类别 Hammering 被空间流认成 HeadMassage（都有人脸）、被时间流认成 BrushingTeeth（都是手上下重复运动），两种线索各有盲区。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1406.2199 · [全文 PDF](https://arxiv.org/pdf/1406.2199) · University of Oxford（Visual Geometry Group）
- 方向：multimodal/video-temporal
