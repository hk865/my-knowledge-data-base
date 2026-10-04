# V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2603.14482)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：V-JEPA 系列视频自监督（在特征空间预测被遮住的视频块）擅长全局理解与运动，逐块特征却噪声大、局部结构碎片化：V-JEPA 2 的冻结特征加线性头，ADE20K 分割只有 22.2 mIoU，NYUv2 深度 RMSE 0.682（§2.2）；DINO 系的密集特征好，却只从图像学，学不到时间动态。
- **核心方法**：作者的诊断是：原损失只算被遮块，可见块（上下文 token）没有局部监督，会像[寄存器](../arxiv-2309.16588/README.md)一样被挪去汇集全局信息。四个改动：密集预测损失，可见块与被遮块都计入；深层自监督，在多个中间层施加同一目标；图像与视频各用自己的分词器、共用一个编码器；数据扩到 VisionMix-163M（图像部分从 100 万张扩到 LVD-142M 的 1.42 亿张），模型扩到 2B 参数的 ViT-G，再蒸馏出 ViT-B/L。与 V-JEPA 2 ViT-g 相比，冻结 ADE20K 从 24.4 升到 47.9，NYUv2 线性深度 RMSE 从 0.642 降到 0.307（DINOv3 ViT-7B 为 0.309），SSv2 动作识别 77.7%（DINOv3 为 71.1%）；ImageNet 85.5% 仍低于 DINOv3 的 88.1%（Fig.2）。沿用 V-JEPA 2-AC 的流程零样本部署到 Franka 机械臂，抓杯子的成功率在同样规划设置下从 60% 升到 70%，规划 8 步时到 80%（每项 10 个任务，Table 6）。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号（图像与视频）= 密集预测损失 + 多层自监督"一行；[入门页](../../fields/visual-representation/README.md)主线第 8 个节点"只监督被遮块会让可见 token 变成全局汇集器"的证据，也连到[世界模型方向](../../fields/world-models/README.md)与 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)。自述：ADE20K、Cityscapes 这类杂乱场景仍落后最好的图像编码器，作者推测 VisionMix 中高度杂乱的场景较少；机器人任务的失败多来自夹爪动作规划（过早闭合、运送途中松开），不是空间理解。代码与模型已发布。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2603.14482（当前 v3，2026-06）· [全文 PDF](https://arxiv.org/pdf/2603.14482) · Meta FAIR（另有 Universidad de Zaragoza 作者）
- 方向：multimodal/visual-representation、multimodal/video-temporal、multimodal/world-models
