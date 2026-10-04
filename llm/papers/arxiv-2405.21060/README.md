# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.21060) · [ICML 2024 正式版](https://proceedings.mlr.press/v235/dao24a.html)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：[Mamba](../mamba/reading.md) 这类状态空间模型（SSM，用固定大小的状态逐步递推的序列层）在中小规模上已能与 Transformer 竞争，但它的选择性 scan 用不上 GPU 的矩阵乘法单元，训练效率不如注意力，也接不上为 Transformer 发展出来的理论与系统优化。作者要说明 SSM 与注意力到底是什么关系，并据此把 SSM 算快。
- **核心方法**：把序列层都写成"输出 = 一个下三角矩阵乘输入"，证明 SSM 对应的矩阵正是半可分矩阵（下三角部分内任取一个子矩阵，秩都不超过状态大小 N，§3）。在此基础上提出 SSD 层（structured state space duality，结构化状态空间对偶），相对 Mamba 只改两处：每步的转移 A_t 从对角阵简化为"标量乘单位阵"，头维度从 1 加大到 64 或 128（§2.4）。这样同一层既能按递推（线性复杂度）算，也能写成带衰减 mask 的注意力（二次形式，mask 的元素是逐步标量的连乘），作者把这个矩阵切成块，对角块按注意力形式用矩阵乘法算，非对角块利用低秩结构化成较短的递推，把两种算法结合起来（§6）。专用实现比 Mamba 优化过的选择性 scan 快 2–8 倍，状态可放大到 Mamba 的 8 倍以上而几乎不变慢，序列长 2K 起快于 FlashAttention-2，16K 时快 6 倍（§1、Figure 10）。用 SSD 作核心层的新架构叫 Mamba-2，摘要称它在语言建模上仍与 Transformer 有竞争力，实验覆盖 Pile 上 125M 到 2.7B 的模型（§9.2）。
- **为什么在这个库里**：[架构方向](../../fields/architecture/README.md)"固定大小的状态"一节中 Mamba 之后的节点，也是 [Nemotron 3](../arxiv-2512.20856/README.md) 混合结构用的序列层（[Baseline 页](../../fields/architecture/BASELINES.md)"层排布"一格）；[递推状态谱系](../../../foundations/relations/recurrent-state.md)第 6 节据它把一类 SSM 与带衰减的线性注意力看成同一个算子的两种算法。它给出了混合比例最早的一组扫描：350M、48 层、Pile 上训练 7B token，全部用 SSD 时验证困惑度 8.60，Transformer++（现代配方的 Transformer）8.68；换入 6 层注意力时最低，为 8.26，换入 24 层时回升到 8.50，作者概括为约 10% 的层用注意力最好，并假设 SSM 层做一般的序列映射、注意力层负责检索前文（§9.2.3、Table 2）。2.7B、300B token 上，58 层 SSD 加 6 层注意力的混合在 Pile 困惑度（5.95）与零样本平均准确率（61.0）上都好于纯 Mamba-2（6.09、60.2）和 Transformer++（6.13、60.2）（Table 3），是 [长上下文方向](../../fields/long-context/README.md)"线性注意力与递推状态"一路里"固定状态要配少量注意力"的直接证据。优先级：必读。

## 批注

**易误读**

- "快 2–8 倍"比较的是 SSD 层的算子与 Mamba 的融合 scan 算子，图中条件是状态扩展 N = 64；作者在 §9.3 写明，序列长 2K 这样的短序列上，整个 Mamba-2 模型的训练效率可能不如同参数的 Transformer，因为 Transformer 有一半层是硬件效率很高的 MLP。
- "约 10% 注意力层最好"只来自 350M、7B token 的困惑度扫描，最低点在 6/48 层（12.5%），5 到 9 层之间差别在 0.02 以内；2.7B 上只比较了 6 层注意力这一种混合配置（§9.2.3）。
- 题名的"Transformers are SSMs"是向 Katharopoulos 等"Transformers are RNNs"致敬，原文脚注写明这种对应只针对某些形式的注意力（§1 脚注 1）；SSD 的二次形式没有 softmax。

**与其他论文的关联**

- 转移从 Mamba 的对角阵收成每头一个标量，换来矩阵乘法；Kimi Linear 的 KDA 在保留分块并行的前提下把逐通道的衰减加了回来（[递推状态谱系](../../../foundations/relations/recurrent-state.md)第 6、7 节）。
- 混合比例可与 [Jamba](../arxiv-2403.19887/README.md)（注意力:Mamba = 1:7）和 Kimi Linear（3:1，即 25% 全注意力）对照；三者的规模、数据与指标都不同，比例不能直接比较。
- MQAR（多查询联想召回）合成任务上，状态从 N = 16 加到 64、256 持续改善，同为 N = 16 时 Mamba-2 也明显好于 Mamba（§9.1、Figure 8）；这与 [Repeat After Me](../arxiv-2402.01032/README.md)、[Based](../arxiv-2402.18668/README.md) 测出的"固定状态召回弱"是同一个问题的两面：加大状态能缓解，但不能消除。

## 身份信息

- 稳定标识：arxiv:2405.21060 · [全文 PDF](https://arxiv.org/pdf/2405.21060) · Tri Dao（Princeton University）、Albert Gu（Carnegie Mellon University） · ICML 2024（PMLR 235:10041–10071）
- 方向：llm/architecture、llm/long-context
