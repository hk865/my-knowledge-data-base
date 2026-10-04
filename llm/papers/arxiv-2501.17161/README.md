# SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.17161)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：同一任务上，SFT 与 RL 各自带来的是记住训练数据，还是能迁移到规则变体的泛化。
- **核心方法**：在纯文本与图像两种形式的 GeneralPoints（用四张牌算出目标数的算术游戏）和真实街景导航 V-IRL 上，从同一个 Llama-3.2-Vision-11B 出发分别做 SFT 与以结果为奖励的 RL，再换规则、换视觉测试：RL 在两类变体上都能泛化，SFT 倾向记住训练数据、在分布外变差，且 SFT 规模加大会损害视觉识别。但 SFT 仍是 RL 的前提：它稳定了输出格式，没有 SFT 初始化的 RL 训练失败。作者自述：从极度欠拟合或过拟合的检查点出发时 RL 作用有限，过拟合检查点上的 RL 无法恢复分布外表现（§6）。
- **为什么在这个库里**：[SFT Baseline 表](../../fields/posttraining/sft/BASELINES.md)与 [RL Baseline 表](../../fields/posttraining/rl/BASELINES.md)之间的对照实验：说明为什么 2025 年的配方是"少量 SFT 冷启动 + 大量 RL"。它测的是规则游戏与导航，不是开放对话。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2501.17161 · [全文 PDF](https://arxiv.org/pdf/2501.17161) · 港大、UC Berkeley、Google DeepMind、NYU、阿尔伯塔大学
- 方向：llm/posttraining/sft、llm/posttraining/rl
