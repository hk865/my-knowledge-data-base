# PaLM: Scaling Language Modeling with Pathways

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2204.02311)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：进一步理解规模对 few-shot 学习的作用：训练一个 540B 参数、稠密激活的 decoder-only Transformer 语言模型。
- **核心方法**：在 6144 块 TPU v4 上用 Pathways 系统跨两个 TPU Pod 训练，数据 780B token。结构改动：SwiGLU 激活、注意力与 FFN 并行计算（大规模下训练快约 15%）、多查询注意力、各层不用偏置；损失中加 z-loss（系数 10⁻⁴·log²Z，让 softmax 归一化项的对数 log Z 接近 0），作者称它提高了训练稳定性。few-shot 设定下，29 个英语 benchmark 中有 28 个超过此前最好结果。训练中出现约 20 次损失尖峰，梯度裁剪开着也没用，小模型上没有出现；团队从尖峰前约 100 步的检查点重启、跳过约 200–500 个批次。同样的批次从更早的检查点训练却不出尖峰，作者据此推断尖峰来自特定数据批次与特定参数状态的组合，并写明没有找到有原则的缓解办法。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"损失稳定"一节的起点：[Wortsman 等](../arxiv-2309.14322/README.md)在小模型上复现了它描述的输出 logit 不稳定，z-loss 后来被 OLMo 2 沿用。"主线历史"第 1 阶段里，它是 decoder-only 在不微调设定下胜出的节点；原文同时写明，同等训练成本下 encoder-decoder 在分类任务微调上通常更好（第 6.1.2 节）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2204.02311 · [全文 PDF](https://arxiv.org/pdf/2204.02311) · Google Research
- 方向：llm/pretraining
