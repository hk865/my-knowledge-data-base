# EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2502.09560)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多模态大模型当具身 Agent 时，高层规划与低层控制分别做得怎样，缺少统一的细粒度评测。
- **核心方法**：四个环境（EB-ALFRED、EB-Habitat 测高层，EB-Navigation、EB-Manipulation 测低层）、六个能力子集（常识、复杂指令、空间、外观、长程等），共 1,128 个测试实例。最强模型高层 64%–68%，低层操作只有 28.9%；长程子集从 96% 降到 58%；GPT-4o 的错误以规划错误为主。
- **为什么在这个库里**：[具身 Agent](../../fields/embodied-agents/README.md)主线第 4 步：为"通用大模型高层够用、低层不够"提供量化证据。优先级：选读。
