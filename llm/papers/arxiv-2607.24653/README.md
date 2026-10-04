# Kimi K3: Open Frontier Intelligence

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.24653)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在 [Kimi K2](../arxiv-2507.20534/README.md) 之上同时扩大参数（2.78T 总参数、104B 激活）、上下文（1M token）和模态（原生视觉），并提高单位算力带来的效果。
- **核心方法**：注意力用 3:1 的 KDA 与 MLA 混合（来自 [Kimi Linear](../arxiv-2510.26692/README.md)），MLA 层不用位置编码，并加一个按输入、逐通道的输出门，最后一层固定为全局注意力；残差改为 [Attention Residuals](../arxiv-2603.15031/README.md)；FFN 改为 Stable LatentMoE：路由专家在压缩到一半宽度的潜空间里计算，896 个专家每次激活 16 个。作者写明这样的稀疏度放大了两种失败：路由分支近四次连续矩阵乘法在 2.8T 规模下造成内部激活爆炸，近千个专家超出了逐步更新偏置的均衡方法的适用范围；对应的修补是在专家聚合后加 RMSNorm，以及按路由分数分位数直接设定偏置（Quantile Balancing）。优化器为按注意力头分块正交化的 Per-Head Muon，并保留 K2 的权重截断。规模定律显示整体缩放效率约为 K2 的 2.5 倍；在各自独立调优的超参下，余弦衰减的最终损失低于 K2 使用的 WSD 调度。长上下文在预训练中从 8K 加到 64K，在冷却期从 256K 加到 1M，并合成只有读遍整个 1M 上下文才能解出的任务，作者写明仅有长度不能带来长程能力。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md) Kimi 路线的最新节点，"问题与手段"表中 Kimi 的条目大多在这里汇合。原文自述总体表现仍落后于最强的闭源模型。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2607.24653 · [全文 PDF](https://arxiv.org/pdf/2607.24653) · Kimi Team（Moonshot AI）
- 方向：llm/pretraining、llm/architecture、llm/long-context
