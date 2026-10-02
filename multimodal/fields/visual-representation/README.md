# 视觉表征 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

视觉表征把像素转成后续任务可用的特征。要把网络架构与学习目标分开：同一个视觉Transformer可以用标签监督、遮挡重建或自蒸馏学习。

## 一个容易混淆的边界

ViT是架构；MAE和DINO体现不同学习信号。好看的特征可视化不等于所有下游任务都更好。

## 入门任务

把一张图分成patch，再比较三个目标分别要求模型预测什么、哪些分支参与梯度更新。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/14-attention-transformer.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../../papers/vit/README.md)
2. [Masked Autoencoders Are Scalable Vision Learners](../../papers/mae/README.md)
3. [Emerging Properties in Self-Supervised Vision Transformers](../../papers/dino/README.md)
