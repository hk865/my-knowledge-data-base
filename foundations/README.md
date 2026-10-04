# 深度学习基础

[回到全库](../README.md) · [完整学习导航](../docs/foundations/00-learning-navigation.md)

这里是24个基础与进阶模块的分层入口。完整讲义在 docs/foundations/ 路径。

基础层只讲机制：一个计算怎样进行、为什么这样设计，不分模态，也不涉及团队与 benchmark。机制在各领域怎样发展，写在对应的领域页（例如[视觉表征](../multimodal/fields/visual-representation/README.md)、[预训练](../llm/fields/pretraining/README.md)、[训练科学](../cross-domain/fields/training-science/README.md)）；跨领域的论证写在[观点层](../perspectives/README.md)。

## 五个分区

每个分区页是一张概念地图：各模块解决什么计算问题，先读什么，谁是谁的特例或推广。

- [架构与信息流](fields/architectures/README.md)：CNN、RNN、LSTM、注意力、QKV、VAE、扩散及架构扩展
- [优化与参数更新](fields/optimization/README.md)：梯度与SGD、动量、Adam、Muon
- [任务、损失与监督](fields/objectives/README.md)：回归、分类、预训练、机器人IMU与正则化
- [数据与实验流程](fields/data/README.md)：数据契约、流水线、分类实验、IMU实验及数据集选型
- [进阶连接](fields/advanced/README.md)：分布式训练、强化学习、迁移与元学习

## 跨模块关系

- [关系页索引](relations/README.md)：跨越三个以上模块的概念链，例如[递推状态谱系](relations/recurrent-state.md)和[注意力与 FFN 的分工谱系](relations/attention-ffn-division.md)。只涉及两个模块的关系，写在各篇讲义末尾的"与其他概念的关系"一节。

## 从概念走向论文

- [Baseline入口](BASELINES.md)
- [学习路线](ROADMAP.md)
- [论文原文与讲解目录](PAPERS.md)
