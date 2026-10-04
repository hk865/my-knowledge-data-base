# 模型科学的基线

本页对应[模型科学入门页](README.md)的第二层理解：基线是谁，后续工作分别在改它的哪个部件。阅读练习见[路线图](ROADMAP.md)，全部文献见[论文目录](PAPERS.md)。

## 基线是谁、为什么是它

- **[ROME：Locating and Editing Factual Associations in GPT](../../papers/arxiv-2202.05262/README.md)**（Meng、Bau、Andonian、Belinkov 2022）。它定义了"定位—编辑"这一研究接口：输入是"主语—关系"形式的提示（例如"The Space Needle is located in the city of"），目标是模型给出的宾语；方法是因果追踪（给主语加噪声，再把某一层某个位置的激活恢复成干净值，看正确答案的概率恢复多少）；验证方式是按定位结果改写权重，看编辑是否成功、能否泛化到换说法的提示、是否影响相邻的主语。后续关于事实回忆的工作都沿用它的数据构造和这三项评价。
- **[Transformer Feed-Forward Layers Are Key-Value Memories](../../papers/arxiv-2012.14913/README.md)**（Geva 等 2021）。它定义了读 FFN 参数的方式：W_1 的列是 key，W_2 的行是 value，key 用激活最强的训练前缀来读，value 投影到输出词表来读。ROME 的秩一编辑正是把一层 MLP 当作这样一张键值表来改写（推导见[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 4–5 节）。
- **[In-context Learning and Induction Heads](../../papers/arxiv-2209.11895/README.md)**（Olsson 等 2022）。它是注意力一侧的基线：把注意力头拆成决定看哪里的 QK 电路与决定写出什么的 OV 电路，把多个头的跨层组合当作分析单位，并用训练过程中的同时性、架构改动和消融三类证据把机制与能力联系起来。

## 基线的结构拆分

一项模型科学研究可以拆成五个可替换的部件：

1. **研究对象**：哪个模型、哪类知识或能力。ROME 是 GPT-2 XL 上的事实陈述（附录扩到 GPT-J 与 GPT-NeoX）；Olsson 等是从小型纯注意力模型到 13B 模型的上下文学习。
2. **读出手段**：怎样看到内部信息。可以是恢复激活后看输出概率、把向量投影到词表、训练探针，或直接把权重画出来。
3. **干预手段**：怎样改动模型来检验因果。可以是加噪再恢复激活、切断注意力边、消融某些头、改写权重，或从参数中遗忘某段信息。
4. **分析单位**：一个子层在一个位置、一个注意力头、跨层组合的电路、子层之间的信息流，或者整层。
5. **评价口径**：平均间接效应、敲除后的概率下降、编辑的成功率、泛化与特异性、上下文学习分数、相对基线的探针准确率。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 干预手段 | 从恢复激活换成切断注意力边（注意力敲除），作用在一段层上 | [Dissecting Recall](../../papers/arxiv-2304.14767/README.md)（Geva 等 2023） | 补上了事实从主语位置被读到预测位置的路径，切断中高层对主语的注意力后，正确答案概率最多下降约 60%；一次切断一段层，所以定位到层的精度有限（原文局限一节） |
| 读出手段 | 把主语表示和注意力输出投影到词表 | Dissecting Recall | 看到主语表示在较早层 MLP 中富集了大量属性，约 70% 的预测里可以观察到注意力头抽取属性；投影在早期层只是近似 |
| 分析单位 | 从单个子层换成跨层组合的两个注意力头 | [Induction Heads](../../papers/arxiv-2209.11895/README.md) | 一个电路同时对应一项能力（上下文学习）与一个训练时刻（相变）；带 MLP 的大模型上只有相关性证据 |
| 读出手段 | 从只看注意力权重换成看"权重 × 被读取向量变换后的范数" | [Naturalness of Attention](../../../llm/papers/arxiv-2311.13508/README.md) | 在 CodeBERT 的多数层中与语法结构吻合得更好，例如第 2 层最高吻合率 83.4% 对 54.8%（同一批头、同一种标注）；只研究了一个模型，且有若干层是权重本身吻合得更好 |
| 研究对象与读出手段 | 换成代码模型，用逐层探针做系统比较 | [Probing Pretrained Models of Source Code](../../../llm/papers/arxiv-2202.08975/README.md)、[INSPECT](../../papers/arxiv-2312.05092/README.md) | 覆盖多个代码模型和 15 个探针任务（INSPECT），并以 BERT 为基线；证据停在"预测"层级，没有干预 |
| 干预手段与研究对象 | 从参数中遗忘推理步骤，研究对象换成模型写出的推理链 | [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](../../../llm/papers/url-https-aclanthology.org-2025.emnlp-main.504/README.md)（FUR） | 把参数干预用于检验解释是否忠实，在 4 个模型、5 个多选问答数据集上常常能通过遗忘关键步骤改变预测；本库只核对了摘要 |
| 研究对象 | 把发现写进架构：静态 N-gram 模式交给哈希查表 | [Engram](../../../llm/papers/arxiv-2601.07372/README.md) | 同总参数、同每 token 计算量下，把约 20%–25% 的稀疏参数从 MoE 挪给查表时验证损失最低；关掉查表的分析是训练与推理不一致的事后消融 |

## 批注

**易误读**

- 表中 Dissecting Recall 的两行是同一篇论文的两个改动，分开列是因为它们改的是不同部件。
- ROME 的定位数字是 GPT-2 XL 上约 1000 条事实陈述的平均；附录在 GPT-J 与 GPT-NeoX 上看到相似的形状，但主语最后一个 token 上早期层注意力的作用更明显（原文附录 B）。
- 探针一行的"没有干预"是证据层级的差别：这两篇的目的是比较模型与层之间的可读出信息，问题本身就在预测层级。

**与其他论文的关联**

- [注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)：表中前三篇与 Engram 都是这条关系链的节点，每个节点的手算与原文证据在那里。
- [Making Reasoning Matter](../../../llm/papers/url-https-aclanthology.org-2024.findings-emnlp.882/README.md)：与 FUR 研究同一个问题，用的是对 12 个大模型的因果中介分析，干预对象是生成的中间步骤而不是参数。
- [Judging LLM-as-a-Judge](../../papers/llm-judge/README.md)：原"机制与可信解释"方向在这里列过它，它研究的是模型评审是否可靠，基线角色见[评估与监督可靠性](../evaluation/BASELINES.md)。

**未核实 / 待验证**

- FUR 只核对了摘要，表中它的位置依据摘要中的方法描述。
- 视觉模型一侧还没有可以放进这张表的干预类工作。
