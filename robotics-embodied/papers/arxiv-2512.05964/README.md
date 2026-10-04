# Training-Time Action Conditioning for Efficient Real-Time Chunking

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.05964)

- **解决什么**：推理时 RTC（实时动作块接续，边执行旧动作边生成新块）的引导本身又增加延迟。
- **核心方法**：随机模拟延迟，前缀不加噪、后缀计算损失，将动作接续学进策略。
- **为什么在这个库里**：[VLA Baseline](../../fields/vla/BASELINES.md)的"训练目标 + 推理调度"一格；接在 RTC 后理解部署成本怎样转移到训练。优先级：必读。
