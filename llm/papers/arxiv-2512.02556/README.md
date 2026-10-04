# DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

> 状态：技术精读 · 2025 · [原文](https://arxiv.org/abs/2512.02556)

[返回大语言模型目录](../../README.md)

- **解决什么**：作者把开源模型落后于闭源模型归结为三点：原始注意力在长序列上效率低；后训练算力投入不足；智能体场景下的泛化与指令遵循差。
- **核心方法**：从 DeepSeek-V3.1-Terminus（上下文已扩到 128K）的检查点继续预训练，唯一的结构改动是 DSA（DeepSeek 稀疏注意力）：一个很小的"闪电索引器"给每个查询与历史 token 打分，主注意力只读得分最高的 2048 个 KV。DSA 在 MLA（多头潜在注意力）的 MQA 模式下实现，每个潜向量被所有查询头共享。继续预训练分两段：先保持稠密注意力、冻结索引器以外的全部参数，用 2.1B token 让索引器的打分分布对齐主注意力的分布（稠密预热）；再放开全部参数做稀疏训练，共 943.7B token。主注意力的复杂度从 O(L²) 降到 O(Lk)（k 是选中的 token 数），索引器本身仍是 O(L²)，但计算量小得多。后训练用可扩展的强化学习协议，算力超过预训练成本的 10%，并大规模合成智能体任务。
- **为什么在这个库里**：[预训练方向](../../fields/pretraining/README.md)两处证据。"预训练与后训练的分工"：后训练算力已超过预训练成本的 10%，作者仍把世界知识广度落后于闭源模型归因于总训练 FLOPs 较少，计划扩大预训练算力。"更长更大的注意力"：训练时稀疏一路中 [NSA](../arxiv-2502.11089/README.md) 与 [DeepSeek-V4](../arxiv-2606.19348/README.md) 之间的一步，"稠密预热后转稀疏"的课程从这里开始。它自述的做不好的场景：128K 的上限让 20% 以上的搜索智能体测试超长；工具调用评测中模型常做冗余的自我验证，轨迹超出 128K。优先级：选读（预训练部分只需读第 2 节与结论）。

## 阅读入口

- [技术精读](reading.md)：闪电索引器与两段式继续训练、128K 下的计算与读取手算、短序列开销与索引器瓶颈，以及与 NSA 的逐项对照
- [图解与说明](figures/README.md)
- [证据档案](evidence.json)与[原文版本与阅读记录](source.json)

## 阅读顺序

[DeepSeek-V2 精读](../deepseek-v2/reading.md)（MLA）→ [NSA 精读](../arxiv-2502.11089/reading.md)（训练时就稀疏）→ 本篇 → [DeepSeek-V4](../arxiv-2606.19348/README.md)（先压缩再稀疏）。

## 身份信息

- 稳定标识：arxiv:2512.02556 · [全文 PDF](https://arxiv.org/pdf/2512.02556) · DeepSeek-AI
- 方向：llm/pretraining、llm/architecture、llm/posttraining/rl
