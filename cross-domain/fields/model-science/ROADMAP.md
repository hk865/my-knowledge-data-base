# 模型科学：阅读与问题路线

本页给出一条阅读路线和几项检验理解的练习。领域地图见[模型科学入门页](README.md)，基线拆分见 [Baseline 页](BASELINES.md)，全部文献见[论文目录](PAPERS.md)。

## 第一步：限定问题

模型科学的每个结论都要说明它由哪一层级的证据支撑：**观察**（看权重，或把内部向量投影到词表）、**预测**（探针：在冻结表示上训练简单分类器）、**干预**（改动激活或权重，看输出怎样变）。可视化、探针、干预与因果检验依次提供更强的证据。模型用语言写出的解释（例如推理链）也是一种观察，它是否忠实于实际的计算，同样要用干预来检验。

## 第二步：沿具体文章拆机制

1. [QKV 讲义](../../../foundations/lessons/15-qkv-deep-dive.md)第 4–5 节与 [Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 10.1 节：手算 A 与 V 的分工和 FFN。
2. [FFN 键值记忆](../../papers/arxiv-2012.14913/README.md)：参数怎样读成键值表（观察）。
3. [ROME](../../papers/arxiv-2202.05262/README.md)：因果追踪定位事实，再用秩一更新改写（干预）。
4. [Induction Heads](../../papers/arxiv-2209.11895/README.md)：跨层组合的注意力电路，以及它与上下文学习、训练相变的对应。
5. [Dissecting Recall](../../papers/arxiv-2304.14767/README.md)：事实从 MLP 存储到注意力读出的完整路径。
6. [Engram](../../../llm/papers/arxiv-2601.07372/README.md)：把"静态模式查表"写进架构。

这六步的前后关系与每一步的证据，见[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)。探针一线可以并行读 [Probing Pretrained Models of Source Code](../../../llm/papers/arxiv-2202.08975/README.md) 与 [INSPECT](../../papers/arxiv-2312.05092/README.md)；视觉一侧读 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 9 节与 [ViT 精读](../../../multimodal/papers/vit/reading.md)。

## 第三步：做能检验理解的工作

- **给证据定级。** 把每篇文献的核心主张标为观察、预测或干预，再写出要排除替代解释还需要什么实验。示例：FFN 键值记忆中"低层 key 偏浅层模式"属于观察，要说明模型依赖这些 key，需要像 ROME 那样恢复或改写对应激活；INSPECT 的探针结果属于预测，要说明模型用到了某个代码性质，需要在表示中抹去该性质后看下游任务是否变差。
- **重做两处手算。** 按关系页第 1 节，把输入中只被 V 读取的一列乘 10，确认 A 不变而输出变了；按第 4 节，用 x = [1, −2] 和三组 key、value 算一次 FFN 的键值读法，确认只有第 1 个 key 被命中。
- **对照感受野与注意力距离。** 按[CNN 讲义](../../../foundations/lessons/11-cnn.md)第 4 节算出 3×3、步长 1 的卷积堆叠到 L 层时的感受野 (2L+1)×(2L+1)，再看 ViT 原文 Fig.7 中最低层各个头的平均注意力距离，说明 ViT 的局部头与 CNN 早期层在做的事情有何相似。
- **读一条推理链。** 选一个多步推理的例子，写出要检验"推理链忠实于模型实际计算"需要怎样的干预，再与 [FUR](../../../llm/papers/url-https-aclanthology.org-2025.emnlp-main.504/README.md) 和 [Making Reasoning Matter](../../../llm/papers/url-https-aclanthology.org-2024.findings-emnlp.882/README.md) 的做法对照。

## 第四步：记录结论

记录时分三栏：原文支持的事实（附章节位置）、自己的解释、仍需实验验证的假设。自己跑过实验的结论标明"已复现"及设置；只读过原文的，按原文的模型与数据范围写结论。

## 批注

**易误读**

- 探针能预测某个属性，说明信息存在于表示中，不足以说明模型依赖这个属性；流畅的推理链也可能不是产生答案的实际过程。两者都要靠干预检验。
- 第二步的顺序同时是时间顺序和问题链顺序，每一步回答上一步留下的问题，依据见入门页"主线历史"。

**与其他论文的关联**

- [训练科学](../training-science/README.md)：Induction Heads 的相变发生在训练早期，适合与训练动态的工作一起读。
- [评估与监督可靠性](../evaluation/ROADMAP.md)：模型评审、监督可靠性一类的工作在那条路线中。
