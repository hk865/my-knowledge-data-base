# 视觉表征：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

视觉表征把像素转成后续任务可用的特征。要把网络架构与学习目标分开：同一个视觉Transformer可以用标签监督、遮挡重建或自蒸馏学习。

## 第二步：沿具体文章拆机制

[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../../papers/vit/README.md) → [Masked Autoencoders Are Scalable Vision Learners](../../papers/mae/README.md) → [Emerging Properties in Self-Supervised Vision Transformers](../../papers/dino/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

把一张图分成patch，再比较三个目标分别要求模型预测什么、哪些分支参与梯度更新。

## 第四步：保留边界

ViT是架构；MAE和DINO体现不同学习信号。好看的特征可视化不等于所有下游任务都更好。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
