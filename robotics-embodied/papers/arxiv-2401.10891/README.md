# Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2401.10891)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：深度标注依赖传感器、立体匹配或 SfM，成本高甚至在某些情形下不可得；度量深度方法泛化不如相对深度的 MiDaS。
- **核心方法**：150 万张标注图训练教师，为 6200 万张无标注图打伪标签，对学生施加强扰动并加 DINOv2 特征对齐损失，输出相对深度（仿射不变视差）。零样本 KITTI AbsRel 0.076，MiDaS v3.1 为 0.127；在 NYUv2 上微调为度量深度后 δ1 0.984。原文写明模型最大只到 ViT-L，512×512 训练分辨率对实际应用不够。
- **为什么在这个库里**：[Baseline 页](../../fields/perception/BASELINES.md)"深度监督"一格；它的真实标注问题由 V2 处理。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2401.10891 · [全文 PDF](https://arxiv.org/pdf/2401.10891v2) · Lihe Yang、Bingyi Kang、Zilong Huang、Xiaogang Xu、Jiashi Feng等（HKU、TikTok、CUHK、浙江大学）
- 发表：CVPR 2024
- 方向：robotics/perception
