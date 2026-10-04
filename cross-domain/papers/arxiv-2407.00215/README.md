# LLM Critics Help Catch LLM Bugs

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2407.00215)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：RLHF 受限于人评估模型输出的能力；模型越强，人越难判断代码这类输出是否正确。
- **核心方法**：用 RLHF 训练"批评者"模型（CriticGPT），为真实助手任务中的代码写自然语言批评、指出问题；训练与评测数据包括由标注员有意在代码中插入 bug（tampering）再要求找出。在含自然出现错误的代码上，模型写的批评有 63% 被偏好于人类批评；它找出的插入 bug 多于付费的人类代码审查员；在 ChatGPT 训练数据中被评为"无缺陷"的样本里也找出数百个错误。评价批评时同时看全面性、是否幻觉出不存在的 bug、是否挑小毛病；局限是批评者会幻觉 bug、挑刺，可能误导人，人机组合找到的 bug 与模型相当而幻觉更少。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"代码质量"一节中"代码审查能力"的例子：审查能力本身可以用 RLHF 训练，审查的评测要同时看找全与误报两侧。与 [弱模型评判强模型](../arxiv-2407.04622/README.md) 同属可扩展监督的思路。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2407.00215 · [全文 PDF](https://arxiv.org/pdf/2407.00215) · OpenAI（superalignment 可扩展监督团队）
- 发表：arXiv v1（预印本）
- 方向：cross-domain/evaluation、llm/posttraining/preferences
