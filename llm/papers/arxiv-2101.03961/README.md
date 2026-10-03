# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2101.03961)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：混合专家（MoE，把一层拆成许多"专家"子网络、每个 token 只激活其中少数几个）能在计算量不变的前提下大幅增加参数，但路由复杂、通信开销大、训练不稳定，难以普及。
- **核心方法**：相对 Shazeer 等 2017 的 MoE 层（每个 token 送往得分最高的 k 个专家，原作者认为 k > 1 路由才能得到有效梯度），把路由简化为每个 token 只送往 1 个专家（Switch 层），用它替换 T5 中的稠密 FFN（前馈子层），再配合训练技巧，首次让大型稀疏模型能用 bfloat16（一种 16 位低精度浮点格式）训练；在同样的计算资源下，基于 T5-Base 与 T5-Large 的版本预训练最多提速 7 倍。
- **为什么在这个库里**：[注意力与 FFN 的分工谱系](../../../foundations/relations/attention-ffn-division.md)第 7 节"MoE"节点的起点：被稀疏化的是 FFN；附录 A 试过把注意力里生成 Q、K、V 的投影专家化，因 bfloat16 下训练发散而没有采用。上一节点 [Dissecting Recall](../../../cross-domain/papers/arxiv-2304.14767/README.md) 说明事实主要存于 MLP、由注意力读出；同一节点的 [DeepSeekMoE](../arxiv-2401.06066/README.md) 把专家切得更细并加入共享专家；下一节点 [Engram](../arxiv-2601.07372/README.md) 在 MoE 之外再加一条查表式的稀疏轴。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2101.03961 · [全文 PDF](https://arxiv.org/pdf/2101.03961)
- 方向：llm/pretraining、llm/architecture
