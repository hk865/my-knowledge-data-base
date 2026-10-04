# DINOv2: Learning Robust Visual Features without Supervision

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2304.07193)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言中任务无关的预训练特征可以不经微调直接使用；视觉也需要这样的通用特征：跨图像分布、跨任务、冻结即用。作者认为已有的自监督方法只要在足够多、来源多样的筛选数据上训练，就能做到。
- **核心方法**：数据：从 12 亿张去重后的网页图像中，以 ImageNet-22k 等已整理的数据集为查询，检索出相近的图像，得到 1.42 亿张的 LVD-142M。目标：DINO 的图像级自蒸馏加 iBOT 的块级遮蔽目标，教师输出的中心化换成 Sinkhorn-Knopp，再加 KoLeo 正则让一批特征分布得更均匀。训练约 10 亿参数的 ViT-g/14，再蒸馏成小模型；实现上比同类代码快约 2 倍、显存约为 1/3。冻结特征的 ImageNet 线性评测比此前最好的自监督特征（iBOT ViT-L/16）高 4.2 个百分点，略高于 OpenCLIP ViT-G/14；同样迭代数下，未筛选的 1.42 亿张随机图 ImageNet 线性 83.3、iNaturalist 68.0，筛选后为 85.8、82.3。
- **为什么在这个库里**：[视觉表征方向](../../fields/visual-representation/README.md)主线第 7 个节点，[Baseline 页](../../fields/visual-representation/BASELINES.md)第三个基线"冻结大编码器"之一：Registers、Web-SSL、Perception Encoder、DINOv3 都以它为对照，[OpenVLA](../../../robotics-embodied/papers/openvla/reading.md) 拼接它与 SigLIP 两路特征。自述局限：在 Dollar Street 上高收入家庭比低收入家庭高 31.7%；数据筛选以已有数据集为锚；416 分辨率训练约为 224 的 3 倍计算。后来发现它的大模型有高范数伪影 token，由 [Registers](../arxiv-2309.16588/README.md) 修复。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2304.07193 · [全文 PDF](https://arxiv.org/pdf/2304.07193) · Meta AI Research、Inria · TMLR（01/2024）
- 方向：multimodal/visual-representation、robotics/perception
