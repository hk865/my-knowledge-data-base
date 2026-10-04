# Distilling the Knowledge in a Neural Network

> 状态：文献卡 · 2015 · [原文](https://arxiv.org/abs/1503.02531)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多个模型的集成（或一个强正则化的大模型）更准，但部署给大量用户时太贵。[Caruana 等](../url-cornell-compression.kdd06/README.md)已经证明可以把集成压进单个模型，作者要给出一个更通用的压缩办法；另外提出一种由一个通用模型和许多专家模型组成的集成，专家只负责区分通用模型容易混淆的类别。
- **核心方法**：教师与学生的 softmax 都除以温度 T，学生在迁移集上用高温下与教师软目标的交叉熵，加上权重较小的硬标签交叉熵训练；软目标的梯度按 1/T² 缩放，所以与硬标签合用时要乘回 T²（§2）。高温极限下，这等价于 [Ba & Caruana](../arxiv-1312.6184/README.md) 的 logit 匹配（§2.1）。Android 语音搜索的声学模型（约 2000 小时语音、约 7 亿个训练样本）上，基线帧准确率 58.9%，10 个模型的集成 61.1%，蒸馏出的同尺寸单模型 60.8%，拿到了集成提升的 80% 以上（Table 1、§4.1）；只用 3% 的数据时，硬标签训练严重过拟合，早停时为 44.5%，软目标训练到 57.0%（Table 5）。
- **为什么在这个库里**：[知识蒸馏方向](../../fields/knowledge-distillation/README.md)的经典基线（[Baseline 页](../../fields/knowledge-distillation/BASELINES.md)"基线是谁"一节），"温度软目标 + 硬标签"定义了后来的工作要替换的部件。它也写出两个坑：迁移集里缺类时学生的偏置会错，MNIST 迁移集去掉所有"3"后，把 3 的偏置调高 3.5，98.6% 的 3 能认对；只保留 7 和 8 时，调偏置前测试误差 47.3%（§3）。JFT（Google 内部 1 亿张图、1.5 万类）上加 61 个专家模型，开发集 top-1 准确率从 25.0% 提到 26.1%（Table 3），但结论写明尚未证明能把专家的知识蒸回单个大网络（§8）；这件事到 2025–2026 年才由多教师 on-policy 蒸馏做成（方向入门页阶段 7）。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1503.02531 · [全文 PDF](https://arxiv.org/pdf/1503.02531) · Geoffrey Hinton、Oriol Vinyals、Jeff Dean（Google） · NIPS 2014 Deep Learning Workshop（arXiv 评注）
- 方向：cross-domain/knowledge-distillation
