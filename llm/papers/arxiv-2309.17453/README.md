# Efficient Streaming Language Models with Attention Sinks

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.17453)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多轮对话这类流式应用要求模型连续处理很长的输入，但缓存全部历史 KV 太占显存，模型又不能泛化到超过训练长度的文本；只缓存最近 token 的窗口注意力，在文本长度超过缓存大小、开头的 token 被逐出后就会失效。
- **核心方法**：作者发现注意力汇聚（attention sink）：不论语义是否重要，模型都把大量注意力分给开头几个 token。他们的解释是 softmax 要求一行注意力权重加起来等于 1，当前查询找不到强匹配时，多余的权重需要地方放，而开头的 token 对之后所有位置都可见；把开头 4 个 token 换成换行符仍能恢复效果，说明起作用的是位置而非内容。StreamingLLM 据此始终保留开头 4 个 token 的 KV，再加最近 token 的滑动窗口，不用微调就让 Llama-2、MPT、Falcon、Pythia 稳定处理 400 万 token 以上，比滑动窗口重算快最多 22.2 倍。作者另外从头预训练 160M 参数的模型，给每个训练样本开头加一个可学习的 sink token，推理时只保留这一个 token 即可稳定地流式生成。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)"注意力不丢失"一节的第一个失败场景（截断缓存），也是"显式提供 sink"一路的源头：[DeepSeek-V4](../arxiv-2606.19348/README.md) 在 softmax 分母里加可学习的 sink 项属于同一思路；相反的一路是 [Gated Attention](../arxiv-2505.06708/README.md) 用门控消除汇聚。作者写明它不扩展上下文窗口、不增强长程记忆，不适合需要长程记忆的任务。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2309.17453 · [全文 PDF](https://arxiv.org/pdf/2309.17453) · MIT、Meta AI、CMU、NVIDIA · ICLR 2024；代码开放（mit-han-lab/streaming-llm）
- 方向：llm/pretraining、llm/long-context
