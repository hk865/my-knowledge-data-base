# DINOv3

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2508.10104)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自监督理论上可以随数据和模型一起扩大，但长时间训练大模型时，密集（逐块）特征会退化；这个问题在 DINOv2 的训练中已以较轻程度出现，此前一直没有解决。
- **核心方法**：数据：从约 170 亿张 Instagram 公开图像中，用分层 k-means 聚类后平衡采样得到 16.89 亿张（LVD-1689M），另加按种子数据集检索的部分与 ImageNet 等原始数据集。模型扩到 7B 参数的 ViT（带 4 个寄存器）。作者观察到：ViT-g 与 7B 的 ImageNet 线性分类随训练单调上升，VOC 上的逐块线性分割却在约 20 万次迭代后下降，7B 甚至跌到早期水平以下，原因是块特征与 [CLS] 越来越相似、局部性下降。修法 Gram anchoring：让学生块特征之间的相似度矩阵（Gram 矩阵）贴近早期教师的相似度矩阵。之后做高分辨率后训练，蒸馏出 ViT-S 到 ViT-L 及 ConvNeXt 的一族模型，并另做与文本的对齐。冻结主干上 COCO 检测 66.1 mAP、ADE20k 分割 63.0 mIoU，ADE20k 只用线性头为 55.9；ImageNet 线性 88.4%，与 SigLIP 2（89.1%）、PEcore（89.3%）相近；同一算法用于卫星图像也超过此前方法。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 自蒸馏 + Gram anchoring"与"数据 = LVD-1689M"两行；DINO 一支到 2025 年的终点，也是"图像级目标与密集特征互相拉扯"的直接证据（[DINO 精读](../dino/reading.md)"局限与后续"第 4 条）。附录自述：需要识别文字的分类（路牌、商标、商品）明显弱于图文训练的 PEcore（例如 GTSRB 87.5% 对 94.8%）；低收入组比最高收入组低 23%，欧洲与非洲相差 14% 以上（DINOv2 为 17% 以上）。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2508.10104 · [全文 PDF](https://arxiv.org/pdf/2508.10104) · Meta AI Research（另有 WRI、Inria 作者） · 技术报告
- 方向：multimodal/visual-representation、robotics/perception
