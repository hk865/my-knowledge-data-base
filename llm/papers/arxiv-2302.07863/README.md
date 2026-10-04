# Speculative Decoding with Big Little Decoder

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2302.07863)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Transformer 生成文本延迟高，需要在不改训练、不改结构的前提下，让大小两个模型协作提速。
- **核心方法**：提出 BiLD：小模型自回归地生成，大模型只偶尔以非自回归方式并行修正。两条策略协调二者：回退策略在小模型最大预测概率低于阈值时把控制权交给大模型；回滚策略让大模型回看已有草稿，找到两者分布距离超过阈值的最早位置，删去该处及之后的 token 由大模型替换。在机器翻译（IWSLT 2017、WMT 2014 德英）和摘要（XSUM、CNN/DailyMail）上，NVIDIA T4 上最高加速 2.12 倍，生成质量略有下降。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"近似协作"一格：用两个阈值换质量—延迟折中，不保证大模型原分布。与 [Leviathan 等的投机解码](../arxiv-2211.17192/README.md) 对照，分清"精确验证"与"阈值接管"。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2302.07863 · [全文 PDF](https://arxiv.org/pdf/2302.07863) · NeurIPS 2023 · 代码开源
- 作者：Sehoon Kim、Karttikeya Mangalam、Suhong Moon、Jitendra Malik、Michael W. Mahoney、Amir Gholami、Kurt Keutzer（UC Berkeley、ICSI、LBNL）
- 方向：llm/inference
