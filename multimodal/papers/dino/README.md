# Emerging Properties in Self-Supervised Vision Transformers

> 状态：技术精读 · 2021 · [原文](https://arxiv.org/abs/2104.14294)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：ViT 当时相对卷积网络还没有显出优势，作者怀疑原因之一是有监督预训练把一张图压成几千类中的一个标签。自监督方法又各自带着防坍塌部件（坍塌一句话：网络对所有输入输出同一个结果）：对比学习要负样本与大批量，BYOL 要预测头和 BatchNorm，SwAV 要 Sinkhorn-Knopp 均衡，而且主要在 ResNet 上验证。
- **核心方法**：相对 BYOL、SwAV 等前作，去掉负样本、预测头和 BatchNorm，改用自蒸馏：学生匹配教师（学生参数的指数滑动平均）对同一张图另一个裁剪的输出分布，防坍塌只靠对教师输出做中心化与低温度锐化，再用 multi-crop 让学生从局部小裁剪推出与全局一致的分布。不用标签训练的 ViT-S/8，冻结特征只用 k 近邻就达到 ImageNet 78.3%（表 2），去掉动量教师则坍塌到 0.1%（表 7）。最后一层注意力能分出前景：PASCAL VOC12 上 ViT-S/16 的 Jaccard（掩码与真值的交并比）为 45.9，有监督训练的同一模型为 27.3（图 4）。
- **为什么在这个库里**：[视觉表征方向 Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 自蒸馏"一行，与 [MAE](../mae/README.md) 相邻，是[入门页](../../fields/visual-representation/README.md)主线里 2021 年"对 ViT 的四种回答"之一；后续的 I-JEPA、DINOv2、Registers、DINOv3 从信号、数据、架构几个部件修补它，DINOv2 又成为"冻结的大编码器"基线之一。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：自蒸馏的居中与锐化手算；"局限与后续"补了 DINOv2、Registers、DINOv3
- [本篇图解与说明](figures/README.md)

## 可选的阅读顺序

[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../vit/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2104.14294 · Facebook AI Research、Inria、索邦大学
- 年份：2021
- [官方原文页面](https://arxiv.org/abs/2104.14294)
- [官方全文入口](https://arxiv.org/pdf/2104.14294v2)
- 阅读版本：v2
- 方向：multimodal/visual-representation
