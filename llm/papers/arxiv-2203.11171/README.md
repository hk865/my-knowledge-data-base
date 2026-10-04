# Self-Consistency Improves Chain of Thought Reasoning in Language Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2203.11171)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：思维链提示用贪心解码只走一条推理路径，一步出错整题就错；复杂题往往有多条不同的推理路径通向同一个正确答案（§1）。
- **核心方法**：自洽（self-consistency）解码：同一道题用采样生成多条推理链（实验中 40 条），丢掉推理过程，只对最终答案做多数投票。不需要额外训练、辅助模型或人工标注。GSM8K 上 PaLM 540B 从思维链贪心解码的 56.5% 升到 74.4%，code-davinci-002 从 60.1% 升到 78.0%（Table 2）。自述局限是计算成本随采样条数增加，作者建议先用 5 到 10 条，因为收益很快饱和（§5、Figure 2）。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"并行多采样再选"一支的基线：它说明不需要验证器、只靠多数投票就能把多算的算力换成准确率；[Large Language Monkeys](../arxiv-2407.21787/README.md) 后来显示，这种选择方法在采样数增大后会先于覆盖率进入平台。前作是 [CoT](../arxiv-2201.11903/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2203.11171 · [全文](https://arxiv.org/pdf/2203.11171) · Google Research（Brain Team）
- 方向：llm/inference
