# Attention与Transformer 从软对齐到并行交互

[返回学习导航](00-learning-navigation.md) · [架构模块地图](01-architectures.md)

## 先读两分钟

Attention让当前位置按需求访问其他位置；Transformer把这种交互放进主体，减少序列对齐递推。QKV、位置机制、FFN、残差、mask各有职责。先理解信息流，再按训练目标区分encoder、decoder和encoder–decoder。

![Attention与Transformer 从软对齐到并行交互总览](../../assets/foundations/transformer-summary.svg)


## 1 先弄清表示 然后再谈注意力

语言首先要变成数值。词袋把词的出现次数汇总，常丢掉次序；one-hot保留离散身份但不表达相似性；嵌入表 E∈ℝ^(Vocab× d) 把token ID映射为可学习向量。神经语言模型在Transformer前很久就使用联合学习的分布式词表示。[Bengio等神经语言模型，2003](https://jmlr.csail.mit.edu/papers/volume3/bengio03a/bengio03a.pdf)

这些是表示背景，不是一条“词袋必然产生QKV”的历史链。tokenizer、嵌入表、当前序列的隐藏状态也不是同一物：tokenizer把文本分成符号；嵌入表是参数；X∈ℝ^(n× d)是本次输入的 n 个token或patch的表示。在高层，X已融合上下文，远不只是查表结果。换成视觉patch、IMU窗口或地图单元，后面的注意力计算仍可成立。

## 2 真正的历史问题是什么

早期encoder–decoder常把整个源句压成一个向量，再让循环decoder生成译文。Bahdanau等2014年提出学习软对齐，让decoder按当前需求读取不同源位置，缓解固定向量瓶颈。2017年Transformer进一步把序列对齐的递推和卷积从主体中拿走，用self-attention组织输入输出表示，以获得更高的训练并行性和更短的长距离信息路径。[软对齐原文](https://arxiv.org/abs/1409.0473)；[Transformer原文第1至3节](https://arxiv.org/abs/1706.03762)

这段历史支持“序列建模→可学习访问→注意力主导架构”。Q/K/V的检索类比有助于理解机制，但不要据此编造“某个数据库系统直接发明Transformer”的历史。

## 3 Q K V怎样实现一次检索

先考虑单头self-attention，令 X∈ℝ^(n× d)：

Q=XWQ，K=XWK，均为n×dk；V=XWV，为n×dv
A=softmax_rows(QKᵀ/√dk + mask)，形状n×n；O=AV，形状n×dv

W_Q,W_K是 d× d_k，W_V是 d× d_v。式中的mask可表达可见性限制，也可另加位置等偏置。对一个位置而言，Q是“我用什么条件查询”，K是“我怎样被查询匹配”，V是“匹配后传出什么内容”。每行softmax把分数转成非负且和为1的混合权重。除以 √(d_k) 的动机是控制点积随维度增长的尺度，避免softmax过早饱和；它不是保证任何训练分布下方差都固定的定理。

**最小例子。** 暂设某个query对三个记忆单元的权重为 [0.8,0.1,0.1]，三行value为 [1,0]、[0,1]、[1,1]，输出就是 [0.9,0.2]。分数回答“从哪里拿”，value回答“拿到什么”，两者共同决定结果。A本身也含输入相关信息，只是它的坐标轴是“位置对”；不能把“用于打分”说成“完全不携带信息”。

机器人中的cross-attention更直观：当前本体状态有 n_q 个query，地图有 n_m 个单元。Q来自状态，K,V来自地图，则 A:n_q× n_m，O:n_q× d_v。同一块地形可能对当前步态很重要，对另一状态不重要。与描述子匹配相似之处在于可学习相似度；不同之处在于常用的是软信息混合，不必形成一对一几何对应，更不自带匹配正确性保证。

![不同mask的信息可见性](../../assets/foundations/transformer-masks.svg)

## 4 独立QKV模块

关于投影能否删去、两矩阵能否合为一个M、低秩与稀疏、V和词袋的区别，详见[QKV为什么有匹配还需要内容](15-qkv-deep-dive.md)。先把本节的信息流理解清楚，再深入消融与历史。

## 5 位置机制与QKV为什么是两件事

若没有位置、mask或其他顺序信号，self-attention对token排列是等变的：重排输入行，会相应重排输出行。Q/K投影可以学习内容关系，却不会凭空知道一个词位于第几位。

因此另设位置机制：原始Transformer把固定正弦或学习的位置向量加到输入；相对位置偏置按距离改分数；RoPE在投影后旋转Q和K，使内积带有相对位置信息。它们回答“在哪里、相距多远”，Q/K投影回答“用哪些内容特征比较”。二者可组合，不能因都出现在分数里就说功能相同。因果mask本身也提供方向与可见性结构，故“没有显式位置编码就绝对没有任何顺序信息”同样过强。[原始位置机制](https://arxiv.org/abs/1706.03762)；[RoPE原文](https://arxiv.org/abs/2104.09864)

## 6 一个Transformer块不只有attention

多头把不同子空间的输出拼接，再投影回 d 维。随后，逐位置FFN对各token做非线性变换，例如 FFN(x)=φ(xW_1+b_1)W_2+b_2，其中 W_1:d× d_(ff)，W_2:d_(ff)× d。残差使原表示和新计算可共同保留，归一化帮助控制数值与优化。原始论文使用post-norm；下式仅示意常见pre-norm安排：

H=X+MHA(Norm(X))；Y=H+FFN(Norm(H))

“attention负责交流，FFN负责局部计算”是有用近似；“attention只存语法，FFN才存知识”却划分过度。两部分的参数与残差表示跨层协作，FFN也可处理结构特征，attention也可承载与提取事实相关内容。输出行为不能按模块名字机械归属。

## 7 常见变体分别改了什么

- **Encoder-only，如BERT：**通常让输入位置双向可见，原始BERT通过masked language modeling等目标预训练，常用于检索表示、分类和逐位置预测。[BERT](https://arxiv.org/abs/1810.04805)
- **Decoder-only：**通常使用因果mask，以 p(x)=Π_t p(x_t| x_(<t))训练生成。训练知道整个真值序列，可并行算各位置的next-token损失；生成时未知未来，一般逐token追加并缓存K/V。不能由“训练并行”推得“生成也一次完成”。
- **Encoder–decoder：**encoder理解已知输入，decoder因果生成输出，并用cross-attention访问输入；适合翻译等条件转导，T5是代表。[T5](https://arxiv.org/abs/1910.10683)
- **ViT及多模态Transformer：**把图像patch或其他模态变成token，再安排交互。ViT说明同一骨架可迁移到视觉，不意味着视觉先验永远无用。[ViT](https://arxiv.org/abs/2010.11929)
- **MQA/GQA：**让多个query头共享一组或若干组K/V，减少自回归推理的KV缓存与带宽成本。它们共享的是不同头的K/V，不是简单令 Q=K。[MQA](https://arxiv.org/abs/1911.02150)；[GQA](https://arxiv.org/abs/2305.13245)
- **长序列与实现优化：**局部/稀疏注意力限制可见边，线性注意力改变或近似混合形式；FlashAttention则重排计算与访存，计算的是精确attention，不能把它写成“取消二次注意力算术复杂度”。[FlashAttention](https://arxiv.org/abs/2205.14135)

“encoder更通用、decoder更特化”不是由名字直接推出的。若把一个encoder式块改为因果mask，再用next-token目标训练，其信息流就接近causal Transformer；原始encoder–decoder的decoder还多一个cross-attention。双向可见利于利用完整已知上下文，但在严格在线任务中可能泄漏未来。能力来自结构、数据、目标及训练过程的组合。

**何时选。** 需要灵活跨位置或跨模态交互、可以利用预训练与批量并行时，Transformer很有吸引力。限制是普通全注意力的成对交互成本随长度平方增长、生成KV缓存随上下文增长、长程检索和长度外推并不自动可靠。机器人部署还应比较闭环延迟、输入同步、token化的信息损失与传感缺失时的行为。


![机制展开](../../assets/foundations/transformer-parallel.svg)

## 相关论文精读

### Bahdanau 先看到固定向量瓶颈

[原文](https://arxiv.org/abs/1409.0473)先读引言、软对齐定义与长度相关实验。画出decoder在每一步读哪些encoder状态，再回答：新增的是另一份固定句向量，还是随解码状态改变的访问？不要把“attention出现”与“RNN已被取消”混为一件事。

### Transformer 把五个设计选择分开

[原文](https://arxiv.org/abs/1706.03762)按第3.1节堆栈、第3.2节attention、第3.5节位置、第4节复杂度/路径长度阅读。原文的模型是encoder–decoder，并非只有现代decoder-only形态。论文的多头、位置、残差和FFN是一个协作系统，名字里的“all”不表示其余部件都不重要。

### BERT与T5 用信息可见性和目标比较

[BERT](https://arxiv.org/abs/1810.04805)看遮盖哪些token、允许看哪些上下文；[T5](https://arxiv.org/abs/1910.10683)看文本到文本接口与预训练设置。这里不是选“哪个名字更通用”，而是比较已知输入、待生成输出、mask和目标是否吻合任务。

## 自测与最小实验

把“机器人看到台阶”视为四个token，分别画双向mask和因果mask。因果训练时四个位置是否可并行算损失？可以，因为真值输入已知且mask阻止未来泄漏；生成时为什么仍要等待前一token？因为下一个真实输入还没产生。再尝试打乱输入顺序：没有位置与mask的self-attention只会跟着重排，不会知道原先顺序。

继续读[QKV独立模块](15-qkv-deep-dive.md)，其中专门讨论一个M、共享W、低秩与稀疏、V=X以及OV合并的条件。
