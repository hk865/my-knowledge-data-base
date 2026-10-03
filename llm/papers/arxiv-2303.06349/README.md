# Resurrecting Recurrent Neural Networks for Long Sequences

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2303.06349)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：深层状态空间模型（SSM，一类用线性状态方程逐步更新隐藏状态的序列层，代表是 S4）在长序列任务上远强于普通 RNN，但不清楚这份优势来自连续时间离散化、HiPPO 初始化，还是更简单的因素。
- **核心方法**：从普通 tanh RNN 出发逐步消融，依次做四处改动：去掉递推中的非线性（线性递推，可用并行 scan 训练）、把转移矩阵对角化为复数对角阵、用指数参数化让特征值模长始终小于 1 并初始化在靠近单位圆的环上、对输入做按特征值的归一化。得到的 Linear Recurrent Unit（LRU）在 Long Range Arena 全部任务上达到与 S4/S4D/S5 相近的准确率，且训练速度相当，不依赖连续时间离散化。
- **为什么在这个库里**：[递推状态谱系](../../../foundations/relations/recurrent-state.md)中连接"RNN"与"SSM"的节点：它说明 SSM 的关键成分可以从 RNN 一侧用稳定性与信号传播的论证推出来，是读 S4 与 [Mamba](../mamba/README.md) 时的参照。优先级：选读。
