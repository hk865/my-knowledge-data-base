# BEiT: BERT Pre-Training of Image Transformers

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2106.08254)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：ViT 比 CNN 更依赖数据，自监督预训练是出路；但把 BERT 的遮蔽语言建模搬到图像上时，图像块没有现成的词表，不能像预测词那样做分类，直接回归像素又会把建模能力浪费在短程依赖和高频细节上。
- **核心方法**：先用 DALL·E 的离散 VAE 把 224×224 的图"分词"成 14×14 个视觉 token（词表 8192），再按块状方式遮住约 40% 的图像块，让 ViT 从剩余的块预测被遮位置的视觉 token，最后整体微调。只用 ImageNet-1K，ViT-B 微调 83.2%（224），ViT-L 85.2%（224）、86.3%（384），高于同数据的 DeiT 与 DINO；ADE20K 分割 45.6 mIoU，略高于有监督预训练的 45.3。线性评测很弱：BEiT-B 56.7%，同为 ViT-B 的 MoCo v3 为 76.7%，而两者微调都是 83.2%（附录 Table 9）。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 遮蔽预测离散视觉 token"一行，遮蔽图像建模一支的起点，比 [MAE](../mae/README.md) 早约五个月；MAE 改为直接重建像素并去掉分词器，DINOv2 吸收的 iBOT 块级目标也属这一支。线性评测与微调之间 20 个百分点的落差，是入门页"从测量看"排名翻转的又一个例子。代价是多了一个预先训练好的外部分词器。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2106.08254 · [全文 PDF](https://arxiv.org/pdf/2106.08254) · Harbin Institute of Technology、Microsoft Research
- 方向：multimodal/visual-representation
