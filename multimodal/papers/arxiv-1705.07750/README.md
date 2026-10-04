# Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset

> 状态：文献卡 · 2017 · [原文](https://arxiv.org/abs/1705.07750)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：UCF-101、HMDB-51 只有约 1 万段视频，多数方法在上面表现相近，分不出哪种视频结构更好；视频上能否像 ImageNet 那样靠大数据预训练再迁移，尚无答案。
- **核心方法**：使用新的 Kinetics 数据集（400 类人类动作、约 24 万段训练视频、每段约 10 秒、已裁剪）重新比较五种结构，并提出 I3D：把 ImageNet 上训好的 2D 网络（Inception-v1）的 N×N 卷积核膨胀成 N×N×N，2D 权重沿时间复制 N 份再除以 N，使一张图重复成的"静止视频"输出不变；仍保留光流第二路。Kinetics 上双流 I3D 74.2%；Kinetics 预训练后 UCF-101 98.0%、HMDB-51 80.9%。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 2 步、[Baseline 页](../../fields/video-temporal/BASELINES.md)的第一个基线（3D 卷积 + Kinetics 预训练 + 多视图测试）。它的 Table 2 同时给出外观偏差的证据：Kinetics 上逐帧分类再平均的基线已有 62.2%，光流单路 63.4% 低于 RGB 单路 71.1%（与 UCF-101、HMDB-51 相反）。后来视频生成的 FVD 指标也用 I3D 特征计算。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1705.07750 · [全文 PDF](https://arxiv.org/pdf/1705.07750) · DeepMind、University of Oxford
- 方向：multimodal/video-temporal
