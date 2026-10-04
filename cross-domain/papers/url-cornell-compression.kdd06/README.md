# Model Compression

> 状态：文献卡 · 2006 · [原文](https://www.cs.cornell.edu/~caruana/compression.kdd06.pdf)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：表现最好的分类器常是成百上千个基模型组成的集成，存储和运行代价让它用不到测试集极大（作者举 Google）、存储紧张（PDA）或算力有限（助听器）的场合。作者要把集成"压"成一个又小又快、表现相近的模型。
- **核心方法**：让集成（Caruana 等提出的 ensemble selection）给一大批无标签数据打标签，再用这批数据训练一个小神经网络去模仿集成；学生学的是集成的输出，而不是原始训练集的标签。缺少无标签数据时，用作者提出的 MUNGE 合成伪数据：给每个训练样本找最近邻，离散属性以概率 p 互换，连续属性以概率 p 在对方取值附近按正态分布重新采样（§2.3、Algorithm 1）；对照的 RANDOM（各属性独立采样）分布太宽，NBE（朴素贝叶斯估计联合分布）在角落处失真（§2、Figure 1）。8 个二分类问题上，用 4k 原始样本加 396k MUNGE 伪数据训练 256 个隐藏单元的模仿网络，平均 RMSE 0.264，集成 0.263，只用 4k 原始数据训练的最好神经网络 0.282，压缩拿到了可能提升的 97%（Table 2）；模仿网络比集成小 100 到 100,000 倍、快 100 到 10,000 倍（§3）。
- **为什么在这个库里**：[知识蒸馏方向](../../fields/knowledge-distillation/README.md)阶段 1 的起点，[Baseline 页](../../fields/knowledge-distillation/BASELINES.md)"数据由谁写出 = 合成伪数据"一格的代表：蒸馏的"教师给数据打标签、学生模仿教师输出"这一结构从这里开始，比"蒸馏"这个名字早了近十年。它也写出了第一个失败条件：ADULT 上压缩无效，模仿网络只比直接训练的网络略好、不如集成库里最好的单模型；作者猜测原因是 14、16、41 种取值的离散属性独热展开后神经网络不擅长，或 MUNGE 造不出这类数据（§3）。优先级：选读。

## 身份信息

- 稳定标识：url:cornell:compression.kdd06 · Cristian Buciluă、Rich Caruana、Alexandru Niculescu-Mizil（Cornell University） · KDD 2006
- 方向：cross-domain/knowledge-distillation
