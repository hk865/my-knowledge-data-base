# 知识蒸馏的早期文献（2006–2015）

[返回知识蒸馏入门页](README.md) · [论文目录](PAPERS.md) · [来源记录](history-papers.json)

本页列出"教师给数据打标签 → 匹配 logit 与温度软目标 → 传中间层"这三步的原始文献。三步的完整叙述（每一步留下的问题、改了什么、做不好的场景）在入门页"主线历史"的阶段 1–3，这里只给每篇的位置和读法。

## 四篇原始文献

- [Model Compression](../../papers/url-cornell-compression.kdd06/README.md)（Buciluă、Caruana、Niculescu-Mizil，KDD 2006）：让大型集成给大量无标签或合成的伪数据打标签，再训练一个小神经网络去模仿；"学生学教师的输出"这一结构从这里开始。
- [Do Deep Nets Really Need to be Deep?](../../papers/arxiv-1312.6184/README.md)（Ba、Caruana，arXiv 2013，NIPS 2014）：浅网络用 L2 损失回归深网络 softmax 之前的 logit，用压缩来检验深度本身是否必要。
- [FitNets: Hints for Thin Deep Nets](../../papers/arxiv-1412.6550/README.md)（Romero 等，arXiv 2014，ICLR 2015）：在蒸馏之外让学生的中间层去预测教师的中间层，使比教师更深、更窄的学生能训练。
- [Distilling the Knowledge in a Neural Network](../../papers/arxiv-1503.02531/README.md)（Hinton、Vinyals、Dean，arXiv 2015）：温度软目标加硬标签，并证明高温极限下等价于前一篇的 logit 匹配；本方向的经典基线。

## 读这段历史时要分开的四件事

讲"蒸馏起源于哪一年"时，常把四个不同的问题混在一起，应当分别回答：

1. **术语的首次使用**：谁最早用"蒸馏"称呼这个过程。Hinton 等 2015 的题名和正文用的是"distilling / distillation"，前两篇用的是"model compression"和"mimic"。
2. **方法的前作**：谁最早让一个模型去学另一个模型的输出。Hinton 等在摘要里把这一点归于 Caruana 及其合作者（即 Model Compression）。
3. **输出模仿**：学生学的是标签、logit 还是带温度的分布，对应上面第 1、2、4 篇。
4. **中间特征对齐**：学生学的是教师的中间表示，对应 FitNets，以及后来的 MiniLM、RADIO。

`[判断]` 今天"logit 蒸馏 / 特征蒸馏 / 序列蒸馏"的分类是事后整理出来的，不能反过来当成当年作者的动机：Model Compression 要解决的是集成太大、太慢，Ba & Caruana 要回答的是深度本身是否必要，FitNets 要解决的是深而窄的网络训不动，只有 Hinton 等把"把知识从大模型搬到小模型"本身当作目标。

## 批注

**易误读**

- 四篇的年份口径不同：Ba & Caruana 的 arXiv 首版是 2013 年 12 月，会议版是 NIPS 2014；FitNets 的 arXiv 首版是 2014 年 12 月，会议版是 ICLR 2015；Hinton 等只有 arXiv 版（2015 年 3 月），arXiv 评注写的是 NIPS 2014 Deep Learning Workshop。本库的论文目录按 arXiv 首版年份记。

**未核实 / 待验证**

- "知识蒸馏起源于 2011 年"的说法没有找到对应的论文，未核实；在找到具体文献之前，不把 2011 年写进主线历史。
- 综述 [DOI 10.1016/j.mlwa.2024.100605](https://doi.org/10.1016/j.mlwa.2024.100605) 的出版社页面无法直接打开，只核对到出版社的检索索引，内容未读，本库没有引用它的结论。
- Stealing Machine Learning Models via Prediction APIs（USENIX）的论文身份已核对；正文未读，它与蒸馏的关系（题名所说的经由预测接口复制模型）本页没有展开。
