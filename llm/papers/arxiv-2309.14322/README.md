# Small-scale proxies for large-scale Transformer training instabilities

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.14322)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：训练大 Transformer 的团队报告过一些只在大规模出现、同样超参的小模型上不出现的训练不稳定；复现一次要大量资源，原因因此难以研究。
- **核心方法**：用"学习率与最终损失的关系"作为观察工具，定义学习率敏感度（LR sensitivity：学习率在大范围变化时，最终损失偏离最优值的程度）。只要把学习率调高，小模型上同样出现大模型报告过的两类不稳定：注意力 logit 增长，以及输出 logit 偏离对数概率（PaLM 用 z-loss 处理的那一类）；大规模上用过的缓解办法 qk-layernorm（计算注意力分数前对 Q、K 做层归一化）和 z-loss 在小模型上同样有效，能在三个数量级的学习率范围内稳定训练。再看其他干预对敏感度的影响：更长的 warm-up 与和学习率解耦的权重衰减降低敏感度，加深网络比加宽更快地提高敏感度。最后从激活与梯度范数随规模的变化提前预测不稳定，例如梯度 RMS 随参数量下降、逼近 AdamW 的 ε 时，某一层的更新可能塌缩。（作者限定研究的是缓慢发散一类的不稳定，不是突发的损失尖峰。）
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"损失稳定"一节中，从 [PaLM](../arxiv-2204.02311/README.md) 的尖峰走到 QK-Norm 成为常用部件之间的一环：此后 OLMo 2、Qwen3、Gemma 3、DeepSeek-V4 都采用 QK 归一化。也是"损失尖峰有没有统一的原理"这一开放问题的入口。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2309.14322 · [全文 PDF](https://arxiv.org/pdf/2309.14322) · Google DeepMind
- 方向：llm/pretraining、cross-domain/training-science
