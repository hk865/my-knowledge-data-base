# YaRN: Efficient Context Window Extension of Large Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.00071)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：RoPE 模型无法泛化到训练长度之外；PI 把所有维度等比例压缩，高频维度（负责区分相邻 token）被压得分不清，局部的相对距离信息随之丢失（§1、§2–3）。
- **核心方法**：按频率分段处理：波长远小于训练长度的高频维度不插值，波长超过训练长度的低频维度按 PI 插值，中间用斜坡过渡（NTK-by-parts，§3.2）；再给注意力 logit 乘一个随扩展倍数 s 增大的温度系数，√(1/t) = 0.1 ln(s) + 1（§3.3）。Llama 2 7B/13B 在 64K 文本块上训练 400 步扩到 64K，再训 200 步扩到 128K；128K 的 passkey 检索 7B、13B 都是 99.4%，HF Open LLM 四项短任务平均略降（7B MMLU 43.8→41.7）。摘要称所需 token 比以往方法少 10 倍、训练步数少 2.5 倍。
- **为什么在这个库里**：[长上下文方向](../../fields/long-context/README.md)"位置"一环的通用做法：DeepSeek-V2、V3 用 YaRN 从 4K 扩到 128K，[Qwen2.5-1M](../qwen2.5-1m/reading.md) 在推理时只借用它的温度缩放与 DCA 联用，[Gated Attention](../arxiv-2505.06708/README.md) 用它做外推实验。前作是 [PI](../arxiv-2306.15595/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2309.00071 · [全文](https://arxiv.org/pdf/2309.00071) · Nous Research、EleutherAI、University of Geneva
- 方向：llm/long-context
