# Self-Discover: Large Language Models Self-Compose Reasoning Structures

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2402.03620)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：思维链（CoT，让模型先写出推理步骤再作答）对所有任务用同一种推理方式；复杂推理任务需要与任务本身匹配的推理结构。
- **核心方法**：相对 CoT，分两个阶段。第一阶段在任务层面用三个元提示让模型 SELECT（从批判性思维、逐步思考等原子推理模块中挑选）、ADAPT（改写成针对该任务的说法）、IMPLEMENT（组织成显式、可执行的推理结构）；第二阶段对每个实例按这个结构解码。在 BigBench-Hard、grounded agent reasoning 和 MATH 上，GPT-4 与 PaLM 2 的表现比 CoT 最多提高 32%；比 CoT-Self-Consistency（多次采样后投票）高 20% 以上，推理计算少 10–40 倍。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)中"提示层面的推理结构"一支：结构每个任务只生成一次，所以成本低于多次采样投票。可与 [测试时计算预算](../test-time-compute/README.md) 这类"多花采样与验证"的路线对照。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2402.03620 · [全文 PDF](https://arxiv.org/pdf/2402.03620) · Google DeepMind 出版物页面以 Large Language Models Self-Discover Reasoning Structures 为题列出（[页面](https://deepmind.google/research/publications/64816/)）
- 作者：Pei Zhou、Jay Pujara、Xiang Ren、Xinyun Chen、Heng-Tze Cheng、Quoc V. Le、Ed H. Chi、Denny Zhou、Swaroop Mishra、Huaixiu Steven Zheng（南加州大学、Google DeepMind）
- 方向：llm/inference
