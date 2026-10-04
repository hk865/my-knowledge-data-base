# Proving Test Set Contamination in Black Box Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.17623)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：闭源模型的预训练数据不公开，"某个 benchmark 被记住了"长期停留在猜测，需要不依赖训练数据和权重、有误报率保证的检验（摘要、§1）。
- **核心方法**：利用可交换性：没被训练过时，一个数据集的各种排列顺序应当同样可能；被训练过的模型会记住公开仓库里的"规范顺序"，给它更高的似然。比较规范顺序与随机打乱顺序的对数似然，分片后做统计检验，得到有误报率保证的 p 值。在 1.4B 模型、1000 条样本、语料中只出现少数几次的设定下也能检出；审计 LLaMA2、Mistral-7B、Pythia-1.4B、GPT-2 XL 在 8 个 benchmark 上的情况，除 Mistral 的 ARC 与两者在 MMLU 上的弱信号外，没有发现普遍的逐字污染。自述局限：没做多重检验校正；无法证明一个现成数据集真的可交换；只能检测逐字污染，检测不到"读过构造题目所用的原始资料"这类部分污染。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"污染"一节中"从训练语料外部检测"的代表，与 [GSM1k](../arxiv-2405.00332/README.md)"重新出题量落差"的思路互补：前者能给出证明但只管逐字记忆，后者管得更宽但要重新出一套题。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2310.17623 · [全文 PDF](https://arxiv.org/pdf/2310.17623) · Stanford University、Columbia University
- 发表：arXiv 预印本（v2）
- 方向：cross-domain/evaluation、cross-domain/model-science
