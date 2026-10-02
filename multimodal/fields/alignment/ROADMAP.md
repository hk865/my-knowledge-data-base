# 图文对齐：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

图文对齐让两种模态的表示在某种任务上可比较。以对比学习为例，一批配对图文同时提供正样本与负样本，训练后的相似度还能用于检索和候选标签排序。

## 第二步：沿具体文章拆机制

[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../../papers/vit/README.md) → [Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

亲手构造一个小批次相似度矩阵，分别沿图到文与文到图计算匹配目标。

## 第四步：保留边界

相似度排序不是自然语言生成，也不保证模型理解空间关系或精细计数。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
