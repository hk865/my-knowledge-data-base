# Learning to reason with LLMs

> 状态：文献卡 · 2024 · [原文](https://openai.com/index/learning-to-reason-with-llms/)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让语言模型在回答前先进行很长的内部思考（思维链），在数学竞赛、编程竞赛、博士级科学问答这类需要多步推理的任务上大幅提升。
- **核心方法**：官方博客只写到训练方式的层面：用大规模强化学习训练模型产生思维链。博客称 o1 的表现随强化学习的训练算力和思考时间（测试时算力）的增加而平滑提升。AIME 2024（美国数学邀请赛）上 GPT-4o 平均 12%，o1 单次 74%、64 次采样共识 83%、用学习的打分函数在 1000 个样本中重排 93%；Codeforces 上 o1 位于第 89 百分位。OpenAI 决定不向用户展示原始思维链，理由是保留不受约束的思维链以便监控，同时兼顾用户体验与竞争优势，改为展示模型生成的摘要。博客写明 o1-preview 在部分自然语言任务上不如 GPT-4o 受人类评审偏好。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"推理模型"阶段的起点：它把"测试时算力"从外挂的采样与搜索变成模型自己的长思考，并给出训练算力与思考算力两条扩展曲线；结构、数据与训练细节均未公开，公开配方要看 [DeepSeek-R1](../arxiv-2501.12948/README.md) 与 [Kimi k1.5](../arxiv-2501.12599/README.md)。优先级：必读。

## 身份信息

- 稳定标识：url:https://openai.com/index/learning-to-reason-with-llms/ · [全文](https://openai.com/index/learning-to-reason-with-llms/) · OpenAI
- 方向：llm/inference、llm/posttraining/rl
