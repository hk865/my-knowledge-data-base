# On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2608.30320)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在长上下文下，递推状态省缓存，但少数全局注意力层仍昂贵；稀疏注意力的索引器也会随长度增长。论文以 Qwen3.8-Flash-Next 为对象，同时比较能力、成本与训练稳定性。
- **核心方法**：以三层 Gated DeltaNet 接一层全局注意力的混合为起点，在继续预训练时将全局层换成 Qwen Sparse Attention（QSA）：索引器先压缩小块、选块，核心注意力再读取块内 token。模型保留 RoPE；其 NoPE 对照在后训练后出现更多无法终止的生成。QSA 表 3 同时报告 RULER 与八针 MRCR，后者在百万长度上仍有明显退化。
- **为什么在这个库里**：[长上下文 Baseline](../../fields/long-context/BASELINES.md)中"注意力结构"一格的新组合：递推状态与稀疏读取可以放进同一骨干，用来修正按团队划分"线性或稀疏"的二选一图景。原理图与评测口径见[长上下文入门](../../fields/long-context/README.md)。优先级：选读。

## 身份信息
- 稳定标识：arxiv:2608.30320 · Qwen Team · 2026-08-31
- 方向：llm/architecture、llm/long-context

## 批注

**易误读**
- 本文对象是 Qwen3.8-Flash-Next。Qwen3.8-27B 的[官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)仍列 GDN 与门控全注意力，不能按系列名套用 QSA。
- 表 3 的 Full Attn 指混合骨干中的全局层；RULER 是长度区间平均，MRCR 是指定长度的八针配置。

**与其他论文的关联**
- [Qwen3.5](../qwen3.5/README.md)：延续三层递推接一层全局读取的排布，再降低全局层的成本。
- [DeepSeek-V3.2](../arxiv-2512.02556/README.md)：QSA 接续其索引器选择稀疏上下文的思路，转为在层内压缩索引键。
